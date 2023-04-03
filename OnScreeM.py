from tkinter import *
from math import sqrt
import numpy as np

root = Tk()

canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack()

# Create a variable to store the first click
first_click = None
second_click = None

# Create a empty list to put all measurements
# This is not cleaned by space
collected_measurements = []

# Create a variable to store the scale factor
scale_factor = None


# Define main function to recognize clicks
def on_click(event):
    global first_click, second_click, scale_factor, escape_on
    escape_on = False
    
    if scale_factor:
        color = "blue"
    else:
        color = "red"



    # If this is the first click, draw a red circle
    if first_click is None:
        first_click = (event.x, event.y)
        canvas.create_oval(first_click[0]-5, first_click[1]-5, first_click[0]+5, first_click[1]+5, fill=color)


    # If this is the second click, draw a red circle, draw a line between the two points, and calculate the scale factor
    else:
        second_click = (event.x, event.y)
        canvas.create_oval(second_click[0]-5, second_click[1]-5, second_click[0]+5, second_click[1]+5, fill=color)
        canvas.create_line(first_click, second_click, width=5, fill=color)

        # if the scale factor is not defined consider the distance as dscaling factor
        # otherwise, show measurement
        if scale_factor is None:
            pixels = sqrt((second_click[0]-first_click[0])**2 + (second_click[1]-first_click[1])**2)
            scale_factor = pixels / 1.0
            canvas.create_text(event.x+20, event.y+20, text=f"{round(pixels, 0)} px = 1 cm", font=("TkDefaultFont", 20))
            print(f"{scale_factor} px = 1 cm")


        else:
            distance = round(sqrt((second_click[0]-first_click[0])**2 + (second_click[1]-first_click[1])**2) / scale_factor, 2)
            canvas.create_text(event.x+20, event.y+20, text=f"{distance} cm", font=("TkDefaultFont", 20))
            collected_measurements.append(distance)
            print(f"{distance} cm added to the list")

        first_click = None
    

# Bind the on_click function to the left mouse button
canvas.bind("<Button-1>", on_click)


## Set binds to keys and their functions

# Function to clean screen OR kill app
# escape_on = False
def on_escape(event):
    # global escape_on
    # if escape_on:
    #     root.destroy()
    # else:
        # escape_on = True
    canvas.delete("all")
    global first_click, second_click, scale_factor
    first_click = None
    second_click = None
    scale_factor = None


root.bind("<Escape>", on_escape)



# Function to minimize the window when space bar is pressed
def on_space(event):
    root.iconify()
# Bind the on_space function to the space bar key
root.bind("<space>", on_space)



# Function to clean the last measurments in the memory
def on_backspace(event):
    global collected_measurements
    if len(collected_measurements) > 0:
        collected_measurements.pop()
        print("Last measurement removed")
# Bind the on_space function to the BackSpace key
root.bind("<BackSpace>", on_backspace)


# Function to create a way to report max mins and possible outliers
def on_tab(event):
    global collected_measurements

    # Find outliners 
    def find_outliers(lst):
        # Find the first and third quartiles (Q1 and Q3)
        q1, q3 = np.percentile(lst, [25, 75])

        # Find the interquartile range (IQR)
        iqr = q3 - q1

        # Define the outlier limits
        lower_limit = q1 - (1.5 * iqr)
        upper_limit = q3 + (1.5 * iqr)

        # Find the outliers
        outliers = [x for x in lst if x < lower_limit or x > upper_limit]
        
        # Find the minimum and maximum within the non-outlier range
        inliers = [x for x in lst if x >= lower_limit and x <= upper_limit]
        inlier_min = min(inliers)
        inlier_max = max(inliers)

        # Return the results
        return (inlier_min, inlier_max, outliers)

    # Clear the clipboard
    root.clipboard_clear()
    # Put the variable into the clipboard

    minimum, maximum, outliers = find_outliers(collected_measurements)
    

    report = f"{round(minimum,1)}-{round(maximum,1)}"


    if outliers:
        min_outliers = min(outliers)
        max_outliers = max(outliers)
        
        if min_outliers and min_outliers < minimum: 
            report = f"({round(min_outliers,1)}-){report}"
        if max_outliers and max_outliers > maximum: 
            report = f"{report}(-{round(max_outliers,1)})"

    report = report + " cm"

    root.clipboard_append(f"{report}")
    print(f"{report} copied to the clipboard")

root.bind("<Tab>", on_tab)


root.attributes("-fullscreen", True)
root.attributes('-alpha', 0.35)


###mag

from PIL import ImageGrab, ImageDraw, ImageTk

mag_canvas_size = 300
mag_canvas = Canvas(root, width=mag_canvas_size, height=mag_canvas_size, bg='white')
mag_canvas.place(x=10, y=10)


def magnify(event):
    # Get the current cursor position
    x, y = root.winfo_pointerxy()

    
    # Calculate the coordinates of the area to magnify
    mag_factor = mag_canvas_size / 15
    x1, y1 = x - mag_factor, y - mag_factor
    x2, y2 = x + mag_factor, y + mag_factor
    
    # Capture the image around the cursor
    image = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    
    # Draw a crosshair at the cursor position
    draw = ImageDraw.Draw(image)
    draw.line((0, mag_factor, mag_factor*2, mag_factor), fill="black", width=1)
    draw.line((mag_factor, 0, mag_factor, mag_factor*2), fill="black", width=1)
    
    
    
    # Resize the image to fit the mini-canvas
    image = image.resize((300, 300))
    
    # Convert the image to a Tkinter PhotoImage
    photo = ImageTk.PhotoImage(image)
    
    # Update the mini-canvas with the magnified image
    mag_canvas.create_image(0, 0, anchor='nw', image=photo)
    mag_canvas.image = photo  # to prevent garbage collection


# root.bind('<Shift-KeyPress>', magnify)
canvas.bind('<Motion>', magnify)



# def hide_mag_canvas(event):
#     mag_canvas.delete('all')

# root.bind('<Shift-KeyRelease>', hide_mag_canvas)





###mag




root.mainloop()







