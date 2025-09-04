import matplotlib.pyplot as plt
import numpy as np

def plot_3d_sphere(ax, center, radius):
    """
    Plots a 3D sphere as a wireframe.
    
    Args:
        ax: The Matplotlib axes object with '3d' projection.
        center (tuple): The (x, y, z) coordinates of the sphere's center.
        radius (float): The radius of the sphere.
    """
    # Create the mesh for the sphere surface
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    x = radius * np.outer(np.cos(u), np.sin(v)) + center[0]
    y = radius * np.outer(np.sin(u), np.sin(v)) + center[1]
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + center[2]

    # Plot the sphere wireframe
    ax.plot_wireframe(x, y, z, color='b', alpha=0.5)

def main():
    # Setup the figure and 3D axes
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Get input for sphere parameters
    x_center, y_center, z_center = map(float, input("Enter the coordinates of the center (x, y, z): ").split())
    radius = float(input("Enter the radius of the sphere: "))
    
    # Plot the sphere
    plot_3d_sphere(ax, (x_center, y_center, z_center), radius)
    
    # Set labels and title
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('3D Sphere Wireframe')
    
    plt.show()

if __name__ == "__main__":
    main()
