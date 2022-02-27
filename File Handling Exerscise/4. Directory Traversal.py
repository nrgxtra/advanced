import os
import pathlib
directory = input()
dd = dict()

for root, directories, files in  os.walk(directory):
    for file in files:
        extension = '.' + file.split('.')[-1]
        if extension not in dd:
            dd[extension] = []
        dd[extension].append(file)
result = ''
for ext in sorted(dd.keys()):
    result += ext + '\n'
    for file in sorted(dd[ext]):
        result += f'- - - {file}\n'
new_directory = str(pathlib.Path.home()) + os.path.sep + 'Desktop'
final = new_directory + os.path.sep + 'report.txt'
with open(final, 'x') as report_fh:
    report_fh.write(result)







