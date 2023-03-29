#This is my first dictionary.

#Create a dictionary with key-value pairs.
drivers = {
    "Alpine" : ["Gasly", "Ocon"],
    "Aston Martin": ["Stroll", "Alonso"],
    "Alfa Romeo": ["Bottas", "Zhou"],
    "AlphaTauri": ["Tsunoda", "De Vries"],
    "Ferrari": ["Leclerc", "Sainz"],
    "Haas F1 Team": ["Hulkenberg", "Magnussen"],
    "McLaren": ["Norris", "Piastri"],
    "Mercedes": ["Hamilton", "Russel"],
    "Red Bull Racing": ["Perez", "Verstappen"],
    "Williams": ["Sargeant", "Albon"]
}


#Access the value of a specific key.
alpine_drivers = drivers["Alpine"]
print("\nThe Apline drivers are:", alpine_drivers)

#Add a new key-value pair to the dictionary.
drivers["Mastercard Lola"] = ["f", "Bigger F"]
just_why = drivers["Mastercard Lola"]
print("\nMastercard Lola never made it", just_why)

#Update the valu for a specific key.
drivers["Ferrari"] = "Binotto why?!"
meme_engineer = drivers["Ferrari"]
print("\nFerrari could have been great,", meme_engineer)

#Remove a key-value pair using the 'del' keyword.
del drivers["Haas F1 Team"]
del drivers["Mastercard Lola"]
print("\nF1 Improved:", drivers)

#Check if a key exists on the dictionary.
if "Williams" in drivers:
    print("\nI miss Senna.")

#Iterate through the dictionary keys and values.
for scuderia, team in drivers.items():
    print("\nThe team for", scuderia, "is", team )

