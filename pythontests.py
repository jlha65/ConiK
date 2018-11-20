import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['lines.color'] = 'k'
mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['k'])

x = np.linspace(-9, 9, 400)
y = np.linspace(-5, 5, 400)
x, y = np.meshgrid(x, y)


def axes():
    plt.axhline(0, alpha=.1)
    plt.axvline(0, alpha=.1)

A = 5
B = -2
C = -1
axes()
plt.contour(x, y, (A*x**2 + B*x + C - y ), [0], colors='green')

# Focus.
# plt.plot(a, 0, '.')
# Directrix.
# plt.axvline(-a)

plt.show()
# a = 5
# b = 2
# c = 1
# axes()
# plt.contour(x, y,(a*x**2 + b*x + c), [0], colors='k')
# plt.show()








# import matplotlib.pyplot as plt 
# import numpy as np
# from sympy import sympify, lambdify
# from sympy.abc import x
# from sympy.abc import y

# fig = plt.figure(1) 
# ax = fig.add_subplot(111) 

# # set up axis 
# ax.spines['left'].set_position('zero') 
# ax.spines['right'].set_color('none') 
# ax.spines['bottom'].set_position('zero') 
# ax.spines['top'].set_color('none') 
# ax.xaxis.set_ticks_position('bottom') 
# ax.yaxis.set_ticks_position('left') 

# # setup x and y ranges and precision
# xx = np.arange(-0.5,5.5,0.01) 

# # draw my curve 
# myfunction=sympify(1/(x-2) + 1/(y-2))
# mylambdifiedfunction=lambdify(x,myfunction,'numpy')
# ax.plot(xx, mylambdifiedfunction(xx),zorder=100,linewidth=3,color='red') 

# #set bounds 
# ax.set_xbound(-1,6)
# ax.set_ybound(-4,4) 

# plt.show()






# import matplotlib.pyplot as plt
# from matplotlib.pyplot import contour

# a = .3
# axes()
# plt.contour(x, y, (y**2 - 4*a*x), [0], colors='k')
# plt.show()



# def show_shape(patch):
# 	ax=plt.gca()
# 	ax.add_patch(patch)
# 	plt.axis('scaled')
# 	# plt.show('r')

# def create_circle():
#     circle= plt.Circle((1,1), radius= 2)
#     return circle

# a=[]
# b=[]
# # y=0
# # x=-50

# for x in range(-50,50,1):
#     y=x**2+2*x+2
#     a.append(x)
#     b.append(y)
#     #x= x+1


# c = create_circle()
# show_shape(c)

# fig= plt.figure()
# # show_shape(fig)
# axes=fig.add_subplot(111)
# axes.plot(a,b)
# plt.show()
