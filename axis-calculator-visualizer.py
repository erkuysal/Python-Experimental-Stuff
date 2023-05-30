import math
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_rotation():
    # Taking Inputs
    x_angle = float(entry_x.get())
    y_angle = float(entry_y.get())
    z_angle = float(entry_z.get())

    # Convert Angles To Radians
    angle_x_rad = math.radians(x_angle)
    angle_y_rad = math.radians(y_angle)
    angle_z_rad = math.radians(z_angle)

    # Rotation Matrices
    rotation_x = np.array([[1, 0, 0],
                           [0, math.cos(angle_x_rad), -math.sin(angle_x_rad)],
                           [0, math.sin(angle_x_rad), math.cos(angle_x_rad)]])

    rotation_y = np.array([[math.cos(angle_y_rad), 0, math.sin(angle_y_rad)],
                           [0, 1, 0],
                           [-math.sin(angle_y_rad), 0, math.cos(angle_y_rad)]])

    rotation_z = np.array([[math.cos(angle_z_rad), -math.sin(angle_z_rad), 0],
                           [math.sin(angle_z_rad), math.cos(angle_z_rad), 0],
                           [0, 0, 1]])

    # Combine Rotation matrices to get final rotation matrix
    rotation_matrix = np.dot(rotation_z, np.dot(rotation_y, rotation_x))

    # Generate a unit cube
    vertices = np.array([[1, 1, 1], [-1, 1, 1], [-1, -1, 1], [1, -1, 1],
                         [1, 1, -1], [-1, 1, -1], [-1, -1, -1], [1, -1, -1]])

    # Apply rotation matrix to the cube vertices
    rotated_vertices = np.dot(vertices, rotation_matrix)

    # Plot the rotated cube
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i in range(0, 4):
        ax.plot3D(rotated_vertices[i:i+2, 0], rotated_vertices[i:i+2, 1], rotated_vertices[i:i+2, 2], 'b')
        ax.plot3D(rotated_vertices[[i, (i+1) % 4+4], 0], rotated_vertices[[i, (i+1) % 4+4], 1],
                  rotated_vertices[[i, (i+1) % 4+4], 2], 'b')
        ax.plot3D(rotated_vertices[i+4:i+6, 0], rotated_vertices[i+4:i+6, 1], rotated_vertices[i+4:i+6, 2], 'b')
        ax.plot3D([rotated_vertices[i, 0], rotated_vertices[i+4, 0]],
                  [rotated_vertices[i, 1], rotated_vertices[i+4, 1]],
                  [rotated_vertices[i, 2], rotated_vertices[i+4, 2]], 'b')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Rotated Cube')
    ax.set_box_aspect([1, 1, 1])  # Fix the aspect ratio of the plot
    ax.view_init(azim=45, elev=30)  # Set the viewpoint

    plt.show()


# Screen Display Section

window = tk.Tk()
window.title("Rotation Visualizer")

# Input Labels and Entry fields
label_x = tk.Label(window, text="Rotation X (degrees): ")
label_x.pack()
entry_x = tk.Entry(window)
entry_x.pack()

label_y = tk.Label(window, text="Rotation Y (degrees): ")
label_y.pack()
entry_y = tk.Entry(window)
entry_y.pack()

label_z = tk.Label(window, text="Rotation Z (degrees): ")
label_z.pack()
entry_z = tk.Entry(window)
entry_z.pack()

# Create visualize Button
visualize_button = tk.Button(window, text="VISUALIZE", command=visualize_rotation)
visualize_button.pack()

# Run the Tkinter event loop
window.mainloop()
