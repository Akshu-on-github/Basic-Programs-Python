'''
write a program to obtain x,y,z form the user and calculate : 4x^4+3y^3+9z+6*3.141
solution='''

x,y,z=input("enter the values of x,y,z").split()
x,y,z=int(x),int(y),int(z)
print ("answer of expersion=",(pow((x*4),4)+pow((3*y),3)+9*z+6*3.141))