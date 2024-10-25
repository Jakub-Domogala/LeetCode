from collections import defaultdict
import os
import re


class FileCounter:
    def __init__(self):
        self.pattern = r"^\d{4}\. .*\.(py|java)$"
        self.start_dir = "."

    def count_files_with_pattern(self):
        count = 0
        dir_count_dict = defaultdict(int)
        cheked_dict = defaultdict(bool)
        for root, dirs, files in os.walk(self.start_dir):
            for file in files:
                if re.match(self.pattern, file):
                    match = re.match(r"(\d{4})\.", file).groups(1)
                    if match not in cheked_dict:
                        dir_count_dict[root] += 1
                        count += 1
                    else:
                        cheked_dict[match] = True
        return count, dir_count_dict

if __name__ == "__main__":
    for e in [f"{key}:\t{value}" for key, value in sorted(FileCounter().count_files_with_pattern()[1].items())]:
        print(e)
