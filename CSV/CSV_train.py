import csv

with open("new_car_packs.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter="\t")
    for row in reader: 
        print(row)