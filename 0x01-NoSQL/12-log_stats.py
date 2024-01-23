#!/usr/bin/env python3
""" script that provides some stats
    about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    nGets = nginx_collection.count_documents({"method": "GET"})
    nPosts = nginx_collection.count_documents({"method": "POST"})
    nPuts = nginx_collection.count_documents({"method": "PUT"})
    nPatchs = nginx_collection.count_documents({"method": "PATCH"})
    nDelets = nginx_collection.count_documents({"method": "DELETE"})
    print(f'{nginx_collection.count_documents({})} logs')
    # status check GET
    status_pipeline = [
       {
        '$match': {"method": "GET", "path": "/status"}
       },
       {
        '$count': 'total_status'
       }
    ]
    stats = nginx_collection.aggregate(status_pipeline)
    for stats in stats:
        print('{} status check'.format(stats.get('total_status')))
