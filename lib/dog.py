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

    def __init__(self):
        self._name = ""
        self._breed = ""

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <=25:
            self._name = name
        else:
            print("Name must be a string between 1 and 25 characters.")

    name = property(get_name, set_name,)   

    def get_breed(self):
        print("Getting the breed.")
        return self._breed
    def set_breed(self, breed):
        if (type(breed) in APPROVED_BREEDS):
            print(f"Setting breed to {breed}")
            self._breed = breed
        else:
            print("Name must be a string between 1 and 25 characters.")

    breed = property (get_breed, set_breed,)
