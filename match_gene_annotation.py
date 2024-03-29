# Python 3.7.5
# ENSG00000223972.5	DDX11L1	chr1	11869	14409	+
# python match_gene.py Pancreas_TcgaTargetGTEX.tsv   
# python match_gene.py TcgaTargetGtex_gene_expected_count_raw_new.tsv   
# python match_gene.py geo2r.tsv   
# python match_gene_v2.py  01-Pancreas_Tcga_Sur_cox_Annotation.tsv 02-Pancreas_TcgaTargetGTEX_Annotation.tsv
import re
import sys
opt_nominate=2
if len(sys.argv)<3:
	print("python "+sys.argv[0]+"  <ref.annotation.tsv> input_file [opt_nominate=2]")
	sys.exit(0)
opt_header=sys.argv[1]
if len(sys.argv)>3:
	opt_nominate=int(sys.argv[3])
	opt_header=sys.argv[2]


Id_geneLocation=0
dic_geneAnnotation={}
filename=sys.argv[1];
input_file =open(filename)
reads=input_file.readline()
while reads:
	reads=re.sub(r'[\r\n]+','',reads)
	readset=re.split("\s+",reads) 	
	readset[0]="\'"+readset[0]
	readset[1]="\'"+readset[1]
	geneId=re.sub(r'\.\S+','',readset[0])
	reads="\t".join(readset)
	geneId=re.sub(r'[\'\"]+','',geneId).upper()
	dic_geneAnnotation[geneId]=reads
	reads=input_file. readline()
input_file.close()

print("Loading map file done...")

filename=sys.argv[2];input_file =open(filename)
opfname=re.sub(r'[\.\_]+[a-zA-Z0-9]+$','_Annotation.tsv',sys.argv[opt_nominate]);opt_file =open(opfname,"w")
opfname=re.sub(r'[\.\_]+[a-zA-Z0-9]+$','_Sel_Annotation.tsv',sys.argv[opt_nominate]);opts_file =open(opfname,"w")

reads=input_file. readline()
reads=re.sub(r'[\r\n]+','',reads)
readset=re.split("\s+",reads) 	
geneId=re.sub(r'\.\S+','',readset[Id_geneLocation]).upper()
opt_file.write(reads)
if geneId in dic_geneAnnotation:
	opts_file.write(reads)
	opts_file.write("\t"+dic_geneAnnotation[geneId])
	opt_file.write("\t"+dic_geneAnnotation[geneId])
else:
	opts_file.write(reads)
	# opt_file.write("\tid\tgene\tchrom\tchromStart\tchromEnd\tstrand")
	# opts_file.write("\tid\tgene\tchrom\tchromStart\tchromEnd\tstrand")	
	opt_file.write("\t"+opt_header)
	opts_file.write("\t"+opt_header)
opt_file.write("\n")
opts_file.write("\n")

reads=input_file. readline()
while reads:
	reads=re.sub(r'[\r\n]+','',reads)
	readset=re.split("\s+",reads) 	
	readgenes=re.split("\|",readset[Id_geneLocation]) 	
	opt_file.write(reads)
	# print(readset[Id_geneLocation])
	for geneIds in readgenes:
		
		geneId=re.sub(r'\.\S+','',geneIds).upper()
		geneId=re.sub(r'[\'\"]+','',geneId).upper()	
		# print(geneIds)
		# print(geneId)
		if geneId in dic_geneAnnotation:
			opt_file.write("\t"+dic_geneAnnotation[geneId])
			opts_file.write(reads)
			opts_file.write("\t"+dic_geneAnnotation[geneId])
			opts_file.write("\n")		
			# isHit=True
			break
	opt_file.write("\n")
	reads=input_file. readline()
input_file.close()
opt_file.close()
opts_file.close()

print("Mapping done...")

