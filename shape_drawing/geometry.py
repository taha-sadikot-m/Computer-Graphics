import turtle
import math
import random
import time

class InfiniteGeometry:
    def __init__(self):
        # Setup the screen
        self.screen = turtle.Screen()
        self.screen.bgcolor("black")
        self.screen.title("Mind-Blowing Infinite Geometry Animation")
        self.screen.setup(width=1200, height=800)
        self.screen.colormode(255)
        self.screen.tracer(0)  # Turn off animation for faster drawing
        
        # Create multiple turtles for different patterns
        self.spiral_turtle = turtle.Turtle()
        self.fractal_turtle = turtle.Turtle()
        self.circle_turtle = turtle.Turtle()
        self.polygon_turtle = turtle.Turtle()
        
        # Configure turtles
        self.setup_turtle(self.spiral_turtle)
        self.setup_turtle(self.fractal_turtle)
        self.setup_turtle(self.circle_turtle)
        self.setup_turtle(self.polygon_turtle)
        
        # Animation parameters
        self.angle = 0
        self.size_factor = 1
        self.color_shift = 0
        self.pattern_phase = 0
        
    def setup_turtle(self, t):
        """Configure turtle settings"""
        t.speed(0)
        t.pensize(2)
        t.hideturtle()
        
    def get_rainbow_color(self, offset=0):
        """Generate rainbow colors based on time and offset"""
        hue = (self.color_shift + offset) % 360
        # Convert HSV to RGB
        r = int(255 * (1 + math.cos(math.radians(hue))) / 2)
        g = int(255 * (1 + math.cos(math.radians(hue + 120))) / 2)
        b = int(255 * (1 + math.cos(math.radians(hue + 240))) / 2)
        return (r, g, b)
    
    def draw_spiraling_polygons(self):
        """Draw animated spiraling polygons"""
        self.spiral_turtle.clear()
        self.spiral_turtle.goto(0, 0)
        
        num_polygons = 8
        for i in range(num_polygons):
            # Calculate dynamic parameters
            size = 50 + i * 20 * self.size_factor
            sides = 3 + i
            rotation = self.angle + i * 45
            
            # Set rainbow color
            color = self.get_rainbow_color(i * 45)
            self.spiral_turtle.pencolor(color)
            
            # Move to starting position
            x = math.cos(math.radians(rotation)) * i * 30
            y = math.sin(math.radians(rotation)) * i * 30
            self.spiral_turtle.goto(x, y)
            self.spiral_turtle.setheading(rotation)
            
            # Draw polygon
            self.spiral_turtle.pendown()
            for _ in range(sides):
                self.spiral_turtle.forward(size)
                self.spiral_turtle.right(360 / sides)
            self.spiral_turtle.penup()
    
    def draw_fractal_tree(self):
        """Draw animated fractal tree patterns"""
        self.fractal_turtle.clear()
        
        # Draw multiple fractal trees
        positions = [(200, -200), (-200, -200), (0, 150), (300, 0), (-300, 0)]
        
        for i, pos in enumerate(positions):
            self.fractal_turtle.goto(pos)
            self.fractal_turtle.setheading(90 + math.sin(self.angle * 0.02 + i) * 30)
            
            color = self.get_rainbow_color(i * 72)
            self.fractal_turtle.pencolor(color)
            
            branch_length = 80 + math.sin(self.angle * 0.03 + i) * 20
            self.draw_fractal_branch(branch_length, 4)
    
    def draw_fractal_branch(self, length, depth):
        """Recursive fractal branch drawing"""
        if depth == 0 or length < 5:
            return
        
        self.fractal_turtle.pendown()
        self.fractal_turtle.forward(length)
        
        # Right branch
        self.fractal_turtle.right(30 + math.sin(self.angle * 0.01) * 15)
        self.draw_fractal_branch(length * 0.7, depth - 1)
        
        # Left branch
        self.fractal_turtle.left(60 + math.sin(self.angle * 0.01) * 30)
        self.draw_fractal_branch(length * 0.7, depth - 1)
        
        # Return to original position and heading
        self.fractal_turtle.right(30 + math.sin(self.angle * 0.01) * 15)
        self.fractal_turtle.penup()
        self.fractal_turtle.backward(length)
    
    def draw_concentric_circles(self):
        """Draw animated concentric circles with varying patterns"""
        self.circle_turtle.clear()
        
        num_circles = 12
        for i in range(num_circles):
            # Calculate dynamic parameters
            radius = 20 + i * 25
            x_offset = math.cos(self.angle * 0.02 + i * 0.5) * 100
            y_offset = math.sin(self.angle * 0.02 + i * 0.5) * 50
            
            # Set position
            self.circle_turtle.goto(x_offset, y_offset - radius)
            
            # Set rainbow color
            color = self.get_rainbow_color(i * 30)
            self.circle_turtle.pencolor(color)
            
            # Draw circle with animated segments
            self.circle_turtle.pendown()
            segments = 36
            segment_angle = 360 / segments
            
            for j in range(segments):
                # Create pulsing effect
                if (j + int(self.angle * 0.5)) % 6 < 3:
                    self.circle_turtle.pendown()
                else:
                    self.circle_turtle.penup()
                
                arc_length = 2 * math.pi * radius / segments
                self.circle_turtle.forward(arc_length)
                self.circle_turtle.left(segment_angle)
            
            self.circle_turtle.penup()
    
    def draw_rotating_mandalas(self):
        """Draw rotating mandala patterns"""
        self.polygon_turtle.clear()
        
        centers = [(0, 0), (400, 200), (-400, 200), (400, -200), (-400, -200)]
        
        for center_idx, center in enumerate(centers):
            self.polygon_turtle.goto(center)
            
            # Draw mandala layers
            layers = 5
            for layer in range(layers):
                radius = 30 + layer * 25
                petals = 6 + layer * 2
                
                for petal in range(petals):
                    # Calculate petal position
                    petal_angle = (360 / petals) * petal + self.angle + center_idx * 30
                    x = center[0] + math.cos(math.radians(petal_angle)) * radius
                    y = center[1] + math.sin(math.radians(petal_angle)) * radius
                    
                    # Move to petal position
                    self.polygon_turtle.goto(x, y)
                    self.polygon_turtle.setheading(petal_angle + 90)
                    
                    # Set color
                    color = self.get_rainbow_color(petal * 15 + layer * 45 + center_idx * 72)
                    self.polygon_turtle.pencolor(color)
                    
                    # Draw petal
                    petal_size = 15 + math.sin(self.angle * 0.03 + petal) * 5
                    self.polygon_turtle.pendown()
                    for _ in range(3):  # Triangle petal
                        self.polygon_turtle.forward(petal_size)
                        self.polygon_turtle.right(120)
                    self.polygon_turtle.penup()
    
    def draw_infinity_loops(self):
        """Draw animated infinity symbol patterns"""
        self.spiral_turtle.goto(0, 0)
        
        # Draw multiple infinity loops at different scales and orientations
        for i in range(5):
            scale = 0.5 + i * 0.3
            rotation = i * 36 + self.angle * 0.5
            
            color = self.get_rainbow_color(i * 72)
            self.spiral_turtle.pencolor(color)
            
            # Save position
            start_x, start_y = 0, 0
            
            # Draw infinity loop
            self.spiral_turtle.pendown()
            for t in range(360):
                # Parametric infinity curve (lemniscate)
                angle_rad = math.radians(t * 2)
                r = scale * 100 / (1 + math.cos(angle_rad) ** 2)
                x = r * math.cos(angle_rad) * math.cos(math.radians(rotation))
                y = r * math.sin(angle_rad) * math.cos(angle_rad) * math.sin(math.radians(rotation)) + \
                    r * math.cos(angle_rad) * math.sin(math.radians(rotation))
                
                self.spiral_turtle.goto(start_x + x, start_y + y)
            
            self.spiral_turtle.penup()
    
    def animate(self):
        """Main animation loop"""
        try:
            while True:
                # Update animation parameters
                self.angle += 2
                self.color_shift += 3
                self.size_factor = 1 + 0.3 * math.sin(self.angle * 0.02)
                self.pattern_phase += 1
                
                # Cycle through different pattern combinations
                pattern_cycle = (self.pattern_phase // 200) % 4
                
                if pattern_cycle == 0:
                    self.draw_spiraling_polygons()
                    self.draw_concentric_circles()
                elif pattern_cycle == 1:
                    self.draw_fractal_tree()
                    self.draw_rotating_mandalas()
                elif pattern_cycle == 2:
                    self.draw_infinity_loops()
                    self.draw_spiraling_polygons()
                else:
                    self.draw_rotating_mandalas()
                    self.draw_concentric_circles()
                    self.draw_fractal_tree()
                
                # Update screen
                self.screen.update()
                time.sleep(0.03)  # Control animation speed
                
                # Reset angle to prevent overflow
                if self.angle > 36000:
                    self.angle = 0
                if self.color_shift > 36000:
                    self.color_shift = 0
                    
        except turtle.Terminator:
            pass
    
    def start_animation(self):
        """Start the infinite geometry animation"""
        print("Starting Mind-Blowing Infinite Geometry Animation!")
        print("Close the window to stop the animation.")
        self.animate()

def main():
    """Main function to run the infinite geometry animation"""
    geometry = InfiniteGeometry()
    geometry.start_animation()

if __name__ == "__main__":
    main()