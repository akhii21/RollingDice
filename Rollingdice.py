import tkinter as tk
import random
from PIL import Image, ImageTk

class DiceRollSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Dice Rolling Simulator")
        self.master.geometry("800x800")
        self.master.configure(bg="#2E4057")

        self.title_label = tk.Label(self.master, text="Roll the Dice!", font=('Arial', 24), fg="#FFFFFF", bg="#2E4057")
        self.title_label.pack(pady=20)

        self.dice_image = Image.open("die.jpeg")
        self.dice_photo = ImageTk.PhotoImage(self.dice_image)
        self.dice_label = tk.Label(self.master, image=self.dice_photo, bg="#2E4057")
        self.dice_label.pack(pady=20)

        self.roll_button = tk.Button(self.master, text="Roll", font=('Arial', 20), fg="black", bg="#008CBA", command=self.roll_dice)
        self.roll_button.pack(pady=20)

    def roll_dice(self):
        dice_value = random.randint(1, 6)
        dice_image = Image.open(f"dice{dice_value}.png")
        dice_photo = ImageTk.PhotoImage(dice_image)
        self.dice_label.configure(image=dice_photo)
        self.dice_label.image = dice_photo

root = tk.Tk()
DiceRollSimulator(root)
root.mainloop()
