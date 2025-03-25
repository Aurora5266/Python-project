def admin():
    import time
    def view_sales_report():
        try:
            with open("sales_feedback.txt", "r") as file:
                print("\nSales and Feedback Report:")
                print(file.read())
        except FileNotFoundError:
            print("No sales data available yet.")
    def update():
        print("You can change you username and password here!")
        username=input("enter new username:")
        password=input("enter new passowrd:")
        with open("admin.txt","r+") as admin_files:
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

        with open("admin.txt","w") as admin_files:
            admin_files.writelines(updated_lines)

    def staff():
        with open("admin.txt","r+") as admin_files:
            lines=admin_files.readlines()
            
        output=[]
        a=0
        for line in lines:
                if "Staff" in line:
                    a=1
                    
                if a==1:
                    output.append(line.strip())
        for line in output:
                print(line)
        
        operation=input("What would you like to do?(Add,edit,delete):")
        if operation.lower()=='add':
            with open("admin.txt","a+") as admin_files:
                position=input("enter the position of the employee:")
                name=input("enter the name of the employee:")
                updated_lines = []
                
                for line in lines:
                    updated_lines.append(line)
                    if position.lower()=="manager":
                        if line.strip() == "Staff:":
                            
                            updated_lines.append(f"{position}:{name}\n")
                            print(f"{name} is appointed as {position}")
                if position.lower()=="chef":
                        
                    updated_lines.append(f"{position}:{name}\n")
                    print(f"{name} is appointed as {position}")
                            

                
                with open("admin.txt", 'w') as file:
                    file.writelines(updated_lines)
                    
            a=0
            output=[]
            for line in updated_lines:
                if "Staff:" in line:
                    a=1
                    
                if a==1:
                    output.append(line.strip())
            for line in output:
                print(line)
                
                
        elif operation.lower()=='edit':
            print(" ")
        elif operation.lower()=='delete':
            fire=input("Who would you like to fire?:")
            updated_lines=[]
    
            with open("admin.txt","r+") as admin_files:
                    lines=admin_files.readlines()
            for line in lines:
                
                if ":" in line:
                    word=line.split(":",1)[1].strip()
                    if word==fire:
                        print(f"{fire} is fired!")
                        continue
                    updated_lines.append(line)
            with open("admin.txt", 'w') as file:
                    file.writelines(updated_lines)
            a=0
            output=[]
            for line in updated_lines:
                if "Staff:" in line:
                    a=1
                    
                if a==1:
                    output.append(line.strip())
            for line in output:
                print(line)
  
    print("welcome back admin!!")
    time.sleep(2)
    print("What operation would you like to perform?")
    print("1.Manage staff - Manager, Chef (Add, Edit, Delete) ")
    print("2.View sales report based on month and feedback send by customers etc. ")
    print("3.Update your own profile")
    operation=int(input("enter your operation(1,2,3,4):"))
    if operation == 3:
                update()
    elif operation == 1:
                staff()
    elif operation ==2:
                view_sales_report()
    
admin()      

    
