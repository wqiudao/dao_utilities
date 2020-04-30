# Python 3.7.5
#从NCBI下载的ncbi genbank 提取基因注释信息，生成结果： transcriptId          
import re,sys,gzip

if len(sys.argv)!=2:
	print("python "+sys.argv[0]+" ncbi.gbff[.gz]")
	sys.exit(0)

gbff=sys.argv[1]

opfname=re.sub(r'[\.\_]+[a-zA-Z0-9]+$','_AnnotationGene.tsv',gbff);opt_file =open(opfname,"w")

if re.search('\.gz$',gbff) is None:
	print("gbff")
	opt_file.write("transcriptId\tgeneId\tgeneSymbol\torganism\tgeneSynonym\tdefinition\tversion\n")
	input_file =open(gbff)
	reads=input_file. readline()
	while reads:
		if re.search('^//',reads):
			# print()
			rs=str(locus)+"\t"+str(geneid)+"\t"+str(gene)+"\t"+str(organism)+"\t"+str(gene_synonym)+"\t"+str(definition)+"\t"+str(version)
			opt_file.write(rs+"\n")

	
		rs_m=re.search('^LOCUS\s+(\S+)',reads)
		if rs_m:
			locus,definition,version,organism,gene,gene_synonym,geneid=0,0,0,0,0,0,0
			locus=rs_m.group(1)
			# print(rs_m.group(1))
			
		
		rs_m=re.search('^DEFINITION\s+(.*)',reads)
		if rs_m:definition=re.sub(r'\s+','_',rs_m.group(1))
			
		rs_m=re.search('^VERSION\s+(\S+)',reads)
		if rs_m:version=rs_m.group(1)
			
		rs_m=re.search('^SOURCE\s+(.*)',reads)
		if rs_m:organism=re.sub(r'\s+','_',rs_m.group(1))
			
		rs_m=re.search('^\s+gene\s+\d+',reads)
		if rs_m:
			while reads:
				rs_m=re.search('/gene="(\S+)"',reads)
				if rs_m:gene="\'"+rs_m.group(1)
				
				rs_m=re.search('/gene_synonym="(.*)',reads)          
				if rs_m:
					gene_synonym=rs_m.group(1)
					reads=input_file. readline()
					if re.search('/note="',reads) is None:
						gene_synonym+=reads
					gene_synonym=re.sub(r'[\r\n\s\"\']+','',gene_synonym)	
					
				rs_m=re.search('"GeneID:(\d+)"',reads)
				if rs_m:geneid=rs_m.group(1)
				if int(geneid) > 0:
					break
				reads=input_file. readline()
		reads=input_file. readline()
	input_file.close()	

else:
	print("gz")
	opt_file.write("transcriptId\tgeneId\tgeneSymbol\torganism\tgeneSynonym\tdefinition\tversion\n")
	input_file = gzip.open(gbff)
	for reads in input_file:
		# print(reads)
		reads=str(reads)
		reads=re.sub(r'^b[\'\"]','',reads)	
		reads=re.sub(r'\\n\'$','',reads)	
		# print(reads)
		if re.search('^//',reads):
			# print()
			gene_synonym=re.sub(r'[\r\n\s\"\']+','',str(gene_synonym))
			rs=str(locus)+"\t"+str(geneid)+"\t"+str(gene)+"\t"+str(organism)+"\t"+str(gene_synonym)+"\t"+str(definition)+"\t"+str(version)
			opt_file.write(rs+"\n")

	
		rs_m=re.search('^LOCUS\s+(\S+)',reads)
		if rs_m:
			locus,definition,version,organism,gene,gene_synonym,geneid=0,0,0,0,0,0,0
			locus=rs_m.group(1)
			gene_synonym_check=0
			gene_check=0
			# print(rs_m.group(1))
			
		
		rs_m=re.search('^DEFINITION\s+(.*)',reads)
		if rs_m:definition=re.sub(r'\s+','_',rs_m.group(1))
			
		rs_m=re.search('^VERSION\s+(\S+)',reads)
		if rs_m:version=rs_m.group(1)
			
		rs_m=re.search('^SOURCE\s+(.*)',reads)
		if rs_m:organism=re.sub(r'\s+','_',rs_m.group(1))
			
		rs_m=re.search('^\s+gene\s+\d+',reads)
		
		if rs_m:
			gene_check=1
		if gene_check > 0:
			rs_m=re.search('/gene="(\S+)"',reads)
			if rs_m:gene="\'"+rs_m.group(1)
			
			rs_m=re.search('/gene_synonym="(.*)',reads)     



			
			if rs_m and gene_synonym_check==0:
				gene_synonym_check=1
				gene_synonym=rs_m.group(1)
				continue
			if gene_synonym_check > 0 and re.search('/note="',reads):
				gene_synonym_check=2				

			if gene_synonym_check==1 and re.search('/note="',reads) is None:
				gene_synonym+=reads
				gene_synonym_check=2
				# print(reads+" wqd")
			rs_m=re.search('"GeneID:(\d+)"',reads)
			if rs_m:geneid=rs_m.group(1)
	
	
		
 	



	input_file.close()
opt_file.close()









