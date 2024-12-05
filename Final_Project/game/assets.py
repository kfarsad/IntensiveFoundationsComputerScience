import os
import turtle

# Define the path to the assets directory
ASSETS_DIR = os.path.join(os.path.dirname(__file__), '..', 'memory_game_2024')

def load_assets():
    """
    Dynamically load all .gif assets from the memory_game_2024 directory.
    Returns a dictionary mapping asset names to their file paths.
    """
    assets = {}

    # Check if the assets directory exists
    if not os.path.exists(ASSETS_DIR):
        raise FileNotFoundError(f"Assets directory not found: {ASSETS_DIR}")

    # Iterate through files in the assets directory
    for filename in os.listdir(ASSETS_DIR):
        if filename.endswith('.gif'):  # Only process .gif files
            asset_path = os.path.join(ASSETS_DIR, filename)
            turtle.register_shape(asset_path)  # Register the shape with Turtle
            asset_name = os.path.splitext(filename)[0]  # Use the filename without extension as the key
            assets[asset_name] = asset_path
            print(f"Loaded asset: {asset_path}")  # Optional: Debugging output

    # Check if any assets were loaded
    if not assets:
        print("Warning: No .gif assets found in the directory.")

    return assets
