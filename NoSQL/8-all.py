#!/usr/bin/env python3

"""
function that lists all documents in a collection
"""

def list_all(mongo_collection):
    docs = mongo_collection.find()

    if docs.count() == 0:
        return []
    
    return docs