import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def plot_3d_triangle(vertices):
    """
    Plots a 3D triangle given its vertices.

    Args:
        vertices (list or np.ndarray): A list or NumPy array of three 3D points,
                                       e.g., [[x1, y1, z1], [x2, y2, z2], [x3, y3, z3]].
    """
    # Create the figure and a 3D axes object
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Convert vertices to a NumPy array for easier manipulation
    vertices = np.array(vertices)

    # Create a Poly3DCollection from the vertices to represent the triangle
    # alpha controls transparency, edgecolor sets the color of the edges
    triangle = Poly3DCollection([vertices], alpha=0.8, facecolors='cyan', edgecolor='k', linewidths=1)
    
    # Add the triangle to the 3D plot
    ax.add_collection3d(triangle)

    # Set axis limits based on the triangle's vertices to ensure it's visible
    min_coords = np.min(vertices, axis=0)
    max_coords = np.max(vertices, axis=0)
    ax.set_xlim([min_coords[0] - 1, max_coords[0] + 1])
    ax.set_ylim([min_coords[1] - 1, max_coords[1] + 1])
    ax.set_zlim([min_coords[2] - 1, max_coords[2] + 1])

    ax.set_title("3D Triangle Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")

    # Display the plot
    plt.show()

# --- Main program execution ---
if __name__ == "__main__":
    print("Enter the coordinates for the three vertices of the triangle.")
    try:
        # Get input for each vertex
        v1 = list(map(float, input("Enter coordinates for Vertex 1 (x1, y1, z1): ").split()))
        v2 = list(map(float, input("Enter coordinates for Vertex 2 (x2, y2, z2): ").split()))
        v3 = list(map(float, input("Enter coordinates for Vertex 3 (x3, y3, z3): ").split()))

        # Ensure that the input lists have 3 elements each
        if len(v1) == 3 and len(v2) == 3 and len(v3) == 3:
            triangle_vertices = [v1, v2, v3]
            plot_3d_triangle(triangle_vertices)
        else:
            print("Invalid input. Each vertex requires three coordinates (x, y, z).")
            
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces for each coordinate.")
    except Exception as e:
        print(f"An error occurred: {e}")

