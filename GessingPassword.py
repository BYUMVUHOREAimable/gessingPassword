import os
from random import randint

pas = input("Send the password: ")

keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
        "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
        "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
        "Y", "Z"]

pwg = ""
while pwg != pas:
    pwg = ""
    for i in range(len(pas)):
        guessPass = keys[randint(0, len(keys) - 1)]
        pwg += str(guessPass)
    
    print(pwg)
    print("Attacking... please wait!")
    os.system("cls")  # Change to "clear" if using Linux/macOS

print(f"The pass is: {pwg}")
