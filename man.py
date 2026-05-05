contacts = {}
menu = ("1.Add contacts\n2.Search contacts\n3.Show all\n4.Delet Contacts\n5.Edit contacts\n6.Exit")
def save_to_file() :
    with open("contacts.txt" , "w") as file :
        for name , phone in contacts.items() :
            file.write(f"{name}:{phone}\n")
def load_from_file() :
    try:
        with open("contacts.txt" , "r" ) as file :
            for line in file :
                name , phone = line.strip().split(":")
                contacts[name] = phone    
    except FileNotFoundError :
        pass
def add_contacts() :
    name = input("Name")
    phone = input("Phone")
    contacts[name] = phone
    print("saved")
    save_to_file()
def search_contacts() :
    name = input("Name")
    if name in contacts :
        print(f" Phone number : {contacts[name]}")
    else :
        print("Contacts Not Found")
def show_all() :
    if not contacts :
        print("Your Phone Book İs Empty!")
    else :
        for name , phone in contacts.items() :
            print(f"Name : {name} | Phone : {phone}")
def delet_contacts() :
    name = input("Enter Name To Delet :")
    if name in contacts:
        del contacts[name]
        print(f"*** {name} Deleted successfully! ***")   
        save_to_file()
    else :
        print("This Name Dose Not Exist!")
def edit_contacts() :
    name = input("Enter the name you want to edit :")
    if name in contacts :
        print(f"current number for{name} is: {contacts[name]}")
        new_phone = input("Enter new phone number :")
        contacts[name] = new_phone
        print("***Updated Successfully!***")
        save_to_file()
    else :
       print("this name dos not exist in your contacts!")             
def exit_program() :
    print("save All History")
    save_to_file()    
    

load_from_file()              
while True :
    try :
        print(menu)
        choice = int(input("select"))
        
        if choice == 1 :
            add_contacts()
        elif choice == 2 :
            search_contacts()
        elif choice == 3 :
            show_all()
        elif choice == 4 :
            delet_contacts()
        elif choice == 5 :
            edit_contacts()    
        elif choice == 6 :
            exit_program() 
            break       
    except ValueError :
        print("\n Just Enter The Number ") 
    