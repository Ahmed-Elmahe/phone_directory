"""
Project No.1
project title: Phone directory
data of directory:
|---------------------|
|name  |  phone number|
|---------------------|
|Amal	  | 1111111111|
|Mohammed | 2222222222|
|Khadijah | 3333333333|
|Abdullah | 4444444444|
|Rawan	  | 5555555555|
|Faisal	  | 6666666666|
|Layla	  | 7777777777|
|---------------------|
"""

phone_directory = {
    "Amal": "1111111111",
    "Mohammed": "2222222222",
    "Khadijah": "3333333333",
    "Abdullah": "4444444444",
    "Rawan": "5555555555",
    "Faisal": "6666666666",
    "Layla": "7777777777"
}

#search by number
def searchNuber(number):
    if not number.isdigit() or len(number) != 10:
        return "This is invalid number"
    for name, num in phone_directory.items():
        if num == number:
            return name
    return "Sorry, the number is not found"

#search by name
def searchName(name):
    if name in phone_directory:
        return phone_directory[name]
    return "Sorry, the name is not found"

def addNewphone(name, number):
    if not name.isdigit() or len(number) != 10:
        return "This is invalid number"
    if name in phone_directory:
        return "This name already exists in the phone book"

    phone_directory[name] = number

    return "Entry added successfully"

while True:
    print("\nMenu")
    print("1. Search by number")
    print("2. Search by name")
    print("3. Add new phone")
    print("4. Exit")

    choice = int(input("Enter the number for what do you want to do: "))

    if choice == 1:
        number = input("Enter the phone number: ")
        print(searchNuber(number))
    elif choice == 2:
        name = str(input("Enter the name of the owner of the number you want: "))
        print(searchName(name))
    elif choice == 3:
        name = str(input("Enter the new name: "))
        number = input("Enter the new number: ")
        print(addNewphone(name, number))
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please select again")