import tldextract
from sys import argv
script, in_file_name = argv

domains = open(in_file_name + "_domains", "w+")
with open(in_file_name, "r") as urls:
    for line in urls:
        ext = tldextract.extract(line)
        domains.write(ext.domain + "." + ext.suffix + "\n")
