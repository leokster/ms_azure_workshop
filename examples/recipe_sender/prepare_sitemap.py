import smtplib
from email.message import EmailMessage
import xml.etree.ElementTree as ET
import numpy as np
import regex as re
parser = ET.XMLParser(encoding="utf-8")
tree = ET.fromstring(xmlstring, parser=parser)

link_xml = ET.parse("recipe_sender/sitemap.xml", parser=parser)

recipes = []
with open('recipes.txt', 'w') as recep:
    with open("recipe_sender/sitemap.xml", "r") as f:
        for line in f.readlines():
            url = re.search("<loc>(.*)</loc>", line, re.DOTALL).group(1)
            url_split = url.split("-")
            if len(url_split)>=3 and url_split[-1].isnumeric() and url_split[-2]=="rezept":
                recep.write("{}\n".format(url))


