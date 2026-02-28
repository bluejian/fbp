"""
Composite Jian's face onto the Mario sprite.
Steps:
1. Load the Mario outfit (has a white/hollow face area)
2. Load Jian's face photo
3. Crop just the face area from the photo
4. Create a circular mask for the face
5. Paste the face into the Mario sprite's face opening
6. Save the final composite
"""
from PIL import Image, ImageDraw, ImageFilter

# Paths
MARIO_PATH = "public/images/mario-outfit-2.png"
FACE_PATH = "public/images/jian11.jpeg"
OUTPUT_PATH = "public/images/jian-mario-final.png"

# Load images
mario = Image.open(MARIO_PATH).convert("RGBA")
face_photo = Image.open(FACE_PATH).convert("RGBA")

mario_w, mario_h = mario.size
print(f"Mario sprite size: {mario_w}x{mario_h}")

# The face hole in the Mario sprite is approximately in the upper third
# Based on the sprite, the face area is roughly centered horizontally
# and sits under the hat (about 20-35% from top, centered)

# For this specific sprite, the white face area is roughly:
# x: 25%-65% of width, y: 15%-45% of height
face_center_x = int(mario_w * 0.48)
face_center_y = int(mario_h * 0.32)
face_radius = int(mario_w * 0.18)  # radius of face circle

print(f"Face placement: center=({face_center_x},{face_center_y}), radius={face_radius}")

# Crop Jian's face - focus on the center of the photo (the face)
fw, fh = face_photo.size
# The face is centered in the photo, crop a square around the center-upper area
crop_size = min(fw, fh) // 2
face_cx = fw // 2
face_cy = int(fh * 0.38)  # Face is in the upper part of the photo
crop_box = (
    face_cx - crop_size // 2,
    face_cy - crop_size // 2,
    face_cx + crop_size // 2,
    face_cy + crop_size // 2
)
face_cropped = face_photo.crop(crop_box)

# Resize face to fit the face hole
face_diameter = face_radius * 2
face_resized = face_cropped.resize((face_diameter, face_diameter), Image.LANCZOS)

# Create circular mask with soft edges
mask = Image.new("L", (face_diameter, face_diameter), 0)
draw = ImageDraw.Draw(mask)
# Draw a filled circle
draw.ellipse([0, 0, face_diameter - 1, face_diameter - 1], fill=255)
# Slightly blur the mask edges for smoother blending
mask = mask.filter(ImageFilter.GaussianBlur(radius=2))

# Apply the circular mask to the face
face_circular = Image.new("RGBA", (face_diameter, face_diameter), (0, 0, 0, 0))
face_circular.paste(face_resized, (0, 0), mask)

# Calculate paste position (top-left corner)
paste_x = face_center_x - face_radius
paste_y = face_center_y - face_radius

# Create a working copy
result = mario.copy()

# First paste the face BEHIND the Mario sprite
# Create a new canvas, paste face first, then Mario on top
canvas = Image.new("RGBA", mario.size, (0, 0, 0, 0))
canvas.paste(face_circular, (paste_x, paste_y), face_circular)

# Now paste Mario on top - the hat and body will cover the edges of the face
# We need to composite so transparent areas show the face underneath
result = Image.alpha_composite(canvas, mario)

# Save
result.save(OUTPUT_PATH, "PNG")
print(f"Saved composite to: {OUTPUT_PATH}")
print(f"Final size: {result.size}")
