import sys

users =[]

def add_user(users):
    name = input("Enter your name: ")
    address= input("Enter your address: ")
    newuser = {"Name":name,"Address":address}
    users.append(newuser)
    print(users)

def list_user(users):
    print("S.N.\t\tName \t\t\t Address ")
    for index,user in enumerate(users):
        print(str(index) +"\t\t"+ user["Name"]+"\t\t\t"+user["Address"])

def edit_user(users):
    editindex = int(input("Enter the user index you want to edit : "))
    newname = input("Enter the new name : ")
    newaddress = input("Enter new address : ")
    user = users[editindex]
    user["Name"] = newname
    user["Address"] = newaddress

def delete_user(users):
    delname = input("Enter name of user you want to delete : ")
    for user in users:
        if user["Name"] == delname:
            users.remove(user)

def menu():
    print("\n***Would you like to***")
    print("1. Add User\n2. List the created users\n3. Edit user \n4. Delete a user ")

def main():
    with open('userdetail.txt','r+') as file:
        for line in file:
            print(line, end = '')
        while True:
            menu()
            choice = int(input("select an option: \n"))
            if choice == 1:
                add_user(users)
                print("New user is added")
            elif choice==2:
                print("list of current users")
                list_user(users)
            elif choice==3:
                list_user(users)
                edit_user(users)
                print("New list\n ")
                list_user(users)
            elif choice==4:
                delete_user(users)
                print("User is deleted")
            else:
                print("Thankyou!")
                break

        file.writelines(str(users))
        file.close()

if __name__ == "__main__":
    sys.exit(main())

