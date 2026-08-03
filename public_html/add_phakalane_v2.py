#!/usr/bin/env python3
"""Add Phakalane Golf Estate to completed projects."""

with open('public_html/assets/index-ESYA4Re6.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the closing bracket of project 124 - search for the pattern that ends id:124
search_str = '},{id:125,'
if search_str in content:
    print("✗ Project 125 already exists")
else:
    # Search for where the projects array ends - it should be after id:124
    #  Find  the pattern: ...id:124,...}] (end of projects array)
    pattern_start = content.find('id:124,name:"3D Jungle Gym Design')
    if pattern_start == -1:
        print("✗ Could not find project 124")
    else:
        # Find the closing bracket of the projects array after project 124
        # Look for "]}," which marks the end of the Qi array
        search_pos = pattern_start + 100
        while search_pos < len(content) - 100:
            if content[search_pos:search_pos+3] == ']},' or content[search_pos:search_pos+2] == ']}':
                # Found the end of array, insert before it
                new_project = ',{id:125,name:"Custom Jungle Gym Installation — Phakalane Golf Estate",location:"Phakalane Golf Estate, Gaborone",description:"Professional custom jungle gym installation with multiple play elements and safety features",completedAt:"10 Feb 2026",revenueBWP:18600,tags:["Custom Jungle Gym Installation","Private Residence"],images:["https://i.postimg.cc/3w0D9PQm/6507F332-08A8-4BF0-8844-22AB1BC044C8-1-102-a.jpg","https://i.postimg.cc/BZmQLMRg/6216BC37-FE21-44C3-82B2-64CF1FC10268-1-102-a.jpg","https://i.postimg.cc/tJcjrmj1/5339FFD6-6A07-4925-81E1-D97637DE56A3-1-102-a.jpg","https://i.postimg.cc/V6LPzcsy/822272C3-EA28-4F06-9FE1-59D8E456939E-1-105-c.jpg","https://i.postimg.cc/FF6XXqMR/7859692E-948A-406D-8290-2D4C802F2C55-1-102-a.jpg","https://i.postimg.cc/GpdZj1y5/C1A42310-5FED-4642-9958-85EDA2D67F1D-1-102-a.jpg","https://i.postimg.cc/1R85FpPR/D8EEEEC7-CDE3-43A7-8945-47B15611D6CF-1-201-a.jpg","https://i.postimg.cc/rphM0pPh/EAABDD20-24EC-4C68-A752-5B26B93ED791-1-105-c.jpg"]}'
                
                new_content = content[:search_pos] + new_project + content[search_pos:]
                
                with open('public_html/assets/index-ESYA4Re6.js', 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print("✓ Successfully added Phakalane Golf Estate project")
                print("  - Project id: 125")
                print("  - Revenue: P 19,600")
                print("  - Images: 8 photos")
                print("  - Status: Completed")
                break
            search_pos += 1
