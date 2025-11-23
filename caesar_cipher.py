print(r"""
   _____                                   _____ _       _               
  / ____|                                 / ____(_)     | |              
 | |     __ _  ___  ___  ___  __ _ _ __  | |     _ _ __ | |__   ___ _ __ 
 | |    / _` |/ _ \/ __|/ _ \/ _` | '__| | |    | | '_ \| '_ \ / _ \ '__|
 | |___| (_| |  __/\__ \  __/ (_| | |    | |____| | |_) | | | |  __/ |   
  \_____\__,_|\___||___/\___|\__,_|_|     \_____|_| .__/|_| |_|\___|_|   
                                                  | |                    
                                                  |_|                    

                   CAESAR CIPHER
""")

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

a = int(input("Enter the Option :- 1 for Normal to Encryption and 2 for Encryption to Normal : "))
s = ""

if a == 1:
    b = input("Enter the Message you want to encrypt : ")
    c = int(input("Enter the Shifting amount : "))
    for x in b:
        if x.lower() in letters:
            i = letters.index(x.lower())
            new = (i + c) % 26
            s += letters[new]
        else:
            s += x
    print(s)

elif a == 2:
    b = input("Enter the Message you want to decrypt : ")
    c = int(input("Enter the Shifting amount : "))
    for x in b:
        if x.lower() in letters:
            i = letters.index(x.lower())
            new = (i - c) % 26
            s += letters[new]
        else:
            s += x
    print(s)
