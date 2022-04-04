class calculator:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def adder(self):
        return self.input1 + self.input2

    def subtractor(self):
        return self.input1 - self.input2

    def multiplier(self):
        return self.input1 * self.input2

    def divider(self):
        return self.input1 / self.input2

    def clear(self):
        self.input1 = 0
        self.input2 = 0

#asks the two operands from user
input1 = int(input("Enter the first operand: "))
input2 = int(input("Enter the second operand: "))

objCalc = calculator(input1, input2)

#addition of numbers
print("The output of", objCalc.input1, "+", objCalc.input2, "is", objCalc.adder())

#subtraction of numbers
print("The output of", objCalc.input1, "-", objCalc.input2, "is", objCalc.subtractor())

#multiplication of numbers
print("The output of", objCalc.input1, "*", objCalc.input2, "is", objCalc.multiplier())

#division of numbers
print("The output of", objCalc.input1, "/", objCalc.input2, "is", objCalc.divider())

#clearing the operands
objCalc.clear()
print("The first operand is now", objCalc.input1)
print("The second operand is now", objCalc.input2)

