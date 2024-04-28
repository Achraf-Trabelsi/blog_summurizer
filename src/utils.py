"""Helper functions that serve different modules"""


class StringyIO:
    """emulate a file-like object based on string data"""

    def __init__(self, name: str, data: str):
        self.data = data
        self._name = name

    @property
    def name(self):
        return self._name

    def read(self):
        return self.data
