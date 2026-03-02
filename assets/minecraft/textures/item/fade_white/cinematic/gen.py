from PIL import Image

# Path to the base image
base_image_path = "assets/minecraft/textures/item/fade_white/cinematic/base.png"  # Replace with your base image path



for opacity in range(0,255):


    # Open the base image
    base_img = Image.open(base_image_path).convert("RGBA")

    # Define the color of the 1x1 pixel overlay (e.g., red with 50% opacity)
    overlay_color = (250, 250, 250, opacity)  # (R, G, B, A) - Red with 50% opacity

    # Create a 1x1 pixel image with the desired overlay color
    overlay_pixel = Image.new("RGBA", (80, 37), overlay_color)


    # Specify the position where the resized overlay will be placed on the base image
    position = (0, 4)  # Modify this to place the pixel overlay where you want (x, y)

    # Apply the resized overlay onto the base image
    base_img.paste(overlay_pixel, position, overlay_pixel)  # The third parameter is the alpha mask

    # Save the resulting image
    output_path = f"assets/minecraft/textures/item/fade_white/cinematic/{opacity}.png"
    base_img.save(output_path)

    print(f"Image with the resized pixel overlay saved as {output_path}")
