#!/usr/bin/env python3
import os
import logging
from pymongo import MongoClient

""" Python script that provides some stats
about Nginx logs stored in MongoDB"""

# Basic logging setup
logging.basicConfig(level=logging.INFO)


def log_stats():
    """ Displays the total number of logs,
    counts of different HTTPmethods, and the number of logs with method GET
    and path /status."""
    try:
        # MongoDB connection
        mongo_url = os.getenv('MONGO_URL', 'mongodb://localhost:27017/')
        client = MongoClient(mongo_url)
        db = client['logs']
        nginx_collection = db['nginx']

        # Total number of logs
        total_logs = nginx_collection.count_documents({})
        logging.info(f"{total_logs} logs")

        # Methods statistics
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        logging.info("Methods:")

        for method in methods:
            count = nginx_collection.count_documents({"method": method})
            logging.info(f"  method {method}: {count}")

        # No of documents
        status_checks = nginx_collection.count_documents(
                {"method": "GET", "path": "/status"})
        logging.info(f"{status_checks} status check")

    except Exception as e:
        logging.error(f"An error occured: {e}")


if __name__ == "__main__":
    log_stats()
