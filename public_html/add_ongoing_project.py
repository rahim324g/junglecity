#!/usr/bin/env python3
"""Add new ongoing projects to the Zi array in the minified bundle."""

import re
import json

def add_ongoing_projects(projects_list):
    """Add multiple new projects to the ongoing projects Zi array."""

    # Read the bundle
    with open('public_html/assets/index-ESYA4Re6.js', 'r', encoding='utf-8') as f:
        content = f.read()

    # Build all new projects as a single addition
    new_projects_str = ""
    for project_data in projects_list:
        # Convert images and tags to minified format
        images_str = ",".join([f'"{img}"' for img in project_data['images']])
        tags_str = ",".join([f'"{tag}"' for tag in project_data['tags']])

        # Create the new project in minified format (with leading comma)
        new_project = f',{{id:{project_data["id"]},name:"{project_data["name"]}",location:"{project_data["location"]}",status:"{project_data["status"]}",progress:{project_data["progress"]},eta:"{project_data["eta"]}",description:"{project_data["description"]}",tags:[{tags_str}],images:[{images_str}],beforeAfter:{str(project_data["beforeAfter"]).lower()}}}'
        new_projects_str += new_project

    # Find the insertion point - before the closing bracket of Zi array
    # Look for the last project and the closing bracket
    pattern = r'(\{id:3,name:"LouieVille Kgale Hill"[^}]*beforeAfter:!1\})\]'

    if re.search(pattern, content):
        # Replace the closing bracket with new projects + closing bracket
        new_content = re.sub(pattern, r'\1' + new_projects_str + r']', content)

        # Write the updated bundle
        with open('public_html/assets/index-ESYA4Re6.js', 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"✓ Successfully added {len(projects_list)} projects to Ongoing Projects:")
        for project in projects_list:
            print(f"  - '{project['name']}' (ID: {project['id']}, Status: {project['status']}, Progress: {project['progress']}%)")
        return True
    else:
        print("✗ Could not find insertion point in Zi array")
        return False

if __name__ == "__main__":
    # Example usage - add your new projects here
    new_projects = [
        {
            "id": 8,
            "name": "Botlhale Cambridge International School Jungle Gym",
            "location": "Gaborone, Botswana",
            "status": "In Progress",
            "progress": 35,
            "eta": "April 2026",
            "description": "Custom-designed jungle gym installation for Botlhale Cambridge International School featuring multiple climbing structures, slides, rope challenges, and age-appropriate play zones for primary school students.",
            "tags": ["School Installation", "Custom Design"],
            "images": [
                "https://i.postimg.cc/qq2HKy3F/IMG-4223.jpg",
                "https://i.postimg.cc/xdX7HLrK/Whats-App-Image-2026-02-20-at-10-21-41.jpg"
            ],
            "beforeAfter": False
        }
    ]

    success = add_ongoing_projects(new_projects)
    if not success:
        print("Failed to add one or more projects")
        exit(1)