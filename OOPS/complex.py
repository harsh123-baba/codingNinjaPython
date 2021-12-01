class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    
    def Print(self):
        print(self.real, "+ j", self.img)
    
    
    def Addition(self, c1):
        newreal = self.real + c1.real
        newimg = self.img + c1.img
        self.real = newreal
        self.img = newimg

    
    def Multi(self, c1):
        newreal = self.real * c1.real
        newimg = self.img * c1.img
        self.real = newreal
        self.img = newimg

    
c = Complex(3, 4)
c1 = Complex(3, 4)
c.Print()
c1.Print()
c.Addition(c1)
c.Print()