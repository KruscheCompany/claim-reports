#!/bin/python
import os, sys
import json
from pprint import pprint

with open('report.txt') as f:
    data = json.load(f)

file = open("report.html","w")


file.write("<html>")
file.write("<body style='background-color:#eeeeee;'>")

file.write('<h1>Vulnerabilities Report</h1>')
file.write('<table>')
for x in data["vulnerabilities"]:
#  if x['severity'] == "High":
#  elif x['severity'] == "Critical":
#  elif x['severity'] == "Medium":
#  elif x['severity'] == "Low":
#  else:
  file.write('<tr>')
  file.write("<td>" +  x['severity'] + "</td><td>" + "<a href='" + x['link'] +"'>" +  x['vulnerability']+ "</a></td><td>" + x['namespace'] + "</td><td>" + x['featurename'] + "</td>")
  file.write('</tr>')
file.write('</table>')
file.write("</body>")
file.write("</html>")
