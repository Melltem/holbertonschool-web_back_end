#!/usr/bin/env python3

""" comment. """


def insert_school(mongo_collection, **kwargs):
    """ comment. """
    return mongo_collection.insert_one(kwargs).inserted_id
