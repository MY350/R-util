import tkinter as tk
import random

rubiks_moves = [
    "U", "U'", "U2",   # Up face
    "D", "D'", "D2",   # Down face
    "L", "L'", "L2",   # Left face
    "R", "R'", "R2",   # Right face
    "F", "F'", "F2",   # Front face
    "B", "B'", "B2"    # Back face
]
scramble = []

def update_label():
    for i in range(random.randint(11, 20)):
      move = random.randint(0, 17)
      scramble.append(rubiks_moves[move])
    theScramble = ' ,'.join(scramble)
    label.config(text=theScramble)

# Create the main application window
root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("300x150")

# Create a label
label = tk.Label(root, text="")
label.pack(pady=10)

# Create a button
button = tk.Button(root, text="Generate scramble", command=update_label)
button.pack(pady=10)

# Run the application
root.mainloop()
