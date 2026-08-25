import os
import shutil
import re

base_dir = r"f:\PycharmProject\Algorithm"
array_dir = os.path.join(base_dir, "array")
archive_dir = os.path.join(array_dir, "archive")

# Create non-array target directories
other_dirs = {
    "oop": ["Bus.py", "hotel.py", "restaurant.py", "shoppingcart.py", "voting.py"],
    "math_and_string": ["13. RomanToInteger.py", "9. PalindromeNumber.py", "7, ReverseInteger.py", 
                        "204. CountPrimes.py", "263. Ugly Number.py", "58.py", "28. leetcode.py"],
    "dict": ["706. DesignHashMap.py", "535. EncodeAndDecodeTinyURL.py"],
    "queue": ["933.py"]
}

for d, files in other_dirs.items():
    d_path = os.path.join(base_dir, d)
    os.makedirs(d_path, exist_ok=True)
    for f in files:
        f_path = os.path.join(array_dir, f)
        if os.path.exists(f_path):
            shutil.move(f_path, os.path.join(d_path, f))

# Move oop folder if it exists in array
oop_folder = os.path.join(array_dir, "oop")
if os.path.exists(oop_folder):
    # Merge contents into base/oop
    for item in os.listdir(oop_folder):
        shutil.move(os.path.join(oop_folder, item), os.path.join(base_dir, "oop", item))
    os.rmdir(oop_folder)

# Define array techniques
techniques = ["two_pointers", "subarray", "searching_sorting", "basic_operations"]
for t in techniques:
    os.makedirs(os.path.join(array_dir, t), exist_ok=True)
os.makedirs(archive_dir, exist_ok=True)

# Helper to normalize file names to group duplicates
def get_core_name(filename):
    name = filename.lower()
    if name.endswith('.py'):
        name = name[:-3]
    # Remove prefix numbers like 1., 1.1, 10., etc.
    name = re.sub(r'^(\d+(\.\d+)?\s*\+?\s*\d*\.?\s*)', '', name)
    # Remove trailing _1, _2
    name = re.sub(r'_\d+$', '', name)
    # Remove dots and trim spaces
    name = name.replace('.', '').strip()
    return name

def classify_core(core_name):
    if any(x in core_name for x in ['two_sum', 'twosum', 'remove_duplicate', 'move_zero', 'palidrome', 'palindrome', 'rearrange_negative', 'remove_element', 'intersection']):
        return "two_pointers"
    if any(x in core_name for x in ['subarray', 'find_all_sum', 'sum']):
        return "subarray"
    if any(x in core_name for x in ['sort', 'search', 'square', 'absolute_difference']):
        return "searching_sorting"
    return "basic_operations"

grouped_files = {}

for f in os.listdir(array_dir):
    f_path = os.path.join(array_dir, f)
    if not os.path.isfile(f_path) or not f.endswith('.py'):
        continue
        
    core = get_core_name(f)
    if core not in grouped_files:
        grouped_files[core] = []
    
    size = os.path.getsize(f_path)
    grouped_files[core].append({'name': f, 'path': f_path, 'size': size})

# Process groups: Keep the largest file in the technique folder, move others to archive
for core, files in grouped_files.items():
    # Sort files by size descending
    files.sort(key=lambda x: x['size'], reverse=True)
    
    technique = classify_core(core)
    best_file = files[0]
    
    # Move the best file to the technique folder
    dest_path = os.path.join(array_dir, technique, best_file['name'])
    print(f"Keeping {best_file['name']} in {technique}")
    shutil.move(best_file['path'], dest_path)
    
    # Move the rest to archive
    for dup in files[1:]:
        print(f"Archiving {dup['name']}")
        dest_archive = os.path.join(archive_dir, dup['name'])
        shutil.move(dup['path'], dest_archive)

print("Done organizing array folder.")
