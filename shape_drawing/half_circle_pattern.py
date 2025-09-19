import turtle as t

t.speed(0)
t.bgcolor('black')
t.pencolor('red')

for i in range(170):
   t.rt(i)
   t.circle(150,i)
   t.fd(i)
   t.rt(80)

t.done()

