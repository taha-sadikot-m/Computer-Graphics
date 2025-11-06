# Create a Program to perform 3D rotation of a cube
# Cube size and rotation parameters will be taken from user
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def create_square_vertices(center_x, center_y, center_z, side_length):
    """
    Creates vertices for a 3D cube (3D square with equal dimensions).
    
    Args:
        center_x (float): X-coordinate of the cube's center.
        center_y (float): Y-coordinate of the cube's center.
        center_z (float): Z-coordinate of the cube's center.
        side_length (float): Length of one side of the cube.

    Returns:
        numpy.ndarray: Array of 8 vertices representing the cube corners.
    """
    half_side = side_length / 2.0
    
    # Define cube vertices (8 corners of a cube)
    vertices = np.array([
        # Bottom face (z = center_z - half_side)
        [center_x - half_side, center_y - half_side, center_z - half_side],  # 0: Bottom-front-left
        [center_x + half_side, center_y - half_side, center_z - half_side],  # 1: Bottom-front-right
        [center_x + half_side, center_y + half_side, center_z - half_side],  # 2: Bottom-back-right
        [center_x - half_side, center_y + half_side, center_z - half_side],  # 3: Bottom-back-left
        # Top face (z = center_z + half_side)
        [center_x - half_side, center_y - half_side, center_z + half_side],  # 4: Top-front-left
        [center_x + half_side, center_y - half_side, center_z + half_side],  # 5: Top-front-right
        [center_x + half_side, center_y + half_side, center_z + half_side],  # 6: Top-back-right
        [center_x - half_side, center_y + half_side, center_z + half_side]   # 7: Top-back-left
    ])
    
    return vertices

def rotate_cube(vertices, center_x, center_y, center_z, axis, angle_degrees):
    """
    Performs 3D rotation on cube vertices around a specified axis.
    
    Args:
        vertices (numpy.ndarray): Original vertices of the cube.
        center_x (float): X-coordinate of rotation center.
        center_y (float): Y-coordinate of rotation center.
        center_z (float): Z-coordinate of rotation center.
        axis (str): Rotation axis ('x', 'y', or 'z').
        angle_degrees (float): Rotation angle in degrees.
    
    Returns:
        numpy.ndarray: Rotated vertices.
    """
    angle_radians = np.radians(angle_degrees)
    center = np.array([center_x, center_y, center_z])
    
    # Translate vertices to origin (center becomes 0,0,0)
    translated_vertices = vertices - center
    
    # Create rotation matrix based on axis
    if axis.lower() == 'x':
        rotation_matrix = np.array([
            [1, 0, 0],
            [0, np.cos(angle_radians), -np.sin(angle_radians)],
            [0, np.sin(angle_radians), np.cos(angle_radians)]
        ])
    elif axis.lower() == 'y':
        rotation_matrix = np.array([
            [np.cos(angle_radians), 0, np.sin(angle_radians)],
            [0, 1, 0],
            [-np.sin(angle_radians), 0, np.cos(angle_radians)]
        ])
    elif axis.lower() == 'z':
        rotation_matrix = np.array([
            [np.cos(angle_radians), -np.sin(angle_radians), 0],
            [np.sin(angle_radians), np.cos(angle_radians), 0],
            [0, 0, 1]
        ])
    else:
        raise ValueError("Axis must be 'x', 'y', or 'z'.")
    
    # Apply rotation
    rotated_vertices = translated_vertices.dot(rotation_matrix.T)
    
    # Translate back to original center
    final_vertices = rotated_vertices + center
    
    return final_vertices

def plot_cube(vertices, color='lightblue', alpha=0.6, edge_color='blue', title="3D Cube"):
    """
    Plots a single 3D cube.
    
    Args:
        vertices (numpy.ndarray): Vertices of the cube to plot.
        color (str): Face color of the cube.
        alpha (float): Transparency level.
        edge_color (str): Color of the edges.
        title (str): Title for the plot.
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Define the 6 faces of the cube using vertex indices
    faces_indices = [
        [0, 1, 2, 3],  # Bottom face
        [4, 5, 6, 7],  # Top face
        [0, 1, 5, 4],  # Front face
        [2, 3, 7, 6],  # Back face
        [0, 3, 7, 4],  # Left face
        [1, 2, 6, 5]   # Right face
    ]
    
    # Create cube faces using the vertices
    cube_faces = [vertices[face_idx] for face_idx in faces_indices]
    cube_collection = Poly3DCollection(
        cube_faces, alpha=alpha, facecolors=color, edgecolors=edge_color, linewidths=2
    )
    ax.add_collection3d(cube_collection)
    
    # Plot vertices as points
    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], 
              color='red', s=100, label='Vertices')
    
    # Set axis limits with some padding
    all_coords = vertices.flatten()
    margin = np.ptp(all_coords) * 0.2
    min_coord = np.min(all_coords) - margin
    max_coord = np.max(all_coords) + margin
    
    ax.set_xlim([min_coord, max_coord])
    ax.set_ylim([min_coord, max_coord])
    ax.set_zlim([min_coord, max_coord])
    
    # Set equal aspect ratio
    ax.set_box_aspect([1, 1, 1])
    
    # Set labels and title
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title(title)
    ax.legend()
    
    plt.show(block=False)
    plt.pause(0.001)

def plot_comparison(original_vertices, rotated_vertices):
    """
    Plots both original and rotated cubes for comparison.
    
    Args:
        original_vertices (numpy.ndarray): Original cube vertices.
        rotated_vertices (numpy.ndarray): Rotated cube vertices.
    """
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Define the 6 faces of the cube using vertex indices
    faces_indices = [
        [0, 1, 2, 3],  # Bottom face
        [4, 5, 6, 7],  # Top face
        [0, 1, 5, 4],  # Front face
        [2, 3, 7, 6],  # Back face
        [0, 3, 7, 4],  # Left face
        [1, 2, 6, 5]   # Right face
    ]
    
    # Original cube (lighter/transparent)
    original_faces = [original_vertices[face_idx] for face_idx in faces_indices]
    original_collection = Poly3DCollection(
        original_faces, alpha=0.3, facecolors='lightblue', 
        edgecolors='blue', linewidths=2, label='Original'
    )
    ax.add_collection3d(original_collection)
    
    # Rotated cube (more prominent)
    rotated_faces = [rotated_vertices[face_idx] for face_idx in faces_indices]
    rotated_collection = Poly3DCollection(
        rotated_faces, alpha=0.7, facecolors='lightcoral', 
        edgecolors='red', linewidths=2, label='Rotated'
    )
    ax.add_collection3d(rotated_collection)
    
    # Plot vertices
    ax.scatter(original_vertices[:, 0], original_vertices[:, 1], original_vertices[:, 2], 
              color='blue', s=80, label='Original Vertices')
    ax.scatter(rotated_vertices[:, 0], rotated_vertices[:, 1], rotated_vertices[:, 2], 
              color='red', s=100, label='Rotated Vertices')
    
    # Set axis limits to show both cubes
    all_vertices = np.vstack((original_vertices, rotated_vertices))
    all_coords = all_vertices.flatten()
    margin = np.ptp(all_coords) * 0.1
    min_coord = np.min(all_coords) - margin
    max_coord = np.max(all_coords) + margin
    
    ax.set_xlim([min_coord, max_coord])
    ax.set_ylim([min_coord, max_coord])
    ax.set_zlim([min_coord, max_coord])
    
    # Set equal aspect ratio
    ax.set_box_aspect([1, 1, 1])
    
    # Set labels and title
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('3D Rotation Comparison: Original (Blue) vs Rotated (Red)')
    ax.legend()
    
    plt.show(block=False)
    plt.pause(0.001)

def main():
    """
    Main function to execute the 3D rotation program.
    """
    print("=== 3D Cube Rotation Program ===")
    print()
    
    try:
        # Get cube parameters from user
        print("Enter the cube parameters:")
        center_x, center_y, center_z = map(float, input("Enter cube center coordinates (x, y, z): ").split())
        side_length = float(input("Enter the side length of the cube: "))
        
        # Create original cube
        original_vertices = create_square_vertices(center_x, center_y, center_z, side_length)
        
        # Display original cube
        print(f"\nOriginal 3D cube created with center at ({center_x}, {center_y}, {center_z}) and side length {side_length}")
        plot_cube(original_vertices, title="Original 3D Cube")
        
        # Interactive rotation menu
        while True:
            print("\n=== Rotation Menu ===")
            print("1. Perform Rotation")
            print("2. Show Original Cube")
            print("3. Exit")
            
            try:
                choice = int(input("Enter your choice (1-3): "))
                
                if choice == 1:
                    # Get rotation parameters
                    print("\nEnter rotation parameters:")
                    axis = input("Enter rotation axis (x, y, or z): ").lower().strip()
                    
                    if axis not in ['x', 'y', 'z']:
                        print("Invalid axis! Please enter 'x', 'y', or 'z'.")
                        continue
                    
                    angle_degrees = float(input("Enter rotation angle in degrees: "))
                    
                    # Perform rotation
                    rotated_vertices = rotate_cube(original_vertices, center_x, center_y, center_z, axis, angle_degrees)
                    
                    # Display results
                    print(f"\nRotation applied: {angle_degrees}° around {axis.upper()}-axis")
                    print("Displaying comparison...")
                    
                    # Show both original and rotated cubes
                    plot_comparison(original_vertices, rotated_vertices)
                    
                    # Show rotated cube details
                    print("\nRotated cube vertices:")
                    for i, vertex in enumerate(rotated_vertices):
                        print(f"  Vertex {i+1}: ({vertex[0]:.2f}, {vertex[1]:.2f}, {vertex[2]:.2f})")
                
                elif choice == 2:
                    plot_cube(original_vertices, title="Original 3D Cube")
                
                elif choice == 3:
                    print("Exiting program...")
                    break
                
                else:
                    print("Invalid choice! Please enter 1, 2, or 3.")
                    
            except ValueError:
                print("Invalid input! Please enter a valid number.")
            except Exception as e:
                print(f"An error occurred: {e}")
        
        # Keep the final plot window open
        plt.show()
        
    except ValueError:
        print("Invalid input! Please enter numbers separated by spaces.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()