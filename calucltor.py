import tkinter as tk

class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator - Advanced Calculator for Analysts")
        self.root.geometry("420x600")
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(False, False)

        self.expression = ""

        # Display
        self.display = tk.Entry(
            root,
            font=("Segoe UI", 28),
            bg="#252526",
            fg="white",
            bd=0,
            justify="right",
            insertbackground="white"
        )
        self.display.pack(fill="both", padx=15, pady=20, ipady=20)

        # Button Frame
        frame = tk.Frame(root, bg="#1e1e1e")
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        buttons = [
            ["C", "(", ")", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):

                if text == "=":
                    color = "#0e639c"
                elif text in ["+", "-", "*", "/", "(", ")"]:
                    color = "#3a3d41"
                elif text == "C":
                    color = "#d13438"
                else:
                    color = "#2d2d30"

                btn = tk.Button(
                    frame,
                    text=text,
                    font=("Segoe UI", 18, "bold"),
                    bg=color,
                    fg="white",
                    bd=0,
                    activebackground="#555",
                    activeforeground="white",
                    command=lambda t=text: self.click(t)
                )

                btn.grid(
                    row=r,
                    column=c,
                    sticky="nsew",
                    padx=5,
                    pady=5
                )

        for i in range(5):
            frame.rowconfigure(i, weight=1)

        for i in range(4):
            frame.columnconfigure(i, weight=1)

    def click(self, value):
        if value == "C":
            self.expression = ""
            self.display.delete(0, tk.END)

        elif value == "=":
            try:
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.expression = result
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ""

        else:
            self.expression += str(value)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)


root = tk.Tk()
app = ModernCalculator(root)
root.mainloop()