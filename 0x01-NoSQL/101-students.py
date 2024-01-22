#!/usr/bin/env python3
""" function that returns all 
    students sorted by average score
"""


def top_students(mongo_collection):
     """
      returns all students sorted by average score:
     """
     pipeline = [{
       $group: {
          _id: None,
          'averageScore': {'$avg': '$score'}
         }
    }]

    mongo_collection.aggregate(pipeline)
