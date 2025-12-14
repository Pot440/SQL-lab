import json, csv
import os

datalistlist = []

with open('data.csv', newline='') as csvfile:
    importer = csv.reader(csvfile, delimiter=',')
    next(importer)
    for row in importer:
        print(', '.join(row))
        print(row[1])
        testy = float(row[1])
        datalistlist.append(row)

companyindex = 1

outputfile = 'insertScript.sql'
with open(outputfile, 'w', newline='', ) as sql_file:
    sql_file.write("INSERT INTO `Company Table` (`id`, `ticker`, `company name`)\n")
    sql_file.write("VALUES (1, 'AAPL', 'Apple Inc.');\n")
    for i in datalistlist:
        idate = i[0]
        #high low table
        sql_file.write("INSERT INTO `High_Low Table` (`stock_id`, `Date`, `High`, `Low`)\n")
        sql_file.write(f"VALUES ('{companyindex}', '{idate}', {i[2]}, {i[3]});\n")
        #open close table
        sql_file.write("INSERT INTO `Open_Close Table` (`stock_id`, `Date`, `Open`, `Close`, `Adj Close`)\n")
        sql_file.write(f"VALUES ('{companyindex}', '{idate}', {i[1]}, {i[4]}, {i[5]});\n")
        #volume table
        sql_file.write("INSERT INTO `Volume Table` (`stock_id`, `Date`, `Volume`)\n")
        sql_file.write(f"VALUES ('{companyindex}', '{idate}', {i[6]});\n")

    




