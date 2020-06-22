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
ofh =open(opfname,"w")
reads=input_file. readline()
while reads:
	reads=re.sub(r'[\r\n]+','',reads)
	readset=re.split(r'\t+',reads)
	# print(readset[2])
	ofh.write(readset[1]+"\t")
	matchObj = re.search( r"("+preAnchor+")([ATCG]+"+")("+ postAnchor+')', readset[2], re.I)
	if matchObj:
		# print(matchObj.group(2))
		ofh.write(matchObj.group(2)+"\t")
	else:
		ofh.write("NA\t")
	ofh.write(readset[0]+"\t"+readset[2]+"\n")
	reads=input_file. readline()
ofh.close()	
input_file.close()

