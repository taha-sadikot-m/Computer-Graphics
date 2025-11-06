# Create program to create animation of triangle transforming into circle and square
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

def create_triangle_points(center_x, center_y, radius, num_points=100):
    """
    Creates points for an equilateral triangle with specified number of points for smooth morphing.
    
    Args:
        center_x (float): X-coordinate of the center.
        center_y (float): Y-coordinate of the center.
        radius (float): Distance from center to vertices.
        num_points (int): Number of points to create smooth triangle outline.
    
    Returns:
        tuple: Arrays of x and y coordinates.
    """
    # Create the three vertices of an equilateral triangle
    vertices_angles = np.array([np.pi/2, np.pi/2 + 2*np.pi/3, np.pi/2 + 4*np.pi/3])  # Start from top
    vertices_x = center_x + radius * np.cos(vertices_angles)
    vertices_y = center_y + radius * np.sin(vertices_angles)
    
    # Create smooth triangle by interpolating along the edges
    points_per_side = num_points // 3
    remainder = num_points % 3
    
    x_points = []
    y_points = []
    
    for i in range(3):
        # Current vertex and next vertex
        curr_x, curr_y = vertices_x[i], vertices_y[i]
        next_x, next_y = vertices_x[(i + 1) % 3], vertices_y[(i + 1) % 3]
        
        # Number of points for this side (distribute remainder)
        side_points = points_per_side + (1 if i < remainder else 0)
        
        # Create points along this edge (excluding the last point to avoid duplication)
        if side_points > 0:
            t_values = np.linspace(0, 1, side_points + 1)[:-1]
            side_x = curr_x + t_values * (next_x - curr_x)
            side_y = curr_y + t_values * (next_y - curr_y)
            
            x_points.extend(side_x)
            y_points.extend(side_y)
    
    return np.array(x_points), np.array(y_points)

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

def create_square_points(center_x, center_y, side_length, num_points=100):
    """
    Creates points for a square with specified number of points for smooth morphing.
    
    Args:
        center_x (float): X-coordinate of the center.
        center_y (float): Y-coordinate of the center.
        side_length (float): Length of each side of the square.
        num_points (int): Number of points to create smooth square outline.
    
    Returns:
        tuple: Arrays of x and y coordinates.
    """
    half_side = side_length / 2
    
    # Define the four vertices of the square
    vertices_x = np.array([center_x - half_side, center_x + half_side, 
                          center_x + half_side, center_x - half_side])
    vertices_y = np.array([center_y - half_side, center_y - half_side, 
                          center_y + half_side, center_y + half_side])
    
    # Create smooth square by interpolating along the edges
    points_per_side = num_points // 4
    remainder = num_points % 4
    
    x_points = []
    y_points = []
    
    for i in range(4):
        # Current vertex and next vertex
        curr_x, curr_y = vertices_x[i], vertices_y[i]
        next_x, next_y = vertices_x[(i + 1) % 4], vertices_y[(i + 1) % 4]
        
        # Number of points for this side (distribute remainder)
        side_points = points_per_side + (1 if i < remainder else 0)
        
        # Create points along this edge (excluding the last point to avoid duplication)
        if side_points > 0:
            t_values = np.linspace(0, 1, side_points + 1)[:-1]
            side_x = curr_x + t_values * (next_x - curr_x)
            side_y = curr_y + t_values * (next_y - curr_y)
            
            x_points.extend(side_x)
            y_points.extend(side_y)
    
    return np.array(x_points), np.array(y_points)

def interpolate_shapes(shape1_x, shape1_y, shape2_x, shape2_y, t):
    """
    Interpolates between two shapes using parameter t.
    
    Args:
        shape1_x, shape1_y: First shape coordinates.
        shape2_x, shape2_y: Second shape coordinates.
        t (float): Interpolation parameter (0 to 1).
    
    Returns:
        tuple: Interpolated x and y coordinates.
    """
    # Ensure both shapes have the same number of points by interpolation
    num_points = max(len(shape1_x), len(shape2_x))
    
    # Resample shapes to have the same number of points
    if len(shape1_x) != num_points:
        indices = np.linspace(0, len(shape1_x)-1, num_points)
        shape1_x = np.interp(indices, np.arange(len(shape1_x)), shape1_x)
        shape1_y = np.interp(indices, np.arange(len(shape1_y)), shape1_y)
    
    if len(shape2_x) != num_points:
        indices = np.linspace(0, len(shape2_x)-1, num_points)
        shape2_x = np.interp(indices, np.arange(len(shape2_x)), shape2_x)
        shape2_y = np.interp(indices, np.arange(len(shape2_y)), shape2_y)
    
    # Linear interpolation
    x = (1 - t) * shape1_x + t * shape2_x
    y = (1 - t) * shape1_y + t * shape2_y
    
    return x, y

def create_morphing_animation():
    """
    Creates the main morphing animation from triangle to circle to square.
    """
    print("=== Triangle to Circle to Square Animation ===")
    print()
    
    try:
        # Get animation parameters from user
        center_x, center_y = map(float, input("Enter center coordinates (x, y): ").split())
        size = float(input("Enter size parameter (radius/side length): "))
        
        # Animation parameters
        frames_per_transformation = 60
        pause_frames = 30
        total_frames = 3 * frames_per_transformation + 2 * pause_frames
        
        # Create shapes with same number of points for smooth morphing
        num_morph_points = 120  # Divisible by 3 and 4 for clean triangle and square
        triangle_x, triangle_y = create_triangle_points(center_x, center_y, size, num_morph_points)
        circle_x, circle_y = create_circle_points(center_x, center_y, size, num_morph_points)
        square_x, square_y = create_square_points(center_x, center_y, size * 1.4, num_morph_points)  # Slightly larger for visual balance
        
        # Setup the plot
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_xlim(center_x - size * 2.5, center_x + size * 2.5)
        ax.set_ylim(center_y - size * 2.5, center_y + size * 2.5)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        
        # Create line and fill objects
        line, = ax.plot([], [], 'b-', linewidth=3, label='Shape')
        fill = ax.fill([], [], alpha=0.3, color='lightblue')[0]
        title_text = ax.text(0.5, 0.95, '', transform=ax.transAxes, 
                            fontsize=14, ha='center', weight='bold')
        progress_text = ax.text(0.02, 0.02, '', transform=ax.transAxes, 
                               fontsize=10, ha='left')
        
        ax.legend()
        
        def animate(frame):
            """
            Animation function called for each frame.
            
            Args:
                frame (int): Current frame number.
            """
            current_x, current_y = [], []
            current_title = ""
            progress = ""
            
            if frame < frames_per_transformation:
                # Triangle to Circle transformation
                t = frame / frames_per_transformation
                current_x, current_y = interpolate_shapes(triangle_x, triangle_y, circle_x, circle_y, t)
                current_title = f"Triangle → Circle (Progress: {t*100:.1f}%)"
                progress = f"Phase 1/3: Triangle morphing to Circle"
                
            elif frame < frames_per_transformation + pause_frames:
                # Pause at circle
                current_x, current_y = circle_x, circle_y
                current_title = "Circle (Pausing...)"
                progress = f"Phase 1/3: Circle Complete"
                
            elif frame < 2 * frames_per_transformation + pause_frames:
                # Circle to Square transformation
                t = (frame - frames_per_transformation - pause_frames) / frames_per_transformation
                current_x, current_y = interpolate_shapes(circle_x, circle_y, square_x, square_y, t)
                current_title = f"Circle → Square (Progress: {t*100:.1f}%)"
                progress = f"Phase 2/3: Circle morphing to Square"
                
            elif frame < 2 * frames_per_transformation + 2 * pause_frames:
                # Pause at square
                current_x, current_y = square_x, square_y
                current_title = "Square (Pausing...)"
                progress = f"Phase 2/3: Square Complete"
                
            else:
                # Square back to Triangle transformation
                t = (frame - 2 * frames_per_transformation - 2 * pause_frames) / frames_per_transformation
                current_x, current_y = interpolate_shapes(square_x, square_y, triangle_x, triangle_y, t)
                current_title = f"Square → Triangle (Progress: {t*100:.1f}%)"
                progress = f"Phase 3/3: Square morphing back to Triangle"
            
            # Close the shape by adding the first point at the end
            current_x = np.append(current_x, current_x[0])
            current_y = np.append(current_y, current_y[0])
            
            # Update line and fill
            line.set_data(current_x, current_y)
            fill.set_xy(np.column_stack((current_x, current_y)))
            
            # Update text
            title_text.set_text(current_title)
            progress_text.set_text(progress)
            
            return line, fill, title_text, progress_text
        
        # Create and run animation
        print(f"Starting animation with center at ({center_x}, {center_y}) and size {size}")
        print("Animation will show: Triangle → Circle → Square → Triangle")
        print("Close the window to exit...")
        
        ani = animation.FuncAnimation(fig, animate, frames=total_frames, 
                                    interval=100, blit=True, repeat=True)
        
        plt.title("Shape Morphing Animation")
        plt.tight_layout()
        plt.show()
        
        return ani
        
    except ValueError:
        print("Invalid input! Please enter numbers separated by spaces.")
    except Exception as e:
        print(f"An error occurred: {e}")

def create_simple_static_demo():
    """
    Creates a simple static demonstration of the three shapes.
    """
    print("\n=== Static Shape Demonstration ===")
    
    try:
        center_x, center_y = map(float, input("Enter center coordinates (x, y): ").split())
        size = float(input("Enter size parameter: "))
        
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        
        # Triangle
        tri_x, tri_y = create_triangle_points(center_x, center_y, size)
        tri_x = np.append(tri_x, tri_x[0])  # Close the shape
        tri_y = np.append(tri_y, tri_y[0])
        
        axes[0].plot(tri_x, tri_y, 'b-', linewidth=3)
        axes[0].fill(tri_x, tri_y, alpha=0.3, color='lightblue')
        axes[0].set_title('Triangle', fontsize=14, weight='bold')
        axes[0].grid(True, alpha=0.3)
        axes[0].set_aspect('equal')
        
        # Circle
        cir_x, cir_y = create_circle_points(center_x, center_y, size)
        axes[1].plot(cir_x, cir_y, 'g-', linewidth=3)
        axes[1].fill(cir_x, cir_y, alpha=0.3, color='lightgreen')
        axes[1].set_title('Circle', fontsize=14, weight='bold')
        axes[1].grid(True, alpha=0.3)
        axes[1].set_aspect('equal')
        
        # Square
        sq_x, sq_y = create_square_points(center_x, center_y, size * 1.4)
        sq_x = np.append(sq_x, sq_x[0])  # Close the shape
        sq_y = np.append(sq_y, sq_y[0])
        
        axes[2].plot(sq_x, sq_y, 'r-', linewidth=3)
        axes[2].fill(sq_x, sq_y, alpha=0.3, color='lightcoral')
        axes[2].set_title('Square', fontsize=14, weight='bold')
        axes[2].grid(True, alpha=0.3)
        axes[2].set_aspect('equal')
        
        # Set equal limits for all subplots
        for ax in axes:
            ax.set_xlim(center_x - size * 2, center_x + size * 2)
            ax.set_ylim(center_y - size * 2, center_y + size * 2)
            ax.set_xlabel('X-axis')
            ax.set_ylabel('Y-axis')
        
        plt.suptitle('Shape Transformation Preview', fontsize=16, weight='bold')
        plt.tight_layout()
        plt.show()
        
    except ValueError:
        print("Invalid input! Please enter numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """
    Main function to execute the shape morphing program.
    """
    print("=== Shape Morphing Animation Program ===")
    print("This program creates smooth animations transforming between shapes:")
    print("Triangle → Circle → Square → Triangle")
    print()
    
    while True:
        print("=== Menu ===")
        print("1. Run Morphing Animation")
        print("2. Show Static Shape Preview")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice (1-3): "))
            
            if choice == 1:
                animation_obj = create_morphing_animation()
                
            elif choice == 2:
                create_simple_static_demo()
                
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

