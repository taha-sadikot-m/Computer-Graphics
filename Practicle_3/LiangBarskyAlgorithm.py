# Liang-Barsky line clipping algorithm with turtle graphics
import turtle
import time

def liang_barsky_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    """
    Liang-Barsky line clipping algorithm
    Returns clipped line coordinates or None if line is completely outside
    """
    dx = x2 - x1
    dy = y2 - y1

    p = [-dx, dx, -dy, dy]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]

    t0, t1 = 0.0, 1.0

    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return None  # Line is parallel and outside the clipping window
        else:
            r = q[i] / p[i]
            if p[i] < 0:
                if r > t1:
                    return None  # Line is outside the clipping window
                elif r > t0:
                    t0 = r  # Update t0
            else:
                if r < t0:
                    return None  # Line is outside the clipping window
                elif r < t1:
                    t1 = r  # Update t1

    clipped_x1 = x1 + t0 * dx
    clipped_y1 = y1 + t0 * dy
    clipped_x2 = x1 + t1 * dx
    clipped_y2 = y1 + t1 * dy

    return (clipped_x1, clipped_y1, clipped_x2, clipped_y2)

def draw_clipping_window(turtle_obj, xmin, ymin, xmax, ymax):
    """Draw the clipping window rectangle"""
    turtle_obj.penup()
    turtle_obj.goto(xmin, ymin)
    turtle_obj.pendown()
    turtle_obj.pencolor("blue")
    turtle_obj.pensize(3)
    
    # Draw rectangle
    turtle_obj.goto(xmax, ymin)
    turtle_obj.goto(xmax, ymax)
    turtle_obj.goto(xmin, ymax)
    turtle_obj.goto(xmin, ymin)
    
    # Add labels
    turtle_obj.penup()
    turtle_obj.goto(xmin - 20, ymin - 20)
    turtle_obj.write(f"({xmin},{ymin})", font=("Arial", 10, "normal"))
    turtle_obj.goto(xmax + 10, ymax + 10)
    turtle_obj.write(f"({xmax},{ymax})", font=("Arial", 10, "normal"))

def draw_original_line(turtle_obj, x1, y1, x2, y2):
    """Draw the original line before clipping"""
    turtle_obj.penup()
    turtle_obj.goto(x1, y1)
    turtle_obj.pencolor("red")
    turtle_obj.pensize(2)
    turtle_obj.pendown()
    turtle_obj.goto(x2, y2)
    
    # Mark endpoints
    turtle_obj.penup()
    turtle_obj.goto(x1, y1)
    turtle_obj.dot(8, "red")
    turtle_obj.goto(x2, y2)
    turtle_obj.dot(8, "red")
    
    # Label endpoints
    turtle_obj.goto(x1 - 30, y1 + 15)
    turtle_obj.write(f"P1({x1},{y1})", font=("Arial", 9, "normal"))
    turtle_obj.goto(x2 + 15, y2 + 15)
    turtle_obj.write(f"P2({x2},{y2})", font=("Arial", 9, "normal"))

def draw_clipped_line(turtle_obj, clipped_coords):
    """Draw the clipped line"""
    if clipped_coords is None:
        # Line is completely outside
        turtle_obj.penup()
        turtle_obj.goto(0, -250)
        turtle_obj.pencolor("black")
        turtle_obj.write("Line is completely OUTSIDE the clipping window!", 
                        align="center", font=("Arial", 14, "bold"))
        return
    
    x1, y1, x2, y2 = clipped_coords
    
    # Draw clipped line
    turtle_obj.penup()
    turtle_obj.goto(x1, y1)
    turtle_obj.pencolor("green")
    turtle_obj.pensize(4)
    turtle_obj.pendown()
    turtle_obj.goto(x2, y2)
    
    # Mark clipped endpoints
    turtle_obj.penup()
    turtle_obj.goto(x1, y1)
    turtle_obj.dot(10, "green")
    turtle_obj.goto(x2, y2)
    turtle_obj.dot(10, "green")
    
    # Label clipped endpoints
    turtle_obj.goto(x1 - 30, y1 - 25)
    turtle_obj.pencolor("green")
    turtle_obj.write(f"C1({x1:.1f},{y1:.1f})", font=("Arial", 9, "bold"))
    turtle_obj.goto(x2 + 15, y2 - 25)
    turtle_obj.write(f"C2({x2:.1f},{y2:.1f})", font=("Arial", 9, "bold"))
    
    # Status message
    turtle_obj.penup()
    turtle_obj.goto(0, -250)
    turtle_obj.pencolor("green")
    turtle_obj.write("Line CLIPPED successfully!", align="center", font=("Arial", 14, "bold"))

def setup_screen():
    """Setup turtle screen"""
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    screen.title("Liang-Barsky Line Clipping Algorithm")
    return screen

def create_turtle():
    """Create and configure turtle"""
    t = turtle.Turtle()
    t.speed(3)
    t.hideturtle()
    return t

def demonstrate_clipping():
    """Main demonstration function for single line clipping"""
    print("=== Liang-Barsky Line Clipping Algorithm ===")
    print("This program demonstrates single line clipping using turtle graphics")
    print()
    
    # Get clipping window coordinates
    print("Enter clipping window coordinates:")
    xmin = float(input("Enter xmin (left boundary): "))
    ymin = float(input("Enter ymin (bottom boundary): "))
    xmax = float(input("Enter xmax (right boundary): "))
    ymax = float(input("Enter ymax (top boundary): "))
    
    # Get line coordinates
    print("\nEnter line segment coordinates:")
    x1 = float(input("Enter x1 (start point x): "))
    y1 = float(input("Enter y1 (start point y): "))
    x2 = float(input("Enter x2 (end point x): "))
    y2 = float(input("Enter y2 (end point y): "))
    
    # Setup graphics
    screen = setup_screen()
    artist = create_turtle()
    
    # Clear screen and add title
    artist.penup()
    artist.goto(0, 250)
    artist.pencolor("black")
    artist.write("Liang-Barsky Line Clipping Algorithm", 
                align="center", font=("Arial", 16, "bold"))
    
    # Draw clipping window
    print("\nDrawing clipping window...")
    time.sleep(1)
    draw_clipping_window(artist, xmin, ymin, xmax, ymax)
    
    # Draw original line
    print("Drawing original line...")
    time.sleep(1)
    draw_original_line(artist, x1, y1, x2, y2)
    
    # Perform clipping
    print("Performing clipping algorithm...")
    time.sleep(1)
    clipped_result = liang_barsky_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax)
    
    # Display results
    print("\nClipping Results:")
    if clipped_result is None:
        print("Line is completely outside the clipping window")
    else:
        cx1, cy1, cx2, cy2 = clipped_result
        print(f"Original line: ({x1}, {y1}) to ({x2}, {y2})")
        print(f"Clipped line: ({cx1:.2f}, {cy1:.2f}) to ({cx2:.2f}, {cy2:.2f})")
    
    # Draw clipped line
    time.sleep(1)
    draw_clipped_line(artist, clipped_result)
    
    # Add legend
    artist.penup()
    artist.goto(-380, -200)
    artist.pencolor("black")
    artist.write("Legend:", font=("Arial", 12, "bold"))
    
    artist.goto(-380, -220)
    artist.pencolor("blue")
    artist.write("Blue: Clipping Window", font=("Arial", 10, "normal"))
    
    artist.goto(-380, -235)
    artist.pencolor("red")
    artist.write("Red: Original Line", font=("Arial", 10, "normal"))
    
    artist.goto(-380, -250)
    artist.pencolor("green")
    artist.write("Green: Clipped Line", font=("Arial", 10, "normal"))
    
    print("\nVisualization complete! Click on the graphics window to exit.")
    screen.exitonclick()

# Example usage and test cases
def run_test_cases():
    """Run some predefined test cases"""
    test_cases = [
        # Case 1: Line completely inside
        {"window": (-100, -100, 100, 100), "line": (-50, -50, 50, 50), "desc": "Line completely inside"},
        
        # Case 2: Line completely outside
        {"window": (-100, -100, 100, 100), "line": (150, 150, 200, 200), "desc": "Line completely outside"},
        
        # Case 3: Line partially inside
        {"window": (-100, -100, 100, 100), "line": (-150, 0, 150, 0), "desc": "Line crosses window horizontally"},
        
        # Case 4: Line crosses corner
        {"window": (-100, -100, 100, 100), "line": (-150, -150, 150, 150), "desc": "Line crosses diagonally"}
    ]
    
    print("Running test cases...")
    for i, case in enumerate(test_cases):
        print(f"\nTest Case {i+1}: {case['desc']}")
        xmin, ymin, xmax, ymax = case["window"]
        x1, y1, x2, y2 = case["line"]
        
        result = liang_barsky_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax)
        print(f"  Window: ({xmin}, {ymin}) to ({xmax}, {ymax})")
        print(f"  Original: ({x1}, {y1}) to ({x2}, {y2})")
        
        if result is None:
            print("  Result: Line completely outside")
        else:
            cx1, cy1, cx2, cy2 = result
            print(f"  Clipped: ({cx1:.2f}, {cy1:.2f}) to ({cx2:.2f}, {cy2:.2f})")

def clear_screen(artist):
    """Clear the screen for next drawing"""
    artist.clear()

def demonstrate_static_cases():
    """Demonstrate different clipping cases with static inputs and turtle graphics"""
    cases = [
        {
            "name": "Case 1: Line Completely Inside",
            "window": (-100, -100, 100, 100),
            "line": (-50, -30, 60, 40),
            "description": "Both endpoints are inside the clipping window"
        },
        {
            "name": "Case 2: Line Completely Outside",
            "window": (-100, -100, 100, 100),
            "line": (150, 150, 200, 200),
            "description": "Both endpoints are outside the clipping window"
        },
        {
            "name": "Case 3: Line Crosses Left and Right Boundaries",
            "window": (-100, -100, 100, 100),
            "line": (-150, 0, 150, 50),
            "description": "Line enters from left and exits from right"
        },
        {
            "name": "Case 4: Line Crosses Top and Bottom Boundaries",
            "window": (-100, -100, 100, 100),
            "line": (0, -150, 30, 150),
            "description": "Line enters from bottom and exits from top"
        },
        {
            "name": "Case 5: Line Crosses Corner to Corner",
            "window": (-100, -100, 100, 100),
            "line": (-150, -150, 150, 150),
            "description": "Line crosses diagonally through the window"
        },
        {
            "name": "Case 6: One Point Inside, One Outside",
            "window": (-100, -100, 100, 100),
            "line": (-50, -50, 150, 80),
            "description": "Start point inside, end point outside"
        },
        {
            "name": "Case 7: Horizontal Line Partially Clipped",
            "window": (-100, -100, 100, 100),
            "line": (-120, 50, 120, 50),
            "description": "Horizontal line crossing left and right boundaries"
        },
        {
            "name": "Case 8: Vertical Line Partially Clipped",
            "window": (-100, -100, 100, 100),
            "line": (50, -120, 50, 120),
            "description": "Vertical line crossing top and bottom boundaries"
        }
    ]
    
    print("=== Static Cases Demonstration ===")
    print("This will show 8 different clipping scenarios")
    print("Each case will be displayed in the same window")
    print("Click on the graphics window to proceed to the next case")
    print()
    
    # Setup graphics once for all cases
    screen = setup_screen()
    artist = create_turtle()
    
    # Add instruction text
    artist.penup()
    artist.goto(0, 270)
    artist.pencolor("purple")
    artist.write("Click anywhere on this window to proceed to Case 1", 
                align="center", font=("Arial", 14, "bold"))
    
    # Wait for first click to start
    screen.onclick(lambda x, y: None)
    screen.listen()
    
    for i, case in enumerate(cases):
        print(f"\nShowing {case['name']}")
        print(f"Description: {case['description']}")
        
        # Clear previous drawing
        clear_screen(artist)
        
        # Extract coordinates
        xmin, ymin, xmax, ymax = case["window"]
        x1, y1, x2, y2 = case["line"]
        
        # Add case title
        artist.penup()
        artist.goto(0, 250)
        artist.pencolor("black")
        artist.write(case["name"], align="center", font=("Arial", 16, "bold"))
        
        artist.goto(0, 230)
        artist.write(case["description"], align="center", font=("Arial", 12, "normal"))
        
        # Draw clipping window
        draw_clipping_window(artist, xmin, ymin, xmax, ymax)
        
        # Draw original line
        draw_original_line(artist, x1, y1, x2, y2)
        
        # Perform clipping
        clipped_result = liang_barsky_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax)
        
        # Draw clipped line
        draw_clipped_line(artist, clipped_result)
        
        # Add case-specific information
        artist.penup()
        artist.goto(-380, -180)
        artist.pencolor("black")
        artist.write("Case Details:", font=("Arial", 12, "bold"))
        
        artist.goto(-380, -200)
        artist.write(f"Window: ({xmin}, {ymin}) to ({xmax}, {ymax})", font=("Arial", 10, "normal"))
        
        artist.goto(-380, -215)
        artist.write(f"Original: ({x1}, {y1}) to ({x2}, {y2})", font=("Arial", 10, "normal"))
        
        if clipped_result is None:
            artist.goto(-380, -230)
            artist.pencolor("red")
            artist.write("Result: COMPLETELY OUTSIDE", font=("Arial", 10, "bold"))
        else:
            cx1, cy1, cx2, cy2 = clipped_result
            artist.goto(-380, -230)
            artist.pencolor("green")
            artist.write(f"Clipped: ({cx1:.1f}, {cy1:.1f}) to ({cx2:.1f}, {cy2:.1f})", font=("Arial", 10, "bold"))
            
            # Check if line was actually clipped
            if (abs(x1 - cx1) < 0.01 and abs(y1 - cy1) < 0.01 and 
                abs(x2 - cx2) < 0.01 and abs(y2 - cy2) < 0.01):
                artist.goto(-380, -245)
                artist.write("Status: COMPLETELY INSIDE (No clipping needed)", font=("Arial", 10, "normal"))
            else:
                artist.goto(-380, -245)
                artist.write("Status: PARTIALLY CLIPPED", font=("Arial", 10, "normal"))
        
        # Add legend
        artist.goto(200, -200)
        artist.pencolor("black")
        artist.write("Legend:", font=("Arial", 12, "bold"))
        
        artist.goto(200, -220)
        artist.pencolor("blue")
        artist.write("Blue: Clipping Window", font=("Arial", 10, "normal"))
        
        artist.goto(200, -235)
        artist.pencolor("red")
        artist.write("Red: Original Line", font=("Arial", 10, "normal"))
        
        artist.goto(200, -250)
        artist.pencolor("green")
        artist.write("Green: Clipped Result", font=("Arial", 10, "normal"))
        
        # Add navigation instruction
        if i < len(cases) - 1:
            artist.goto(0, -270)
            artist.pencolor("purple")
            artist.write(f"Click anywhere to continue to Case {i+2}", 
                        align="center", font=("Arial", 12, "bold"))
            
            # Wait for click to continue
            screen.onclick(lambda x, y: None)
            screen.listen()
        else:
            artist.goto(0, -270)
            artist.pencolor("purple")
            artist.write("All cases completed! Click to exit", 
                        align="center", font=("Arial", 12, "bold"))
    
    print("\nAll static cases demonstration completed!")
    print("Click on the graphics window to exit.")
    screen.exitonclick()

if __name__ == "__main__":
    print("=== Liang-Barsky Line Clipping Algorithm ===")
    print("Choose an option:")
    print("1. Interactive demonstration (Enter your own coordinates)")
    print("2. Run console test cases (Text output only)")
    print("3. Static cases demonstration (8 predefined visual cases)")
    
    choice = input("Enter your choice (1, 2, or 3): ")
    
    if choice == "1":
        demonstrate_clipping()
    elif choice == "2":
        run_test_cases()
        print("\nWould you like to see the interactive demonstration as well? (y/n)")
        if input().lower() == 'y':
            demonstrate_clipping()
    elif choice == "3":
        demonstrate_static_cases()
    else:
        print("Invalid choice. Running interactive demonstration...")
        demonstrate_clipping()
