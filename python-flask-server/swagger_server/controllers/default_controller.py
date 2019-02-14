import connexion
import six

from swagger_server.models.errorunknown import ERRORUNKNOWN  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.persons import Persons  # noqa: E501
from swagger_server import util
from flask import request, abourt, Response, jsonify

def persons_get(User_Agent, pageSize=None, pageNumber=None):  # noqa: E501
    """Gets some persons

    Returns a list containing all persons. # noqa: E501

    :param User_Agent: 
    :type User_Agent: str
    :param pageSize: Number of persons returned
    :type pageSize: int
    :param pageNumber: Page number
    :type pageNumber: int

    :rtype: Persons
    """
    return 'do some magic!'

persons_list = []

def persons_post(person=None):  # noqa: E501
    """Creates a person

    Adds a new person to the persons list. # noqa: E501

    :param person: The person to create.
    :type person: dict | bytes

    :rtype: None
    """
    # dateOfBirth = util.deserialize_date(dateOfBirth)

    if connexion.request.is_json:
    person = Person.from_dict(connexion.request.get_json()) #noqa

    person_list.append(person)
    return Response(mimetype='application/json',status=204)


def persons_username_delete():  # noqa: E501
    """Deletes a person

    Delete a single person identified via its username # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def persons_username_get(User_Agent, username):  # noqa: E501
    """Gets a person

    Returns a single person for its username # noqa: E501

    :param User_Agent: 
    :type User_Agent: str
    :param username: The person&#39;s username
    :type username: str

    :rtype: ERRORUNKNOWN
    """
    return 'do some magic!'
