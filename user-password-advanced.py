
infofile = open(r"C:\Users\ABDELHAMEED\Desktop\abonga\project X\info.txt", "a")
infofile = open(r"C:\Users\ABDELHAMEED\Desktop\abonga\project X\info.txt", "r")
# infofile = open(r"C:\Users\ABDELHAMEED\Desktop\abonga\project X\info.txt","r")
print("Hello to the system", end=" :\n")
if not bool(infofile.read()) :
    infofile = open(r"C:\Users\ABDELHAMEED\Desktop\abonga\project X\info.txt","w")
    adduser = input("add username here . ").strip().capitalize()
    addpassword = input("choose password here . ").strip()
    infofile.write(f"{adduser},{addpassword}\n")
    infofile.close()


while True :
    choose = input("choose (write number)\n1- \"log in\"\n2- \"make acc\"\n3- \"exit\"  . ").strip()
    
    if choose == "1" : 
            infofile = open(r"C:\Users\ABDELHAMEED\Desktop\abonga\project X\info.txt","r")
            print("=-" * 10)
            askuser = input("username : ").strip().capitalize()
            askpassword = input("password : ").strip()
            if f"{askuser},{askpassword}\n" in infofile.readlines() :
                print("=-" * 10)
                print(f"welcome to the system Mr.{askuser}")
            else :
                print("=-" * 10)
                print("username or password are not True")
    elif choose == "2": # make acc
        infofile = open(r"C:\Users\ABDELHAMEED\Desktop\abonga\project X\info.txt","a")
        print("=-" * 10)
        adduser = input("add username here . ").strip().capitalize()
        addpassword = input("choose password here . ").strip()
        infofile.write(f"{adduser},{addpassword}\n")
        infofile.close()
    elif choose == "3":
         print("The terminal has been close")
         break
    else :
        print("pls write number (1 , 2 , 3)")