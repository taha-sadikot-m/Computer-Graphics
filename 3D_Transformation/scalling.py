# Create a Program to perform 3D scaling of a cube
# Cube size and scaling parameters will be taken from user
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

def scale_cube_uniform(vertices, center_x, center_y, center_z, scale_factor):
    """
    Performs uniform 3D scaling on cube vertices (same scale factor for all axes).
    
    Args:
        vertices (numpy.ndarray): Original vertices of the cube.
        center_x (float): X-coordinate of scaling center.
        center_y (float): Y-coordinate of scaling center.
        center_z (float): Z-coordinate of scaling center.
        scale_factor (float): Uniform scaling factor for all axes.
    
    Returns:
        numpy.ndarray: Scaled vertices.
    """
    center = np.array([center_x, center_y, center_z])
    
    # Translate to origin, scale, then translate back
    scaled_vertices = center + (vertices - center) * scale_factor
    
    return scaled_vertices

def scale_cube_non_uniform(vertices, center_x, center_y, center_z, sx, sy, sz):
    """
    Performs non-uniform 3D scaling on cube vertices (different scale factors for each axis).
    
    Args:
        vertices (numpy.ndarray): Original vertices of the cube.
        center_x (float): X-coordinate of scaling center.
        center_y (float): Y-coordinate of scaling center.
        center_z (float): Z-coordinate of scaling center.
        sx (float): Scaling factor for X-axis.
        sy (float): Scaling factor for Y-axis.
        sz (float): Scaling factor for Z-axis.
    
    Returns:
        numpy.ndarray: Scaled vertices.
    """
    center = np.array([center_x, center_y, center_z])
    scale_factors = np.array([sx, sy, sz])
    
    # Translate to origin
    translated_vertices = vertices - center
    
    # Apply non-uniform scaling
    scaled_vertices = translated_vertices * scale_factors
    
    # Translate back to original center
    final_vertices = scaled_vertices + center
    
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

def plot_comparison(original_vertices, scaled_vertices, scaling_type="Scaled"):
    """
    Plots both original and scaled cubes for comparison.
    
    Args:
        original_vertices (numpy.ndarray): Original cube vertices.
        scaled_vertices (numpy.ndarray): Scaled cube vertices.
        scaling_type (str): Type of scaling performed for title.
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
    
    # Scaled cube (more prominent)
    scaled_faces = [scaled_vertices[face_idx] for face_idx in faces_indices]
    scaled_collection = Poly3DCollection(
        scaled_faces, alpha=0.7, facecolors='lightgreen', 
        edgecolors='green', linewidths=2, label=scaling_type
    )
    ax.add_collection3d(scaled_collection)
    
    # Plot vertices
    ax.scatter(original_vertices[:, 0], original_vertices[:, 1], original_vertices[:, 2], 
              color='blue', s=80, label='Original Vertices')
    ax.scatter(scaled_vertices[:, 0], scaled_vertices[:, 1], scaled_vertices[:, 2], 
              color='green', s=100, label=f'{scaling_type} Vertices')
    
    # Set axis limits to show both cubes
    all_vertices = np.vstack((original_vertices, scaled_vertices))
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
    ax.set_title(f'3D Scaling Comparison: Original (Blue) vs {scaling_type} (Green)')
    ax.legend()
    
    plt.show(block=False)
    plt.pause(0.001)

def main():
    """
    Main function to execute the 3D scaling program.
    """
    print("=== 3D Cube Scaling Program ===")
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
        
        # Interactive scaling menu
        while True:
            print("\n=== Scaling Menu ===")
            print("1. Uniform Scaling (same factor for all axes)")
            print("2. Non-Uniform Scaling (different factors for each axis)")
            print("3. Show Original Cube")
            print("4. Exit")
            
            try:
                choice = int(input("Enter your choice (1-4): "))
                
                if choice == 1:
                    # Uniform scaling
                    print("\nEnter uniform scaling parameters:")
                    scale_factor = float(input("Enter uniform scaling factor: "))
                    
                    if scale_factor <= 0:
                        print("Scaling factor must be positive!")
                        continue
                    
                    # Perform uniform scaling
                    scaled_vertices = scale_cube_uniform(original_vertices, center_x, center_y, center_z, scale_factor)
                    
                    # Display results
                    scaling_description = "enlarged" if scale_factor > 1 else "reduced" if scale_factor < 1 else "unchanged"
                    print(f"\nUniform scaling applied: factor = {scale_factor} (cube {scaling_description})")
                    print("Displaying comparison...")
                    
                    # Show both original and scaled cubes
                    plot_comparison(original_vertices, scaled_vertices, "Uniformly Scaled")
                    
                    # Show scaled cube details
                    print("\nUniformly scaled cube vertices:")
                    for i, vertex in enumerate(scaled_vertices):
                        print(f"  Vertex {i+1}: ({vertex[0]:.2f}, {vertex[1]:.2f}, {vertex[2]:.2f})")
                
                elif choice == 2:
                    # Non-uniform scaling
                    print("\nEnter non-uniform scaling parameters:")
                    sx = float(input("Enter scaling factor for X-axis: "))
                    sy = float(input("Enter scaling factor for Y-axis: "))
                    sz = float(input("Enter scaling factor for Z-axis: "))
                    
                    if sx <= 0 or sy <= 0 or sz <= 0:
                        print("All scaling factors must be positive!")
                        continue
                    
                    # Perform non-uniform scaling
                    scaled_vertices = scale_cube_non_uniform(original_vertices, center_x, center_y, center_z, sx, sy, sz)
                    
                    # Display results
                    print(f"\nNon-uniform scaling applied: sx={sx}, sy={sy}, sz={sz}")
                    print("Displaying comparison...")
                    
                    # Show both original and scaled cubes
                    plot_comparison(original_vertices, scaled_vertices, "Non-Uniformly Scaled")
                    
                    # Show scaled cube details
                    print("\nNon-uniformly scaled cube vertices:")
                    for i, vertex in enumerate(scaled_vertices):
                        print(f"  Vertex {i+1}: ({vertex[0]:.2f}, {vertex[1]:.2f}, {vertex[2]:.2f})")
                
                elif choice == 3:
                    plot_cube(original_vertices, title="Original 3D Cube")
                
                elif choice == 4:
                    print("Exiting program...")
                    break
                
                else:
                    print("Invalid choice! Please enter 1, 2, 3, or 4.")
                    
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