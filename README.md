# TAI_axolotl
Codes for manuscript of "**Transcriptome age analysis embryo development and regeneration in axolotl**"  
This project builds up a pipeline for transcriptome age index analysis during axolotl embryonic development and regeneration.   
Phylostratigraphy analysis offers an evolutionary perspective to explore the age of genes in various species. Throughout the course of evolution, new genes gradually evolve indispensable roles in fundamental biological processes. However, the transcriptome age of genes and the significant role of new genes in tissue regeneration, also the relationship with embryogenesis remain unexplored. Here, we used axolotl (Ambystoma mexicanum), a species renowned for its remarkable regenerative capacity, to trace the phylogenetic age of genes and categorize them into 18 phylostratas corresponding to different taxonomies. By analyzing bulk transcriptomic data, we observed an hourglass model throughout axolotl embryonic development, with the gastrula phase representing the phylotypic stage characterized by the oldest transcriptome. In addition, phylostratigraphy analysis identified 324 axolotl lineage-specific new genes, which have been partly recruited into co-expression networks associated with DNA damage response biological process. Furthermore, analysis of single-cell transcriptome data revealed that the pattern of limb regeneration recapitulated the developmental hourglass model. Taken the single-cell transcriptome data of limb and telencephalon regeneration together, we found that the cell types with lower differentiation potency expressed younger transcriptomes and vice versa. Finally, we observed that the majority of newly evolved genes demonstrated cell type- and stage-specific expression patterns in axolotls, suggesting their potential contribution to evolution and regeneration processes. These results greatly expand our understanding for new gene evolution in regeneration and phenotypic evolution in general.    
## 1. Data availablility
This study used previously published datasets (Bryant et al. 2017; Jiang et al. 2017; Li et al. 2021; Wei et al. 2022).
## 2. Performing Phylostratigraphy  
Phylostratigraphy analysis for axolotl genes are following the methods in [https://github.com/AlexGa/Phylostratigraphy](https://github.com/AlexGa/Phylostratigraphy).
###  Constructing index for database    
```makeblastdb -dbtype prot -in phyloBlastDB_Drost_Gabel_Grosse_Quint.fa```    
###  Picking the longest transcript for each axolotl gene and Filtering axolotl genes to obtain high confidence protein coding genes    
Following suggestions from author who assemblied the axolotl genome, genes with ORFs which had been verified by RNA-seq from the annotation file (GFF file) were retained as axolotl highly confidence protein coding genes. Those genes located in scaffolds were also filtered out.  
```
perl -e 'while(<>){my $header=$_; chomp $header; my $seq=<>; chomp $seq; my ($tran, $gene) = $header =~ />(\S+?); gene_id "(\S+?)";/; print $tran,"\t",$gene,"\t",length($seq),"\n"}' AmexT_v47.PEPTIDES.fa > link
sort -k2,2 -k3,3nr link | perl -lane '$hash{$F[1]}++; print $_ if $hash{$F[1]} == 1' > link.longest  
perl -e 'open(IN1, shift); while(<IN1>){chomp; @A=split/\s+/; $hash{$A[0]}=1} open(IN2, shift); while(<IN2>){my $header=$_; chomp $header; my $seq=<IN2>; chomp $seq; my ($tran, $gene) = $header =~ />(\S+?); gene_id "(\S+?)";/; print $header,"\n",$seq,"\n" if exists $hash{$tran}}' link.longest AmexT_v47.PEPTIDES.fa > AmexT_v47.PEPTIDES.longest.fa  
les AmexT_v47.release.gtf |egrep "ORF_type \"Putative|N-terminal|C-terminal|Partial" |les|grep -v 'PTC' |les|awk -F "\t" '{print $9}' |sed 's/;/\t/g' |awk -F "\t" '{print $1}' |sed 's/gene_id //g' |sed 's/"//g' |uniq |les |grep -v 'AMEX60DDU'  > AmexT_v47.PEPTIDES.pick  
python3 pick_putative_from_longestFa.py -f AmexT_v47.PEPTIDES.longest.fa -g AmexT_v47.PEPTIDES.pick -o AmexT_v47.PEPTIDES.pick.fa
```
###  Adding taxonomy header for axolotl protein coding sequences    
```python3 add_taxomomy_to_axolotlProtein.fa.py AmexT_v47.PEPTIDES.filter.fasta axolotl.cellular.organisms.header AmexT_v47.PEPTIDES.filter.PSname.fasta```    
###  Aligning axolotl protein coding sequences with phyloBlastDB to obtain the phylostrata map of all axolotl genes    
```perl createPSmap.pl --organism AmexT_v47.PEPTIDES.filter.PSname.fasta --database phyloBlastDB_Drost_Gabel_Grosse_Quint.fa --prefix AmexT_v47.PEPTIDES.filter.PS --seqOffset 1000  --evalue 1e-5 --threads 60 --blastPlus```    
## 3. Obtain the gene expression matrix of axolotl embryonic development      
We downloaded the raw fastq files of axolotl embryonic development data from Jiang et al.(Jiang et al. 2017). All raw fastq were trimmed by trimmomatic and quantified by salmon. Gene expression matrix of each sample was merged into an integrated matrix.    
```#!/bin/sh                  
for i in `cat samplename.txt`      
do java -Xmx30g -jar trimmomatic-0.39.jar PE -threads 45 ${i}_1.fastq.gz  ${i}_2.fastq.gz ${i}_1.clean.fq.gz ${i}_1.unpaired.fq.gz ${i}_2.clean.fq.gz ${i}_2.unpaired.fq.gz   LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:40 TOPHRED33 > ./run_trim.log      
salmon quant --gcBias -l A -i AmexG_v6.0-DD.merge.salmon_sa_index -g Axolotl.v6.0.transcript.gene.txt -1 ${i}_1.clean.fq.gz -2 ${i}_2.clean.fq.gz -p 8 -o ${i}.salmon.count                       
done
Rscript tximport.r    
```
## 4. Adding phylostrata value to axolotl embryonic development matrix      
We added the phylostata map as one cololumn to the axolotl embryonic development gene expression matrix.    
```python3 add_PS_to_geneExpressionMatrix.py Axolotl_filter.salmon.development.txt Axolotl_BlastPlus_PS_map_final_ps_map.tsv Axolotl_filter.salmon.development.PS.txt```  
The gene expression matrix with phylostrata 
## 5.Calculating Transcriptome age index for axolotl embryonic development    
In this step, we will calculate the dynamics of TAI by myTAI during axolotl embryonic development.     
`Rscript TAI-calculate.r`    
# References      
1. Domazet-Loso T, Brajković J, Tautz D. A phylostratigraphy approach to uncover the genomic history of major adaptations in metazoan lineages. Trends Genet. 2007 Nov;23(11):533-9. doi: 10.1016/j.tig.2007.08.014.
2. Drost HG, Gabel A, Liu J, Quint M, Grosse I. myTAI: evolutionary transcriptomics with R. Bioinformatics. 2018 May 1;34(9):1589-1590. doi: 10.1093/bioinformatics/btx835.
3. Xiangyu P, Zitian H, Na Q, Jinman L, Xiang L, Yuanhui Q, Zhuqing Z, JiFeng F. Transcriptome age of embryo development and regeneration in axolotl, ***in revision***.        
* We'd love to hear from you. If you have any questions, please don't be hestitate to contact the author of this manuscript: Xiangyu Pan (pan_xiangyu@nwafu.edu.cn)      
