import json


def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    person = {
        "name": name,
        "age": age,
        "email": email
    }

    return person

def display_pepole(pepole):
    for i, person in enumerate(pepole):
        print(i+1,"-",person["name"], "|", person["age"], "|", person["email"])

def delete_contact(pepole):
    display_pepole(pepole)
    
     
    while True:
        number = input("Enter a number to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(pepole):
                print("invalid number out of range.")

            else:
                break    

        except:
            print("invalid number")
    pepole.pop( number - 1)
    print("Person deleted.")            

def search(People):
    search_name = input("Srarch for a name: ")
    results = []

    for person in People:
        name = person["name"]
        if search_name in name.lower():
            results.append(person)

    display_pepole(results)        


print("Hi, welcome to contact manger system. ")
print()

with open("contact.json", 'r') as f:
    pepole = json.load(f)["contacts"]

pepole = []
while True:
    print("contact list size:", len(pepole))
    command = input("You can 'Add' or 'Delete' or 'Search' and 'Q' for quit: ").lower()
  

    if command == "add":
        person = add_person()
        pepole.append(person)
        print("person added!")
    elif command == "delete":
        delete_contact(pepole)
    elif command == "search":
        search(pepole)
    elif command == "q":
        break
    else:
        print("Invalid command") 



with open("contact.json", 'w') as f:
    pepole = json.dump({"contacts": pepole}, f)



        

     