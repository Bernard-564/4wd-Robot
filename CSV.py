import csv

with open("mtcars-parquet.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file, delimiter=",")
    
    with open("new_car_packs.csv", "w") as new_cars:
        fieldnames = ["model", "hp", "gear"]

        csv_writer = csv.DictWriter(new_cars, fieldnames=fieldnames, delimiter="\t",
                                        extrasaction='ignore')

        csv_writer.writeheader()

        for line in reader:
            csv_writer.writerow(line)

         