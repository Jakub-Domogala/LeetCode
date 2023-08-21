import os
import re
class FileCounter:
    def __init__(self):
        self.pattern = r'^\d\d\d\d\. .*\.py$'
        self.start_dir = '.'
            
    def count_files_with_pattern(self):
        count = 0
        for root, dirs, files in os.walk(self.start_dir):
            for file in files:
                if re.match(self.pattern, file):
                    count += 1
                    
        return count

