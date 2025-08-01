import matplotlib.pyplot as plot

def dda_circle(xc, yc, radius):
    points = []
    x = radius
    y = 0
    p = 1 - radius
    
    while x > y:
        points.append((xc + x, yc + y))
        points.append((xc - x, yc + y))
        points.append((xc + x, yc - y))
        points.append((xc - x, yc - y))
        points.append((xc + y, yc + x))
        points.append((xc - y, yc + x))
        points.append((xc + y, yc - x))
        points.append((xc - y, yc - x))
        
        y += 1
        
        if p <= 0:
            p += 2 * y + 1
        else:
            x -= 1
            p += 2 * (y - x) + 1
            
    return points

xc, yc, radius = input("Enter the center coordinates (xc, yc) and radius: ").split()
xc, yc, radius = map(int, (xc, yc, radius)) 


dda_points = dda_circle(xc, yc, radius)

for point in dda_points:
    plot.plot(point[0], point[1], 'ro')

plot.xlim(xc - radius - 1, xc + radius + 1)
plot.ylim(yc - radius - 1, yc + radius + 1)
plot.grid(color='gray', linestyle='--', linewidth=0.5)
plot.plot(*zip(*dda_points), marker='o', color='b', markersize=3, linewidth=1)
plot.title("DDA Circle Drawing Algorithm")
plot.xlabel("X-axis")
plot.ylabel("Y-axis")
plot.grid()
plot.show()
