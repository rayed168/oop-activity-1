class IOstring:
    def __init__(self):
        self.str1=""
    def get_string(self):
        self.str1=input("Enter a string : ")
    def upper_string(self):
        print("The result is",self.str1.upper())
str1=IOstring()
str1.get_string()
str1.upper_string()        