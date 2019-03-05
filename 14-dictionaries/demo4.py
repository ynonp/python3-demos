import glob
import os.path

# defaultdict
# Counter


all_files_with_extensions = glob.glob('*.*')
print(all_files_with_extensions)

counter = {}
for filenmae in all_files_with_extensions:
    _, ext = os.path.splitext(filenmae)
    try:
        counter[ext] += 1
    except KeyError:
        counter[ext] = 1

print(counter)
