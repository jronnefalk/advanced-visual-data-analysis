import pandas as pd
import matplotlib.pyplot as plt

try:
    cc_data = pd.read_csv("Project/MC2/cc_data.csv", encoding='latin1')
    print("Data inläst korrekt.")
except UnicodeDecodeError:
    print("Fel vid inläsning av data. Ange en annan kodning.")

try:
    loyalty_data = pd.read_csv("Project/MC2/loyalty_data.csv", encoding='latin1')
    print("Data inläst korrekt.")
except UnicodeDecodeError:
    print("Fel vid inläsning av data. Ange en annan kodning.")

print(cc_data.head())
print(loyalty_data.head())

# Skapa en tom dictionary för att lagra data för varje plats
places_data = {}

# Loopa över varje rad i cc_data
for index, row in cc_data.iterrows():
    timestamp = row['timestamp']
    location = row['location']
    price = row['price']
    last4ccnum = row['last4ccnum']
    
    # Skapa en ny lista för platsen om den inte redan finns
    if location not in places_data:
        places_data[location] = []
        
    places_data[location].append({'Tidpunkt': timestamp, 'Pris': price, 'Sista 4 av kreditkortsnummer': last4ccnum})
  

# Loopa över varje rad i loyalty_data
for index, row in loyalty_data.iterrows():
    timestamp = row['timestamp']
    location = row['location']
    price = row['price']
    loyaltynum = row['loyaltynum']  # Om det finns en loyaltynum-kolumn i loyalty_data
    
    # Skapa en ny lista för platsen om den inte redan finns
    if location not in places_data:
        places_data[location] = []
    
    # Lägg till tid, pris och lojalitetsnummer till platsens data
    places_data[location].append({'Tidpunkt': timestamp, 'Pris': price, 'Lojalitetsnummer': loyaltynum})

plt.figure(figsize=(10, 6))
plt.hist(loyalty_data['location'], bins=len(places_data), alpha=0.5, label='Loyalty Data')
plt.hist(cc_data['location'], bins=len(places_data), alpha=0.5, label='CC Data')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Platser')
plt.ylabel('Antal personer')
plt.title('Histogram över antal personer på olika platser')
plt.legend()
plt.tight_layout()
plt.show()

# Funktion för att skapa histogram för ett specifikt tidsintervall
def plot_histogram_for_time_interval(start_date, end_date):
    plt.figure(figsize=(10, 6))
    for location, data in places_data.items():
        timestamps = [entry['Tidpunkt'] for entry in data if start_date <= entry['Tidpunkt'] <= end_date]
        plt.hist(timestamps, bins=20, alpha=0.5, label=location)
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Tidpunkter')
    plt.ylabel('Antal personer')
    plt.title(f'Histogram över antal personer på olika platser mellan {start_date} och {end_date}')
    plt.legend()
    plt.tight_layout()
    plt.show()

# Exempel: Skapa histogram för ett specifikt tidsintervall (01/06/2014 till 02/06/2014)
plot_histogram_for_time_interval('01/06/2014', '02/06/2014')