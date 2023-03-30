import re

def parse_m3u8_file(file_path):
    track_dict = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            match = re.match(r'#EXTINF:.*,(.*)', line)
            if match:
                track_name = match.group(1)
            else:
                match = re.match(r'(http.*)', line)
                if match:
                    track_url = match.group(1)
                    track_dict[track_name] = track_url
    return track_dict

print(parse_m3u8_file('playlist.m3u8'))