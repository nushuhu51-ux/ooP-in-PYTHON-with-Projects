# python writing files (.txt, .json, .csv)

# Text data
import json
employees = {"name": "Spongebob",
             "age": 30 ,
             "job": "Cook"
             }

file_path = "C:/Users/Samuel/OneDrive/Desktop/test.json"
try:
    with open(file=file_path, mode="w") as file:
        json.dump(employees, file, indent=4)
        print(f"json file {file_path} was created")
except FileExistsError:
    print("That file already exist!")
