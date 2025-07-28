#!/usr/bin/env python3
"""
Animal Abstract Base Class Implementation
Defines animal sounds through abstract methods and concrete subclasses.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class representing an animal."""
    
    @abstractmethod
    def make_sound(self) -> str:
        """Produce the characteristic sound of the animal.
        
        Returns:
            str: The sound the animal makes
        """
        pass

class Canine(Animal):
    """Concrete class representing dogs and related species."""
    
    def make_sound(self) -> str:
        """Generate the barking sound of a dog.
        
        Returns:
            str: The sound "Bark"
        """
        return "Bark"

class Feline(Animal):
    """Concrete class representing cats and related species."""
    
    def make_sound(self) -> str:
        """Generate the meowing sound of a cat.
        
        Returns:
            str: The sound "Meow"
        """
        return "Meow"
