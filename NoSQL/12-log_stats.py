#!/usr/bin/env python3
"""Provides stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

if __name__ == "__main__":
    # Connect to the MongoDB server (localhost by default)
    client = MongoClient()

    # Select the database 'logs' and the collection 'nginx'
    collection = client.logs.nginx

    # 1. Count total number of logs/documents
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # 2. Count logs by method
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = collection.count_documents({ "method": method })
        print(f"\tmethod {method}: {method_count}")

    # 3. Count GET requests to /status
    get_status_count = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"method=GET, path=/status: {get_status_count}")
