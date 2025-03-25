import time

def order():
    print("Orders are :")
    with open("order.txt","r") as chef_files:
        print(chef_files.read())
    time.sleep(3)
   # Initialize an empty list

    order_status = input("What is the order status (complete/inprogress)? ").lower()
    if order_status == "complete":
        with open("order_status.txt", "w") as status_file:
            status_file.write("complete")
        with open("order.txt","w") as file:
            file.write("")
    else:
        with open("order_status.txt", "w") as status_file:
            status_file.write("inprogress")
        print("Order is still in progress")
    
def ingredients():
        supplies=[]
        num=int(input("Enter no of ingredients you need:"))
        for i in range(num):
            ingredient=input(f"Enter ingredient no. {i+1}:")
            supplies.append(ingredient+"\n")
        with open("ingredients.txt",'a+') as chef_files:
            chef_files.writelines(supplies)


def update():
        print("You can change you username and password here!")
        username=input("enter new username:")
        password=input("enter new passowrd:")
        with open("chef.txt","r+") as admin_files:
            lines=admin_files.readlines()
        updated_lines=[]
        for line in lines:
                if line.startswith("username:"):
                    updated_lines.append("username:"+username+"\t\n")
                    print("Username Successfully changed")
                elif line.startswith("password:"):
                    updated_lines.append("password:"+password+"\t\n")
                    print("Password Successfully changed")

                else:
                    updated_lines.append(line)

        with open("chef.txt","w") as admin_files:
            admin_files.writelines(updated_lines)
def chef_main():
    print("welcome back chef!!")
    time.sleep(2)
    print("What operation would you like to perform?")
    print("1.View orders from customers")
    print("2.Request ingredients ")
    print("3.Update your own profile")
    operation=int(input("enter your operation(1,2,3):"))
    if operation==3:
        update()
    elif operation==2:
        ingredients()
    elif operation==1:
        order()
if __name__ == "__main__":
    chef_main()


