# Python 3.7.5
# python generate_gRNA_batch_oligonucleotide.py seq 2

import sys,re	

if len(sys.argv)<2:
	print("python "+sys.argv[0]+" sequence [barcodeId=1]")
	sys.exit(0)
 

def buildPoolPre_Suffix(barcodeId):
	" return fullPrefix and  fullSuffix"
	
	satMutBarcodes = [
	   (0,  "No Subpool barcode"),
	   (1,  "Subpool 1: CGGGTTCCGT/GCTTAGAATAGAA"),
	   (2,  "Subpool 2: GTTTATCGGGC/ACTTACTGTACC"),
	   (3,  "Subpool 3: ACCGATGTTGAC/CTCGTAATAGC"),
	   (4,  "Subpool 4: GAGGTCTTTCATGC/CACAACATA"),
	   (5,  "Subpool 5: TATCCCGTGAAGCT/TTCGGTTAA"),
	   (6,  "Subpool 6: TAGTAGTTCAGACGC/ATGTACCC"),
	   (7,  "Subpool 7: GGATGCATGATCTAG/CATCAAGC"),
	   (8,  "Subpool 8: ATGAGGACGAATCT/CACCTAAAG"),
	   (9,  "Subpool 9: GGTAGGCACG/TAAACTTAGAACC"),
	   (10, "Subpool 10: AGTCATGATTCAG/GTTGCAAGTCTAG"),
	]
	barcodeDict = dict(satMutBarcodes)
	barcodeLabel = barcodeDict[barcodeId]
	barcodePre, barcodePost = barcodeLabel.split()[-1].split("/")
	prePrimer = "GGAAAGG"
	pre = "ACGAAACACCG"
	post = "GTTTTAGAGCTAGAAATA"
	postPrimer = "GCAAGTTAAAATAAGGC"
	fullPrefix = barcodePre+prePrimer+pre
	fullSuffix = post+postPrimer+barcodePost
	return fullPrefix, fullSuffix

seqFname=sys.argv[1]
barcodeId=1
if len(sys.argv)>2:
	barcodeId=int(sys.argv[2])
fullPrefix, fullSuffix=buildPoolPre_Suffix(barcodeId)
input_file =open(seqFname)

opfname=re.sub(r'[\.\_]+[a-zA-Z0-9]+$','_gRNA_batch.tsv',seqFname);
ofh =open(opfname,"w")

ofh.write("gRNA_Sequence\tSubpool "+ str(barcodeId) +" Prefix + pLentiGuidePre Primer + pLentiGuidePre + sgRNA + pLentiGuide Post + pLentiGuidePost Primer + Subpool Suffix\tLEN_SEQ\tPAM\n")
reads=input_file. readline()
while reads:
	reads=re.sub(r'[\s\r\n]+','',reads)
	full_oligonucleotide=fullPrefix+reads[:20]+fullSuffix
	ofh.write(reads+"\t"+full_oligonucleotide+"\t"+ str(len(full_oligonucleotide))+"\t"+ reads[20:]+"\n")
	reads=input_file. readline()



ofh.close()
input_file.close()



print("done...")

