import json
from colorama import Fore


def find_matching_values(file1, file2):
    with open(file1, 'r', encoding='utf-8') as fileOne, \
            open(file2, 'r', encoding='utf-8') as fileTwo:
        try:
            data1 = json.load(fileOne)
            data2 = json.load(fileTwo)
        except (json.JSONDecodeError, FileNotFoundError) as exception:
            print(f"{Fore.RED}Error: Failed to load JSON data from "
                  f"{Fore.BLUE}{file1}{Fore.RESET} {Fore.RED}or "
                  f"{Fore.BLUE}{file2}{Fore.RESET}{Fore.RED}."
                  f"{Fore.RESET}")
            print(f"{Fore.RED}{exception}{Fore.RESET}")
            return

        ignored_keys = ["success", "took", "total", "successful", "skipped", "failed", "value", "relation", "max_score",
                        "_index", "_type", "_score", "from", "to"]

        for key1, value1 in get_all_items(data1):
            if is_value_ignored(key1, ignored_keys):
                continue  # Skip ignored keys
            for key2, value2 in get_all_items(data2):
                if value1 == value2 and not is_value_ignored(key2, ignored_keys):
                    print('-' * 100)
                    print(f"{Fore.GREEN}Matched Value:{Fore.RESET}", value1)
                    print(f"JSON Path - file1.json: {key1}")
                    print(f"JSON Path - file2.json: {key2}")


def get_all_items(data, parent_key=''):
    if isinstance(data, dict):
        for k, v in data.items():
            yield from get_all_items(v, parent_key + '.' + str(k) if parent_key else str(k))
    elif isinstance(data, list):
        for i, v in enumerate(data):
            yield from get_all_items(v, parent_key + '.' + str(i))
    else:
        yield parent_key, data


'''
# Here you can add logic to check if the value is ignored
# Returns True if the value should be excluded from the output, False otherwise.
# Below is an example of ignoring values equal to "elastic_value"
'''


def is_value_ignored(json_path, ignored_keys):
    # split the JSON path and check if any part contains an ignored key
    for key in ignored_keys:
        if key in json_path:
            return True
    return False


if __name__ == "__main__":
    # passing 2 JSON files to the function
    find_matching_values('file1.json', 'file2.json')
