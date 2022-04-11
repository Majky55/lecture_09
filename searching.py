import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode= 'r') as json_file:
        data = json.load(json_file)
    if field not in set(data.keys()):
        return None
    return data[field]


def linear_search(field, searched_num):
    findings = {'positions': [], 'count': 0}

    for index, item in enumerate(field):
        if item == searched_num:
            findings['positions'].append(index)
            findings['count'] += 1
        else:
            pass
    return findings


def main():
    sequencial_data = read_data('sequential.json', 'unordered_numbers')
    print(sequencial_data)
    search = linear_search(sequencial_data, 0)
    print(search)


if __name__ == '__main__':
    main()