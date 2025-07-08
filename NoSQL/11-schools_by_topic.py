#!/usr/bin/env python3

""" comment. """


def schools_by_topic(mongo_collection, topic):
    return list(mongo_collection.find(
      { "topic": topic }
))
