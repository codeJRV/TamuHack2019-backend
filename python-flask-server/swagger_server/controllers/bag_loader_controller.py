import connexion
import six


from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.bag import Bag  # noqa: E501
from swagger_server import util
from swagger_server.BagList import BagList

baglist = BagList()

def delete_bag(bagId):  # noqa: E501
    """Delete Bag

     # noqa: E501

    :param bagId: The bag that needs to be deleted
    :type bagId: str

    :rtype: None
    """

    baglist.remove(bagId)
    return 'Deleted'


def get_bag_by_id(bagId):  # noqa: E501
    """Get bag location from Id

     # noqa: E501

    :param bagId: The id of the bag that needs to be fetched.
    :type bagId: str

    :rtype: ApiResponse
    """



    test = baglist.get(bagId)

    response = ApiResponse()
    response = response.from_dict(test)
    return response


def load_bag(body):  # noqa: E501
    """Load a bag into the airplane

     # noqa: E501

    :param body: Request a bag to be loaded. Give a unique name for your luggage 
    :type body: dict | bytes

    :rtype: ApiResponse
    """

    print (body)
    print ("Nobody")


    if connexion.request.is_json:
        body = Bag.from_dict(connexion.request.get_json())  # noqa: E501

    print (body.bag_id, body.bag_weight)

    baglist.add(body.bag_id, body.bag_weight)
    
    test = baglist.get(body.bag_id)

    response = ApiResponse()
    response = response.from_dict(test)
    return response
