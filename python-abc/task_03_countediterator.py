#!/usr/bin/env python3
"""Iterator that keeps count of items retrieved."""

class CountedIterator:
    """Custom iterator that tracks number of items consumed."""
    
    def __init__(self, iterable):
        """Initialize with iterable and set up counter.
        
        Args:
            iterable: Any iterable object (list, tuple, etc.)
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def __iter__(self):
        """Return self as iterator object."""
        return self

    def __next__(self):
        """Get next item and increment counter.
        
        Returns:
            Next item from iterator
            
        Raises:
            StopIteration: When no more items available
        """
        item = next(self.iterator)  # May raise StopIteration
        self.counter += 1
        return item

    def get_count(self):
        """Return number of items retrieved so far.
        
        Returns:
            int: Count of items iterated
        """
        return self.counter
