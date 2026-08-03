#!/usr/bin/env python3
"""Extract and update Phakalane project with correct image URLs"""

BUNDLE_PATH = "public_html/assets/index-ESYA4Re6.js"

# Real working image URLs
REAL_IMAGES = [
    "https://i.postimg.cc/3w0D9PQm/6507F332-08A8-4BF0-8844-22AB1BC044C8-1-102-a.jpg",
    "https://i.postimg.cc/BZmQLMRg/6216BC37-FE21-44C3-82B2-64CF1FC10268-1-102-a.jpg",
    "https://i.postimg.cc/tJcjrmj1/5339FFD6-6A07-4925-81E1-D97637DE56A3-1-102-a.jpg",
    "https://i.postimg.cc/V6LPzcsy/822272C3-EA28-4F06-9FE1-59D8E456939E-1-105-c.jpg",
    "https://i.postimg.cc/FF6XXqMR/7859692E-948A-406D-8290-2D4C802F2C55-1-102-a.jpg",
    "https://i.postimg.cc/GpdZj1y5/C1A42310-5FED-4642-9958-85EDA2D67F1D-1-102-a.jpg",
    "https://i.postimg.cc/1R85FpPR/D8EEEEC7-CDE3-43A7-8945-47B15611D6CF-1-201-a.jpg",
    "https://i.postimg.cc/rphM0pPh/EAABDD20-24EC-4C68-A752-5B26B93ED791-1-105-c.jpg",
]

# Create the images array string
images_str = '","'.join(REAL_IMAGES)
images_array = f'["{images_str}"]'

print(f"Images array to insert:\n{images_array}\n")

# Read bundle
with open(BUNDLE_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the id:125 project object
# Pattern: {id:125,...images:[...]}
import re

# Find everything from {id:125 to the next closing brace that belongs to it
# This is complex in minified code, so let's use a simpler approach:
# Find "id:125," and replace everything up to the closing images array

# Look for the pattern: id:125,name:"Custom Jungle Gym...",... more stuff ...,images:[...]}
pattern = r'({id:125,name:"Custom Jungle Gym Installation — Phakalane Golf Estate"[^}]*?),images:\[[^\]]*\]'

def replace_images(match):
    # Get the part before images
    before_images = match.group(1)
    # Return it with the new images array
    return f'{before_images},images:{images_array}'

new_content = re.sub(pattern, replace_images, content, count=1)

if new_content != content:
    print("✓ Found and replacing Phakalane project images...")
    with open(BUNDLE_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("✅ Image URLs updated successfully!")
    
    # Verify
    with open(BUNDLE_PATH, 'r', encoding='utf-8') as f:
        verify = f.read()
    if "3w0D9PQm" in verify and "rphM0pPh" in verify:
        print("✓ Verified: New image URLs are in the bundle")
else:
    print("⚠ Could not find the exact pattern. Trying alternative approach...")
    # Alternative: find where "Custom Jungle Gym Installation — Phakalane Golf Estate" is
    # and look for images array near it
    phakalane_pos = content.find("Custom Jungle Gym Installation — Phakalane Golf Estate")
    if phakalane_pos > -1:
        print(f"✓ Found Phakalane project at position {phakalane_pos}")
        context = content[max(0, phakalane_pos-100):min(len(content), phakalane_pos+500)]
        print(f"Context:\n{context}\n")
        
        # Try to find and replace the images array after this position
        images_start = content.find('images:[',  phakalane_pos)
        if images_start > -1:
            print(f"✓ Found images array at position {images_start}")
            images_end = content.find(']', images_start) + 1
            old_images = content[images_start:images_end]
            print(f"Old images: {old_images[:100]}...")
            
            new_bundle = content[:images_start] + f'images:{images_array}' + content[images_end:]
            with open(BUNDLE_PATH, 'w', encoding='utf-8') as f:
                f.write(new_bundle)
            print("✓ Replaced images array")
            print("✅ Image URLs updated successfully!")
    else:
        print("✗ Could not find Phakalane project in bundle")
