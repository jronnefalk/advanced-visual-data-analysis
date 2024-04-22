import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Download necessary NLTK resources
nltk.download("punkt")  # for tokenization
nltk.download("stopwords")  # for stopwords


def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    text = "".join([char for char in text if char not in string.punctuation])
    # Tokenize text
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words]
    # Combine tokens back into a single string
    return " ".join(tokens)


# Load data
# Try reading just the first few lines to see how pandas is interpreting the columns
data = pd.read_csv("TNM098-MC3-2011.csv", delimiter=";")
print(data.head())
print(data.columns)


# Apply preprocessing to the Content column
data["Processed_Content"] = data["Content"].apply(preprocess_text)

# Display the first few rows of the processed data
print(data[["Content", "Processed_Content"]].head())
