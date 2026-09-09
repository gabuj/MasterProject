"""
This script reads an HDF5 file and prints its structure, including groups and datasets.
"""
import h5py

def print_structure(name, obj):
    """Callback function to print the type and name of each item."""
    if isinstance(obj, h5py.Dataset):
        print(f"Dataset: /{name} (Shape: {obj.shape}, Type: {obj.dtype})")
    elif isinstance(obj, h5py.Group):
        print(f"Group:   /{name}")


file_path ="DataAnalysis/Calibration/DataFilesCal/Files_TokyoCouette/mean.h5"

with h5py.File(file_path, 'r') as f:
    print(f"--- Structure of {file_path} ---")
    # visititems recursively goes through all groups and datasets
    f.visititems(print_structure)