import os
import re
import shutil

downloads = "/users/km/downloads"

for root, dirs, files in os.walk(downloads, topdown=False):
    for name in files:
        if re.search(("^C\d{5}_.*zip$"), name):
            print(os.path.join(root,name))
            shutil.unpack_archive("name", [downloads], [zip])