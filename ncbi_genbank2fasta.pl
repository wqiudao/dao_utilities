#Extraction information from genbank flatfiles 
#从genbank文件中抽提信息，组成，fasta格式，UTR，CDS，等结果。    //
# perl ncbi_genbank2fasta.pl GRCh38_latest_rna.gbff
# perl ncbi_genbank2fasta.pl GCF_000001405.39_GRCh38.p13_rna.gbff


open UTR_5,">".$ARGV[0].'.UTR_5.fasta';
open UTR_3,">".$ARGV[0].'.UTR_3.fasta';
open CDS,">".$ARGV[0].'.CDS.fasta';
open EXONs,">".$ARGV[0].'.ALL_EXONs.fasta';

($locus,$version,$features,$gene_s,$gene_e,$origin,$origin_seq,$utr_5_seq,$utr_3_seq,$cds_seq,$gene)=('','','','','','','','','','','','','');
($utr_5,$utr_3,$cds_s,$cds_e)=(0 ,0 ,0 ,0);

	
while(<>)
{

	$_=~s/[\r\n]+//g;
	if($_ eq '//'){
	
		$origin_seq=~s/[\s\d]+//g;
		if($cds_s >0){
			
			$utr_5=$cds_s-$gene_s;
			$utr_3=$gene_e-$cds_e;
			$utr_5_seq=substr $origin_seq,0,$utr_5;
			$utr_3_seq=substr $origin_seq,$cds_e,$utr_3;
			$cds_seq=substr $origin_seq,$cds_s-1,$cds_e-$cds_s+1;
			# print $locus,"\t",$version,$features,$gene_s,$gene_e,$cds_s,$cds_e,$origin,"\n",$origin_seq,"\n";
			# print $utr_5,"\t",$utr_3,"\n";
			# print $utr_5_seq,"\n",$utr_3_seq,"\n",$cds_seq,"\n";
			
			
			if(length($utr_5_seq)>0)
			{
			
				print UTR_5 '>hg38_ncbiRefSeq_',$version,' "',$gene,'" gene_len:',$gene_e,' 5utr_len:',$utr_5,' cds_len:',$cds_e-$cds_s+1,' 3utr_len:',$utr_3,"\n";
				print UTR_5 $utr_5_seq,"\n";		
			
			}

	 
			if(length($utr_3_seq)>0)
			{
			
				print UTR_3 '>hg38_ncbiRefSeq_',$version,' "',$gene,'" gene_len:',$gene_e,' 3utr_len:',$utr_3,' 5utr_len:',$utr_5,' cds_len:',$cds_e-$cds_s+1,"\n";
				print UTR_3 $utr_3_seq,"\n";		
			
			}

	 
			if(length($cds_seq)>0)
			{
			
				print CDS '>hg38_ncbiRefSeq_',$version,' "',$gene,'" gene_len:',$gene_e,' cds_len:',$cds_e-$cds_s+1,' 5utr_len:',$utr_5,' 3utr_len:',$utr_3,"\n";
				print CDS $cds_seq,"\n";		
			
			}

		}

		print EXONs  '>hg38_ncbiRefSeq_',$version,' "',$gene,'" exons_all_len:',$gene_e,' cds_left:',$cds_s,' cds_right:',$cds_e,"\n";
		print EXONs $origin_seq,"\n";		
		

 
 
		($locus,$version,$features,$gene_s,$gene_e,$origin,$origin_seq,$utr_5_seq,$utr_3_seq,$cds_seq,$gene)=('','','','','','','','','','','','','');
		($utr_5,$utr_3,$cds_s,$cds_e)=(0 ,0 ,0 ,0);

		# print $locus,$version,$gene,$cds_s,$cds_e,$origin,$origin_seq,"\n";
		
	}
 
	if($_=~/LOCUS\s+(\S+)/){
		$locus=$1;
		 
	}

 
	if($_=~/VERSION\s+(\S+)/){
		$version=$1;
	 
	}
	if($_=~/FEATURES\s+\S+/){
		$features=1;
		 
		
	}

	if($features && $_=~/gene\s+(\d+)..(\d+)/){
		$gene_s=$1;
		$gene_e=$2;
		 
	}
	# /gene="A2M"
	if($gene_s && $_=~/\/gene\=\"(\S+)\"/){
		$gene=$1;
		 
		
	}	
	if($features && $_=~/CDS\s+(\d+)..(\d+)/){
		$cds_s=$1;
		$cds_e=$2;
		 
		
	}
	if($features && $origin){
		$origin_seq.=$_;
	}
	if($features && $_=~/ORIGIN/){
		$origin=1;
	}






}












print $locus,$version,$gene,$cds_s,$cds_e,$origin,$origin_seq,"\n";











close UTR_5;
close UTR_3;
close CDS;
close EXONs;