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


def pattern_search(field, pattern):
    findings = set()
    for index, sub in enumerate(field[:-len(pattern)]):
        if field[index: index + len(pattern)] == pattern:
            findings.add(index)
    return findings


def main():
    sequencial_data_lin = read_data('sequential.json', 'unordered_numbers')
    print(sequencial_data_lin)
    search = linear_search(sequencial_data_lin, 0)
    print(search)
    sequencial_data_pat = read_data('sequential.json', 'dna_sequence')
    print(sequencial_data_pat)
    search = pattern_search(sequencial_data_pat, 'ATA')
    print(search)


if __name__ == '__main__':
    main()