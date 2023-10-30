import os
from matplotlib import pyplot as plt
from matplotlib.ticker import NullLocator


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



def plot_side_by_side(images_and_titles):
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









