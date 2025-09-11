#Cohen–Sutherland algorithm

import turtle

#regin codes
inside = 0
left = 1
right =2
bottom = 4
top = 8

def calculate_code(x,y):
    code = inside
    if x < xmin:
        code = code | left
    elif x > xmax:
        code = code | right
    if y < ymin:
        code = code | bottom
    elif y > ymax:
        code = code | top
    return code

'''
This will return dictionary of clipped line coordinates if line is accepted
{
    ïnside": true/false/"partially",
    ïnsidewindow": [(x1,y1),(x2,y2)]/None
    "outsidewindow": [[(x1_out,y1_out),(x2_out,y2_out)],[[(x1_out,y1_out),(x2_out,y2_out)]]]/None
}
the points of outside window will be used to print line with dotted pattern to show its outside the window and poins 
of inside window will be used to print line with solid pattern to show its inside the window

the outside windoe cordniate willbe the cordinates of line from windoe boundary to the line end point which is outside the window
'''
def calculate_clip(x1,y1,x2,y2):
    # Store original coordinates
    orig_x1, orig_y1 = x1, y1
    orig_x2, orig_y2 = x2, y2
    
    code1 = calculate_code(x1,y1)
    code2 = calculate_code(x2,y2)
    accept = False
    reutrn_dict = {}

    while True:
        if code1==0 and code2==0:
            # Line is completely inside
            accept = True
            break
        elif (code1 & code2) !=0:
            # Line is completely outside
            reutrn_dict["inside"] = False
            reutrn_dict["insidewindow"] = None
            reutrn_dict["outsidewindow"] = [[(orig_x1,orig_y1),(orig_x2,orig_y2)]]
            return reutrn_dict
        else:

            if code1 !=0:
                code_out = code1
            else:
                code_out = code2
            
            if code_out & top:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif code_out & bottom:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif code_out & right:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif code_out & left:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin
                
            if code_out == code1:
                x1,y1 = x,y
                code1 = calculate_code(x1,y1)
            else:
                x2,y2 = x,y
                code2 = calculate_code(x2,y2)
    
    # Handle the results based on what happened
    if accept:
        # Check if line was clipped or was originally completely inside
        if (orig_x1 == x1 and orig_y1 == y1 and orig_x2 == x2 and orig_y2 == y2):
            # Line was completely inside originally
            reutrn_dict["inside"] = True
            reutrn_dict["insidewindow"] = [(x1,y1),(x2,y2)]
            reutrn_dict["outsidewindow"] = None
        else:
            # Line was partially inside (clipped)
            reutrn_dict["inside"] = "partially"
            reutrn_dict["insidewindow"] = [(x1,y1),(x2,y2)]
            
            # Calculate outside segments
            outside_segments = []
            
            # Check if first point was clipped
            if orig_x1 != x1 or orig_y1 != y1:
                outside_segments.append([(orig_x1, orig_y1), (x1, y1)])
            
            # Check if second point was clipped
            if orig_x2 != x2 or orig_y2 != y2:
                outside_segments.append([(x2, y2), (orig_x2, orig_y2)])
            
            reutrn_dict["outsidewindow"] = outside_segments if outside_segments else None
    
    return reutrn_dict
            


def print_lines_and_screen(xmin, ymin, xmax, ymax, line_segments):
    turtle.speed(0)
    turtle.hideturtle()
    
    # Draw clipping window
    turtle.penup()
    turtle.goto(xmin, ymin)
    turtle.pendown()
    turtle.goto(xmax, ymin)
    turtle.goto(xmax, ymax)
    turtle.goto(xmin, ymax)
    turtle.goto(xmin, ymin)
    
    # Draw line segments
    for segment in line_segments:
        (x1, y1), (x2, y2), pattern = segment
        if pattern == "solid":
            turtle.penup()
            turtle.goto(x1, y1)
            turtle.pendown()
            turtle.goto(x2, y2)
        elif pattern == "dotted":
            # Draw dotted line
            distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
            steps = int(distance / 5)  # Adjust spacing of dots
            for i in range(steps + 1):
                t = i / steps
                x = x1 + t * (x2 - x1)
                y = y1 + t * (y2 - y1)
                if i % 2 == 0:  # Draw dot
                    turtle.penup()
                    turtle.goto(x, y)
                    turtle.pendown()
                    turtle.dot(3)  # Size of the dot

    turtle.done()



#take input for window size
x1_win,y1_win = map(int,input("Enter first corner of window (x1 y1): ").split())
x2_win,y2_win = map(int,input("Enter second corner of window (x2 y2): ").split())

# Automatically determine bottom-left and top-right corners
xmin = min(x1_win, x2_win)
xmax = max(x1_win, x2_win)
ymin = min(y1_win, y2_win)
ymax = max(y1_win, y2_win)

print(f"Window set: Bottom-left ({xmin}, {ymin}) to Top-right ({xmax}, {ymax})")

#take input for line endpoints
x1,y1 = map(int,input("Enter first endpoint of line (x1 y1): ").split())
x2,y2 = map(int,input("Enter second endpoint of line (x2 y2): ").split())

# Calculate clipping
result = calculate_clip(x1, y1, x2, y2)

line_segments = []
if result["inside"] == True:
    line_segments.append((result["insidewindow"][0], result["insidewindow"][1], "solid"))
elif result["inside"] == "partially":
    line_segments.append((result["insidewindow"][0], result["insidewindow"][1], "solid"))
    if result["outsidewindow"]:
        for outside_segment in result["outsidewindow"]:
            line_segments.append((outside_segment[0], outside_segment[1], "dotted"))
elif result["inside"] == False:
    if result["outsidewindow"]:
        for outside_segment in result["outsidewindow"]:
            line_segments.append((outside_segment[0], outside_segment[1], "dotted"))
            
# Print lines and clipping window
print_lines_and_screen(xmin, ymin, xmax, ymax, line_segments)

