class FacebookRecord:

    def __init__(self):

        self.followers = {}

    def new_follower(self, username):
        if username not in self.followers:
            self.followers[username] = {
                "likes": 0,
                "comments": 0
            }

    def like(self, username, count):
        if username not in self.followers:
            self.followers[username] = {
                "likes": count,
                "comments": 0
            }
        else:
            self.followers[username]["likes"] += count

    def comment(self, username):
        if username not in self.followers:
            self.followers[username] = {
                "likes": 0,
                "comments": 1
            }
        else:
            self.followers[username]["comments"] += 1

    def blocked(self, username):
        if username in self.followers:
            del self.followers[username]
        else:
            print(f'{username} doesn\'t exist.')

    def execute(self):
        print(f'{len(self.followers)} followers')
        for user, stats in self.followers.items():
            total = stats["likes"] + stats["comments"]
            print(f'{user}: {total}')

def main():

    facebook_statistics = FacebookRecord()

    while True:
        line = input()
        if line == "Log out":
            break

        parts = line.split(": ")

        command = parts[0]

        if command == "New follower":
            facebook_statistics.new_follower(parts[1])

        elif command == "Like":
            username, count = parts[1], int(parts[2])
            facebook_statistics.like(username, count)

        elif command == "Comment":
            username = parts[1]
            facebook_statistics.comment(username)


        elif command == "Blocked":
            username = parts[1]
            facebook_statistics.blocked(username)

    facebook_statistics.execute()

main()