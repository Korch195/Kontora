class Menu:
    def __init__(self, items):
        self.items = items
        self.cursor_position = 0

    def display(self):
        result = []
        for i, item in enumerate(self.items):
            if i == self.cursor_position:
                result.append(f"['{item}']")
            else:
                result.append(f"'{item}'")
        return "[" + ", ".join(result) + "]"

    def to_the_right(self):
        self.cursor_position = (self.cursor_position + 1) % len(self.items)

    def to_the_left(self):
        self.cursor_position = (self.cursor_position - 1) % len(self.items)