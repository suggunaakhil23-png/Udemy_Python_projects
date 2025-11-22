import random

print(r"""
 _    _                                         
| |  | |                                        
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                     
                     |___/                      

            WELCOME  TO  HANGMAN!
""")

easy_words = [
    "apple", "tiger", "pizza", "cloud", "train",
    "chair", "heart", "beach", "magic", "music",
    "phone", "light", "robot", "smile", "plant"
]

medium_words = [
    "python", "guitar", "rocket", "planet", "bridge",
    "castle", "forest", "silver", "dragon", "camera",
    "puzzle", "window", "island", "hammer", "memory"
]

hard_words = [
    "dynamite", "avalanche", "labyrinth", "quarantine", "hologram",
    "paradox", "vortex", "synthesis", "phenomenon", "algorithm",
    "cryptic", "monolith", "spectrum", "threshold", "particle"
]

hangman_stages = [
r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]

s = input("Enter your difficulty (Easy or Medium or Hard) : ")

if s.lower() == "easy":
    a = random.choice(easy_words)
    d = list(a)
    b = []
    for x in range(len(a)):
        b.append('_')
    print("Word to guess is ")
    for x in range(len(b)):
        print(b[x], end=" ")
    print()
    c = 0
    f = 0
    while c <= 6 or f <= len(b):
        e = input("Guess the letter:")
        if e in d:
            index = d.index(e)
            b[index] = e
            for x in range(len(b)):
                print(b[x], end=" ")
            print()
            print(hangman_stages[c])
            print("Lives left are ", end=" ")
            print(6 - c)
            f += 1
        else:
            c += 1
            print(hangman_stages[c])
            print("Lives left are ", end=" ")
            print(6 - c)
        if c == 6:
            print(hangman_stages[c])
            print("HangMan died :(")
            break
        elif c < 6 and f == len(b):
            print("HangMan is Saved and you guessed the word")
            break

if s.lower() == "medium":
    a = random.choice(medium_words)
    d = list(a)
    b = []
    for x in range(len(a)):
        b.append('_')
    print("Word to guess is ")
    for x in range(len(b)):
        print(b[x], end=" ")
    print()
    c = 0
    f = 0
    while c <= 6 or f <= len(b):
        e = input("Guess the letter:")
        if e in d:
            index = d.index(e)
            b[index] = e
            for x in range(len(b)):
                print(b[x], end=" ")
            print()
            print(hangman_stages[c])
            print("Lives left are ", end=" ")
            print(6 - c)
            f += 1
        else:
            c += 1
            print(hangman_stages[c])
            print("Lives left are ", end=" ")
            print(6 - c)
        if c == 6:
            print(hangman_stages[c])
            print("HangMan died :(")
            break
        elif c < 6 and f == len(b):
            print("HangMan is Saved and you guessed the word")
            break

if s.lower() == "hard":
    a = random.choice(hard_words)
    d = list(a)
    b = []
    for x in range(len(a)):
        b.append('_')
    print("Word to guess is ")
    for x in range(len(b)):
        print(b[x], end=" ")
    print()
    c = 0
    f = 0
    while c <= 6 or f <= len(b):
        e = input("Guess the letter:")
        if e in d:
            index = d.index(e)
            b[index] = e
            for x in range(len(b)):
                print(b[x], end=" ")
            print()
            print(hangman_stages[c])
            print("Lives left are ", end=" ")
            print(6 - c)
            f += 1
        else:
            c += 1
            print(hangman_stages[c])
            print("Lives left are ", end=" ")
            print(6 - c)
        if c == 6:
            print(hangman_stages[c])
            print("HangMan died :(")
            break
        elif c < 6 and f == len(b):
            print("HangMan is Saved and you guessed the word")
            break
