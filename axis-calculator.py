import math
import tkinter as tk

def calculate_rotation():
    # Taking Inputs
    x_angle = float(entry_x.get())
    y_angle = float(entry_y.get())
    z_angle = float(entry_z.get())

    # Convert Angles To Radians
    angle_x_rad = math.radians(x_angle)
    angle_y_rad = math.radians(y_angle)
    angle_z_rad = math.radians(z_angle)

    # Rotation Matrices

    """
     To perform a rotation using a rotation matrix, 
     you multiply the rotation matrix by the coordinates of the point or vector you want to rotate.
     The result is the new coordinates after the rotation. 
    """

    rotation_x = [[1, 0, 0],                                           # this row represents x axis
                  [0, math.cos(angle_x_rad), -math.sin(angle_x_rad)], # Angle_x_rad represents angle of rotation x
                  [0, math.sin(angle_x_rad), math.cos(angle_x_rad)]]

    rotation_y = [[math.cos(angle_y_rad), 0, math.sin(angle_y_rad)],
                  [0, 1, 0],                                           # this row represents y axis
                  [-math.sin(angle_y_rad), 0, math.cos(angle_y_rad)]]

    rotation_z = [[math.cos(angle_z_rad), -math.sin(angle_z_rad), 0],
                  [math.sin(angle_z_rad), math.cos(angle_z_rad), 0],
                  [0, 0, 1]]                                           # this row represents z axis

    # Combine Rotation matrices to get final rotation matrix
    """
     zip() is a built in python function that can take multiple iterables 
     and constructs the iterator of tuples where each tuples contains elements from each iterable
    """

    rotation_matrix = [[sum(a * b for a, b in zip(row, col)) for col in zip(*rotation_z)] for row in rotation_x]
   # rotation_matrix = np.dot(rotation_z, np.dot(rotation_y, rotation_x))


    # Display rotation matrix
    result_label.config(text = str(rotation_matrix))


# Screen Display Section

window = tk.Tk()
window.title("Rotation Calculator")

# Input Labels and Entry fields
label_x = tk.Label(window, text ="Rotation X (degrees): ")
label_x.pack()
entry_x = tk.Entry(window)
entry_x.pack()

label_y = tk.Label(window, text ="Rotation Y (degrees): ")
label_y.pack()
entry_y = tk.Entry(window)
entry_y.pack()

label_z = tk.Label(window, text ="Rotation Z (degrees): ")
label_z.pack()
entry_z = tk.Entry(window)
entry_z.pack()

# Create calculate Button
calculate_button = tk.Button(window, text = "CALCULATE", command = calculate_rotation)
calculate_button.pack()

# Create result Label
result_label = tk.Label(window, text="Result")
result_label.pack()

# Run the Tkinter event loop
window.mainloop()