class Athi:
    def name(self,name):                      # Instance Methods
        print("Name is :",name)
    def age(self,age):
        print("age is :" , age)

    @classmethod                              # Class Methods
    def area(cls):
        print("Chennai")

    @staticmethod                             # Static Methods
    def address():
        print("11/15,Street")
x = Athi()
x.name('Krish')
x.address()
x.area()
x.age(20)