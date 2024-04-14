class Menu:
    def __init__(self, items):
        self.items = items
        self.cursor_position = 0

    def to_the_right(self):
        self.cursor_position = (self.cursor_position + 1) % len(self.items)

    def to_the_left(self):
        self.cursor_position = (self.cursor_position - 1) % len(self.items)

    def display(self):
        display_list = [f"['{item}']" if idx == self.cursor_position else f"'{item}'" for idx, item in enumerate(self.items)]
        return "[" + ", ".join(display_list) + "]"
