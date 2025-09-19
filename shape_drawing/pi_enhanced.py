"""
Enhanced Pi Infinite Value Visualization using Turtle Graphics
Features multiple visualization modes and improved visual effects
"""

import turtle
import math
import time
import colorsys
import random

class EnhancedPiVisualization:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.bgcolor("black")
        self.screen.title("Enhanced Infinite Pi Visualization")
        self.screen.setup(width=1000, height=1000)
        self.screen.tracer(0)
        
        # Create multiple turtles for different effects
        self.artist = turtle.Turtle()
        self.artist.speed(0)
        self.artist.penup()
        self.artist.color("white")
        
        self.tracer = turtle.Turtle()  # For drawing connecting lines
        self.tracer.speed(0)
        self.tracer.pensize(1)
        self.tracer.color("darkblue")
        
        # Animation parameters
        self.radius = 30
        self.angle_increment = 12
        self.radius_increment = 3
        self.current_angle = 0
        self.digit_count = 0
        self.mode = "spiral"  # "spiral", "circle", "wave"
        
        # Pi digits with higher precision
        self.pi_string = self.get_extended_pi_digits()
        self.current_index = 0
        
        # Visual effects
        self.colors = self.generate_rainbow_colors(10)
        self.show_connections = True
        self.fade_effect = True
        self.previous_positions = []
        
        # Animation speed
        self.delay = 0.05
        
    def get_extended_pi_digits(self):
        """Extended pi digits for longer animation"""
        return ("3.1415926535897932384626433832795028841971693993751058209749445923"
               "0781640628620899862803482534211706798214808651328230664709384460955"
               "0582231725359408128481117450284102701938521105559644622948954930381"
               "9644288109756659334461284756482337867831652712019091456485669234603"
               "4861045432664821339360726024914127372458700660631558817488152092096"
               "2829254091715364367892590360011330530548820466521384146951941511609"
               "4330572703657595919530921861173819326117931051185480744623799627495"
               "6735188575272489122793818301194912983367336244065664308602139494639"
               "5224737190702179860943702770539217176293176752384674818467669405132"
               "0005681271452635608277857713427577896091736371787214684409012249534"
               "3014654958537105079227968925894234201995611212902196086403441815981"
               "3629774771309960518707211349999998372978049951059731732816096318595"
               "0244594553469083026425223082533446850352619311881710100031378387528"
               "8658753320838142061717766914730359825349042875546873115956286388235"
               "3787593751957781857780532171226806613001927876611195909216420198938"
               "3676362596148330440022572010654858632788659361533818279682303019520"
               "3530185296897572362259941389124972177528347913151574857242454150695"
               "9508295331168617278558890750983817546374649393192550604009277016711"
               "3900984882401285836160356370766010471018194295559619894676783744944"
               "8255379774726847104047534646208046684259069491293313677028998915210"
               "4752162056966024058038150193511253382430035587640247496473263914199"
               "2726042699227967823547816360093417216412199245863150302861829745557")
    
    def generate_rainbow_colors(self, num_colors):
        """Generate rainbow colors for digits"""
        colors = []
        for i in range(num_colors):
            hue = i / num_colors
            # Use HSV color space for vibrant colors
            rgb = colorsys.hsv_to_rgb(hue, 0.9, 1.0)
            colors.append(rgb)
        return colors
    
    def get_digit_color(self, digit):
        """Get color for digit with some randomization for visual appeal"""
        if digit.isdigit():
            base_color = self.colors[int(digit)]
            # Add slight random variation to make it more dynamic
            variation = 0.1
            r, g, b = base_color
            r = max(0, min(1, r + random.uniform(-variation, variation)))
            g = max(0, min(1, g + random.uniform(-variation, variation)))
            b = max(0, min(1, b + random.uniform(-variation, variation)))
            return (r, g, b)
        return (1, 1, 1)  # White for decimal point
    
    def calculate_position(self, index, digit):
        """Calculate position based on current mode"""
        if self.mode == "spiral":
            return self.calculate_spiral_position(self.current_angle, self.radius)
        elif self.mode == "circle":
            return self.calculate_circle_position(index)
        elif self.mode == "wave":
            return self.calculate_wave_position(index, digit)
        else:
            return self.calculate_spiral_position(self.current_angle, self.radius)
    
    def calculate_spiral_position(self, angle, radius):
        """Spiral pattern - original method"""
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        return x, y
    
    def calculate_circle_position(self, index):
        """Circular pattern with multiple rings"""
        ring = index // 36  # 36 digits per ring
        position_in_ring = index % 36
        ring_radius = 50 + ring * 25
        angle = position_in_ring * 10  # 10 degrees between digits
        
        x = ring_radius * math.cos(math.radians(angle))
        y = ring_radius * math.sin(math.radians(angle))
        return x, y
    
    def calculate_wave_position(self, index, digit):
        """Wave pattern based on digit values"""
        x = (index * 5) - 400  # Spread horizontally
        if digit.isdigit():
            y = int(digit) * 20 - 100  # Height based on digit value
        else:
            y = 0
        return x, y
    
    def draw_digit_with_effects(self, x, y, digit, index):
        """Draw digit with various visual effects"""
        self.artist.goto(x, y)
        self.artist.color(self.get_digit_color(digit))
        
        # Variable font size based on digit value and position
        if digit.isdigit():
            base_size = 10
            digit_value = int(digit)
            size_variation = digit_value + (index % 5)
            font_size = base_size + size_variation
        else:
            font_size = 20  # Decimal point
        
        # Add glow effect for special digits
        if digit in ['3', '1', '4', '1', '5', '9']:  # First few digits of pi
            self.artist.color("gold")
            font_size += 2
        
        self.artist.write(digit, align="center", font=("Arial", font_size, "bold"))
        
        # Store position for connecting lines
        if self.show_connections:
            self.previous_positions.append((x, y))
            if len(self.previous_positions) > 1:
                self.draw_connection_line()
    
    def draw_connection_line(self):
        """Draw connecting lines between digits"""
        if len(self.previous_positions) >= 2:
            prev_x, prev_y = self.previous_positions[-2]
            curr_x, curr_y = self.previous_positions[-1]
            
            self.tracer.penup()
            self.tracer.goto(prev_x, prev_y)
            self.tracer.pendown()
            self.tracer.goto(curr_x, curr_y)
            self.tracer.penup()
    
    def draw_central_display(self):
        """Enhanced central display with more information"""
        # Pi symbol
        self.artist.goto(0, 20)
        self.artist.color("gold")
        self.artist.write("π", align="center", font=("Arial", 48, "bold"))
        
        # Information text
        self.artist.goto(0, -20)
        self.artist.color("lightblue")
        self.artist.write("Infinite Precision", align="center", font=("Arial", 14, "normal"))
        
        self.artist.goto(0, -40)
        self.artist.color("lightgreen")
        self.artist.write(f"Mode: {self.mode.title()}", align="center", font=("Arial", 12, "normal"))
        
        # Draw decorative circle
        self.artist.goto(0, -80)
        self.artist.pendown()
        self.artist.color("darkblue")
        self.artist.circle(15)
        self.artist.penup()
    
    def animate_pi_digits(self):
        """Enhanced animation loop with multiple modes"""
        print(f"Starting Enhanced Pi Visualization - Mode: {self.mode}")
        print("Controls:")
        print("  'q' - Quit")
        print("  's' - Slower")
        print("  'f' - Faster") 
        print("  'm' - Change mode")
        print("  'c' - Toggle connections")
        
        # Setup key bindings
        self.screen.onkey(self.quit_animation, "q")
        self.screen.onkey(self.change_mode, "m")
        self.screen.onkey(self.toggle_connections, "c")
        self.screen.onkey(self.slow_down, "s")
        self.screen.onkey(self.speed_up, "f")
        self.screen.listen()
        
        while self.current_index < len(self.pi_string):
            current_digit = self.pi_string[self.current_index]
            
            # Calculate position based on current mode
            x, y = self.calculate_position(self.current_index, current_digit)
            
            # Draw digit with effects
            self.draw_digit_with_effects(x, y, current_digit, self.current_index)
            
            # Update parameters for next iteration
            self.update_animation_parameters()
            
            self.current_index += 1
            self.digit_count += 1
            
            # Progress updates
            if self.digit_count % 100 == 0:
                print(f"Displayed {self.digit_count} digits... (Mode: {self.mode})")
            
            # Update screen
            self.screen.update()
            time.sleep(self.delay)
        
        print(f"Animation complete! Displayed {self.digit_count} digits of π")
        print("Click anywhere to close the window.")
        self.screen.exitonclick()
    
    def update_animation_parameters(self):
        """Update animation parameters based on current mode"""
        if self.mode == "spiral":
            self.current_angle += self.angle_increment
            if self.current_angle >= 360:
                self.current_angle = 0
                self.radius += self.radius_increment
    
    def change_mode(self):
        """Cycle through different visualization modes"""
        modes = ["spiral", "circle", "wave"]
        current_index = modes.index(self.mode)
        self.mode = modes[(current_index + 1) % len(modes)]
        print(f"Switched to {self.mode} mode")
        
        # Reset parameters for new mode
        if self.mode == "spiral":
            self.radius = 30
            self.current_angle = 0
    
    def toggle_connections(self):
        """Toggle connection lines between digits"""
        self.show_connections = not self.show_connections
        print(f"Connection lines: {'ON' if self.show_connections else 'OFF'}")
    
    def slow_down(self):
        """Decrease animation speed"""
        self.delay = min(0.5, self.delay + 0.02)
        print(f"Speed: {1/self.delay:.1f} digits/second")
    
    def speed_up(self):
        """Increase animation speed"""
        self.delay = max(0.01, self.delay - 0.02)
        print(f"Speed: {1/self.delay:.1f} digits/second")
    
    def quit_animation(self):
        """Quit the animation"""
        print("Animation stopped by user.")
        self.screen.bye()
    
    def run(self):
        """Start the enhanced visualization"""
        print("Enhanced Pi Infinite Value Visualization")
        print("="*40)
        
        # Draw central display
        self.draw_central_display()
        
        # Wait a moment to show the central display
        time.sleep(1)
        
        # Start animation
        self.animate_pi_digits()


def main():
    """Main function"""
    try:
        print("Choose visualization mode:")
        print("1. Spiral (default)")
        print("2. Concentric circles")
        print("3. Wave pattern")
        
        choice = input("Enter choice (1-3, or press Enter for spiral): ").strip()
        
        visualization = EnhancedPiVisualization()
        
        if choice == "2":
            visualization.mode = "circle"
        elif choice == "3":
            visualization.mode = "wave"
        else:
            visualization.mode = "spiral"
        
        visualization.run()
        
    except KeyboardInterrupt:
        print("\nAnimation interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()