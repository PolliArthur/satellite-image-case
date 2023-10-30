import os
from matplotlib import pyplot as plt
import math
import cv2


def list_files(folder_path, extensions):
    """
    List files in a folder based on given extensions.

    Args:
        folder_path (str): The path to the folder you want to search.
        extensions (list of str): List of file extensions to search for (e.g., ['.png', '.jpg']).

    Returns:
        List of file paths that match the specified extensions.
    """
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        return []  # Folder doesn't exist or is not a directory, return an empty list

    matching_files = []
    for root, _, files in os.walk(folder_path):
        for filename in files:
            _, file_extension = os.path.splitext(filename)
            if file_extension.lower() in extensions:
                matching_files.append(os.path.join(root, filename))

    return matching_files



def plot_side_by_side2(images_and_titles):
    """
    Plots multiple images side by side using Matplotlib.

    Args:
        *images_and_titles: Variable number of tuples (image, title) where 'image' is a numpy.ndarray and 'title' is a string.
    """
    
    num_images = len(images_and_titles)
    fig, axes = plt.subplots(1, num_images, figsize=(12, 5))

    for i, (image, title) in enumerate(images_and_titles):
        ax = axes[i]
        ax.imshow(image)
        ax.set_title(title)
        ax.axis('off')

    plt.show()







def plot_side_by_side(images_and_titles, max_col=4, normalize=True, cmap=None, colorbar_label=None, colorbar_ticks=None):
    """
    Plots multiple images side by side using Matplotlib with an optional colormap and a single horizontal colorbar at the vertical middle.

    Args:
        *images_and_titles: Variable number of tuples (image, title) where 'image' is a numpy.ndarray and 'title' is a string.
        max_col: Maximum number of columns per row.
        cmap: The colormap to use for displaying the images. If not specified, a default colormap is used.
        colorbar_label: The label for the colorbar.
        colorbar_ticks: List of values to display as scale ticks on the colorbar.
    """

    num_images = len(images_and_titles)
    rows = math.ceil(num_images / max_col)  # Calculate the number of rows needed

    fig, axes = plt.subplots(rows, max_col, figsize=(16, 5 * (rows)))  # Create a grid of subplots

    for i, (image, title) in enumerate(images_and_titles):
        row = i // max_col  # Calculate the row for the current image
        col = i % max_col  # Calculate the column for the current image
        ax = axes[row, col]
        im = ax.imshow(image, cmap=cmap)  # Use the specified colormap
        ax.set_title(title)
        ax.axis('off')

    # Define the position for the colorbar at the vertical middle
    cbar_x = 0.2
    cbar_y = 0.05
    cbar_width = 0.6
    cbar_height = 0.02

    if normalize:
        # Normalize the colorbar between 0 and 1
        norm = plt.Normalize(vmin=0, vmax=1)
    else:
        norm = None

    cax = fig.add_axes([cbar_x, cbar_y, cbar_width, cbar_height])  # Adjust these values as needed
    cbar = plt.colorbar(im, cax=cax, orientation='horizontal', norm=norm, ticks=colorbar_ticks)

    if colorbar_label:
        cbar.set_label(colorbar_label)  # Customize the label if provided

    plt.tight_layout()
    plt.show()


def apply_erode(result_mask,k_size = 3,k_type =cv2.MORPH_CROSS , _iterations = 3):     
    return cv2.erode(result_mask,cv2.getStructuringElement(k_type, (k_size, k_size)),iterations=_iterations)   
def apply_dilate(result_mask,k_size = 3,k_type =cv2.MORPH_CROSS, _iterations = 3):     
    return cv2.dilate(result_mask,cv2.getStructuringElement(k_type, (k_size, k_size)),iterations=_iterations)  










