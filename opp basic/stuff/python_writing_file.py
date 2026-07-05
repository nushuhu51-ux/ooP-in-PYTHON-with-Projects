# python writing files (.txt, .json, .csv)

# Text data
import json
import csv

employees = [[ "name", "Age", "Job"],
             [ "Sponge", 30 , "Cook"],
             ["Patrick", 37, "Unemployeed"],
             ["Sandy", 27, "Scintist"]]

file_path = "C:/Users/Samuel/OneDrive/Desktop/test.csv"
try:
    with open(file=file_path, mode="w") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"CSV file {file_path} was created")
except FileExistsError:
    print("That file already exist!")
