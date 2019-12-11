#!/usr/bin/env python3
# 
import json
import os

FILE_NAME = "StreamingHistory1.json"

# TODO: If two or more artists can share the same artist name:
#           change logic

# TODO: Missing logic for crediting artist when streamed from
#       a song that they are featured in

def get_most_popular_artist_from_streaming_history(
    base_dir="./",
    streaming_files_prefix="StreamingHistory"):

    streaming_history = read_json_data_from_files_in_common_folder_by_prefix(base_dir, streaming_files_prefix)    

    if len(streaming_history) < 1:
        raise DataNotFound("Unable to read data from streaming history files")

    artist_streams_count = {}

    for i in range(0, len(streaming_history)):
        artist_name = streaming_history[i]["artistName"]
        
        if artist_name in artist_streams_count:
            artist_streams_count[artist_name] = artist_streams_count[artist_name] + 1
        else:
            artist_streams_count[artist_name] = 1
            

    most_popular_artist = next(iter(artist_streams_count))
    most_popular_artist_count = artist_streams_count[most_popular_artist]

    for artist_name, artist_stream_count in artist_streams_count.items():
        if artist_stream_count > most_popular_artist_count:
            most_popular_artist = artist_name
            most_popular_artist_count = artist_streams_count[most_popular_artist]
    
    return most_popular_artist

def get_number_of_times_listened_to_artist_by_name(
    artist_name="",
    base_dir="./",
    streaming_files_prefix="StreamingHistory"):

    streaming_history = read_json_data_from_files_in_common_folder_by_prefix(base_dir, streaming_files_prefix)    

    if len(streaming_history) < 1:
        raise DataNotFound("Unable to read data from streaming history files")

    artist_stream_count = 0

    for i in range(0, len(streaming_history)):
        if streaming_history[i]["artistName"] == artist_name or \
            artist_name in streaming_history[i]["trackName"]:
            artist_stream_count = artist_stream_count + 1
    

    return artist_stream_count

def read_json_data_from_files_in_common_folder_by_prefix(base_dir, prefix):
    data = []

    for file in os.listdir(base_dir):
        if 'json' in file and prefix in file:
            json_path = os.path.join(base_dir, file)
            
            with open(json_path, 'r') as f:
                data = data + json.load(f)
    
    return data

class DataNotFound(Exception):
    def __init__(self, message):
        self.message = message


if __name__ == "__main__":
    print("The most popular artist is:", get_most_popular_artist_from_streaming_history())
    print("The number of times you played 21 Savage including features is:",
        get_number_of_times_listened_to_artist_by_name("21 Savage"))