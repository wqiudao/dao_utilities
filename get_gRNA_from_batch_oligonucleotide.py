# get_gRNA_from_batch_oligonucleotide

import sys,re	
if len(sys.argv)<2:
	print("python "+sys.argv[0]+" batch_oligonucleotide.flat")
	sys.exit(0)

preAnchor = "GGAAAGGACGAAACACCG"
postAnchor = "GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGC"

seqFname=sys.argv[1]
input_file =open(seqFname)
opfname=re.sub(r'[\.\_]+[a-zA-Z0-9]+$','_gRNA_features.tsv',seqFname);
sgRNA_library_file_MAGeCK=re.sub(r'[\.\_]+[a-zA-Z0-9]+$','_sgRNA_library_MAGeCK.tsv',seqFname);
ofh =open(opfname,"w")
ofhm =open(sgRNA_library_file_MAGeCK,"w")
reads=input_file. readline()
sgrna_count=0;
while reads:
	sgrna_count+=1;
	reads=re.sub(r'[\r\n]+','',reads)
	readset=re.split(r'\t+',reads)
	# print(readset[2])
	ofh.write(readset[1]+"\t")
	matchObj = re.search( r"("+preAnchor+")([ATCG]+"+")("+ postAnchor+')', readset[2], re.I)
	if matchObj:
		# print(matchObj.group(2))
		ofh.write(matchObj.group(2)+"\t")
		ofhm.write("s_"+readset[0]+'_'+str(sgrna_count)+"\t")
		ofhm.write(matchObj.group(2)+"\t")
		ofhm.write(readset[1]+"\n")
	else:
		ofh.write("NA\t")
	ofh.write(readset[0]+"\t"+readset[2]+"\n")
	reads=input_file. readline()
ofhm.close()	
ofh.close()	
input_file.close()


