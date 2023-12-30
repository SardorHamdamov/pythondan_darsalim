import turtle as t
import colorsys
t.bgcoler("black")
h=1
t.tracer(200)
t.pensize(1)
def drawin(a,n):
    t.cirle(5+n,60)
    t.right(a)
    t.circle(5+n,60)
t.goto(0,0)
for i in range(600):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+=0.005
    t.pencolor(c)
    draw(1/2,0)
    draw(180,1)
t.done()
