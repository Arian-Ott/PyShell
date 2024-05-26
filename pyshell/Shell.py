"""
"""
import hashlib
import os


class Shell:

    def __init__(self, name):
        self._config = []
        self.name = name
        self._id = hashlib.blake2b(name.encode(), salt=b"um9we89mu0qerwrh").hexdigest()

    def __str__(self):
        return self.name

    def add(self, value):
        pass

    def __dict__(self):
        pass
