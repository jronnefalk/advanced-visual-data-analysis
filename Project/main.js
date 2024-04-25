// Read cc_data.csv
fetch("/MC2/cc_data.csv")
  .then((response) => response.text())
  .then((cc_data) => {
    console.log("Data read successfully.");
    processData(cc_data);
  })
  .catch((error) => {
    console.error("Error reading data. Please provide a different path.");
  });

// Read loyalty_data.csv
fetch("/MC2/loyalty_data.csv")
  .then((response) => response.text())
  .then((loyalty_data) => {
    console.log("Data read successfully.");
    processData(loyalty_data);
  })
  .catch((error) => {
    console.error("Error reading data. Please provide a different path.");
  });

// Function to process the data
function processData(data) {
  const rows = data.split("\n");
  const places_data = {};

  // Loop through each row of the data
  for (let i = 1; i < rows.length; i++) {
    const row = rows[i].split(",");
    const timestamp = row[0];
    const location = row[1];
    const price = parseFloat(row[2]);
    const id = row[3];
    // Create a new list for the location if it doesn't already exist
    if (!places_data[location]) {
      places_data[location] = [];
    }
    // Add time, price, and last 4 of credit card number or loyalty number to the location's data
    places_data[location].push({
      Timestamp: timestamp,
      Price: price,
      ID: id,
    });
  }
  // Display the result
  for (const place in places_data) {
    console.log(`Place: ${place}`);
    for (const entry of places_data[place]) {
      console.log(
        `Timestamp: ${entry.Timestamp}, Price: ${entry.Price}, ID: ${entry.ID}`
      );
    }
  }
}
