#!/usr/bin/env python3
'''Insert a new document in Python
'''


def insert_school(mongo_collection, **kwargs):
    '''Insert a new document in a collection based on kwargs
    '''
    new_school = mongo_collection.insert_one(kwargs)
    return new_school.inserted_id
