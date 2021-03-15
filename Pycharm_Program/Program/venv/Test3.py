"""def pyfunc(r):
    for x in range(r):
        print(' '*(r-x-1)+'+'*(2*x+1))
pyfunc(5)

tst ={"A":1,"B":2,"C":4}
x=list(tst.items())
y=list(reversed(x))
print(x,y)
lst =[1,2,3,4,5,6,7]
lst1 =[1,1,1]
x=list(map(lambda a,b : a**b , lst,(map(lambda a : a*2,lst1))))
print(x)
test_list = ["Apple", "Banana", "Guava", "Apricot", "Mango", "Avocados"]
start_letter = 'A'
print("The original list : " + str(test_list))
with_A = [x for x in test_list if x.startswith(start_letter)]
without_A = [x for x in test_list] #if x not in with_A]
print(with_A,without_A)
"""
file = open("gfg.txt", "r")
Counter = 0

# Reading from file
Content = file.read()
CoList = Content.split("\n")

for i in CoList:
    if i:
        Counter += 1

print("This is the number of lines in the file")
print(Counter)


