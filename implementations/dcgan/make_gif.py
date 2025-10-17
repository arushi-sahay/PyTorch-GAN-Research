import imageio
import os

# Path to your images folder
image_folder = "images"
output_gif = "training_progress.gif"

# Collect all .png files in the folder, sorted by epoch number
images = sorted([img for img in os.listdir(image_folder) if img.endswith(".png")],
                key=lambda x: int(x.split('.')[0]))

# Read images and build the GIF
frames = []
for img in images:
    frame = imageio.imread(os.path.join(image_folder, img))
    frames.append(frame)

# Save GIF
imageio.mimsave(output_gif, frames, duration=0.5)  # duration controls frame speed

print(f"✅ GIF saved as {output_gif}")
