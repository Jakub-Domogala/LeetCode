import os
import urllib.parse

repo_owner = "Jakub-Domogala"
repo_name = "LeetCode"
repo_branch = "master"
repo_base_url = f"https://github.com/{repo_owner}/{repo_name}/blob/{repo_branch}"

output_file = "test.md"

def generate_file_links(directory, indent=""):
    links = ""
    for entry in sorted(os.listdir(directory)):
        if entry[0] == '.':
            continue
        full_path = os.path.join(directory, entry)
        # if os.path.isdir(entry):
        #     # print(entry)
        if os.path.isdir(full_path):
            links += f"{indent}- {entry}\n"
            print(full_path)
            links += generate_file_links(full_path, indent + "  ")
        elif entry.endswith(".py"):  # Check if the file has a .py extension
            # print(directory, full_path)
            file_link = f"{repo_base_url}/{urllib.parse.quote(directory)}/{urllib.parse.quote(entry)}"
            links += f"{indent}- [{entry}]({file_link})\n"
    return links.replace(".%5C", "")

with open(output_file, "w") as f:
    f.write("# Repository Contents\n\n")
    f.write("This README contains links to Python files in the repository.\n\n")
    f.write("## Table of Contents\n")
    file_links = generate_file_links('.')
    f.write(file_links)
