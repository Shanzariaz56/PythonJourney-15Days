import csv
# first write data in csv
data=[["Name", "Age", "City"],
    ["Alice", 28, "New York"],
    ["Bob", 24, "Los Angeles"],
    ["Charlie", 22, "Chicago"],
    ["Name", "Age", "City"],
    ["Alice", 28, "New York"],
    ["Bob", 24, "Los Angeles"],
    ["Charlie", 22, "Chicago"]]
with open("example_data.csv","w") as file:
    writer=csv.writer(file)
    writer.writerows(data)
# read data from csv
with open ("example_data.csv","r") as file:
    read=csv.reader(file)
    for i in read:
        print(i)