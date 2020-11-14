import lec_3_my_module
print(lec_3_my_module.a)
b = lec_3_my_module.a* *2
print(b)

import lec_3_my_module as mm
print(mm.a)
print(mm.a/(1 - mm.a* *3))

from lec_3_my_module import a
print(a)

from lec_3_my_module import a, b
from  lec_3_my_moduleimport *
print(a*b - c)

from lec_3_my_module import gravity_constant as G
g = 500*G/10*2
print(g)
