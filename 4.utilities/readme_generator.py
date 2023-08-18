import os
import urllib.parse

repo_owner = "Jakub-Domogala"
repo_name = "LeetCode"
repo_branch = "master"
repo_base_url = f"https://github.com/{repo_owner}/{repo_name}/blob/{repo_branch}"

output_file = "README.md"

def generate_file_links(directory="", indent=""):
    links = ""
    entries = os.listdir("./" + directory)
    entries.sort()  # Sort the entries alphabetically
    for entry in entries:
        if entry[0] == '.':
            continue
        full_path = os.path.join(directory, entry)
        if os.path.isdir(full_path):
            links += f"{indent}- {entry}\n"
            links += generate_file_links(full_path, indent + "  ")
        elif entry.endswith(".py") and entry != "readme_generator.py":  # Check if the file has a .py extension
            file_link = f"{repo_base_url}/{urllib.parse.quote(directory)}/{urllib.parse.quote(entry)}".replace('\\', '/').replace('%5C', '/')
            links += f"{indent}- [{entry}]({file_link})\n"
    return links

with open(output_file, "w") as f:
    f.write("# LeetCode\n\n")
    f.write("![ghost-white](https://github.com/Jakub-Domogala/LeetCode/assets/78169141/46417268-208f-438b-8670-85166ac484b5) \n")
    f.write('\n')
    f.write("\n\n")
    f.write("## Table of Contents\n")
    file_links = generate_file_links()
    f.write(file_links)
