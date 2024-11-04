# ---------------------------Calculator Functions----------------------

# ---------------------------Importing Modules----------------------

from Func_Arithmetics import get_operator  # Importing the get_operator function from the Func_Arithmetics module

# ---------------------------Creating Function Class----------------------

class CalBack:
    def __init__(self):
        # Initializing variables to store numbers and the selected operation
        self.initial = 0    # Stores the first number for calculations
        self.final = 0      # Stores the second number for calculations
        self.temp = 0       # Temporary variable to hold current input
        self.operation = None  # Stores the current operation to be performed

    # ---------------------------Backend Working----------------------

    def get_temp(self):
        # Returns the current temporary value (temp) for display or further processing
        return self.temp

    def read_nums(self, num):
        # Updates the temporary variable by adding the new digit
        # Allows multi-digit numbers to be formed from consecutive single-digit inputs
        self.temp = (self.temp * 10) + num
        return self.temp

    def operator_called(self, operation: str):
        # Stores the current temp value into initial if it’s not zero
        # Resets temp to zero and sets the operation
        if self.temp != 0:
            self.initial = self.temp
            self.temp = 0
        self.operation = get_operator(operation)  # Sets the chosen arithmetic operation

    def get_ans(self):
        # Executes the stored operation with initial and final numbers
        # Resets temp and updates initial with the result
        self.final = self.temp
        self.initial = self.operation(self.initial, self.final)  # Perform operation
        self.temp = 0  # Reset temp for next calculation
        return self.initial  # Return the result

    def clear_all(self):
        # Resets all variables to their default values to clear the calculator
        self.temp = 0
        self.initial = 0
        self.final = 0
        self.operation = None

    # ---------------------------END---------------------
