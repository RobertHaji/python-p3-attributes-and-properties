#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name: str = "Unnamed", breed: str = "Beagle"):
        self._name = None  # Initialize the private attribute
        self.name = name    # Use the setter to validate the name
        self.breed = breed  # Use the setter to validate the breed

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # Save in title case
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = "Unnamed"  # Default name

    @property
    def breed(self) -> str:
        return self._breed

    @breed.setter
    def breed(self, value: str):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
            self._breed = "Beagle"  # Default breed
     
            

    
    
    