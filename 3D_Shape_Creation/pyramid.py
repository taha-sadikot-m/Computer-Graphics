import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def plot_3d_pyramid(base_center_x, base_center_y, base_z, base_side_length, apex_z):
    """
    Plots a 3D square-based pyramid.

    Args:
        base_center_x (float): X-coordinate of the center of the pyramid's base.
        base_center_y (float): Y-coordinate of the center of the pyramid's base.
        base_z (float): Z-coordinate of the base plane.
        base_side_length (float): Length of one side of the square base.
        apex_z (float): Z-coordinate of the pyramid's apex (tip).
    """
    # Define the vertices of the pyramid
    half_side = base_side_length / 2.0
    
    # Base vertices (counter-clockwise)
    v1 = [base_center_x - half_side, base_center_y - half_side, base_z]
    v2 = [base_center_x + half_side, base_center_y - half_side, base_z]
    v3 = [base_center_x + half_side, base_center_y + half_side, base_z]
    v4 = [base_center_x - half_side, base_center_y + half_side, base_z]
    
    # Apex vertex
    apex = [base_center_x, base_center_y, apex_z]

    vertices = np.array([v1, v2, v3, v4, apex])

    # Define the faces of the pyramid using indices of the vertices array
    # Each list represents a face and contains the indices of its vertices
    faces = [
        [vertices[0], vertices[1], vertices[4]], # Side 1 (v1, v2, apex)
        [vertices[1], vertices[2], vertices[4]], # Side 2 (v2, v3, apex)
        [vertices[2], vertices[3], vertices[4]], # Side 3 (v3, v4, apex)
        [vertices[3], vertices[0], vertices[4]], # Side 4 (v4, v1, apex)
        [vertices[0], vertices[1], vertices[2], vertices[3]] # Base (v1, v2, v3, v4)
    ]

    # Create the figure and a 3D axes object
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Create a Poly3DCollection for the pyramid's faces
    # facecolors can be a single color or a list of colors for each face
    # edgecolor sets the color of the lines forming the edges
    pyramid_faces = Poly3DCollection(faces, alpha=0.6, facecolors='purple', edgecolors='black', linewidths=1)
    
    # Add the collection of faces to the 3D plot
    ax.add_collection3d(pyramid_faces)

    # Optionally, plot the vertices as scatter points
    ax.scatter(vertices[:,0], vertices[:,1], vertices[:,2], color='blue', s=50)

    # Set axis limits to ensure the pyramid is fully visible
    max_range = np.array([vertices[:,0].max()-vertices[:,0].min(), 
                          vertices[:,1].max()-vertices[:,1].min(), 
                          vertices[:,2].max()-vertices[:,2].min()]).max() / 2.0

    mid_x = (vertices[:,0].max()+vertices[:,0].min()) * 0.5
    mid_y = (vertices[:,1].max()+vertices[:,1].min()) * 0.5
    mid_z = (vertices[:,2].max()+vertices[:,2].min()) * 0.5

    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    ax.set_title("3D Pyramid Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")

    # Display the plot
    plt.show()

# --- Main program execution ---
if __name__ == "__main__":
    print("Enter parameters for the 3D pyramid:")
    try:
        base_center_x, base_center_y, base_z = map(float, input("Enter base center coordinates (x, y, z): ").split())
        base_side_length = float(input("Enter the side length of the square base: "))
        apex_z = float(input("Enter the Z-coordinate of the pyramid's apex: "))

        plot_3d_pyramid(base_center_x, base_center_y, base_z, base_side_length, apex_z)
            
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")
    except Exception as e:
        print(f"An error occurred: {e}")
