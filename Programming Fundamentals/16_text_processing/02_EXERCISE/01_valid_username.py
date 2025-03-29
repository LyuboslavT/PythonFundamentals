usernames = input()

user = usernames.split(", ")

allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"


def is_valid(username):
    if 3 <= len(username) <= 16:
        for ch in username:
            if ch not in allowed_chars:
                return False
        return True
    return False


for name in user:
    if is_valid(name):
        print(name)