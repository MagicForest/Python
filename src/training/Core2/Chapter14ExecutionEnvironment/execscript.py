def exec_script(file_path):
    file = open(file_path)
    exec file
    file.close()

if __name__ == '__main__':
    exec_script('hello.py')