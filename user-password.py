info = {
    "all" : [],
}
adduser = input("add username here . ").strip().capitalize()
addpassword = input("choose password here . ").strip()
info["all"].append([adduser,addpassword])

while True :
    choose = input("choose (write number)\n1- \"log in\"\n2- \"make acc\"\n3- \"exit\"  . ").strip()
    
    if choose == "1" : 
            print("=-" * 10)
            askuser = input("username : ").strip().capitalize()
            askpassword = input("password : ").strip()
            if [askuser, askpassword] in info["all"] :
                print("=-" * 10)
                print(f"welcome to the system Mr.{askuser}")
            else :
                print("=-" * 10)
                print("username or password are not True")
    elif choose == "2": # make acc
        print("=-" * 10)
        adduser = input("add username here . ").strip().capitalize()
        addpassword = input("choose password here . ").strip()
        info["all"].append([adduser,addpassword])
    elif choose == "3":
         print("The Terminal has been closed")
         break
    else :
        print("pls write number (1 , 2 , 3)")