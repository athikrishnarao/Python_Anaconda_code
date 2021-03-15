class V:
    def applyBreak(self):
        print("Braking")
    def soundhorn(self):
        print("Horn High")
class car(V):
    def weels(self):
        print("4Weels")
class BMW(car):
    def applyBreak(self):
        print("ABS Breaking")
class Audi(car):
    def __init__(self):
        print("Hi")
x = V()
x.applyBreak()
x.soundhorn()
y= car()
y.weels()
z =BMW()
z.applyBreak()

a= Audi()
a.soundhorn()