#!/usr/bin/python3
"""
this defines the basemodel module
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """ BaseModel class defines common attributes and methods that can be
    inherited by other classes in application.

    Attributes:
        id (str): universally unique identifier (UUID) for object.
        created_at (datetime): indicating object's creation time.
        updated_at (datetime): indicating object's last update time.

    Methods:
        __init__: Initializes a new instance of BaseModel class.
        __str__: Returns a string representation of object.
        save: Updates 'updated_at' attribute to current timestamp.
        to_dict: Converts object to a dictionary format.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes new instance of BaseModel class.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        date_format = "%Y-%m-%dT%H:%M:%S.%f"
                        self.__dict__[key] = datetime.strptime(
                                value, date_format)
                    else:
                        self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns string representation of object.

        Returns:
            str: string containing class name, id
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates 'updated_at' attribute to current timestamp.
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts object to dictionary format.

        Returns:
            dict: dictionary representation of object.
        """
        obj = self.__dict__.copy()
        obj['__class__'] = self.__class__.__name__
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj
