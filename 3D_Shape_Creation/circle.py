import matplotlib.pyplot as plt
import numpy as np

def calculate_3d_sphere_surface(center_x, center_y, center_z, radius, num_points=50):
    phi = np.linspace(0, 2 * np.pi, num_points)  # Azimuthal angle (0 to 2*pi)
    theta = np.linspace(0, np.pi, num_points)    # Polar angle (0 to pi)
    phi, theta = np.meshgrid(phi, theta)

    x = center_x + radius * np.sin(theta) * np.cos(phi)
    y = center_y + radius * np.sin(theta) * np.sin(phi)
    z = center_z + radius * np.cos(theta)
    
    return x, y, z

def plot_3d_sphere_wireframe(x_coords, y_coords, z_coords):
   
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_wireframe(x_coords, y_coords, z_coords, color='blue') # Changed to plot_wireframe
    
    ax.set_title("3D Wireframe Sphere Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")

    ax.set_box_aspect([np.ptp(x_coords), np.ptp(y_coords), np.ptp(z_coords)])
    plt.show()



center_x, center_y, center_z = map(float, input("Enter the coordinates of the center (x, y, z): ").split())
radius = float(input("Enter the radius of the sphere: "))
       
x, y, z = calculate_3d_sphere_surface(center_x, center_y, center_z, radius)
        
plot_3d_sphere_wireframe(x, y, z)
        
    