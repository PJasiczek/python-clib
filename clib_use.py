import ctypes
import math
import matplotlib.pyplot as plt

speed_start = 0;

l = input("l [m]: ")
L = input("L [m]: ")
H = input("H [m]: ")
angle = input("Kąt nachylenia [°]: ")
radius = input("Promień [m]: ")

libc = ctypes.CDLL("./libclib.so")
libc.get_y_block.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
libc.get_y_block.restype = ctypes.c_double
y = libc.get_y_block(ctypes.c_double(float(l)), ctypes.c_double(float(L)), ctypes.c_double(float(H)),
                     ctypes.c_double(math.radians(float(angle))),ctypes.c_double(float(radius)))

print("\nPozycja środka bloczka: x -", l, "[m] y -", round(y,2), "[m] \n")

time = input("Przedział czasu [s]: ")

end_x = math.sqrt(pow(float(L),2) - pow((float(H)-(math.sin(math.radians(float(angle)))*float(radius))),2)) + math.cos(math.radians(float(angle)))*float(radius)

libc.speed_block.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)
libc.speed_block.restype=ctypes.c_double
speed_end = libc.speed_block(ctypes.c_double(float(l)), ctypes.c_double(float(y)), ctypes.c_double(float(end_x)),
                         ctypes.c_double(float(H)), ctypes.c_double(float(time)))

libc.acceleration_of_the_block.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.c_double)
libc.acceleration_of_the_block.restype=ctypes.c_double
acceleration = libc.acceleration_of_the_block(ctypes.c_double(float(speed_start)), ctypes.c_double(float(speed_end)), ctypes.c_double(float(time)))

print("\nPrędkość bloczka wynosi:  ", round(speed_end,4) , " [m/s]")
print("Przyśpieszenie bloczka wynosi:  ", round(acceleration,4), " [m/s²]")

line1,=plt.plot(l, round(y,2), 'ro', label="[x,y]")
plt.title('Wykres położenia bloczka w zależności od podanych prametrów')
plt.ylabel('y [m]')
plt.xlabel('x [m]')
first_legend = plt.legend(handles=[line1], loc=1)
ax = plt.gca().add_artist(first_legend)
plt.savefig('graph.png')
plt.show()

line2,=plt.plot([0, float(time)], [0, speed_end], label="prędkość")
plt.title('Wykres zależności prędkości od czasu')
plt.ylabel('Prędkość [m/s]')
plt.xlabel('Czas [s]')
plt.legend(handles=[line2], loc=4)
plt.savefig('graph1.png')
plt.show()

line3,=plt.plot([0, float(time)], [acceleration, acceleration], label="przyśpieszenie")
plt.title('Wykres zależności przyśpieszenia od czasu')
plt.ylabel('Przyśpieszenie [m/s²]')
plt.xlabel('Czas [s]')
plt.legend(handles=[line3], loc=4)
plt.savefig('graph2.png')
plt.show()