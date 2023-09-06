person = { 
           "name" : "Hajar" ,
           "age"  : 17 ,
           "hobbies" : ["swiming", "sleepping"]
}
print(person["name"])
print(person["age"])

person["age"]=18
person["country"]="bahrain"
print(person)
print(len(person))

person["hobbies"].append("eating")
print(person)
def check_hobbies(person):
    if person["hobbies"] > "three hobbies":
        print("WOW U ARE AMAZ")
    else: 
        print("NOT AMAZ")

