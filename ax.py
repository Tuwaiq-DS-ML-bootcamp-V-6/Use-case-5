from PIL import Image

# Open an image file
with Image.open('header.png') as img:
    # Set the desired size
    new_width = 800
    new_height = 600
    # Resize the image
    resized_img = img.resize((new_width, new_height))
    # Save the resized image
    resized_img.save('header.png')