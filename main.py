import hashlib
import sys

import requests

PREFIX_LEN = 5
LINE_DELIMITER = ":"
API_URL = "https://api.pwnedpasswords.com/range/"


def check_pwd(password=""):
    hash = hashlib.sha1(bytes(password, "utf8")).hexdigest()
    hash_prefix = hash[0:PREFIX_LEN]
    hash_suffix = hash[PREFIX_LEN:]

    response = requests.get(API_URL + hash_prefix)
    if response.status_code != 200:
        raise Exception("PwnedPasswords API looks down")

    results = response.text.split("\n")
    for result in results:
        hash_suffix_candidate, count = result.split(LINE_DELIMITER)
        if hash_suffix_candidate.lower().lstrip() == hash_suffix:
            return True
    return False


if len(sys.argv) > 1:
    if sys.argv[1] == '-f':
        file_name = sys.argv[2]
        with open(file_name, mode="r") as file:
            for item in file:
                item = item.rstrip()
                answer = check_pwd(item)
                if answer:
                    print(item, " : LEAKED!")
                else:
                    print(item, " : NOT LEAKED!")
    else:
        password = sys.argv[1]
        answer = check_pwd(password)
        if answer:
            print(password, " : LEAKED!")
        else:
            print(password, " : NOT LEAKED!")
