print(r"""
   _____                      _            _         _             
  / ____|                    | |          | |       | |            
 | (___   ___  ___ _ __   ___| |_ __ _  __| | ___   | |_ ___  _ __ 
  \___ \ / _ \/ _ \ '_ \ / _ \ __/ _` |/ _` |/ _ \  | __/ _ \| '__|
  ____) |  __/  __/ | | |  __/ || (_| | (_| | (_) | | || (_) | |   
 |_____/ \___|\___|_| |_|\___|\__\__,_|\__,_|\___/   \__\___/|_|   

                          🔨
                    SECRET AUCTION
""")
auction_list = {}
print("Welcome to The Seenetadotor(Secret Auction)")
def winner(auction_list):
    s = 0
    t = " "
    for key in auction_list:
        if auction_list[key] > s :
            t = key
            s = auction_list[key]
    print(f"The Winner of the Auction is : {t}")

def auction() :
    a = input("Enter your name : ")
    b = int(input("Enter the amount value you want to bid ? : $"))
    auction_list[a] = b
    c = input("Are there any other bidders? yes or no : ")
    if(c.lower() == "yes") :
        print("\n" * 100)
        auction()
    else :
        winner(auction_list)
auction()