import re


class Dir:
    def __init__(self, path) -> None:
        self.path = path
        self.parent_folders = "/".join(current_path.split("/")[:-1])
        self.sub_dirs = []
        self.size = 0
        self.file_count = 0
        self.file_list = []

    def add_contents(self, content):
        size = 0
        if content.startswith("dir"):
            self.sub_dirs.append(content[4:])

        else:
            # digits = re.compile(r"\d+")
            # size = int(re.findall(digits, content)[0])
            size, file = content.split()
            self.size += int(size)
            self.file_count += 1
            self.file_list.append(file)
        return int(size)


with open("day_07.input") as f:
    lines = f.read().split("\n")

lines.append("$ cd ..")
total_size = 0
current_path = "."
disk = {current_path: Dir(current_path)}
folder_name = ""
for i, line in enumerate(lines[1:], start=1):
    # print(line)
    # input
    if line.startswith("$"):
        commands = line[2:].split()

        if len(commands) == 2 and commands[1] != "..":
            # cd

            folder_name = "/" + commands[1]
            current_path += folder_name

            if current_path not in disk:
                disk[current_path] = Dir(
                    current_path,
                )

        if len(commands) == 2 and commands[1] == "..":
            # up one directory
            size = disk[current_path].size
            current_path = "/".join(current_path.split("/")[:-1])
            disk[current_path].size += size
    # output
    else:
        total_size += disk[current_path].add_contents(line)


# def part1():
#     output = 0
#     for dir in disk.values():
#         if dir.size <= 30000000:
#             output += dir.size
#     return output


total_disk = disk["."].size
print(total_disk)

space_needed = 70000000 - total_disk
space_needed = 30000000 - space_needed
print(space_needed)

dir_list = []
for dir in disk.values():
    if dir.size >= space_needed:
        dir_list.append(dir.size)
dir_list = sorted(dir_list)
print(dir_list)
# output = []
# for dir in disk.values():
#     if dir.size <= 30000000:
#         output.append(dir.size)
# # sorted(output)
# print(output[0])
