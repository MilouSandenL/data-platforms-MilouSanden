import re
from pathlib import Path

print("This is path of this script")

data_path = print(Path(__file__).parent /"data" /"ml_text_raw")

with open (data_path/"ml_text_raw.txt", 'r') as file:
    raw_text = file.read()

# tar bort extra spacing
text_fix_spacing = re.sub(r"\s+", " ", raw_text)

print(text_fix_spacing)

