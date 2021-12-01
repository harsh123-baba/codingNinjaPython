class Fraction:
    def __init__(self, num, den):
        if den ==0:
            # throw error
            den = 1
        self.num = num
        self.den = den
    
    def Print(self):
        if self.num == 0:
            print(0)
        if self.den == 1:
            print(self.num)
        
        print(self.num , " / ", self.den)
    
    def simplify(self):
        current = min(self.num , self.den)
        
        while(current > 1):
            if self.num % current==0 and self.den% current == 0:
                break
            current-=1
        self.num = self.num//current
        self.den = self.den//current

    def Addition(self, n2):
        newnum = self.num*n2.den + n2.num* self.den
        newden = self.den * self.den 
        self.num = newnum
        self.den = newden
        self.simplify()

    def milti(self , n2):
        newden = self.den*n2.den
        newnum = self.num*n2.num
        self.num = newnum
        self.den = newden
        self.simplify()
f = Fraction(14, 6)
f.simplify()
f.Print()
f1 = Fraction(20, 10)
# f1.Print()
f1.simplify()
f1.Print()

f.Addition(f1)
f.Print()
f.milti(f1)
f.Print()


