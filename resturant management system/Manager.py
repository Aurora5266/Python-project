from time import sleep
def add(file_name,name):
    with open(file_name,"a+") as add_to_file:
        add_to_file.seek(0)
        content = add_to_file.readlines()
        if name + "\n" not in content:
            add_to_file.write(name.title() + "\n")  #.title() capitalizes first letter of each word

def edit_customer(name):
    list_of_customers = []
    with open("customers_list.txt","r") as edit_customers:
            lines = edit_customers.readlines()
            for line in lines:
                list_of_customers.append(line.strip())
            if name in list_of_customers:
                new_name = input(f"Enter the new name for the {name}")
                name_index = list_of_customers.index(name)
                list_of_customers[name_index] = new_name.strip().title()
                with open("customers_list.txt","w") as change_customers:
                    for customer in list_of_customers:
                        change_customers.write(customer + "\n")
                print(f"{name} has been updated successfully.")
            else:
                print(f"{name} not found in the customers list.")
                                        
def delete_customer(name):
    list_of_customers = []
    with open("customers_list.txt","r") as delete_customers:
            lines = delete_customers.readlines()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            for line in lines:
                list_of_customers.append(line.strip())
            if name in list_of_customers:
                list_of_customers.remove(name)
                with open("customers_list.txt","w") as remaining_customers:
                    for customer in list_of_customers:
                        remaining_customers.write(customer + "\n")

def view(file_name):
    with open(file_name,"r") as list_file:
        list_content = list_file.read()
        print(list_content)   
                         
while(True):
    print("1.Manage Customer. \n2.Manage Menu Categories and Pricing. \n3.View ingredients list requested by chef. \n4.Update own profile.\n5.Exit")
    choice = int(input(""))
    if choice==1:
        print("1.Add Customer \n2.Edit Customer \n3.Delete Customer \n4.View Customer")
        choice_manage_customers = int(input(""))
        if choice_manage_customers == 1:
            customer_name = input("Enter full name of the Customer.")
            add("customers_list.txt",customer_name.strip())
            print(f"{customer_name} added successfully.")
        elif choice_manage_customers == 2:
            customer_name = input("Enter the name of the Customer to edit").title()
            edit_customer(customer_name.strip())
            
        elif choice_manage_customers == 3:
            customer_name = input("Enter the customer's name to delete")
            delete_customer(customer_name.strip())
            print(f"{customer_name} deleted successfully.")
        elif choice_manage_customers == 4:
            view("customers_list.txt")
        else:
            print("Invalid Choice")
        sleep(1)
    elif choice == 2:
        print("1.View Menu \n2.Add in Menu \n3.Delete in Menu")
        choice_manage_menu = int(input(""))
        if choice_manage_menu == 1:
            view("menu.txt")
        elif choice_manage_menu == 2:
            add_food = input("What would you like to add?\n")
            in_category = int(input("Which category is the item?\n1.Appetizers\n2.Soups and Salads\n3.Main Course\n4.Seafood Specialities\n5.Deserts\n6.Beverages\n"))
            if in_category in [1,2,3,4,5,6]:
                if in_category == 1:
                    in_category = "Appetizers:"
                elif in_category == 2:
                    in_category = "Soups and Salads:"
                elif in_category == 3:
                    in_category = "Main Course:"
                elif in_category == 4:
                    in_category = "Seafood Specialities:"
                elif in_category == 5:
                    in_category = "Desserts:"
                elif in_category == 6:
                    in_category = "Beverages:"
                else:
                    print("Invalid Category")
                price_food = float(input("What price would you set for this item?"))
                with open("menu.txt","a+") as add_menu:
                    add_menu.seek(0)
                    content = add_menu.readlines()
                    new_content = []
                    found_category = False
                    for line in content:
                        new_content.append(line)
                        if line.strip() == in_category.strip():
                            found_category = True
                            new_content.append(f"{add_food}: {price_food}\n")
                with open("menu.txt","w") as update_menu:
                    update_menu.writelines(new_content)
                print(f"{add_food} added to {in_category.split(':')} successfully.")
                print("Thank you for your work.")
        sleep(1)
    elif choice == 3:
        with open("ingredients.txt","r") as ingredient_requested:
            ingredient_requested_list = ingredient_requested.read()
            print(ingredient_requested_list)
            request=input("Would you like to place and order for the ingredients?(y/n):")
            if request.lower() == "y":
                with open("ingredients.txt", "w") as file:
                    file.write("")  # Write empty string to clear the file
                print("order have been placed.")
                
    elif choice == 4:
        pass
    elif choice ==5:
        sleep(1)
        print("Thank you for your work.")
        break
    else:
        print("Invalid Option")