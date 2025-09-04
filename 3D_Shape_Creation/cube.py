import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from itertools import product

def calculate_cube_vertices(center_x, center_y, center_z, side_length):
    half_side = side_length / 2.0
    r = [-half_side, half_side]
    vertices_relative = np.array(list(product(r, r, r)))
    center_offset = np.array([center_x, center_y, center_z])
    vertices = vertices_relative + center_offset
    return vertices

#keep the center same only increase the sice of cube according to input
def translate_cube(vertices, tx, ty, tz):
    translation_vector = np.array([tx, ty, tz])
    translated_vertices = vertices + translation_vector
    return translated_vertices

#center will be same only increase the size of cube
def scale_cube(vertices, center_x, center_y, center_z, scale_factor):
    center = np.array([center_x, center_y, center_z])
    scaled_vertices = center + (vertices - center) * scale_factor
    return scaled_vertices

def rotate_cube(vertices, center_x, center_y, center_z, axis, angle_degrees):
    angle_radians = np.radians(angle_degrees)
    center = np.array([center_x, center_y, center_z])
    translated_vertices = vertices - center

    if axis == 'x':
        rotation_matrix = np.array([
            [1, 0, 0],
            [0, np.cos(angle_radians), -np.sin(angle_radians)],
            [0, np.sin(angle_radians), np.cos(angle_radians)]
        ])
    elif axis == 'y':
        rotation_matrix = np.array([
            [np.cos(angle_radians), 0, np.sin(angle_radians)],
            [0, 1, 0],
            [-np.sin(angle_radians), 0, np.cos(angle_radians)]
        ])
    elif axis == 'z':
        rotation_matrix = np.array([
            [np.cos(angle_radians), -np.sin(angle_radians), 0],
            [np.sin(angle_radians), np.cos(angle_radians), 0],
            [0, 0, 1]
        ])
    else:
        raise ValueError("Axis must be 'x', 'y', or 'z'.")

    rotated_vertices = translated_vertices.dot(rotation_matrix.T)
    final_vertices = rotated_vertices + center
    return final_vertices

def shearing_cube(vertices, shear_xy=0, shear_xz=0, shear_yx=0, shear_yz=0, shear_zx=0, shear_zy=0):
    shearing_matrix = np.array([
        [1, shear_xy, shear_xz],
        [shear_yx, 1, shear_yz],
        [shear_zx, shear_zy, 1]
    ])
    sheared_vertices = vertices.dot(shearing_matrix.T)
    return sheared_vertices



def plot_cube(vertices):
    # Define the 6 faces using vertex indices
    faces_indices = [
        [0, 1, 3, 2],  # Bottom face
        [4, 5, 7, 6],  # Top face
        [0, 1, 5, 4],  # Front face
        [2, 3, 7, 6],  # Back face
        [0, 2, 6, 4],  # Left face
        [1, 3, 7, 5]   # Right face
    ]
    cube_faces = [vertices[face_idx] for face_idx in faces_indices]

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    cube_collection = Poly3DCollection(
        cube_faces, alpha=0.6, facecolors='lightcoral', edgecolors='black', linewidths=1)
    ax.add_collection3d(cube_collection)

    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='blue', s=50)

    min_coords = np.min(vertices, axis=0)
    max_coords = np.max(vertices, axis=0)
    side_length = max_coords[0] - min_coords[0]

    ax.set_xlim([min_coords[0] - 0.1 * side_length, max_coords[0] + 0.1 * side_length])
    ax.set_ylim([min_coords[1] - 0.1 * side_length, max_coords[1] + 0.1 * side_length])
    ax.set_zlim([min_coords[2] - 0.1 * side_length, max_coords[2] + 0.1 * side_length])

    ax.set_box_aspect([1, 1, 1])
    ax.set_title("3D Cube Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")

    plt.show(block=False)

def plot_two_cubes(original_vertices, updated_vertices):
    faces_indices = [
        [0, 1, 3, 2],  # Bottom face
        [4, 5, 7, 6],  # Top face
        [0, 1, 5, 4],  # Front face
        [2, 3, 7, 6],  # Back face
        [0, 2, 6, 4],  # Left face
        [1, 3, 7, 5]   # Right face
    ]

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Original cube faces with lighter color
    original_faces = [original_vertices[face_idx] for face_idx in faces_indices]
    original_collection = Poly3DCollection(
        original_faces, alpha=0.2, facecolors='lightblue', edgecolors='blue', linewidths=1)
    ax.add_collection3d(original_collection)
    ax.scatter(original_vertices[:, 0], original_vertices[:, 1], original_vertices[:, 2], color='blue', s=20)

    # Updated cube faces with stronger color
    updated_faces = [updated_vertices[face_idx] for face_idx in faces_indices]
    updated_collection = Poly3DCollection(
        updated_faces, alpha=0.6, facecolors='lightcoral', edgecolors='red', linewidths=1)
    ax.add_collection3d(updated_collection)
    ax.scatter(updated_vertices[:, 0], updated_vertices[:, 1], updated_vertices[:, 2], color='red', s=50)

    # Compute overall min/max coords for both cubes
    all_vertices = np.vstack((original_vertices, updated_vertices))
    min_coords = np.min(all_vertices, axis=0)
    max_coords = np.max(all_vertices, axis=0)
    side_length = max(max_coords - min_coords)

    ax.set_xlim([min_coords[0] - 0.1 * side_length, max_coords[0] + 0.1 * side_length])
    ax.set_ylim([min_coords[1] - 0.1 * side_length, max_coords[1] + 0.1 * side_length])
    ax.set_zlim([min_coords[2] - 0.1 * side_length, max_coords[2] + 0.1 * side_length])

    ax.set_box_aspect([1, 1, 1])
    ax.set_title("Original (blue) and Updated (red) Cubes")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")

    plt.show(block=False)
    plt.pause(0.001)


center_x, center_y, center_z = map(float, input("Enter cube center coordinates (x, y, z): ").split())
side_length = float(input("Enter the side length of the cube: "))

vertices = calculate_cube_vertices(center_x, center_y, center_z, side_length)
plot_cube(vertices)

original_vertices = calculate_cube_vertices(center_x, center_y, center_z, side_length)
current_vertices = original_vertices.copy()


print('1 :- Translation')
print('2 :- Scaling')
print('3 :- Rotation')
print('4 :- Shearing')
print('5 :- Exit')

choice = int(input("Enter your choice: "))
while choice != 5:
    if choice == 1:
        tx, ty, tz = map(float, input("Enter translation distances (tx, ty, tz): ").split())
        translated_current_vertices = translate_cube(current_vertices, tx, ty, tz)
        plot_two_cubes(original_vertices, translated_current_vertices)
    elif choice == 2:
        scale_factor = float(input("Enter scaling factor: "))
        scaled_current_vertices = scale_cube(current_vertices, center_x, center_y, center_z, scale_factor)
        plot_two_cubes(original_vertices, scaled_current_vertices)
    elif choice == 3:
        axis = input("Enter rotation axis (x, y, or z): ").lower()
        angle_degrees = float(input("Enter rotation angle in degrees: "))
        rotated_current_vertices = rotate_cube(current_vertices, center_x, center_y, center_z, axis, angle_degrees)
        plot_two_cubes(original_vertices, rotated_current_vertices)
    elif choice == 4:
        shear_xy = float(input("Enter shear factor for XY plane: "))
        shear_xz = float(input("Enter shear factor for XZ plane: "))
        shear_yx = float(input("Enter shear factor for YX plane: "))
        shear_yz = float(input("Enter shear factor for YZ plane: "))
        shear_zx = float(input("Enter shear factor for ZX plane: "))
        shear_zy = float(input("Enter shear factor for ZY plane: "))
        sheared_current_vertices = shearing_cube(current_vertices, shear_xy, shear_xz, shear_yx, shear_yz, shear_zx, shear_zy)
        plot_two_cubes(original_vertices, sheared_current_vertices)
    else:
        print("Invalid choice. Please try again.")
    
    print('1 :- Translation')
    print('2 :- Scaling')
    print('3 :- Rotation')
    print('4 :- Exit')
    choice = int(input("Enter your choice: "))

plt.show()  # Hold final plot window open