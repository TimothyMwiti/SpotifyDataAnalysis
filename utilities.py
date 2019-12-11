#!/usr/bin/env python3

import json
import os

def read_json_data_from_files_in_common_folder_by_prefix(base_dir, prefix):
    data = []

    for file in os.listdir(base_dir):
        if 'json' in file and prefix in file:
            json_path = os.path.join(base_dir, file)
            
            with open(json_path, 'r') as f:
                data = data + json.load(f)
    
    return data