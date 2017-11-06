def get_cleaned_file_lines(file_name, clean_file_func):
    file_object = open(file_name)
    lines = file_object.readlines()
    file_object.close()
    return clean_file_func(lines)


def clean_lines(lines):
    return map(lambda line : line.strip(), lines)

def clean_lines_by_list_comprehension(lines):
    return  [lines[i].strip() for i in range(len(lines))]


if __name__ == '__main__':
    print get_cleaned_file_lines('file_11_11.txt', clean_lines)
    print get_cleaned_file_lines('file_11_11.txt', clean_lines_by_list_comprehension)
