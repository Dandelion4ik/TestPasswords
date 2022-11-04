import hashlib
import requests

PREFIX_LEN = 5
LINE_DELIMITER = ":"
API_URL = "https://api.pwnedpasswords.com/range/"





password = 'TEst'
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
        print(True, int(count))
        break
