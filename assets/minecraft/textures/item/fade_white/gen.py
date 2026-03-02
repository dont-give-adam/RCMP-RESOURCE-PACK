from PIL import Image

# Directory to save images
output_dir = "assets/minecraft/textures/item/fade_black/"

# Create directory if it doesn't exist
import os
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate images with opacity from 0 to 255
for opacity in range(256):
    # Create an RGBA image with a transparent background
    img = Image.new('RGBA', (1, 1), (0, 0, 0, opacity))  # White pixel with varying opacity

    # Save the image with the corresponding opacity value
    img.save(os.path.join(output_dir, f"{opacity}.png"))

print(f"Images have been saved to {output_dir}")