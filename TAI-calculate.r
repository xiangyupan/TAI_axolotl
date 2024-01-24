library(myTAI)
data <- read.table("Axolotl_filter.salmon.development.PS.forTAI.txt",sep="\t",header=T)
dataset <- as.data.frame(data)
TAI(dataset)
'''
      S1       S2       S3       S4       S5       S6       S7       S8 
7.662042 6.985666 7.169445 6.040866 8.594242 6.407251 5.816550 6.099229 
      S9      S10      S11      S12      S14      S16      S19      S24 
5.572378 5.407244 5.426832 5.909185 5.577332 7.133462 6.100398 5.102927 
     S40 
5.455224 
'''
pdf("Axolotl_filter_protein.embryo.development.TAI.pdf")
PlotSignature(ExpressionSet=dataset,measure="TAI",TestStatistic="FlatLineTest",xlab = "Stage",ylab = "TAI")
FlatLineTest(ExpressionSet=dataset,permutations=1000,plotHistogram=TRUE)
dev.off()
pdf("Axolotl_filter_protein.embryo.development.TAI-contribution.pdf"
# visualize phylostrata contribution to the global TAI pattern
PlotContribution( ExpressionSet = dataset,
                   legendName    = "PS",
                   xlab           = "Ontogeny",
                   ylab           = "Transcriptome Age Index",
                   y.ticks        = 10)

pTAI(PhyloExpressionSetExample)
dev.off()
