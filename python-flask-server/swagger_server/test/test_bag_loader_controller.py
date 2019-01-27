# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.bag import Bag  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBagLoaderController(BaseTestCase):
    """BagLoaderController integration test stubs"""

    def test_delete_bag(self):
        """Test case for delete_bag

        Delete Bag
        """
        response = self.client.open(
            '/bagloader//{bagId}'.format(bagId='bagId_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_bag_by_id(self):
        """Test case for get_bag_by_id

        Get bag location from Id
        """
        response = self.client.open(
            '/bagloader//{bagId}'.format(bagId='bagId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_load_bag(self):
        """Test case for load_bag

        Load a bag into the airplane
        """
        body = Bag()
        response = self.client.open(
            '/bagloader//load',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
