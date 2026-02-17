import random
import string

def generate_password():
    lenght = int(input("Enter the desired password lenght: ").strip())
    include_uppercase = input("include upercase letters? (yes/no): ").strip().lower()
    include_specail = input("Include specail charachters? (yes/no): ").strip().lower()
    include_digits = input("Include digits? (yes/no): ").strip().lower()

    if lenght < 4:
        print("Password lenght must be at least 4 characters. ")
        
        return
    
    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase =="yes" else ''
    specail = string.punctuation if include_specail =="yes" else ''
    digits = string.digits if include_digits == "yes" else ''

    all_charachters = lower + uppercase + specail + digits
     
    required_charcters = [] 
    if include_uppercase == "yes":
        required_charcters.append(random.choice(uppercase))
    if include_specail == "yes":
        required_charcters.append(random.choice(specail))
    if include_digits == "yes":
        required_charcters.append(random.choice(digits))
    
    remainig_lenght = lenght - len(required_charcters)
    password = required_charcters

    for _ in range(remainig_lenght):
        characters = random.choice(all_charachters)
        password.append(characters)

    random.shuffle(password)
    str_password = "".join(password)
    return str_password

password = generate_password()   

print(password)

  