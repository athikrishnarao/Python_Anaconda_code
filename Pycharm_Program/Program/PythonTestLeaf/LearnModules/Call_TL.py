#Way 01
import PythonTestLeaf.LearnModules.TL_Modules

w = PythonTestLeaf.LearnModules.TL_Modules.a()
w.a1()
w.a2()

r = PythonTestLeaf.LearnModules.TL_Modules
print(r.Athi())

#Way 02
from PythonTestLeaf.LearnModules.TL_Modules import c
x= PythonTestLeaf.LearnModules.TL_Modules.c()
x.c1()

#way 03
from PythonTestLeaf.LearnModules.TL_Modules import b as B
#y = PythonTestLeaf.LearnModules.TL_Modules.b()
#y.b1()
x = B()
x.b1()

#Way 04
from PythonTestLeaf.LearnModules.TL_Modules import a as A , b as B
e = A()
f = B()
e.a2()
e.a1()
f.b1()


