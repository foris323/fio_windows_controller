

import json
from collections import OrderedDict

all_data = OrderedDict({"randread.log": "read",
                        "randwrite.log": "write",
                        "read.log": "read",
                        "randwrite.log": "randwrite"})

csv = ""
keys = all_data.keys()
csv += ",".join(keys)
csv += "\n"

iops_list = []
for k, v in all_data.items():
    with open(k) as f:
        data = json.load(f)
        iops = int(data["jobs"][0][v]["iops"])
        iops_list.append(iops)

csv += ",".join(iops_list)
with open("data.csv", "w") as f:
    f.write(csv)
