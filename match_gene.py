# Python 3.7.5
#根据指定列数匹配基因，ENSG00000242268.2，因为存在版本号，所以，统一去掉。 
# gencode.v23.annotation.gene.probemap  注释文件，可以替换
# id	gene	chrom	chromStart	chromEnd	strand
# ENSG00000223972.5	DDX11L1	chr1	11869	14409	+
# python match_gene.py Pancreas_TcgaTargetGTEX.tsv 

import re
import sys

Id_geneLocation=0
dic_geneAnnotation={}
if len(sys.argv)>2:
	Id_geneLocation=sys.argv[2]

filename="gencode.v23.annotation.gene.probemap";input_file =open(filename)
reads=input_file. readline()
while reads:
	reads=re.sub(r'[\r\n]+','',reads)
	readset=re.split("\s+",reads) 	
	geneId=re.sub(r'\.\S+','',readset[0])
	dic_geneAnnotation[geneId]=reads
	reads=input_file. readline()
input_file.close()

print("Loading map file done...")

filename=sys.argv[1];input_file =open(filename)
opfname=re.sub(r'[\.\_]+[a-zA-Z0-9]+$','_Annotation.tsv',sys.argv[1]);opt_file =open(opfname,"w")

reads=input_file. readline()
reads=re.sub(r'[\r\n]+','',reads)
readset=re.split("\s+",reads) 	
geneId=re.sub(r'\.\S+','',readset[Id_geneLocation])
opt_file.write(reads)
if geneId in dic_geneAnnotation:
	opt_file.write("\t"+dic_geneAnnotation[geneId])
else:
	opt_file.write("\tid\tgene\tchrom\tchromStart\tchromEnd\tstrand")
opt_file.write("\n")

reads=input_file. readline()
while reads:
	reads=re.sub(r'[\r\n]+','',reads)
	readset=re.split("\s+",reads) 	
	geneId=re.sub(r'\.\S+','',readset[Id_geneLocation])
	opt_file.write(reads)
	if geneId in dic_geneAnnotation:
		opt_file.write("\t"+dic_geneAnnotation[geneId])
	opt_file.write("\n")
	reads=input_file. readline()
input_file.close()
opt_file.close()

print("Mapping done...")











