from os import listdir, path

directory = input()
files_in_dir = [f for f in listdir(directory) if path.isfile(path.join(directory, f))]
folders_in_dir = [f for f in listdir(directory) if path.isdir(path.join(directory, f))]
for folder in folders_in_dir:
    subdirectory = directory + '/' + folder
    files_in_dir.extend([f for f in listdir(subdirectory) if path.isfile(path.join(subdirectory, f))])
extensions_dict = dict()

for file in files_in_dir:
    extension = file.split('.')[1]
    if extension in extensions_dict.keys():
        extensions_dict[extension].append(file)
    else:
        extensions_dict[extension] = [file]

for k in extensions_dict.keys():
    extensions_dict[k].sort()
extensions_dict = dict(sorted(extensions_dict.items()))

output = []
for extension, files in extensions_dict.items():
    output.append(f".{extension}")
    for file in files:
        output.append(f"- - - {file}")
output = "\n".join(output)

file = open(f"{directory}/report.txt", "w")
file.write(output)
file.close()
