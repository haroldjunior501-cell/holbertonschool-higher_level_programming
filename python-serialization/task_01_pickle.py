#!/usr/bin/env python3
"""Custom object serialization using pickle."""
import pickle


class CustomObject:
    """A custom object that supports pickle serialization."""

    def __init__(self, name, age, is_student):
        """Initialize CustomObject with name, age, and is_student."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the object to a file using pickle."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize and return a CustomObject from a pickle file."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
