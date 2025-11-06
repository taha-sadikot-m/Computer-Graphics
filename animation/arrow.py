# Create animation of arrow embedded into circle revolving around its center
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import matplotlib.patches as patches

def create_arrow_points(center_x, center_y, length, width, angle=0):
    """
    Creates points for an arrow shape.
    
    Args:
        center_x (float): X-coordinate of the arrow center.
        center_y (float): Y-coordinate of the arrow center.
        length (float): Length of the arrow.
        width (float): Width of the arrow shaft.
        angle (float): Rotation angle in radians.
    
    Returns:
        tuple: Arrays of x and y coordinates for arrow outline.
    """
    # Define arrow shape relative to origin
    arrow_length = length
    shaft_width = width
    head_width = width * 2
    head_length = length * 0.3
    shaft_length = length - head_length
    
    # Arrow points (starting from bottom left, going clockwise)
    points = np.array([
        [-shaft_length/2, -shaft_width/2],      # Bottom left of shaft
        [-shaft_length/2, shaft_width/2],       # Top left of shaft
        [shaft_length/2, shaft_width/2],        # Top right of shaft
        [shaft_length/2, head_width/2],         # Top of arrow head base
        [arrow_length/2, 0],                    # Arrow tip
        [shaft_length/2, -head_width/2],        # Bottom of arrow head base
        [shaft_length/2, -shaft_width/2],       # Bottom right of shaft
    ])
    
    # Apply rotation
    cos_a, sin_a = np.cos(angle), np.sin(angle)
    rotation_matrix = np.array([[cos_a, -sin_a], [sin_a, cos_a]])
    rotated_points = points @ rotation_matrix.T
    
    # Translate to center position
    x = rotated_points[:, 0] + center_x
    y = rotated_points[:, 1] + center_y
    
    return x, y

def create_circle_points(center_x, center_y, radius, num_points=100):
    """
    Creates points for a circle.
    
    Args:
        center_x (float): X-coordinate of the center.
        center_y (float): Y-coordinate of the center.
        radius (float): Radius of the circle.
        num_points (int): Number of points to create smooth circle.
    
    Returns:
        tuple: Arrays of x and y coordinates.
    """
    angles = np.linspace(0, 2*np.pi, num_points + 1)[:-1]
    x = center_x + radius * np.cos(angles)
    y = center_y + radius * np.sin(angles)
    return x, y

def rotate_point(x, y, center_x, center_y, angle):
    """
    Rotates a point around a center by given angle.
    
    Args:
        x, y (float): Point coordinates.
        center_x, center_y (float): Center of rotation.
        angle (float): Rotation angle in radians.
    
    Returns:
        tuple: New x, y coordinates after rotation.
    """
    cos_a, sin_a = np.cos(angle), np.sin(angle)
    
    # Translate to origin
    translated_x = x - center_x
    translated_y = y - center_y
    
    # Rotate
    rotated_x = translated_x * cos_a - translated_y * sin_a
    rotated_y = translated_x * sin_a + translated_y * cos_a
    
    # Translate back
    new_x = rotated_x + center_x
    new_y = rotated_y + center_y
    
    return new_x, new_y

def create_revolving_arrow_animation():
    """
    Creates the main animation of arrow embedded in circle revolving around center.
    """
    print("=== Revolving Arrow in Circle Animation ===")
    print()
    
    try:
        # Get animation parameters from user
        center_x, center_y = map(float, input("Enter center coordinates (x, y): ").split())
        circle_radius = float(input("Enter circle radius: "))
        arrow_length = float(input("Enter arrow length: "))
        arrow_width = float(input("Enter arrow width: "))
        revolution_radius = float(input("Enter revolution radius (distance from center): "))
        
        # Animation parameters
        total_frames = 200
        revolution_speed = 2 * np.pi / total_frames  # One complete revolution
        
        # Setup the plot
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Set limits to show full revolution path
        max_extent = revolution_radius + circle_radius + arrow_length
        ax.set_xlim(center_x - max_extent * 1.2, center_x + max_extent * 1.2)
        ax.set_ylim(center_y - max_extent * 1.2, center_y + max_extent * 1.2)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        
        # Create plot elements
        circle_line, = ax.plot([], [], 'b-', linewidth=2, label='Circle')
        circle_fill = ax.fill([], [], alpha=0.2, color='lightblue')[0]
        arrow_line, = ax.plot([], [], 'r-', linewidth=3, label='Arrow')
        arrow_fill = ax.fill([], [], alpha=0.7, color='red')[0]
        
        # Center point
        center_point, = ax.plot(center_x, center_y, 'ko', markersize=8, label='Center')
        
        # Revolution path (optional - shows the path the arrow+circle follows)
        revolution_circle_x, revolution_circle_y = create_circle_points(center_x, center_y, revolution_radius)
        ax.plot(revolution_circle_x, revolution_circle_y, '--', color='gray', alpha=0.5, label='Revolution Path')
        
        # Texts for information
        title_text = ax.text(0.5, 0.95, '', transform=ax.transAxes, 
                            fontsize=14, ha='center', weight='bold')
        info_text = ax.text(0.02, 0.02, '', transform=ax.transAxes, 
                           fontsize=10, ha='left')
        
        ax.legend(loc='upper right')
        
        def animate(frame):
            """
            Animation function called for each frame.
            
            Args:
                frame (int): Current frame number.
            """
            # Calculate revolution angle
            revolution_angle = frame * revolution_speed
            
            # Calculate new center position for the circle+arrow system
            current_center_x = center_x + revolution_radius * np.cos(revolution_angle)
            current_center_y = center_y + revolution_radius * np.sin(revolution_angle)
            
            # Create circle at current position
            circle_x, circle_y = create_circle_points(current_center_x, current_center_y, circle_radius)
            
            # Create arrow at current position (arrow also rotates as it revolves)
            arrow_rotation = revolution_angle  # Arrow points in direction of motion
            arrow_x, arrow_y = create_arrow_points(current_center_x, current_center_y, 
                                                 arrow_length, arrow_width, arrow_rotation)
            
            # Close the shapes
            circle_x = np.append(circle_x, circle_x[0])
            circle_y = np.append(circle_y, circle_y[0])
            arrow_x = np.append(arrow_x, arrow_x[0])
            arrow_y = np.append(arrow_y, arrow_y[0])
            
            # Update circle
            circle_line.set_data(circle_x, circle_y)
            circle_fill.set_xy(np.column_stack((circle_x, circle_y)))
            
            # Update arrow
            arrow_line.set_data(arrow_x, arrow_y)
            arrow_fill.set_xy(np.column_stack((arrow_x, arrow_y)))
            
            # Update texts
            angle_degrees = np.degrees(revolution_angle) % 360
            title_text.set_text(f"Arrow in Circle - Revolution Angle: {angle_degrees:.1f}°")
            info_text.set_text(f"Position: ({current_center_x:.1f}, {current_center_y:.1f})")
            
            return circle_line, circle_fill, arrow_line, arrow_fill, title_text, info_text
        
        # Create and run animation
        print(f"Starting animation:")
        print(f"- Center: ({center_x}, {center_y})")
        print(f"- Circle radius: {circle_radius}")
        print(f"- Arrow: {arrow_length}×{arrow_width}")
        print(f"- Revolution radius: {revolution_radius}")
        print("Close the window to exit...")
        
        ani = animation.FuncAnimation(fig, animate, frames=total_frames, 
                                    interval=50, blit=True, repeat=True)
        
        plt.title("Arrow Embedded in Circle - Revolving Animation")
        plt.tight_layout()
        plt.show()
        
        return ani
        
    except ValueError:
        print("Invalid input! Please enter numbers separated by spaces.")
    except Exception as e:
        print(f"An error occurred: {e}")

def create_static_demo():
    """
    Creates a static demonstration showing the arrow and circle at different positions.
    """
    print("\n=== Static Arrow-Circle Demonstration ===")
    
    try:
        center_x, center_y = map(float, input("Enter center coordinates (x, y): ").split())
        circle_radius = float(input("Enter circle radius: "))
        arrow_length = float(input("Enter arrow length: "))
        arrow_width = float(input("Enter arrow width: "))
        revolution_radius = float(input("Enter revolution radius: "))
        
        fig, axes = plt.subplots(2, 2, figsize=(12, 12))
        axes = axes.flatten()
        
        # Show arrow+circle at 4 different positions
        positions = [0, np.pi/2, np.pi, 3*np.pi/2]
        titles = ["0° (Right)", "90° (Top)", "180° (Left)", "270° (Bottom)"]
        
        for i, (angle, title) in enumerate(zip(positions, titles)):
            ax = axes[i]
            
            # Calculate position
            pos_x = center_x + revolution_radius * np.cos(angle)
            pos_y = center_y + revolution_radius * np.sin(angle)
            
            # Create shapes
            circle_x, circle_y = create_circle_points(pos_x, pos_y, circle_radius)
            arrow_x, arrow_y = create_arrow_points(pos_x, pos_y, arrow_length, arrow_width, angle)
            
            # Plot revolution path
            rev_x, rev_y = create_circle_points(center_x, center_y, revolution_radius)
            ax.plot(rev_x, rev_y, '--', color='gray', alpha=0.5, label='Revolution Path')
            
            # Plot circle
            ax.plot(circle_x, color='blue', linewidth=2, label='Circle')
            ax.fill(circle_x, circle_y, alpha=0.2, color='lightblue')
            
            # Plot arrow
            arrow_x = np.append(arrow_x, arrow_x[0])
            arrow_y = np.append(arrow_y, arrow_y[0])
            ax.plot(arrow_x, arrow_y, color='red', linewidth=3, label='Arrow')
            ax.fill(arrow_x, arrow_y, alpha=0.7, color='red')
            
            # Plot centers
            ax.plot(center_x, center_y, 'ko', markersize=8, label='Main Center')
            ax.plot(pos_x, pos_y, 'go', markersize=6, label='Current Center')
            
            # Set limits and labels
            max_extent = revolution_radius + circle_radius + arrow_length
            ax.set_xlim(center_x - max_extent * 1.1, center_x + max_extent * 1.1)
            ax.set_ylim(center_y - max_extent * 1.1, center_y + max_extent * 1.1)
            ax.set_aspect('equal')
            ax.grid(True, alpha=0.3)
            ax.set_title(title, fontsize=12, weight='bold')
            ax.set_xlabel('X-axis')
            ax.set_ylabel('Y-axis')
            
            if i == 0:  # Only show legend for first subplot
                ax.legend(loc='upper right', fontsize=8)
        
        plt.suptitle('Arrow in Circle - Static Positions', fontsize=16, weight='bold')
        plt.tight_layout()
        plt.show()
        
    except ValueError:
        print("Invalid input! Please enter numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """
    Main function to execute the revolving arrow program.
    """
    print("=== Revolving Arrow in Circle Animation Program ===")
    print("This program creates an arrow embedded in a circle that revolves around a center point.")
    print("The arrow rotates to always point in the direction of motion.")
    print()
    
    while True:
        print("=== Menu ===")
        print("1. Run Revolving Animation")
        print("2. Show Static Position Demo")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice (1-3): "))
            
            if choice == 1:
                animation_obj = create_revolving_arrow_animation()
                
            elif choice == 2:
                create_static_demo()
                
            elif choice == 3:
                print("Exiting program... Thank you!")
                break
                
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
                
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Exiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
        
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main() 
