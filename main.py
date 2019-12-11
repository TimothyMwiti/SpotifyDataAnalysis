#!/usr/bin/env python3
 
import json
import os

from utilities import *
# TODO: If two or more artists can share the same artist name:
#           change logic

STREAMING_HISTORY = read_json_data_from_files_in_common_folder_by_prefix("./", "StreamingHistory")
MILLISECONDS_IN_A_MINUTE = 60000

def get_most_popular_artist_from_streaming_history(
    base_dir="./",
    streaming_files_prefix="StreamingHistory"):

    streaming_history = STREAMING_HISTORY

    if len(streaming_history) < 1:
        raise DataNotFound("Unable to read data from streaming history files")

    artist_streams_count = {}

    for i in range(0, len(streaming_history)):
        artist_name = streaming_history[i]["artistName"]       
        if artist_name in artist_streams_count:
            artist_streams_count[artist_name] = artist_streams_count[artist_name] + 1
        else:
            artist_streams_count[artist_name] = 1

        featured_artists = get_list_of_featured_artists_from_track_name(streaming_history[i]["trackName"])

        for artist_name in featured_artists: 
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

    streaming_history = STREAMING_HISTORY

    if len(streaming_history) < 1:
        raise DataNotFound("Unable to read data from streaming history files")

    artist_stream_count = 0

    for i in range(0, len(streaming_history)):
        if streaming_history[i]["artistName"] == artist_name or \
            artist_name in streaming_history[i]["trackName"]:
            artist_stream_count = artist_stream_count + 1
    

    return artist_stream_count


def get_number_of_minutes_listened_to_artist(
    artist_name="",
    base_dir="./",
    streaming_files_prefix="StreamingHistory"):
    
    streaming_history = STREAMING_HISTORY

    if len(streaming_history) < 1:
        raise DataNotFound("Unable to read data from streaming history files")

    milliseconds_listened_to_artist = 0

    for streaming_record in streaming_history:
        if streaming_record["artistName"] == artist_name or \
            artist_name in streaming_record["trackName"]:
            print(str(streaming_record) + "\n\n")
            milliseconds_listened_to_artist = milliseconds_listened_to_artist + streaming_record["msPlayed"]
    
    return milliseconds_listened_to_artist // MILLISECONDS_IN_A_MINUTE

# TODO: Query against API to establish that names in results are artist names
def get_list_of_featured_artists_from_track_name(
    track_name=""):

    if len(track_name) < 1 or ("(" not in track_name and "[" not in track_name):
        return []
    
    featured_artists = []

    if "feat" in track_name:
        featured_artists_str = track_name.split("(")[1][:-1][6:]
    elif "with" in track_name:
        featured_artists_str = track_name.split("with")[-1].strip()
        if ")" == featured_artists_str[-1] or "]" == featured_artists_str[-1]:
            featured_artists_str = featured_artists_str[:-1].strip()
    else:
        featured_artists_str = track_name.split("(")[-1][:-1]
    
    featured_artists = get_artists_from_string_with_multiple_artists(featured_artists_str)

    return featured_artists

def get_artists_from_string_with_multiple_artists(featured_artists_str):
    featured_artists = []
    
    if "&" in featured_artists_str:
        temp_artists_split = featured_artists_str.split("&")
        featured_artists.append(temp_artists_split[-1].strip())

        featured_artists_str = temp_artists_split[0]

        if "," not in featured_artists_str:
            featured_artists.append(featured_artists_str.strip())
        else:
            artists = featured_artists_str.split(",")

            for artist in artists:
                featured_artists.append(artist.strip())
    else:
        featured_artists = [featured_artists_str]
    
    return featured_artists    
    
class DataNotFound(Exception):
    def __init__(self, message):
        self.message = message


if __name__ == "__main__":
    print("The most popular artist is:", get_most_popular_artist_from_streaming_history())
    print("The number of times you played Drake is:",
        get_number_of_times_listened_to_artist_by_name("Drake"))
    print("You listened to Drake for {} minutes.".format(get_number_of_minutes_listened_to_artist("Drake")))