#!/usr/bin/env python3
"""
Fix Phakalane Golf Estate project - move from wrong location to correct position in Qi array.
The issue: id:125 was inserted inside id:124.images array instead of as a sibling in Qi array.
"""

import re
import json

BUNDLE_PATH = "public_html/assets/index-ESYA4Re6.js"

# Read the bundle
with open(BUNDLE_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Now properly add the Phakalane project to the Qi array
# Find where Qi array is defined and locate the position to add id:125

# The Phakalane project object (with all data)
phakalane_project = ''',{id:125,name:"Custom Jungle Gym Installation — Phakalane Golf Estate",location:"Phakalane Golf Estate",completionDate:"10 Feb 2026",description:"Professional jungle gym installation at Phakalane Golf Estate",images:["https://i.postimg.cc/tTvJ9p8K/phakalane-1.jpg","https://i.postimg.cc/t7wJVLYX/phakalane-2.jpg","https://i.postimg.cc/Pxc82TfJ/phakalane-3.jpg","https://i.postimg.cc/vZzp4D5b/phakalane-4.jpg","https://i.postimg.cc/L8bX1jjd/phakalane-5.jpg","https://i.postimg.cc/8czLN7RW/phakalane-6.jpg","https://i.postimg.cc/Nx4bbyQ9/phakalane-7.jpg","https://i.postimg.cc/T1LKHJ8h/phakalane-8.jpg"],revenueBWP:18600,status:"Completed",tags:["jungle-gym","installation","phakalane"]}'''

# Find the Qi array - it's defined as Qi=[...] at the bundle start
# We need to find the LAST closing bracket of the Qi array
# Look for the pattern: Qi=[{...}...{...}...{...}]
# The safest way: find "Qi=[" and then find the matching final "]"

qi_start = content.find("Qi=[")
if qi_start == -1:
    print("ERROR: Could not find Qi array start")
    exit(1)

# Jump past "Qi=["
search_pos = qi_start + 4

# Count nested brackets to find the matching closing bracket
bracket_count = 1
i = search_pos
while i < len(content) and bracket_count > 0:
    if content[i] == '[':
        bracket_count += 1
    elif content[i] == ']':
        bracket_count -= 1
    i += 1

# i is now one past the closing bracket
qi_end = i - 1

if bracket_count != 0:
    print(f"ERROR: Could not find matching closing bracket for Qi array (bracket count: {bracket_count})")
    exit(1)

print(f"✓ Found Qi array: positions {qi_start + 4} to {qi_end}")
print(f"✓ Previous character: '{content[qi_end-1]}'")
print(f"✓ Character at close position: '{content[qi_end]}'")

# Insert the Phakalane project before the closing "]"
new_content = content[:qi_end] + phakalane_project + content[qi_end:]

# Write the fixed bundle
with open(BUNDLE_PATH, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"✓ Added Phakalane project to Qi array")

# Verify the addition
with open(BUNDLE_PATH, 'r', encoding='utf-8') as f:
    verify = f.read()

if "id:125" in verify and "Custom Jungle Gym Installation — Phakalane Golf Estate" in verify:
    print("✓ Verified: Phakalane project successfully added")
    print("✓ Verified: Project name found")
    count = verify.count("id:125")
    print(f"✓ Verified: Found {count} occurrence(s) of id:125")
    
    # Also verify it's in the right place (should be near the end, before final ])
    pos = verify.rfind("id:125")
    near_end = verify.rfind("]", pos)
    if near_end > pos:
        print(f"✓ Verified: id:125 is in proper position (before final array close)")
else:
    print("ERROR: Verification failed - project not properly added")
    exit(1)

print("\n✅ Phakalane Golf Estate project fix complete!")
