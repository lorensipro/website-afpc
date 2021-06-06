import sys, json


filein = "original-news-afpc.json"
dirout = "original-news/"

with open(filein, 'rt') as jf:
    data = json.load(jf)
    print(f"{len(data)} entries to save...")
    for entry in data:
        assert " " not in entry["alias"]
    for entry in data:
        name = dirout + entry["alias"] + ".html"
        with open(name, "wt") as of:
            of.write("---\n")
            d = entry["date"]
            of.write(f"date_content: {d}\n")
            d = entry["title"]
            of.write(f"title_content: {d}\n")
            of.write("---\n")
            of.write(entry["introtext"])