# TAI_axolotl
Codes for manuscript of "Transcriptome age analysis embryo development and regeneration in axolotl"  
This project builds up a pipeline for transcriptome age index analysis during axolotl embryonic development and regeneration.   
Phylostratigraphy analysis offers an evolutionary perspective to explore the age of genes in various species. Throughout the course of evolution, new genes gradually evolve indispensable roles in fundamental biological processes. However, the transcriptome age of genes and the significant role of new genes in tissue regeneration, also the relationship with embryogenesis remain unexplored. Here, we used axolotl (Ambystoma mexicanum), a species renowned for its remarkable regenerative capacity, to trace the phylogenetic age of genes and categorize them into 18 phylostratas corresponding to different taxonomies. By analyzing bulk transcriptomic data, we observed an hourglass model throughout axolotl embryonic development, with the gastrula phase representing the phylotypic stage characterized by the oldest transcriptome. In addition, phylostratigraphy analysis identified 324 axolotl lineage-specific new genes, which have been partly recruited into co-expression networks associated with DNA damage response biological process. Furthermore, analysis of single-cell transcriptome data revealed that the pattern of limb regeneration recapitulated the developmental hourglass model. Taken the single-cell transcriptome data of limb and telencephalon regeneration together, we found that the cell types with lower differentiation potency expressed younger transcriptomes and vice versa. Finally, we observed that the majority of newly evolved genes demonstrated cell type- and stage-specific expression patterns in axolotls, suggesting their potential contribution to evolution and regeneration processes. These results greatly expand our understanding for new gene evolution in regeneration and phenotypic evolution in general.    
## 1. Data availablility
This study used previously published datasets (Bryant et al. 2017; Jiang et al. 2017; Li et al. 2021; Wei et al. 2022).
## 2. Performing Phylostratigraphy  
Phylostratigraphy analysis for axolotl genes are following the methods in [https://github.com/AlexGa/Phylostratigraphy](https://github.com/AlexGa/Phylostratigraphy).
###  Constructing index for database    
`makeblastdb -dbtype prot -in phyloBlastDB_Drost_Gabel_Grosse_Quint.fa`    
###  Adding taxonomy header for axolotl protein coding sequences    
`python3 add_taxomomy_to_axolotlProtein.fa.py AmexT_v47.PEPTIDES.filter.fasta axolotl.cellular.organisms.header AmexT_v47.PEPTIDES.filter.PSname.fasta`    
###  Aligning axolotl protein coding sequences with phyloBlastDB to obtain the phylostrata map of all axolotl genes    
`perl createPSmap.pl --organism AmexT_v47.PEPTIDES.filter.PSname.fasta --database phyloBlastDB_Drost_Gabel_Grosse_Quint.fa --prefix AmexT_v47.PEPTIDES.filter.PS --seqOffset 1000  --evalue 1e-5 --threads 60 --blastPlus`    
###  
