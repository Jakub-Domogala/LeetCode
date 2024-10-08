import os
import urllib.parse
from FileCounter import FileCounter

repo_owner = "Jakub-Domogala"
repo_name = "LeetCode"
repo_branch = "master"
repo_base_url = f"https://github.com/{repo_owner}/{repo_name}/blob/{repo_branch}"

file_extensions_included = [".py"]
files_excluded = [
    "readme_generator.py",
    "test.py",
    "__pycache__",
    "coverage",
    "tempCodeRunnerFile.py",
    "FileCounter.py",
]

input_before = os.path.join("utilities", "readme_beginning.md")
input_after = os.path.join("utilities", "readme_ending.md")

output_file = "README.md"


def generate_file_links(directory="", indent=""):
    links = ""
    entries = os.listdir("./" + directory)
    entries.sort()  # Sort the entries alphabetically
    for entry in entries:
        if entry[0] == "." or entry in files_excluded:
            continue
        full_path = os.path.join(directory, entry)
        if os.path.isdir(full_path):
            links += f"{indent}- {entry}\n"
            links += generate_file_links(full_path, indent + "  ")
        elif (
            os.path.splitext(entry)[1] in file_extensions_included
            and entry not in files_excluded
        ):
            file_link = f"{repo_base_url}/{urllib.parse.quote(directory)}/{urllib.parse.quote(entry)}".replace(
                "\\", "/"
            ).replace(
                "%5C", "/"
            )
            links += f"{indent}- [{entry}]({file_link})\n"
    return links


def get_file_content(filename):
    if not os.path.exists(filename):
        print(f"Warning: {filename} does not exist. Skipping...")
        return ""

    with open(filename, "r") as file:
        return file.read()

count, dir_count_dict = FileCounter().count_files_with_pattern()

with open(output_file, "w") as f:
    f.write(get_file_content(input_before) + "\n")
    f.write("\n")
    f.write("\n\n")
    f.write("## Table of Contents\n")
    file_links = generate_file_links()
    f.write(file_links + "\n--- \n")
    f.write(
        "### " + str(count) + " solutions in total"
    )
    f.write("\n`" + "{:4d}`".format(dir_count_dict['./1.easy']) + " easy problems\n")
    f.write("\n`" + "{:4d}`".format(dir_count_dict['./2.medium']) + " medium problems\n")
    f.write("\n`" + "{:4d}`".format(dir_count_dict['./3.hard']) + " hard problems\n")
    f.write("\n--- \n")
    f.write(get_file_content(input_after))
