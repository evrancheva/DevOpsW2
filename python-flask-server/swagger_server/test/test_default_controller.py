# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.errorunknown import ERRORUNKNOWN  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.persons import Persons  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_persons_get(self):
        """Test case for persons_get

        Gets some persons
        """
        query_string = [('pageSize', 100),
                        ('pageNumber', 1)]
        headers = [('User_Agent', 'User_Agent_example')]
        response = self.client.open(
            '/openapi101/persons',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_persons_post(self):
        """Test case for persons_post

        Creates a person
        """
        data = dict(username='username_example',
                    firstname='firstname_example',
                    lastname='lastname_example',
                    dateOfBirth='2013-10-20')
        response = self.client.open(
            '/openapi101/persons',
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_persons_username_delete(self):
        """Test case for persons_username_delete

        Deletes a person
        """
        response = self.client.open(
            '/openapi101/persons/{username}',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_persons_username_get(self):
        """Test case for persons_username_get

        Gets a person
        """
        headers = [('User_Agent', 'User_Agent_example')]
        response = self.client.open(
            '/openapi101/persons/{username}'.format(username='username_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
