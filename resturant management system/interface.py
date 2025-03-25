import chef
import admin

for i in range(1,4):
   
    username=input("enter your username:")
    password=input("enter your password:")


    admin_file=open("admin.txt","r")
    users = []
    passkey=[]
    for line in admin_file:
        for word in line.split():
            if "username:" in word:
                users.append(word.split("username:")[-1][:10])
            if "password:" in word:
                passkey.append(word.split("password:")[-1][:10])
   
    username_split=username.strip()
    password_split = password.strip()
    if username_split == users[0] and password_split == passkey[0]:
        admin.admin()
        break
        
    elif username_split == users[1] and password_split == passkey[1]: 
        print("welcome")
        break
    elif username_split == users[2] and password_split == passkey[2]:
        chef.chef()
        break


    else:
        print("wrong username or password (",3-i,"chances remaining )")