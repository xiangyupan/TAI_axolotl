perl -e 'while(<>){my $header=$_; chomp $header; my $seq=<>; chomp $seq; my ($tran, $gene) = $header =~ />(\S+?); gene_id "(\S+?)";/; print $tran,"\t",$gene,"\t",length($seq),"\n"}' AmexT_v47.PEPTIDES.fa > link
sort -k2,2 -k3,3nr link | perl -lane '$hash{$F[1]}++; print $_ if $hash{$F[1]} == 1' > link.longest

perl -e 'open(IN1, shift); while(<IN1>){chomp; @A=split/\s+/; $hash{$A[0]}=1} open(IN2, shift); while(<IN2>){my $header=$_; chomp $header; my $seq=<IN2>; chomp $seq; my ($tran, $gene) = $header =~ />(\S+?); gene_id "(\S+?)";/; print $header,"\n",$seq,"\n" if exists $hash{$tran}}' link.longest AmexT_v47.PEPTIDES.fa > AmexT_v47.PEPTIDES.longest.fa 
