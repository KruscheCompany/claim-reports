#!/bin/python
import os, sys
import json
from pprint import pprint

with open('test.txt') as f:
    data = json.load(f)

#file = open("test.html","w")

#file.write("<html>")
#file.write("<body style='background-color:#eeeeee;'>")

#file.write('<h1>Vulnerabilities Report</h1>')
#file.write('<table border="1">')
#file.write('<td>Severity</td><td>Vulnerability</td><td>Package</td><td>Curent version</td></td><td>Fixed in version</td><td>OS Version</td>')
for x in data:
  print(x['priority'] + " " + x['cve'])
#  if x['severity'] == "High":
#  elif x['severity'] == "Critical":
#  elif x['severity'] == "Medium":
#  elif x['severity'] == "Low":
#  else:
#  file.write('<tr>')
#  file.write("<td>" + x['severity'] + "</td><td>" + "<a href='" + x['link'] +"'>" +  x['vulnerability']+ "</a></td><td>" + x['featurename'] + "</td><td>" + x['featureversion'] + "</td><td>" + x['fixedby'] + "</td><td>" + x['namespace'] + "</td>")
#  file.write('</tr>')
#file.write('</table>')
#file.write("</body>")
#file.write("</html>")