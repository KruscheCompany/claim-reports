#!/usr/local/bin/python
import os, sys
import json
from pprint import pprint

with open('report.txt') as f:
    data = json.load(f)

file = open("report.html","w")


file.write("<html>")
file.write("<body style='background-color:#eeeeee;'>")

file.write('Hello World')
file.write('<h1>Vulnerabilities Report</h1>')
for x in data["vulnerabilities"]:
  if x['severity'] == "Hight":
    file.write("<p style='color:FF2D00;'>" +  x['severity'] + " " + "<a href='" + x['link'] +"'>" +  x['vulnerability']+ "</a>" + " in " + x['namespace'] + " [" + x['featurename'] + "]" + "</p>")
  elif x['severity'] == "Critical":
    file.write("<p style='color:9F1E03;'>" +  x['severity'] + " " + "<a href='" + x['link'] +"'>" +  x['vulnerability']+ "</a>" + " in " + x['namespace'] + " [" + x['featurename'] + "]" + "</p>")
  elif x['severity'] == "Medium":
    file.write("<p style='color:FFC500;'>" +  x['severity'] + " " + "<a href='" + x['link'] +"'>" +  x['vulnerability']+ "</a>" + " in " + x['namespace'] + " [" + x['featurename'] + "]" + "</p>")
  elif x['severity'] == "Low":
    file.write("<p style='color:0309DA;'>" +  x['severity'] + " " + "<a href='" + x['link'] +"'>" +  x['vulnerability']+ "</a>" + " in " + x['namespace'] + " [" + x['featurename'] + "]" + "</p>")
file.write("</body>")
file.write("</html>")
