#!/usr/bin/env python3
""" Function that lists all documents in a collection"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection

    param mongo_collection: pymongo collection object
    return: An empty list if no document
    in the collection
    """
    return list(mongo_collection.find())
