contact = { }

def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key, contact.get(key)))

while True:
    op = int(input(" 1. Add new contact \n 2. Search contact \n 3. Display contact \n 4. Edit contact \n 5. Delete contact\n 6. Exit\n Enter your choice "))
    if op == 1:
        na = input("enter the contact name ")
        ph = input("enter the mobile number")
        contact[na] = ph
    elif op == 2:
        s_name = input("enter the contact name ")
        if s_name in contact:
          print(s_name, "'s contact number is ", contact [s_name])
        else:
            print("Name is not found in contact book")
    elif op == 3:
        if not contact:
            print("empty contact book")
        else:
            display_contact()
    elif op == 4:
        e_contact =  input("Enter the contact to be edited ")
        if e_contact in contact:
            ph = input("enter mobile number")
            contact[e_contact]=ph
            print("contact updated")
            display_contact()
        else: 
            print("Name is not found in contact book")
    elif op == 5:
        d_contact = input("Enter the contact to be deleted")
        if d_contact in contact:
            confirm = input("Do you want to delete this contact y/n? ")
            if confirm =='y' or confirm == 'Y':
                contact.pop(d_contact)
                display_contact()
            else:
              print("Name is not found in contact book")
    else:
        break