# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
cnum = complex(input())
print("{:0.3f}".format((((cnum.real)**2)+((cnum.imag)**2))**(0.5)))
print("{:0.3f}".format(cmath.phase(cnum)))
