#list declair
Top10Tools=["R and Python", "Microsoft Excel", "Tableau", "RapidMiner", "KNIME" ,"Power BI", "Apache Spark", "QlikView",
"Talend","Splunk"]
print(Top10Tools)
fileObj=open("datascience.txt", "w")
for top10 in Top10Tools:
    fileObj.write(top10 +" ")

fileObj.close()