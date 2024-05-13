import fs from "fs";

// Importera fs-modulen för att läsa CSV-filer
const fs = require("fs");

// Läs in cc_data.csv
fs.readFile("Project/MC2/cc_data.csv", "latin1", (err, cc_data) => {
  if (err) {
    console.log("Fel vid inläsning av data. Ange en annan väg.");
    return;
  }
  console.log("Data inläst korrekt.");
  // Bearbeta cc_data
  processData(cc_data);
});

// Läs in loyalty_data.csv
fs.readFile("Project/MC2/loyalty_data.csv", "latin1", (err, loyalty_data) => {
  if (err) {
    console.log("Fel vid inläsning av data. Ange en annan väg.");
    return;
  }
  console.log("Data inläst korrekt.");
  // Bearbeta loyalty_data
  processData(loyalty_data);
});

// Funktion för att bearbeta datan
function processData(data) {
  const rows = data.split("\n");
  const places_data = {};

  // Loopa över varje rad i datan
  for (let i = 1; i < rows.length; i++) {
    const row = rows[i].split(",");
    const timestamp = row[0];
    const location = row[1];
    const price = parseFloat(row[2]);
    const id = row[3];
    // Skapa en ny lista för platsen om den inte redan finns
    if (!places_data[location]) {
      places_data[location] = [];
    }
    // Lägg till tid, pris och sista 4 av kreditkortsnummer eller lojalitetsnummer till platsens data
    places_data[location].push({
      Timestamp: timestamp,
      Price: price,
      ID: id,
    });
  }
  // Visa resultatet
  for (const place in places_data) {
    console.log(`Plats: ${place}`);
    for (const entry of places_data[place]) {
      console.log(
        `Tidpunkt: ${entry.Timestamp}, Pris: ${entry.Price}, ID: ${entry.ID}`
      );
    }
  }
}
