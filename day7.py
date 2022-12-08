# Class to hold the directory information with methods to calculate sizes and find the folder to delete
class dir:
    sum_size = 0
    del_dir = float('inf')
    MAX_SIZE = 100000
    def __init__(self, name, parent) -> None:
        self.name = name
        self.file_size = 0
        self.total_size = -1
        self.sub_dir = {}
        self.parent = parent
    def get_sizes(self) -> int:
        # Check if we got total size already
        if self.total_size > -1:
            return self.total_size
        # or calculate it
        else:   
            self.total_size = self.file_size     
            for directory in self.sub_dir.values():
                self.total_size += directory.get_sizes()
            # Add the total to the class variable sum size if under criteria
            if self.total_size <= dir.MAX_SIZE:
                dir.sum_size += self.total_size
            return self.total_size
    def get_delete_size(self, delete_size) -> None:
            # Check if this is the smallest directory that could free up enough space
            if self.total_size >= delete_size and self.total_size < dir.del_dir:
                dir.del_dir = self.total_size
            # Check all sub folders
            for directory in self.sub_dir.values():
                directory.get_delete_size(delete_size)


# Open input file
f = open("day7_input.txt", "r")

# Root of folder structure
root = dir("/", None)

# Variable to hold cur working director
cwd = root

# Read in line by line
for line in f:
    # Check if its a command out an output
    if line[0] == '$':
        # If we moved to root
        if line == "$ cd /\n":
            cwd = root
        # If we run ls then do nothing
        elif line == "$ ls\n":
            pass        
        # Else we changed to a new folder
        else:
            # is it up or down
            _, cmd, directory = line.split(' ')
            if directory == "..\n":
                cwd = cwd.parent
            else:
                cwd = cwd.sub_dir[directory]
    # It is an output
    else:
        # Get info on file / directory
        size, name = line.split(' ')
        # Process if we are directory
        if size == "dir":
            if name not in cwd.sub_dir:
                cwd.sub_dir[name] = dir(name, cwd)
        else:
            cwd.file_size += int(size)



# Calculate size of directories 
root.get_sizes()

# Find required space to delete
space_needed = 30000000 - (70000000 - root.total_size)
root.get_delete_size(space_needed)

# Get results
print(dir.sum_size)
print(dir.del_dir)


f.close()
