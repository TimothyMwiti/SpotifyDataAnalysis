#!/usr/bin/env python3

import json
import os

class Utilities:

    @staticmethod
    def read_json_data_from_files_in_common_folder_by_prefix(base_dir, prefix):
        data = []

        for file in os.listdir(base_dir):
            if 'json' in file and prefix in file:
                json_path = os.path.join(base_dir, file)
                
                with open(json_path, 'r') as f:
                    data = data + json.load(f)
        
        return data  

    
    @staticmethod
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


    # TODO: Query against API to establish that names in results are artist names
    @staticmethod
    def get_list_of_featured_artists_from_track_name(track_name=""):

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
        
        featured_artists = Utilities.get_artists_from_string_with_multiple_artists(featured_artists_str)

        return featured_artists