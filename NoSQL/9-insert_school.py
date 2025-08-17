#!/usr/bin/env python3

"""Inserts a new document in a collection"""


def insert_school(mongo_collection, **kwargs):
    """Returns the id of the new document"""
    document_id = mongo_collection.insert(kwargs)
    return document_id
