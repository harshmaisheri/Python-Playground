import requests
import hashlib
import sys


def request_api(query_string):
    url = "https://api.pwnedpasswords.com/range/" + query_string
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, Please check api and try again later.')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def passwordHash(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1password[:5], sha1password[5:]
    response = request_api(first5)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = passwordHash(password)
        if count:
            print(f'Your Password {password} has been hacked {count} times.')
        else:
            print('Great You have a unique Password')
    return "Done..!!"


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
