# K-Means Image Compression Application

This is a Python-based image compression application that utilizes the K-Means clustering 
algorithm to reduce the number of colors in a PNG image. 
The application provides a graphical user interface (GUI) using the Tkinter library.

![image](https://user-images.githubusercontent.com/82286519/135456546-d2ecf259-f44a-42fc-8c9e-e123d541a149.png)

# Features

- Upload a PNG image.
- Specify the number of colors (K) for compression.
- Compress the image.
- View the original and compressed images side by side.
- Display compression statistics including image size and compression ratio.
- Clear the screen and start over.
- Exit the application.

# Prerequisites

Before running the application, make sure you have the following installed:

- Python (3.6 or higher)


# Required Python Libraries

This application relies on several Python libraries. 
You can install them using the provided **requirements.txt** file. 
To install the required libraries, run the following command:

```bash
pip install -r requirements.txt
```

The required libraries are:

- **Pillow** (PIL Fork): A powerful image processing library.
- **Matplotlib**: A plotting and visualization library.
- **NumPy**: A library for numerical computing in Python.

# Usage

1. Run the TkinterGUI.py script to start the application.
2. Click the "Upload an image" button to select a PNG image from your computer.
3. Optionally, specify the number of colors (K) for compression in the "k-means" input field.
   Leave it blank for a default value of 5.
4. Click the "Compress" button to initiate the compression process. A loading message will appear.
5. Once the compression is complete, the original and compressed images will be displayed side by side.
6. Compression statistics including image size and compression ratio will be shown below the images.
7. You can click the "Clear" button to reset the screen and start over.
8. Click the "Exit" button to close the application.

# Note

- Ensure that the input image is in PNG format for proper compression.
- The compression process may take some time, especially for large images and high values of K.
- The application saves the compressed image as "compressed_K_colors.png" in the same directory as the original image.
