# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ApiResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, location: str=None):  # noqa: E501
        """ApiResponse - a model defined in Swagger

        :param location: The location of this ApiResponse.  # noqa: E501
        :type location: str
        """
        self.swagger_types = {
            'location': str
        }

        self.attribute_map = {
            'location': 'location'
        }

        self._location = location

    @classmethod
    def from_dict(cls, dikt) -> 'ApiResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ApiResponse of this ApiResponse.  # noqa: E501
        :rtype: ApiResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def location(self) -> str:
        """Gets the location of this ApiResponse.


        :return: The location of this ApiResponse.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location: str):
        """Sets the location of this ApiResponse.


        :param location: The location of this ApiResponse.
        :type location: str
        """

        self._location = location
