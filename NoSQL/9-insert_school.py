#!/usr/bin/env python3

"""
function that inserts a new document in a collection based on kwargs
"""

def insert_school(mongo_collection, **kwargs):
    """insert_school function"""

    new_doc = mongo_collection.insert_one(kwargs)
