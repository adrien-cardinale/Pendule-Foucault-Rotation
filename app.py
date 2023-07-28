import os
import shutil
import gzip
from datetime import datetime, timedelta

path = "/home/pendule-foucault/data"

minOldTime = 1

path_dest = "/home/pendule-foucault/data2"

limitDate = datetime.now() - timedelta(days=minOldTime)

for file in os.listdir(path):
    path_file = os.path.join(path, file)
    if os.path.isfile(path_file) and (file.startswith("pFposition") or file.startswith("pFregulateur")) and not file.endswith(".gz"):
        if file + ".gz" in os.listdir(path_dest):
            continue
        path_file_comp = path_file + ".gz"
        if os.path.getmtime(path_file) < limitDate.timestamp():
            print("Compressing file: " + path_file)
            with open(path_file, 'rb') as f_in:
                with gzip.open(path_file_comp, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            shutil.move(path_file_comp, path_dest)
            os.remove(path_file)
