#dictionary is mainly used for stroing any values with key pair
#use case: storing contact info, Database Indexing, Configuration Management
#it can hold configuration option and its value , routing in web server
std={
    "name":"shanza",
    "age":20,
    "grade":3.85
    }
print(std["name"])

#method of dictionary...
print(std.items())  #return list with(key,value) as pair
print(std.get("name"))
print(std.keys())  #gave only keys 
print(std.update({"name":"talhaa"}))
print(std)
del std["name"]  #delete
print(std)
print(std.pop("age"))  #pop
print(std)
#add new key value at the end
std["name"] = "shanza"
print(std)
#nested dictionary.....
dic={"dic1":{"name":"shanza","age":20},
     "dic2":{"name1":"shanzyy","age2":21}}
print(dic.get("dic1"))
print(dic.items())
print(dic["dic2"].get("name1"))
print(dic["dic1"]["name"])
#dictionary comprehension
dic={x:x**3 for x in range(10)}
print(dic)

#square of number
num=[1,6,7,8,9,4]
square={nums:nums**2 for nums in num }
print(square)

#even number
even={n : n**2 for n in range (30) if n%2==0}
print(even)

#create a dictionary of urdu words with values as their English
dic={
    "subha":"morning",
    "raat":"night",
    "din":"day",
    "hello":"greeting"
    }


while True:
    user_word=input("enter the words:")
    if user_word.lower=="exits":
        print("stop")
        break
    if user_word in dic:
        print(dic[user_word])
    else:
        print("not found")
     
#create a dictionary of urdu words with values as their English
dic={
    "subha":"morning",
    "raat":"night",
    "din":"day",
    "hello":"greeting"
    }   
for i in dic: #for keys
    print(i)
#for values
for i in dic:
    print(dic[i])