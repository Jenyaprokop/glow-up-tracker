from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size):
    img = Image.new('RGB', (size, size), color='#0a0e1a')
    draw = ImageDraw.Draw(img)
    
    # Blue circle background
    margin = size * 0.12
    draw.ellipse([margin, margin, size-margin, size-margin], fill='#3b82f6')
    
    # Lightning bolt / flame emoji approximation using text
    # Draw "GU" text
    font_size = int(size * 0.38)
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', font_size)
    except:
        font = ImageFont.load_default()
    
    text = "GU"
    bbox = draw.textbbox((0,0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (size - tw) / 2
    y = (size - th) / 2 - bbox[1]
    draw.text((x, y), text, fill='white', font=font)
    
    return img

for size in [192, 512]:
    img = create_icon(size)
    img.save(f'icon-{size}.png')
    print(f"Created icon-{size}.png")

