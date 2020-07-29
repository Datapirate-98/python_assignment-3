1.1
class sides:
    def __init__(self,a,b,c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
a= int(input("a="))
b= int(input("b="))
c= int(input("c="))

class triangle(sides):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)

    def area(self):
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5        

t = triangle(a,b,c)
print(f"Area of the traingle: {t.area()}")


1.2
def filter_long_words(n,l):
    res = [i for i in l if len(i)>n]
    print(res)


2.1
def len_words(words):
    res = [len(i) for i in words]
    print(res)

2.2
def check_vowel(ch):
    if len(ch) == 1:
        ch = ch.lower()
        print(ch)
        if (ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u"):
            print("True")
        else:
            print("False")
    else:
        print("Must enter a charecter not string!")







