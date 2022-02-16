import csv

hosts = [["workstation.local", "192.168.1.12"], ["webserver.local","10.2.3.12"]]

with open("hosts.csv","w") as hosts_csv:
  writer = csv.writer(hosts_csv)
  writer.writerows(hosts)
