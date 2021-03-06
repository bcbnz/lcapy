from lcapy import Vdc, R, L, C
from matplotlib.pyplot import savefig, show
from numpy import linspace

a = Vdc(10) + R(0.1) + C(0.4) + L(0.2)

tv = linspace(0, 10, 1000)
a.Isc.transient_response().plot(tv)

savefig('series-VRLC1-isc.png')

show()


