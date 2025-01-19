from abc import ABC, abstractmethod
from typing import Any


class ComputerThingsException(Exception):
    def __init__(self, message: str = ''):
        super().__init__(message)

class Metadatad:
    """
    Give objects a metadata dictionary.
    """
    def __init__(self):
        self._metadata = {"uid": None}

    @property
    def metadata(self):
        return self._metadata

    def set_metavalue(self, key_name: str, value: Any, allow_override: bool = False, allow_create: bool = True):
        """
        Set the value of a metadata key-pair.
        :param key_name: the name of the key.
        :param value: the value to set the key to.
        :param allow_override: Override existing values?
        :param allow_create: Create missing keys?
        :return: nothing

        :raises KeyError: If key doesn't exist *and* creation is not allowed.
        :raises ValueError: If key is already set *and* override is not allowed.
        """
        if not allow_create and key_name not in self._metadata.keys():
            raise KeyError(f"Metadata Dictionary: the key '{key_name}' does not exist.")
        elif not allow_override and key_name in self._metadata.keys():
            raise ValueError(f"Metadata Dictionary: the key '{key_name}' already exists and could not be set to '{value}'.")

        else:
            try:
                self._metadata.update({key_name: value})
            except Exception as e:
                print(e)

    def get_metavalue(self, key_name: str, return_none: bool = False):
        """
        Retrieve a metadata value from a key-pair.
        :param key_name: name of the key to retrieve.
        :param return_none: return a value of *None* if missing or empty. Default is *False*.
        :return: the value, None if empty and allowed.
        :raises KeyError: if matching key is not found and not-allowed to return *None*.
        """
        if key_name not in self._metadata.keys():
            if return_none:
                return None
            else:
                raise KeyError(f"Metadata Key Missing: Couldn't find {key_name} in the metadata dictionary.")



class BaseHardware(ABC):

    @abstractmethod
    def __init__(self):
        pass

class BaseSoftware(ABC):

    @abstractmethod
    def __init__(self):
        pass


test = Metadatad()

test.set_metavalue("testing", 100)
print(test.metadata)
test.set_metavalue("testing", 200, allow_override=True)
print(test.metadata)

