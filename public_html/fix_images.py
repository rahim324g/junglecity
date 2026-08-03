#!/usr/bin/env python3
"""Replace placeholder Phakalane image URLs with real ones"""

BUNDLE_PATH = "public_html/assets/index-ESYA4Re6.js"

# Mapping of placeholder URLs to real URLs
IMAGE_REPLACEMENTS = {
    "i.postimg.cc/tTvJ9p8K/phakalane-1.jpg": "i.postimg.cc/3w0D9PQm/6507F332-08A8-4BF0-8844-22AB1BC044C8-1-102-a.jpg",
    "i.postimg.cc/t7wJVLYX/phakalane-2.jpg": "i.postimg.cc/BZmQLMRg/6216BC37-FE21-44C3-82B2-64CF1FC10268-1-102-a.jpg",
    "i.postimg.cc/Pxc82TfJ/phakalane-3.jpg": "i.postimg.cc/tJcjrmj1/5339FFD6-6A07-4925-81E1-D97637DE56A3-1-102-a.jpg",
    "i.postimg.cc/vZzp4D5b/phakalane-4.jpg": "i.postimg.cc/V6LPzcsy/822272C3-EA28-4F06-9FE1-59D8E456939E-1-105-c.jpg",
    "i.postimg.cc/L8bX1jjd/phakalane-5.jpg": "i.postimg.cc/FF6XXqMR/7859692E-948A-406D-8290-2D4C802F2C55-1-102-a.jpg",
    "i.postimg.cc/8czLN7RW/phakalane-6.jpg": "i.postimg.cc/GpdZj1y5/C1A42310-5FED-4642-9958-85EDA2D67F1D-1-102-a.jpg",
    "i.postimg.cc/Nx4bbyQ9/phakalane-7.jpg": "i.postimg.cc/1R85FpPR/D8EEEEC7-CDE3-43A7-8945-47B15611D6CF-1-201-a.jpg",
    "i.postimg.cc/T1LKHJ8h/phakalane-8.jpg": "i.postimg.cc/rphM0pPh/EAABDD20-24EC-4C68-A752-5B26B93ED791-1-105-c.jpg",
}

# Read bundle
with open(BUNDLE_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all image URLs
for old_url, new_url in IMAGE_REPLACEMENTS.items():
    if old_url in content:
        content = content.replace(old_url, new_url)
        print(f"✓ Replaced {old_url.split('/')[-1]}")
    else:
        print(f"⚠ Not found: {old_url}")

# Write back
with open(BUNDLE_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ All image URLs updated successfully!")
