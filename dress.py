import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def draw_curve():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        x = np.linspace(-10, 10, 400)
        y = a * x**2 + b * x + c

        plt.figure("Quadratic Curve")
        plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.title('Graph of the Quadratic Equation')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.show()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# GUI Setup
root = tk.Tk()
root.title("Quadratic Curve Plotter")

tk.Label(root, text="a:").grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

tk.Label(root, text="b:").grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

tk.Label(root, text="c:").grid(row=2, column=0)
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1)

draw_button = tk.Button(root, text="Draw Curve", command=draw_curve)
draw_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
