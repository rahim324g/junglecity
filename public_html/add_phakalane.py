#!/usr/bin/env python3
"""Add Phakalane Golf Estate project to the completed projects list."""

import re
import json

# Read the bundle
with open('public_html/assets/index-ESYA4Re6.js', 'r', encoding='utf-8') as f:
    content = f.read()

# New project data for Phakalane Golf Estate
phakalane_project = {
    "id": 125,
    "name": "Custom Jungle Gym Installation — Phakalane Golf Estate",
    "location": "Phakalane Golf Estate, Gaborone",
    "description": "Professional custom jungle gym installation with multiple play elements and safety features",
    "completedAt": "10 August 2025",
    "revenueBWP": 19600,
    "tags": ["Custom Jungle Gym Installation", "Private Residence"],
    "images": [
        "https://i.postimg.cc/3w0D9PQm/6507F332-08A8-4BF0-8844-22AB1BC044C8-1-102-a.jpg",
        "https://i.postimg.cc/BZmQLMRg/6216BC37-FE21-44C3-82B2-64CF1FC10268-1-102-a.jpg",
        "https://i.postimg.cc/tJcjrmj1/5339FFD6-6A07-4925-81E1-D97637DE56A3-1-102-a.jpg",
        "https://i.postimg.cc/V6LPzcsy/822272C3-EA28-4F06-9FE1-59D8E456939E-1-105-c.jpg",
        "https://i.postimg.cc/FF6XXqMR/7859692E-948A-406D-8290-2D4C802F2C55-1-102-a.jpg",
        "https://i.postimg.cc/GpdZj1y5/C1A42310-5FED-4642-9958-85EDA2D67F1D-1-102-a.jpg",
        "https://i.postimg.cc/1R85FpPR/D8EEEEC7-CDE3-43A7-8945-47B15611D6CF-1-201-a.jpg",
        "https://i.postimg.cc/rphM0pPh/EAABDD20-24EC-4C68-A752-5B26B93ED791-1-105-c.jpg"
    ]
}

# Convert to minified JSON format
# Need to escape quotes and format properly for the minified bundle
images_str = ",".join([f'"{img}"' for img in phakalane_project['images']])
tags_str = ",".join([f'"{tag}"' for tag in phakalane_project['tags']])

# Find the insertion point - after the last project in the array
# Search for a specific pattern that indicates the end of a project
pattern = r'},\{id:124,name:"3D Jungle Gym Design — Extension 11"'
if pattern in content:
    # Find where this section ends to insert our new project after the Extension 11 project
    match = re.search(r'(\},\{id:124,name:"3D Jungle Gym Design — Extension 11"[^}]*images:\[[^\]]*\]})\]([:,])', content)
    
    if match:
        # Create the new project in minified format
        new_project = f',{{id:125,name:"Custom Jungle Gym Installation — Phakalane Golf Estate",location:"Phakalane Golf Estate, Gaborone",description:"Professional custom jungle gym installation with multiple play elements and safety features",completedAt:"10 Feb 2026",revenueBWP:18600,tags:["Custom Jungle Gym Installation","Private Residence"],images:[{images_str}]}}'
        
        # Insert before the closing bracket
        insertion_point = match.end(1)
        new_content = content[:insertion_point] + new_project + content[insertion_point:]
        
        # Write the updated bundle
        with open('public_html/assets/index-ESYA4Re6.js', 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("✓ Successfully added Phakalane Golf Estate project to Completed Projects")
        print(f"  - Project ID: 125")
        print(f"  - Revenue: P 18,600")
        print(f"  - Images: 8 photos added")
    else:
        print("✗ Could not find insertion point in bundle")
else:
    print("✗ Could not locate Extension 11 project reference")
