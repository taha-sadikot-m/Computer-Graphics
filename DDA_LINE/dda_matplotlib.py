import matplotlib.pyplot as plot

def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    
    x_inc = dx / steps
    y_inc = dy / steps
    
    x, y = x1, y1
    points = []
    
    for _ in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc
    
    return points

x1, y1, x2, y2 = input("Enter the coordinates (x1, y1, x2, y2): ").split()
x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))

dda_points = dda_line(x1, y1, x2, y2)

for point in dda_points:
    plot.plot(point[0], point[1], 'ro')

plot.xlim(min(x1, x2) - 1, max(x1, x2) + 1)
plot.ylim(min(y1, y2) - 1, max(y1, y2) + 1)
plot.axhline(0, color='black',linewidth=0.5, ls='--')
plot.axvline(0, color='black',linewidth=0.5, ls='--')
plot.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plot.plot(*zip(*dda_points), marker='o', color='b', markersize=3, linewidth=1)

plot.title("DDA Line Drawing Algorithm")
plot.xlabel("X-axis")
plot.ylabel("Y-axis")
plot.grid()
plot.show()