a = []
with open(r"E:\Udemy Full course\Mail_sender\names.txt") as file:
    a.extend(file.read().splitlines())

for name in a:
    with open(fr"E:\Udemy Full course\Mail_sender\{name}.txt", mode="w") as letter:
        letter.write(f"Dear {name},\n"
                     "You are invited to my birthday this Saturday.\n"
                     "Hope you can make it!\n"
                     "Akhil")
