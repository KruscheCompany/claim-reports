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
file.write('<tr>')
for x in data["vulnerabilities"]:
  if x['severity'] == "High":
    file.write("<td>" +  x['severity'] + "</td><td>" + "<a href='" + x['link'] +"'>" +  x['vulnerability']+ "</a></td><td>" + x['namespace'] + "</td><td>" + x['featurename'] + "</td>")
#  elif x['severity'] == "Critical":
#    file.write("<p style='color:9F1E03;'>" +  x['severity'] + " " + "<a href='" + x['link'] +"'>" +  x['vulnerability']+ "</a>" + " in " + x['namespace'] + " [" + x['featurename'] + "]" + "</p>")
#  elif x['severity'] == "Medium":
#    file.write("<p style='color:FFC500;'>" +  x['severity'] + " " + "<a href='" + x['link'] +"'>" +  x['vulnerability']+ "</a>" + " in " + x['namespace'] + " [" + x['featurename'] + "]" + "</p>")
#  elif x['severity'] == "Low":
#    file.write("<p style='color:0309DA;'>" +  x['severity'] + " " + "<a href='" + x['link'] +"'>" +  x['vulnerability']+ "</a>" + " in " + x['namespace'] + " [" + x['featurename'] + "]" + "</p>")
  else:
    file.write("<p>" +  x['severity'] + " " + "<a href='" + x['link'] +"'>" +  x['vulnerability']+ "</a>" + " in " + x['namespace'] + " [" + x['featurename'] + "]" + "</p>")
file.write('</tr>')
file.write('</table>')
file.write("</body>")
file.write("</html>")
