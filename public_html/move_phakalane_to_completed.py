#!/usr/bin/env python3
import re
import json

def move_phakalane_to_completed():
    # File path
    file_path = "/Users/rahim/Documents/new website /website /domains/junglecity.newicecity.com/public_html/assets/index-ESYA4Re6.js"

    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find Phakalane in Zi array
    zi_pattern = r'Zi=\[([^\]]*)\]'
    zi_match = re.search(zi_pattern, content, re.DOTALL)

    if not zi_match:
        print("Could not find Zi array")
        return

    zi_content = zi_match.group(1)

    # Find Phakalane project (id:1)
    phakalane_pattern = r'\{id:1,[^}]*\}'
    phakalane_match = re.search(phakalane_pattern, zi_content, re.DOTALL)

    if not phakalane_match:
        print("Could not find Phakalane project in Zi array")
        return

    phakalane_obj = phakalane_match.group(0)
    print(f"Found Phakalane: {phakalane_obj[:100]}...")

    # Convert Phakalane object to completed format
    # Extract basic info
    name_match = re.search(r'name:"([^"]*)"', phakalane_obj)
    location_match = re.search(r'location:"([^"]*)"', phakalane_obj)
    description_match = re.search(r'description:"([^"]*)"', phakalane_obj)
    tags_match = re.search(r'tags:\[([^\]]*)\]', phakalane_obj)
    images_match = re.search(r'images:\[([^\]]*)\]', phakalane_obj)

    if not all([name_match, location_match, description_match, tags_match, images_match]):
        print("Could not extract all required fields from Phakalane")
        return

    name = name_match.group(1)
    location = location_match.group(1)
    description = description_match.group(1)
    tags = tags_match.group(1)
    images = images_match.group(1)

    # Create completed project object
    completed_phakalane = f'''{{id:1,name:"{name}",location:"{location}",description:"{description}",completedAt:"20 Apr 2026",revenueBWP:85000,tags:[{tags}],images:[{images}]}}'''

    print(f"Completed Phakalane: {completed_phakalane[:100]}...")

    # Remove Phakalane from Zi array
    zi_without_phakalane = re.sub(phakalane_pattern, '', zi_content, flags=re.DOTALL)

    # Clean up extra commas
    zi_without_phakalane = re.sub(r',,+', ',', zi_without_phakalane)
    zi_without_phakalane = re.sub(r',\s*\]', ']', zi_without_phakalane)

    # Update Zi array
    new_zi = f'Zi=[{zi_without_phakalane}]'
    content = re.sub(zi_pattern, new_zi, content, flags=re.DOTALL)

    # Find Qi array and add Phakalane
    qi_pattern = r'Qi=\[([^\]]*)\]'
    qi_match = re.search(qi_pattern, content, re.DOTALL)

    if not qi_match:
        print("Could not find Qi array")
        return

    qi_content = qi_match.group(1)

    # Add Phakalane to the beginning of Qi array
    new_qi_content = completed_phakalane + ',' + qi_content
    new_qi = f'Qi=[{new_qi_content}]'
    content = re.sub(qi_pattern, new_qi, content, flags=re.DOTALL)

    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Successfully moved Phakalane Golf Estate from ongoing to completed projects!")
    print("- Removed from Zi (ongoing projects)")
    print("- Added to Qi (completed projects) with completion date 20 Apr 2026 and revenue BWP 85,000")

if __name__ == "__main__":
    move_phakalane_to_completed()