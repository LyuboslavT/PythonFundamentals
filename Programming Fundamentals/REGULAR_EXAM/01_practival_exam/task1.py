class StringEditor:

    def __init__(self, initial_string):
        self.string = initial_string

    def translate(self, char, replacement):
        self.string = self.string.replace(char, replacement)
        print(self.string)

    def includes(self, substring):
        if substring in self.string:
            print("True")
        else:
            print("False")

    def start(self, substring):
        if self.string.startswith(substring):
            print("True")
        else:
            print("False")

    def lowercase(self):
        self.string = self.string.lower()
        print(self.string)

    def find_index(self, char):
        print(self.string.rfind(char))

    def remove(self, start_index, count):
        self.string = self.string[:start_index] + self.string[start_index + count:]
        print(self.string)

    def execute(self, actions):
        parts = actions.split()
        action = parts[0]

        if action == "Translate":
            self.translate(parts[1], parts[2])
        elif action == "Includes":
            self.includes(parts[1])
        elif action == "Start":
            self.start(parts[1])
        elif action == "Lowercase":
            self.lowercase()
        elif action == "FindIndex":
            self.find_index(parts[1])
        elif action == "Remove":
            self.remove(int(parts[1]), int(parts[2]))


def main():
    input_string = input()
    edited_string = StringEditor(input_string)

    while True:
        actions = input()
        if actions == "End":
            break
        edited_string.execute(actions)

main()
