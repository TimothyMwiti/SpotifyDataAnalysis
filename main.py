#!/usr/bin/env python3

import json
import os

FILE_NAME = "StreamingHistory1.json"

def get_most_popular_artist_from_streaming_history(
    base_dir="./",
    streaming_files_prefix="StreamingHistory"):

    streaming_history = []

    for file in os.listdir(base_dir):
        if 'json' in file and streaming_files_prefix in file:
            json_path = os.path.join(base_dir, file)
            
            with open(json_path, 'r') as f:
                streaming_history = streaming_history + json.load(f)

    if len(streaming_history) < 1:
        raise DataNotFound("Unable to read data from streaming history files")

    artist_streams_count = {}

    for i in range(0, len(streaming_history)):
        artistName = streaming_history[i]["artistName"]
        
        if artistName in artist_streams_count:
            artist_streams_count[artistName] = artist_streams_count[artistName] + 1
        else:
            artist_streams_count[artistName] = 1
            

    most_popular_artist = next(iter(artist_streams_count)) 

    for key in artist_streams_count:
        if artist_streams_count[key] > artist_streams_count[most_popular_artist]:
            most_popular_artist = key
    
    return most_popular_artist

class DataNotFound(Exception):
    def __init__(self, message):
        self.message = message



if __name__ == "__main__":
    print(get_most_popular_artist_from_streaming_history())