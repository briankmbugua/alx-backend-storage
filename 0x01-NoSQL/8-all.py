#!/usr/bin/env python3
'''List all documents in a collection
'''


def list_all(mongo_collection):
    '''Lists all documents in a collection.
    '''
    documents = []
    for document in mongo_collection.find():
        documents.append(document)
    return documents
