

class Comment:
    def __init__(self, content, author):
        self.author = author
        self.content = content

    def __str__(self):
        return f"----------\n" \
               f"{self.content}\n" \
               f"User: {self.author}\n" \
               f"----------"

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if 3 <= len(value) <= 200:
            self._content = value
        else:
            raise ValueError('Content must be between 3 and 200 characters long!')
