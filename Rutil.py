import tkinter as tk
import random

rubiks_moves = [
    "U", "U'", "U2",   
    "D", "D'", "D2",   
    "L", "L'", "L2",   
    "R", "R'", "R2",   
    "F", "F'", "F2",   
    "B", "B'", "B2"    
]
scramble = []
firstTry = True

def update_label():
    scramble = []
    global firstTry
    for i in range(random.randint(11, 20)):
      move = random.randint(0, 17)
      if firstTry == False:
        while rubiks_moves[move] == scramble[i]:
          move = random.randint(0, 17)
      scramble.append(rubiks_moves[move])
      firstTry = False
    theScramble = ' ,'.join(scramble)
    label.config(text=theScramble)

root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("300x150")

label = tk.Label(root, text="", wraplength=130, justify="center")
label.pack(pady=10)

button = tk.Button(root, text="Generate scramble", command=update_label)
button.pack(pady=10)

root.mainloop()
