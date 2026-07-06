# python reading files (.txt, .json, .csv)
import json
import csv

file_path = "C:/Users/Samuel/OneDrive/Desktop/input.json"
try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("That file is not found")
except PermissionError:
    print("You do not have permission to read that file")