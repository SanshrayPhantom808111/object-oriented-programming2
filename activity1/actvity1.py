class IOstring:
    def __init__(self):
        self.str1 = " "
    def getstring(self):
        self.str1 = input("Enter a striiiiiiiiing fa")
    def upperstring(self):
        print("Result is", self.str1.upper())

str1 = IOstring()
str1.getstring()
str1.upperstring()