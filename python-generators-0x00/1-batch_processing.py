#!/usr/bin/env python3

""" Batch processing Large Data

    This module creates a generator to fetch and process data in batches from the users database
"""

def stream_users_in_batches(batch_size):
    """ A function that fetches rows in batches

        Arguments:
            batch_size: The number of records to be fetched per batch
        Returns: list of records fetched
    """
    