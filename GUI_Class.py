# ---------------------------Importing Modules----------------------

from tkinter import *  # Importing tkinter library for GUI elements
from Calculator_Class import CalBack  # Importing the Calculator backend class

# ---------------------------Constants----------------------

# Setting color and font constants for the GUI
GRAY = "gray24"
AZURE = "azure"
DARK_GRAY = "gray9"
BLUE = "LightSteelBlue4"
FONT = ("Times New Roman", 9, "bold")
FONT2 = ("Times New Roman", 20, "bold")

# ---------------------------Creating GUI Class----------------------

class GuiCal():
    def __init__(self, calculator: CalBack):
        # ---------------------------Initializing Calculator Window----------------------

        self.calculator = calculator  # Initializing the calculator backend instance
        self.window = Tk()  # Creating the main window
        self.window.title("Calculator")  # Setting the window title
        self.window.config(bg=GRAY, padx=20, pady=20)  # Configuring background and padding

        # Creating the display canvas for showing numbers and results
        self.canvas = Canvas(width=380, height=150, bg=DARK_GRAY, highlightthickness=0)
        self.canvas.create_rectangle(10, 20, 370, 130, fill=BLUE)  # Creating a blue rectangle for display background
        # Display text in the center of the rectangle
        self.text_on_cal = self.canvas.create_text(190, 75, text="0", font=FONT2, fill=AZURE, width=320)
        self.canvas.grid(column=0, row=0, columnspan=4, pady=10)  # Placing canvas on grid

        # Creating number and operator buttons with appropriate properties
        # Each button has a command to call specific functions when pressed
        self.button_1 = Button(text="1", bg=GRAY, fg=AZURE, width=10, height=4, font=FONT, command=self.num_1)
        self.button_1.grid(column=0, row=1)

        self.button_2 = Button(text="2", bg=GRAY, fg=AZURE, width=10, height=4, font=FONT, command=self.num_2)
        self.button_2.grid(column=1, row=1)

        self.button_3 = Button(text="3", bg=GRAY, fg=AZURE, width=10, height=4, font=FONT, command=self.num_3)
        self.button_3.grid(column=2, row=1)

        self.button_add = Button(text="+", bg=GRAY, fg=AZURE, width=10, height=4, font=FONT, command=self.operator_add)
        self.button_add.grid(column=3, row=1)

        self.button_4 = Button(text="4", bg=GRAY, fg=AZURE, width=10, height=4, font=FONT, command=self.num_4)
        self.button_4.grid(column=0, row=2)

        self.button_5 = Button(text="5", bg=GRAY, fg=AZURE, width=10, height=4, font=FONT, command=self.num_5)
        self.button_5.grid(column=1, row=2)

        self.button_6 = Button(text="6", bg=GRAY, fg=AZURE, width=10, height=4, font=FONT, command=self.num_6)
        self.button_6.grid(column=2, row=2)

        self.button_sub = Button(text="-", bg=GRAY, fg=AZURE, width=10, height=4, font=FONT, command=self.operator_sub)
        self.button_sub.grid(column=3, row=2)

        self.button_7 = Button(text="7", bg=GRAY, fg=AZURE, width=10, height=4, font=FONT, command=self.num_7)
        self.button_7.grid(column=0, row=3)

        self.button_8 = Button(text="8", bg=GRAY, fg=AZURE, width=10, height=4, font=FONT, command=self.num_8)
        self.button_8.grid(column=1, row=3)

        self.button_9 = Button(text="9", bg=GRAY, fg=AZURE, width=10, height=4, font=FONT, command=self.num_9)
        self.button_9.grid(column=2, row=3)

        self.button_mult = Button(text="x", bg=GRAY, fg=AZURE, width=10, height=4, font=FONT, command=self.operator_multiply)
        self.button_mult.grid(column=3, row=3)

        self.button_0 = Button(text="0", bg=GRAY, fg=AZURE, width=10, height=4, font=FONT, command=self.num_0)
        self.button_0.grid(column=0, row=4)

        self.button_clear = Button(text="clear", bg=GRAY, fg=AZURE, width=10, height=4, font=FONT, command=self.clear)
        self.button_clear.grid(column=1, row=4)

        self.button_ans = Button(text="=", bg=GRAY, fg=AZURE, width=10, height=4, font=FONT, command=self.operator_ans)
        self.button_ans.grid(column=2, row=4)

        self.button_div = Button(text="/", bg=GRAY, fg=AZURE, width=10, height=4, font=FONT, command=self.operator_divide)
        self.button_div.grid(column=3, row=4)

        self.window.mainloop()  # Running the main loop to display the GUI

    # ---------------------------Initializing Calculator Commands----------------------

    # Methods to handle number button clicks
    # Each method updates the display with the entered number
    def num_1(self):
        new_text = self.calculator.read_nums(1)
        self.canvas.itemconfig(self.text_on_cal, text=f"{new_text}")

    def num_2(self):
        new_text = self.calculator.read_nums(2)
        self.canvas.itemconfig(self.text_on_cal, text=f"{new_text}")

    def num_3(self):
        new_text = self.calculator.read_nums(3)
        self.canvas.itemconfig(self.text_on_cal, text=f"{new_text}")

    def num_4(self):
        new_text = self.calculator.read_nums(4)
        self.canvas.itemconfig(self.text_on_cal, text=f"{new_text}")

    def num_5(self):
        new_text = self.calculator.read_nums(5)
        self.canvas.itemconfig(self.text_on_cal, text=f"{new_text}")

    def num_6(self):
        new_text = self.calculator.read_nums(6)
        self.canvas.itemconfig(self.text_on_cal, text=f"{new_text}")

    def num_7(self):
        new_text = self.calculator.read_nums(7)
        self.canvas.itemconfig(self.text_on_cal, text=f"{new_text}")

    def num_8(self):
        new_text = self.calculator.read_nums(8)
        self.canvas.itemconfig(self.text_on_cal, text=f"{new_text}")

    def num_9(self):
        new_text = self.calculator.read_nums(9)
        self.canvas.itemconfig(self.text_on_cal, text=f"{new_text}")

    def num_0(self):
        new_text = self.calculator.read_nums(0)
        self.canvas.itemconfig(self.text_on_cal, text=f"{new_text}")

    # Methods to handle operator button clicks
    # Each method calls operator_called in CalBack and updates the display
    def operator_add(self):
        self.calculator.operator_called("add")
        self.canvas.itemconfig(self.text_on_cal, text=F"{self.calculator.get_temp()}")

    def operator_sub(self):
        self.calculator.operator_called("sub")
        self.canvas.itemconfig(self.text_on_cal, text=F"{self.calculator.get_temp()}")

    def operator_multiply(self):
        self.calculator.operator_called("multiply")
        self.canvas.itemconfig(self.text_on_cal, text=F"{self.calculator.get_temp()}")

    def operator_divide(self):
        self.calculator.operator_called("divide")
        self.canvas.itemconfig(self.text_on_cal, text=F"{self.calculator.get_temp()}")

    # Method to handle the equals button, displaying the calculation result
    def operator_ans(self):
        self.canvas.itemconfig(self.text_on_cal, text=F"{self.calculator.get_ans()}")

    # Method to clear all inputs and reset the display
    def clear(self):
        self.calculator.clear_all()
        self.canvas.itemconfig(self.text_on_cal, text=F"{self.calculator.get_temp()}")

    # ---------------------------END---------------------
