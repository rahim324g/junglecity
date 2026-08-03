#!/usr/bin/env python3
"""
Script to move Phakalane Golf Estate from ongoing projects (Zi) to completed projects (Qi)
"""

import re
import datetime

def complete_phakalane_project():
    # Get today's date in the format used in the Qi array
    today = datetime.datetime.now().strftime("%d %b %Y")

    # Read the bundle file
    with open('/Users/rahim/Documents/new website /website /domains/junglecity.newicecity.com/public_html/assets/index-ESYA4Re6.js', 'r') as f:
        content = f.read()

    # Pattern to match the Phakalane project in Zi array
    # We need to be very specific to match exactly this project
    zi_pattern = r'\{id:1,name:"Phakalane Golf Estate",location:"Gaborone, Phakalane",status:"In Progress",progress:5,eta:"August 2025",description:"A massive custom jungle gym installation featuring four towers, multiple slides, rope bridges, and a dedicated toddler area\.",tags:\["Private Home"\],images:\["https://i\.postimg\.cc/TP5V4vF5/madam-maire-3\.png","https://i\.postimg\.cc/zBSRszjv/madam-maire\.png"\],beforeAfter:!1\}'

    # Create the completed project entry for Qi array
    # Using a reasonable revenue estimate based on the project description
    qi_entry = f'''{{id:1,name:"Phakalane Golf Estate",location:"Gaborone, Phakalane",description:"A massive custom jungle gym installation featuring four towers, multiple slides, rope bridges, and a dedicated toddler area.",completedAt:"{today}",revenueBWP:125000,tags:["Private Home"],images:["https://i.postimg.cc/TP5V4vF5/madam-maire-3.png","https://i.postimg.cc/zBSRszjv/madam-maire.png"]}}'''

    # First, remove the project from Zi array
    if re.search(zi_pattern, content):
        print("Found Phakalane project in Zi array, removing...")
        content = re.sub(zi_pattern, '', content)
        print("Removed from Zi array")
    else:
        print("Warning: Could not find exact Phakalane project pattern in Zi array")
        return False

    # Now add to Qi array - we need to find where Qi array ends
    # Look for the closing ] of Qi array
    qi_end_pattern = r'(\],[^}]*Qi\s*=)'

    # Insert the new completed project before the closing bracket of Qi array
    def add_to_qi(match):
        return match.group(1) + ',' + qi_entry

    content = re.sub(qi_end_pattern, add_to_qi, content, flags=re.DOTALL)

    # Write back to file
    with open('/Users/rahim/Documents/new website /website /domains/junglecity.newicecity.com/public_html/assets/index-ESYA4Re6.js', 'w') as f:
        f.write(content)

    print(f"Successfully moved Phakalane Golf Estate to completed projects with completion date: {today}")
    print("Revenue set to: P125,000")
    return True

if __name__ == "__main__":
    success = complete_phakalane_project()
    if success:
        print("\nProject completion script completed successfully!")
        print("Please refresh your local website to see the changes.")
    else:
        print("\nScript failed. Please check the patterns and try again.")