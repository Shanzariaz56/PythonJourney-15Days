import csv
# write mode
data=[ ["Name", "Age", "City"],
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
    
# read mode
with open("example_data.csv","r",newline="") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
        
# append mode
n_data=[ ["Name", "Age", "City"],
    ["Alice", 28, "New York"],
    ["Bob", 24, "Los Angeles"],
    ["Charlie", 22, "Chicago"],
    ["Name", "Age", "City"],
    ["Alice", 28, "New York"],
    ["Bob", 24, "Los Angeles"],
    ["Charlie", 22, "Chicago"]]
with open ("example_data.csv","a",newline="") as file:
    writer=csv.writer(file)
    writer.writerows(n_data)        

