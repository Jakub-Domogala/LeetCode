import os
import urllib.parse
from FileCounter import FileCounter
from math import log10, floor

repo_owner = "Jakub-Domogala"
repo_name = "LeetCode"
repo_branch = "master"
repo_base_url = f"https://github.com/{repo_owner}/{repo_name}/blob/{repo_branch}"

file_extensions_included = [".py", ".java", ".cpp"]
files_excluded = [
    "readme_generator.py",
    "test.py",
    "t.py",
    "__pycache__",
    "coverage",
    "tempCodeRunnerFile.py",
    "FileCounter.py",
]
dirs_excluded = ["other"]

input_before = os.path.join("utilities", "readme_beginning.md")
input_after = os.path.join("utilities", "readme_ending.md")

output_file = "README.md"


def generate_file_links(directory="", indent=""):
    links = ""
    entries = os.listdir("./" + directory)
    entries.sort()  # Sort the entries alphabetically

    for entry in entries:
        print(entry)
        if entry[0] == "." or entry in files_excluded:
            continue
        full_path = os.path.join(directory, entry)
        if os.path.isdir(full_path) and not os.path.splitext(entry)[0] in dirs_excluded:
            links += f"{indent}- {entry}\n"
            links += generate_file_links(full_path, indent + "  ")
        elif (
            os.path.splitext(entry)[1] in file_extensions_included
            and entry not in files_excluded
            and not os.path.splitext(entry)[0] in dirs_excluded
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
    f.write("### " + str(count) + " solutions in total")
    counters_size = floor(log10(max(dir_count_dict.values()))) + 1
    f.write(
        "\n`"
        + "{:<{w}d}`".format(dir_count_dict["./1.easy"], w=counters_size)
        + " Easy\n"
    )
    f.write(
        "\n`"
        + "{:<{w}d}`".format(dir_count_dict["./2.medium"], w=counters_size)
        + " Medium\n"
    )
    f.write(
        "\n`"
        + "{:<{w}d}`".format(dir_count_dict["./3.hard"], w=counters_size)
        + " Hard\n"
    )
    # f.write("\n--- \n")
    f.write("## Table of Contents\n")
    file_links = generate_file_links()
    f.write(file_links + "\n--- \n")
    f.write(get_file_content(input_after))
