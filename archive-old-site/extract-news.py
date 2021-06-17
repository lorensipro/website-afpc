import sys, json
import html2text


filein = "original-news-afpc.json"
dirout = "original-news-md/"

with open(filein, 'rt') as jf:
    data = json.load(jf)
    print(f"{len(data)} entries to save...")
    for entry in data:
        assert " " not in entry["alias"]
    for entry in data:
        dateday = entry["date"].split()[0]
        if entry["alias"][:2] == "20": # Ca doit etre une date
            name = dirout + entry["alias"] + ".md"
        else:
            name = dirout + dateday + "-" + entry["alias"] + ".md"
        with open(name, "wt") as of:
            of.write("---\n")
            print(dateday)
            text = html2text.html2text(entry["introtext"])
            text = text.replace("\\r","")
            text = text.replace("\\n","")
            text = text.replace("\\t","")
            of.write(f"layout: page\n")
            d = entry["title"]
            of.write(f"title_content: {d}\n")
            if len(d) > 40:
                d = d[:40]+"..."
            of.write(f"title: {d}\n")
            d = entry["date"]
            of.write(f"date_content: {d}\n")
            of.write(f"tags:\n")
            of.write(f"  - archive\n")
            of.write("---\n")
            of.write(text)