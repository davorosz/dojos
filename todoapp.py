import sys

def file_list()
    with open("todolist.txt", "r") as file:
        lines = file.readlines()
        file.close()

def add_to_list():
    item = input("add an item: ")
    with open("todolist.txt", "a") as file:
        file.write("[ ]" + item )
    print("add to the list")
    file.close()

def read_list():
    choose == "list":
    with open("todolist.txt", "r") as f:
        print(f.read())
        file.close()

def archive()
if command =="archive":
    with open("todolist.txt","w") as file_handle:
        for line in range(len(lines)):
            if lines == "x":
                continue
            else:
                file_handle.write(lines)
    print("all to do is deleted")
    file.close()



elif choose == "mark":
    with open("to_do_list.txt", "r+") as f:
        line = f.readlines()

    for line in lines:
        print(line)
