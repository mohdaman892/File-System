
global prompt


class FileNode:
    name = None
    path = None
    children = None
    parent = None

    def __init__(self, path, name, parent):
        self.name = name
        self.path = path
        self.parent = parent
        self.children = {}


class FileSystem:
    current_node = None

    def __init__(self, name):
        self.current_node = FileNode(f"{name}/", name, None)

    def get_current_path(self):
        print(self.current_node.path)

    def create_file(self, filename):
        new_filenode = FileNode(f"{self.current_node.path}{filename}/", filename, self.current_node)
        self.current_node.children[filename] = new_filenode
        new_filenode.children[self.current_node.name] = self.current_node
        print(f"Created {filename} successfully!")

    def delete_file(self, filename):
        if filename in self.current_node.children:
            delete_file_node = self.current_node.children[filename]
            delete_file_node.parent = None
            delete_file_node.children = None
            self.current_node.children.pop(filename)
            print(f"Deleted {filename} successfully!")
        else:
            print(f"{filename} does not exists on this path!")

    def rename_file(self, filename, new_name):
        pass   # TO-DO Costliest operation, need to be optimized

    def open_file(self, filename):
        if filename in self.current_node.children:
            self.current_node = self.current_node.children[filename]
            global prompt
            prompt = f"{self.current_node.path}>"
        else:
            print(f"{filename} does not exists on this path!")

    def go_back(self):
        if self.current_node.parent:
            self.current_node = self.current_node.parent
            global prompt
            prompt = f"{self.current_node.path}>"
        else:
            print("Cannot go back, you are at root or parent does not exists!")

    def show_files(self):
        for child in self.current_node.children:
            if self.current_node.children[child] != self.current_node.parent:
                print(self.current_node.children[child].name, end=" ")
        print()

    def search(self, filename):

        def dfs(root):
            if filename in root.children:
                self.found_path.append(root.children[filename].path)

            for node in root.children.values():
                if node not in visited:
                    visited.add(node)
                    dfs(node)

        visited = set()
        root = self.current_node
        self.found_path = []
        visited.add(root)
        dfs(root)
        print(*self.found_path)


if __name__ == "__main__":
    print("***************************************")
    print("Welcome to Aman's filesystem")
    print("Type pwd for showing the current path")
    print("Type ls for showing all files")
    print("Type mkdir filename for creating")
    print("Type cd.. for going back")
    print("rm filename for removing file")
    print("search filename for searching file")
    print("****************************************")
    initial_name = "C:"
    fs = FileSystem(initial_name)
    commands = {"ls": fs.show_files, "cd": fs.open_file, "rm": fs.delete_file, "search": fs.search,
                "pwd": fs.get_current_path, "mkdir": fs.create_file,
                "cd..": fs.go_back}
    global prompt
    prompt = "C:>"
    while True:
        s = input(prompt)
        if s == "exit":
            break
        try:
            if s.find(" ") != -1:
                l = list(s.split(" "))
                if len(l) == 2:
                    cmd, arg = l[0], l[1]
                    if cmd not in commands:
                        print(f"{cmd} not a valid command!")
                    else:
                        commands[cmd](arg)
                elif len(l) == 3:
                    cmd, arg1, arg2 = l[0], l[1], l[2]
                    if cmd not in commands:
                        print(f"{cmd} not a valid command!")
                    else:
                        commands[cmd](arg1, arg2)
            else:
                cmd = s
                if cmd not in commands:
                    print(f"{cmd} not a valid command!")
                else:
                    commands[cmd]()
        finally:
            continue
