import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.bag import Bag  # noqa: E501
from swagger_server import util


def delete_bag(bagId):  # noqa: E501
    """Delete Bag

     # noqa: E501

    :param bagId: The bag that needs to be deleted
    :type bagId: str

    :rtype: None
    """
    return 'do some magic!'


def get_bag_by_id(bagId):  # noqa: E501
    """Get bag location from Id

     # noqa: E501

    :param bagId: The id of the bag that needs to be fetched.
    :type bagId: str

    :rtype: ApiResponse
    """
    return 'do some magic!'


def load_bag(body):  # noqa: E501
    """Load a bag into the airplane

     # noqa: E501

    :param body: Request a bag to be loaded. Give a unique name for your luggage 
    :type body: dict | bytes

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        body = Bag.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
