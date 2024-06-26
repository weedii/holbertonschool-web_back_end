#!/usr/bin/env python3

"""
function that lists all documents in a collection
"""

def list_all(mongo_collection):
    """list_all function"""

    docs = mongo_collection.find()

    if docs:
        return list(docs)
    else:
        return []