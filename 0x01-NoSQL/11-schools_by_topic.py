#!/usr/bin/env python3
"""returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
     """
       that returns the list of school having a specific topic
     """
     res = []
     schools_by_topic = mongo_collection.find({"topics": topic})
     for doc in schools_by_topic:
            res.append(doc)
     return res

