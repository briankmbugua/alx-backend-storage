#!/usr/bin/env python3
'''Task 14's module.
'''


def top_students(mongo_collection):
    '''Returns all students in a collection sorted by average score.
    '''
    students = mongo_collection.aggregate([
        {
            '$project': {
                'name': 1,
                'averageScore': {'$avg': '$topics.score'}
            }
        },
        {'$sort': {'averageScore': -1}}
    ])
    return students
