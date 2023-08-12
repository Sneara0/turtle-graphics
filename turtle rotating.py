from turtle import *
import colorsys
speed(1)
pensize(2)
bgcolor("black")
h=0.0
for i in range(300):
    c=colorsys.hls_to_rgb(h,1,1)
    pencolor(c)
    h+=0.005
    circle(5-i,100)
   
    circle(5-i,100)
    rt(100)

done()

