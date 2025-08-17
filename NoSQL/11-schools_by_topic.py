#!/usr/bin/env python3

"""Lists all documents with a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Get all documents with a given topic"""
    documents = mongo_collection.find({"topics": topic})
    list_of_documents = [i for i in documents]
    return list_of_documents
