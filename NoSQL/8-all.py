#!/usr/bin/env python3

"""Lists all documents in a collection"""


def list_all(mongo_collection):
    """Returns the documents in a collection if null returns an empty list """
    documents = mongo_collection.find()
    if documents.count() == 0:
        return list()
    return documents
