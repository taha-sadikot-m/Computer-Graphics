"""
Pi Infinite Value Visualization using Turtle Graphics
A beautiful animation that displays the digits of pi in a circular spiral pattern
"""

import turtle
import math
import time
import colorsys

class PiVisualization:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.bgcolor("black")
        self.screen.title("Infinite Pi Visualization")
        self.screen.setup(width=800, height=800)
        self.screen.tracer(0)  # Turn off animation for faster drawing
        
        # Create turtle for drawing
        self.artist = turtle.Turtle()
        self.artist.speed(0)
        self.artist.penup()
        self.artist.color("white")
        
        # Animation parameters
        self.radius = 50
        self.angle_increment = 15  # degrees per digit
        self.radius_increment = 8   # spiral growth
        self.current_angle = 0
        self.digit_count = 0
        
        # Pi digits (we'll use a string of pi digits for better precision)
        self.pi_string = self.get_pi_digits()
        self.current_index = 0
        
        # Color settings
        self.colors = self.generate_colors(10)  # 10 colors for digits 0-9
        
    def get_pi_digits(self):
        """
        Returns a string of pi digits. For more precision, you could use
        external libraries like mpmath or pre-computed pi digits.
        """
        # Using built-in math.pi and extending with known digits
        pi_extended = ("3.1415926535897932384626433832795028841971693993751058209749445923"
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
                      "2726042699227967823547816360093417216412199245863150302861829745557"
                      "0674983850549458858692699569092721079750930295532116534498720275596"
                      "0236480665499119881834797753566369807426542527862551818417574672890"
                      "9777727938000816470600161452491921732172147723501414419735685481613"
                      "6115735255213347574184946848523323907394143334547762416862518983569"
                      "4855620992192221842725502542568876717904946016746097659798123644576"
                      "2654010976639504638210322391948231366510239971506299010517405791643"
                      "7813063946537482364936997093266967565916184265154769173451184632456"
                      "8033065773568964743529211555269825506325860440092265859582969442969"
                      "6328028046001013087134230205982978255063258604400922658595829694429"
                      "696328028046001013087134230205982978255063258604400922658595829694")
        return pi_extended
    
    def generate_colors(self, num_colors):
        """Generate a list of beautiful colors for the digits"""
        colors = []
        for i in range(num_colors):
            hue = i / num_colors
            rgb = colorsys.hsv_to_rgb(hue, 0.8, 0.9)
            colors.append(rgb)
        return colors
    
    def get_digit_color(self, digit):
        """Get color for a specific digit (0-9)"""
        if digit.isdigit():
            return self.colors[int(digit)]
        return (1, 1, 1)  # White for non-digits like decimal point
    
    def draw_digit_at_position(self, x, y, digit):
        """Draw a digit at the specified position with appropriate color"""
        self.artist.goto(x, y)
        self.artist.color(self.get_digit_color(digit))
        
        # Make the digit size vary slightly based on its value for visual interest
        if digit.isdigit():
            font_size = 12 + int(digit)
        else:
            font_size = 16  # Decimal point slightly larger
            
        self.artist.write(digit, align="center", font=("Arial", font_size, "bold"))
    
    def calculate_spiral_position(self, angle, radius):
        """Calculate x, y position for spiral pattern"""
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        return x, y
    
    def animate_pi_digits(self):
        """Main animation loop to display pi digits in a spiral"""
        print("Starting Pi Visualization Animation...")
        print("Press 'q' to quit, 's' to slow down, 'f' to speed up")
        
        # Setup key bindings
        self.screen.onkey(self.quit_animation, "q")
        self.screen.onkey(self.slow_down, "s")
        self.screen.onkey(self.speed_up, "f")
        self.screen.listen()
        
        delay = 0.1  # Initial delay between digits
        
        while self.current_index < len(self.pi_string):
            # Get current digit
            current_digit = self.pi_string[self.current_index]
            
            # Calculate position in spiral
            x, y = self.calculate_spiral_position(self.current_angle, self.radius)
            
            # Draw the digit
            self.draw_digit_at_position(x, y, current_digit)
            
            # Update for next iteration
            self.current_angle += self.angle_increment
            if self.current_angle >= 360:
                self.current_angle = 0
                self.radius += self.radius_increment
            
            self.current_index += 1
            self.digit_count += 1
            
            # Update screen and add delay
            self.screen.update()
            time.sleep(delay)
            
            # Show progress every 50 digits
            if self.digit_count % 50 == 0:
                print(f"Displayed {self.digit_count} digits of pi...")
        
        print(f"Animation complete! Displayed {self.digit_count} digits of pi.")
        print("Click on the window to close.")
        self.screen.exitonclick()
    
    def draw_central_info(self):
        """Draw π symbol and information at the center"""
        self.artist.goto(0, 0)
        self.artist.color("gold")
        self.artist.write("π", align="center", font=("Arial", 36, "bold"))
        
        self.artist.goto(0, -30)
        self.artist.color("lightblue")
        self.artist.write("Infinite Digits", align="center", font=("Arial", 12, "normal"))
    
    def quit_animation(self):
        """Quit the animation"""
        print("Animation stopped by user.")
        self.screen.bye()
    
    def slow_down(self):
        """Placeholder for slowing down animation - would need global delay variable"""
        print("Speed controls would be implemented with global delay variable")
    
    def speed_up(self):
        """Placeholder for speeding up animation - would need global delay variable"""
        print("Speed controls would be implemented with global delay variable")
    
    def run(self):
        """Start the visualization"""
        print("Pi Infinite Value Visualization")
        print("===============================")
        
        # Draw central π symbol
        self.draw_central_info()
        
        # Start the animation
        self.animate_pi_digits()


def main():
    """Main function to run the pi visualization"""
    try:
        visualization = PiVisualization()
        visualization.run()
    except KeyboardInterrupt:
        print("\nAnimation interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()