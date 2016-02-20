import math

x = math.pi/4.0
y = math.sin(x)**2.0 + math.cos(x)**2.0
print y


v0 = 3 # m/s
t = 1 # s
a = 2 # m/s**2
s = v0*t + 0.5*a*t**2
print s


a = 3.3
b = 5.3
a2 = a**2
b2 = b**2

eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2

eq1_pow = (a + b)**2
eq2_pow = (a - b)**2

print 'first equation: ' + str(eq1_sum) + "=" + str(eq1_pow)
print 'Second equation: ' + str(eq2_pow) + "=" + str(eq2_pow)
