import glob
import os.path
import collections
all_files_with_extensions = glob.glob('*.*')
print(all_files_with_extensions)

counter = collections.defaultdict(int)

for filenmae in all_files_with_extensions:
    _, ext = os.path.splitext(filenmae)
    counter[ext] += 1


print(counter)
