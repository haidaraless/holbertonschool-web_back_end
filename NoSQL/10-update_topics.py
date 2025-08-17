#!/usr/bin/env python3

"""Changes all topics of a school document"""


def update_topics(mongo_collection, name, topics):
    """Updates topics with given name of many documents"""
    query = {"name": name}
    values = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, values)
