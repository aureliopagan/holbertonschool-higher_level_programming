#!/usr/bin/env python3
"""Custom list that prints operations as they happen."""

class VerboseList(list):
    """A list that prints notifications for modifications."""
    
    def append(self, item):
        """Add item to end of list with notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """Add multiple items to list with notification."""
        count = len(items)
        super().extend(items)
        print(f"Extended the list with [{count}] items.")

    def remove(self, value):
        """Remove first occurrence of value with notification."""
        print(f"Removed [{value}] from the list.")
        super().remove(value)

    def pop(self, index=-1):
        """Remove and return item at index with notification."""
        item = self[index] if index != -1 else self[-1]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
    