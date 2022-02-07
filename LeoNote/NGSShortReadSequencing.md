# HIGH-THROUGHPUT DNA SEQUENCING (NGS)
High-Throughput DNA sequencing (DNA-seq) is an essential method for clinical and basic biomedical research. DNA-seq has numerous experimental applications, including but not limited to genotyping and variant discovery within individuals, population- and species-level chracterization of genomes, and revealing taxonomic diversity within a metagenomic mixtrue [^noauthor_performance_nodate].


# GATK has limitation
The widely used GATK uses logistic regression to model base errors, hidden Markov models to compute read likelihoods, and naive Bayes calssification to identify variants, which are then filetered to remove likely false positives using a Gaussian mitrue model with hand-crefted features capturing common error modes. These techiques allow the GATK to acheve high but still imperfect accuracy on the Illumina sequencing platform. Generalizing these models to other seuquencing techonogies (for example, Ion Torrent) has proven diffucult due to the need to manually retune or extende these statistical models, which is problematic in an area with such rapid technological progress [^noauthor_universal_nodate].

# DeepVariant
DeepVariant is a NGS data SNP and indel caller that developed by Google using deep neural networks (deep convolutional neural network). Compared with GATK, which is a assorment of statistical models, DeepVariant is a single deep learning model.

## Evaluation of DeepVariant
### **1. Comparision between GATK and DeepVariant on Illimina platform**
**Data:** Platinum Genomes Projects NA12878 <br>
**Replication:** 27 replicates of NA12878 <br>
**Method:** PCR-free WGS 2x151 on an Illumina X10
with coverage from 24x-35x, Standard whole-genome sequencing (WGS) protocol, GATK best-practices pipeline and DeepVariant <br>
**Results:** DeepVariants produced more accurate results with greater consistency across a variety of quality metrics
<center><img src="./NGSShortReadSequencing/1.jpg"></center>
<center><p>DeepVariant (red circles) and the GATK (blue triangles) were run on 27 independently sequenced replicates of NA12878 (PCR-free WGS 2x151 on an Illumina X10 with coverage from 24x-35x). Each panel shows the distribution of values for the given metric (panel label) for DeepVariant and the GATK. DeepVariant produces more accurate SNP and indel calls (F1) when compared to the Genome in a Bottle standard for NA12878 with a higher fraction of sites having the correct genotype assigned (Genotype concordance). DeepVariant finds a similar numbers of indels to the GATK, but has a more consistent ratio of insertions to deletions. DeepVariant finds more SNPs than GATK with a similar ratio of heterozygous variants to homozygous alternative variants (Het/hom ratio) [^noauthor_universal_nodate].<p></center>

### **2. Test on blinded sample**
**Data:** CEPH female sample NA12878, Ashkenazi male sample NA24385
**Method:** DeepVariant trained only on NA12878 and tested on NA24385
**Result:** High accuracy (F1 score) and harmonic mean of sensitivity and positive preditive value (PPV, also called precision) (SNP F1=99.95%, indel F1=98.98%).

### **3. Comparision between DeepVariant and recent and commonly used bioinformatics methods**
**Data:** CEPH female sample NA12878, Ashkenazi male sample NA24385 <br>
**Method:** DeepVariant and other bioinformatics tools <br>
**Result:** DeepVariant demonstrated more than 50% fewer errors per genome compared to the next-best algorithm. <br>

<center>

| Method | Type | F1 | Recall | Precision | TP | FN | FP | FP.gt | FP.al | Version |
|---|---|---|---|---|---|---|---|---|---|---|
| DeepVariant (live GitHub) | Indel | 0.99507 | 0.99347 | 0.99666 | 357,641 | 2350 | 1,198 | 217 | 840 | Latest GitHub v0.4.1-b4e8d37d |
| GATK (raw) | Indel | 0.99366 | 0.99219 | 0.99512 | 357,181 | 2810 | 1,752 | 377 | 995 | 3.8-0-ge9d806836 |
| Strelka | Indel | 0.99227 | 0.98829 | 0.99628 | 355,777 | 4214 | 1,329 | 221 | 855 | 2.8.4-3-gbe58942 |
| DeepVariant (pFDA) | Indel | 0.99112 | 0.98776 | 0.99450 | 355,586 | 4405 | 1,968 | 846 | 1,027 | pFDA submission May 2016 |
| GATK (VQSR) | Indel | 0.99010 | 0.98454 | 0.99573 | 354,425 | 5566 | 1,522 | 343 | 909 | 3.8-0-ge9d806836 |
| GATK (flt) | Indel | 0.98229 | 0.96881 | 0.99615 | 348,764 | 11227 | 1,349 | 370 | 916 | 3.8-0-ge9d806836 |
| FreeBayes | Indel | 0.94091 | 0.91917 | 0.96372 | 330,891 | 29,100 | 12,569 | 9,149 | 3,347 | v1.1.0-54-g49413aa |
| 16GT | Indel | 0.92732 | 0.91102 | 0.94422 | 327,960 | 32,031 | 19,364 | 10,700 | 7,745 | v1.0-34e8f934 |
| SAMtools | Indel | 0.87951 | 0.83369 | 0.93066 | 300,120 | 59,871 | 22,682 | 2,302 | 20,282 | 1.6 |
| DeepVariant (live GitHub) | SNP | 0.99982 | 0.99975 | 0.99989 | 3,054,552 | 754 | 350 | 157 | 38 | Latest GitHub v0.4.1-b4e8d37d |
| DeepVariant (pFDA) | SNP | 0.99958 | 0.99944 | 0.99973 | 3,053,579 | 1,727 | 837 | 409 | 78 | pFDA submission May 2016 |
| Strelka | SNP | 0.99935 | 0.99893 | 0.99976 | 3,052,050 | 3,256 | 732 | 87 | 136 | 2.8.4-3-gbe58942 |
| GATK (raw) | SNP | 0.99914 | 0.99973 | 0.99854 | 3,054,494 | 812 | 4,469 | 176 | 257 | 3.8-0-ge9d806836 |
| 16GT | SNP | 0.99583 | 0.99850 | 0.99318 | 3,050,725 | 4,581 | 20,947 | 3,476 | 3,899 | v1.0-34e8f934 |
| GATK (VQSR) | SNP | 0.99436 | 0.98940 | 0.99937 | 3,022,917 | 32,389 | 1,920 | 80 | 170 | 3.8-0-ge9d806836 |
| FreeBayes | SNP | 0.99124 | 0.98342 | 0.99919 | 3,004,641 | 50,665 | 2,434 | 351 | 1,232 | v1.1.0-54-g49413aa |
| SAMtools | SNP | 0.99021 | 0.98114 | 0.99945 | 2,997,677 | 57,629 | 1,651 | 1,040 | 200 | 1.6 |
| GATK (flt) | SNP | 0.98958 | 0.97953 | 0.99983 | 2,992,764 | 62,542 | 509 | 168 | 26 | 3.8-0-ge9d806836 |

</center>

<center><p>FP.gt: False Positive caused by genotype mismatches; FP.al: False Positive caused by allele mismatch</p></center>

**Data:** synthetic diploid sample CHM1-CHM13 <br>
**Method:** DeepVariant and other bioinformatics tools <br>
**Result:** DeepVariant outperformed all other methods for calling both SNP and indel mutations, without needing to adjust filtering thresholds or other parameters. <br>

<center>

| Method | Type | F1 | Recall | Precision | TP | FN | FP | Version |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DeepVariant | Indel | 0.95806 | 0.92868 | 0.98936 | 529,137 | 40,634 | 5,690 | v0.4.1-b4e8d37d |
| Strelka | Indel | 0.95074 | 0.91623 | 0.98796 | 522,039 | 47,732 | 6,363 | 2.8.4-3-gbe58942 |
| 16GT | Indel | 0.94010 | 0.90803 | 0.97452 | 517,369 | 52,402 | 13,527 | v1.0-34e8f934 |
| GATK (raw) | Indel | 0.93268 | 0.89504 | 0.97363 | 509,969 | 59,802 | 13,811 | 3.8-0-ge9d806836 |
| GATK (VQSR) | Indel | 0.91212 | 0.84497 | 0.99087 | 481,441 | 88,330 | 4,437 | 3.8-0-ge9d806836 |
| FreeBayes | Indel | 0.90438 | 0.83025 | 0.99305 | 473,053 | 96,718 | 3,313 | v1.1.0-54-g49413aa |
| SAMtools | Indel | 0.86976 | 0.79089 | 0.96611 | 450,626 | 119,145 | 15,807 | 1.6 |
| DeepVariant | SNP | 0.99103 | 0.98888 | 0.99319 | 3,518,118 | 39,553 | 24,132 | v0.4.1-b4e8d37d |
| Strelka | SNP | 0.98865 | 0.98107 | 0.99636 | 3,490,314 | 67,357 | 12,749 | 2.8.4-3-gbe58942 |
| 16GT | SNP | 0.97862 | 0.98966 | 0.96782 | 3,520,894 | 36,777 | 117,078 | v1.0-34e8f934 |
| FreeBayes | SNP | 0.96910 | 0.94837 | 0.99075 | 3,373,984 | 183,687 | 31,492 | v1.1.0-54-g49413aa |
| GATK (VQSR) | SNP | 0.96895 | 0.94542 | 0.99368 | 3,363,476 | 194,195 | 21,379 | 3.8-0-ge9d806836 |
| SAMtools | SNP | 0.96818 | 0.94386 | 0.99378 | 3,357,947 | 199,724 | 21,012 | 1.6 |
| GATK (raw) | SNP | 0.96646 | 0.95685 | 0.97627 | 3,404,167 | 153,504 | 82,748 | 3.8-0-ge9d806836 |

</center>

### **4. Further test how DeepVariant perform byond the training data.**
**Method:** Trainning on Grch37, Test on Grch 38. <br>
**Result:** Overall F1=99.45%. <br>

**Method:** Trainning on Grch38, Test on Grch 38. <br>
**Result:** Overall F1=99.53%. <br>

<center>

| Variants | Training | data | Evaluation | data | PPV | Sensitivity | F1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SNPs + indels | b37 | chr1-19 | b38 | chr20-22 | 99.93% | 98.98% | 99.45% |
| b38 | chr1-19 | b38 | chr20-22 | 99.87% | 99.21% | 99.53% |
| SNPs | b37 | chr1-19 | b38 | chr20-22 | 99.98% | 99.23% | 99.60% |
| b38 | chr1-19 | b38 | chr20-22 | 99.93% | 99.35% | 99.64% |
| Indels | b37 | chr1-19 | b38 | chr20-22 | 99.60% | 97.35% | 98.46% |
| b38 | chr1-19 | b38 | chr20-22 | 99.42% | 98.22% | 98.81% |

</center>

**Conclusion:** DeepVariant model learned from one version of the human genome reference can be applied to other versions with effectively no loss in accuracy.


**Method:** Trainning on human data, test on mouse dataset. <br>
**Result:** Overall F1=98.29%. outperforming training on the mouse data itself (F1=97.84%). <br>



<center>

| Variants | Training | data | Evaluation | data | PPV | Sensitivity | F1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SNPs + indels | Human | chr1-19 | Mouse | chr18-19 | 99.53% | 97.07% | 98.29% |
| Mouse | chr1-17 | Mouse | chr18-19 | 99.90% | 95.85% | 97.84% |
| SNPs | Human | chr1-19 | Mouse | chr18-19 | 99.98% | 97.86% | 98.91% |
| Mouse | chr1-17 | Mouse | chr18-19 | 99.99% | 99.10% | 99.54% |
| Indels | Human | chr1-19 | Mouse | chr18-19 | 96.41% | 91.75% | 94.02% |
| Mouse | chr1-17 | Mouse | chr18-19 | 99.15% | 73.80% | 84.62% |

</center>

**Conclusion:** DeepVariant is robust to changes in sequencing depth, preparation protocol, instrument type, genome build and even mammalian species.

## Evaluate cross-platform performance of DeepVariant


# Referenences:
[^noauthor_universal_nodate]: A universal SNP and small-indel variant caller using deep neural networks | Nature Biotechnology. (n.d.). Retrieved 25 January 2022, from https://www.nature.com/articles/nbt.4235

[^noauthor_performance_nodate]: Performance assessment of DNA sequencing platforms in the ABRF Next-Generation Sequencing Study | Nature Biotechnology. (n.d.). Retrieved 26 January 2022, from https://www.nature.com/articles/s41587-021-01049-5

