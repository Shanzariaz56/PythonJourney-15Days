import json
#write mode
data={
    "name": "Alice",
    "age": 28,
    "city": "Los Angeles",
    "skills": ["Java", "C++", "HTML"]
}
    
with open("data_json.json","w") as file:
    json.dump(data,file,indent=4)

# read mode
with open("data_json.json","r") as file:
    data=json.load(file)
    
print(data["name"])
print(data["city"])

# append mode

with open("data_json.json","r") as file:
    data=json.load(file)
# updated with append
data["skills"].append("css")
# update data 
with open("data_json.json","w") as file:
    json.dump(data,file,indent=4)

    

    
