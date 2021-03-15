class TestLeaf:
    cus_num = 78546915
    off_num = 22558899
    _host_num = 895623                         # Private Variable
    def pythonclass(self):
        print("Start Python Class")

    def AWS(self):
        print("Start AWS Class")

    def _DS(self):                             # Private Methods
        print("Start DS Class")

    def access_private_var(self):              # Access private variable via methods
        return TestLeaf._host_num

    def modify(self,new):                      # Modify the private variables
        TestLeaf._host_num = new

    def accessprivatemethods(self):            # Access private methods via public methods
        TestLeaf._DS(self)

x = TestLeaf()
x.AWS()
x.pythonclass()
print(x.off_num)
print(x.cus_num)
print(x.access_private_var())
x.accessprivatemethods()
x.modify('5588')
print(x.access_private_var())
