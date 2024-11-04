# ---------------------------Importing Modules----------------------

from GUI_Class import GuiCal   # Importing the GUI class for the calculator interface
from Calculator_Class import CalBack  # Importing the calculation logic class

# ---------------------------Initializing Classes----------------------

# Creating an instance of CalBack to handle calculation logic
cal_back = CalBack()

# Creating an instance of GuiCal, passing the calculation instance (cal_back) to connect the GUI with the calculator logic
gui_cal = GuiCal(cal_back)

# ---------------------------END---------------------
