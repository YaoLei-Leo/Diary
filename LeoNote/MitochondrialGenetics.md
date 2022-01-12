# Mitochondria Genetics

In MDA, mitochondrial correlated Neuromuscular diseases have following types (https://www.mda.org):

- Friedreich’s ataxia (FA)
- Mitochondrial myopathies
    - Kearns-Sayre syndrome (KSS)
    - Leigh syndrome (subacute necrotizing encephalomyopathy)
    - Mitochondrial DNA depletion syndromes
    - Mitochondrial encephalomyopathy, lactic acidosis and stroke-like episodes (MELAS)
    - Mitochondrial neurogastrointestinal encephalomyopathy (MNGIE)
    - Myoclonus epilepsy with ragged red fibers (MERRF)
    - Neuropathy, ataxia and retinitis pigmentosa (NARP)
    - Pearson syndrome
    - Progressive external opthalmoplegia (PEO)

Skeletal muscle is one of the most metabolically active tissue types with particularly high energetic demands, making it very susceptible to defects in mitochondrial function [1].
## Introduction to Mitochondrial DNA

### 1. What is mitochondria DNA?
   In general, each human cell contains several hundred to 1,000 mitochondria, and each mitochondrion has 2 to 10 copies of mtDNA [3]. Mitochondrial DNA (mtDNA) is a 16,569 bp long, double-stranded supercoiled ring molecule, which does not contain histones. However, it forms a complex with >20 different proteins. Such a spherical nucleoprotein complex 100 nm in diameter is called a nucleoid and contain one or more copy of mtDNA [2].   Mitochondrial proteins are encoded both by the nuclear genome and their own genome (mtDNA), mitochondrial DNA (mtDNA) is primarily inherited from the maternal line [5]. 
   
   <p style="text-align:center"><img src="https://raw.githubusercontent.com/YaoLei-Leo/Diary/main/puppy_diary/mitochondrialGenetics/Mitochondrial%20DNA.jpg"></p>
   <p style="text-align:center">Mitochondrial in cell</p>
   
   Pedigree and phylogenetic analyses have estimated a de novo mtDNA nucleotide substitution rate of ~$10^{-8}$ substitutions per base pair per year. However, from 30,506 samples across the globe, only 2.4% of nucleotides (which is $16500*0.024=396$) show genetic variation with >1% frequency within a population. → The selection might contribute to the non-random distribution of common variants across the mitochondrial genome in the human population [4].

### 2. Macro-haplogroup of mtDNA ([cite from wikipedia](https://en.wikipedia.org/wiki/Macro-haplogroup_L_(mtDNA)))
  In human mitochondrial genetics, **L** is the mitochondrial DNA macro-haplogroup that is at the root of the anatomically modern human (*Homo sapiens*) mtDNA phylogenetic tree. As such, it represents the most ancestral mitochondrial lineage of all currently living modern humans, also dubbed "Mitochondrial Eve".

  <!-- Figure -->
  <p style="text-align:center"><img src="https://raw.githubusercontent.com/YaoLei-Leo/Diary/main/puppy_diary/mitochondrialGenetics/Haplo%20group.png"></p>
  <p style="text-align:center">haplogroup of mitochondria</p>
  <!-- Figure -->

  Mitochondrial haplogroups play a role in modulating the penetrance of mitochondrial diseases or in aged-related disorders.

  Computing mitochondrial haplogroups from NGS data is relatively easy, as many bioinformatics tools have been developed based on the phyloTree data. Such as HaploGrep2, Mitomaster, or HmtDB available on a web-server, or integrated into an all-in-one pipeline as in MToolBox bioinformatics suite, MseqDR mvTool, mit-o-matic. The Phy-Mer software allows the classfication of haplogroup from the FASTQ file, without prior alignment, avoiding mistakes casued by artifactual sequencing variants. Mitomaster allows a quick overview of the variant distribution in the different haplogroups, while HmtDB though multiple queries gives the frequency of a pathogenic variant within the haplogroup [5].

### 3. Pathogenic variants in mtDNA
  Pathogenic varaints of the mitochondrial genome can affect either the protein codeing genes, tRNAs, rRNAs and rRNA genes. Hundreds of pathogenic mtDNA variants implicated in a variety of human diseases have now been reported in the continuously updated Human Mitochondrial Genome Database -- the Mitomap. But as of today (Jul 2018) only 84 variants have a confirmed status, whereas a total of 595 other variants classified as reported, awaiting a final confirmation of pathogenicity [5].

  As the percentage of heteroplasmy increases, the energy production declines until the energy output falls below the minimum necessary for the physiological maintenance of cellular functions, causing the appearance of sumptoms [6].

### 4. Homoplasmy and heteroplasmy
  Due to stochastic segregation of mtDNA, the percentage of mutant and normal mtDNAs may drift during cellular divisions, and the percentage of the mutaition load may vary drastically among the different tissues and organs, from 100% mutant load, defining homoplasmy, to the coexistence of mutant and wildtype copies, defining heteroplasmy [5].

  Sanger sequencing lacks the sensitivity for detecting DNA mutant loads lower than 20%. NGS method is better, the limitation of detection (LOD) close to 5% for pyrosequencing methods and semiconductor techonology. Close to 1% for reversible terminated chemistry. Recently the development of duplex sequencing futher imporoved the power to detect low-level of heteroplasmy down to 0.001% [5].

  Indeed, it is commonly accepted that mtDNA mutations have clinical consequences only over a certain heteroplasmy level, also called threshold effect. Only Mitomap provides partial information mentioning the homoplasmic or heteroplasmic nature of pathogenic variants [5].

  Mutation loads of mtDNA variants could drastically vary in-between and within tissues due to the stochastic segregation of mtDNA. It might also undergo selection in blood cells, as for example the m.3243 A>G, for which heteroplasmy decreases by 1.4% per year in blood. However, when the mutation has identified from a blood sample or from the analysis of more relevant tissues, such as musle or uroepithelial cell, the presence of the heteroplasmic mutation can be linked to the phenotype of the patient [5].


  <p style="text-align:center"><img src="https://raw.githubusercontent.com/YaoLei-Leo/Diary/main/puppy_diary/mitochondrialGenetics/Graphical%20representation%20of%20human%20mitochondrial%20DNA%20variations.png"></p>
  <p style="text-align:center">Graphical representation of human mitochondrial DNA variations. The outer circle depicts the mitochondrial genome with annotated tRNAs (gray), rRNAs (purple), protein-coding genes, and non-coding regions (white).</p>

### 5. Conventional and validation techniques for mtDNA diagnosis
  Targeted Sanger sequencing for the detection of mutations, long-range PCR and Southern blotting for the detection of mtDNA rearrangements and depletions. fluorescent PCR restriction frament length polymorphism (RFLP) and pyrosequencing were used for the quantification of mtDNA variatns and rearrangements. These techniques are still useful as confirmatory and independent tools to ascertain the presence of a given mtDNA variant identified by NGS [5].

### 6. Difficulties of NGS on mitochondrial DNA.
  Interpretation of very low mutational loads, the discovery of variatns of unknown significance, and mutations unrelated to the patient phenotype [5].

### 7. Variants Calling
  There are a number of very good bioinformatic tools specifically designed for the SNV analysis of mtDNA MPS data, including MToolBox, Mutect2, and mtDNA-server [7].

### 8. mtDNA annotation

### 9. mtDNA population and clinical databases [5]
  The number of dedicated databases focusing on mtDNA with an active curation is limited, only three being available online: Mitomap, HmtDB andHmtVar.

  For instance, Mitomap gathered 45,000 whole mtDNA sequences and over 70,000 mtDNA control region sequences. However, the interpretation of the variant frequency in the general population is difficult given that databases include patient data and the peculiarities of mtDNA genetics (incomplete penetrance, heteroplasmy level, influence of mitochondrial haplogroup bakcground).

  Currently, there is no consensus threshold to consider the mtDNA variant is frequent in the population. The thresholds between 0.2 to 0.5% being arbitrarily chosen in several studies.

  General clinical databases such as CLINAR, CLINAR Miner, OMIM also include mtDNA variants but compared with exhaustive databases, they don't have enough variants and information.

### 10. *In Silico* Prediciton Tools and Pathogenicity scores. [5]
  nDNA pathogenicity predicion tools such as SIFT and Pholyphen2 are not suitable to predicte the pathogenicity of mtDNA variants. A set of 38 confirmed pathogenic variants (M) and 224 variants considered to be polymorphism (P) according to Mitomap, were assessed with a set of 19 different prediction tools. The performances of the prediction of pathogenic mtDNA variants differed significantly between the different bioinformatics tool [5].

  Recent tools developed for mtDNA using machine learing based approaches show better performace.
  <!-- Table --> 

  | *In Silico* Prediction Tools       |                       |                                                              |                              |
  | ---------------------------------- | --------------------- | ------------------------------------------------------------ | ---------------------------- |
  | APOGEE                             | Coding variants       | http://mitimpact.css-mendel.it                               | Castellana et al., 2017      |
  | MToolbox                           | Coding variants       | https://github.com/mitoNGS/MToolBox                          | Calabrese et al., 2014       |
  | Mitimpact2                         | Coding variants       | http://mitimpact.css-mendel.it/                              | Castellana et al., 2015      |
  | Mitoclass.1                        | Coding variants       | https://github.com/tonomartin2/MITOCLASS.1                   | Martin-Navarro et al., 2017  |
  | MITOTIP                            | tRNA variants         | https://www.mitomap.org/foswiki/bin/view/MITOMAP/MitoTipInfo | Sonney et al., 2017          |
  | PON-mt-tRNA                        | tRNA variants         | http://structure.bmc.lu.se/PON-mt-tRNA/                      | Niroula and Vihinen, 2016    |
  | Haplogrep2                         | Haplogroup prediction | https://haplogrep.uibk.ac.at/                                | Weissensteiner et al., 2016b |
  
  <!-- Table --> 

  Few tools are dedicated to mitochondrial tRNAs, which accounting for nearly 50% of the mtDNA alterations identified in patients. There are PON-mt-RNA, MITOTOP.

  Prediction has high false positive and false negative rate. To overcome this problem and imporve the prioritization of mtDNA VUS, several teams have developed scoring approches. These scores, which combines algorithms similar to those of *in silico* prediction tools and functional *in vivo* and *in vitro* evaluation, shows better performances.


### 11. Co-occurrence of mtDNA Variants [5]
  Mitochondrial whole genome screening may provide additional information with the co-occurrences of mtDNA variants that may modulate the phenotype. For example, the presence of the heteroplasmic m.12300G>A variant in MT-TL2, with a mutant load of about 10%, was shown to suppress the mitochondrial dysfunction in transmitochondrial cybrid cells carrying the m.3243A>G mutation with 99% mutated mtDNA, emphasizing the need for a complete mtDNA screening.

  A large study analyzing the distribution of know disease-causing mutations in a set of more than 30,000 mtDN sequences has recently suggested that the mtDNA background influences the development of mtDNA mutagenesis with the acquisition of recurrent mtDNA variants.

  it was recently shown that, apart from any pathogenic mtDNA variants, the combination of rare non-synonymous polymorphisms could lead to LHON, as exemplified by both combinations of variants m.14258G>A in the MT-ND6 gene (p.Pro139Leu) and m.14582A> G (p.Val31Ala); m.14258G> A, m.10680G> A in the MT-ND4L gene and m.12033A> G in the MT-ND4 gene.

  Functional studies of cybrid cells carrying both variant combinations revealed that the biochemical deficiency was transferred to mutant cybrids. Unfortunately, currently databases and bioinformatic pipelines do not allow identifying rare co-occurrences of variants, and further developments of these databases are needed to implement a searchable function of possible combinations of mtDNA variants.

### Influence of the Nuclear Genome [5]
  As mitochondria are driven by two genomes, several studies have demonstrated that nuclear variants may modulate the phenotypic expression of mtDNA pathogenic variants.
  For example, it has recently been suggested that the c.572G> T variant (p.Gly191Val) in YARS2, a gene coding formitochondrial tyrosyl-tRNA synthetase was associated with a mitochondrial protein translation defect, worsening mitochondrial respiratory chain deficiency in patients carrying the m.11778G>A LHON mutation. Thus, YARS2 appeared as a nuclear modifier, capable of triggering optic atrophy in individuals carrying them.11778G>A mutation, and would explain the incomplete penetrance of LHON, in addition to other parameters or environmental factors

  Unfortunately, major databases such as Mitomap, HmtDB, and HmtVar do not currently allow the search of the cooccurrence of mtDNA variants or in combination with nuclear variants.



 # References:
[1] Ignatieva, E., Smolina, N., Kostareva, A., & Dmitrieva, R. (2021). Skeletal Muscle Mitochondria Dysfunction in Genetic Neuromuscular Disorders with Cardiac Phenotype. International Journal of Molecular Sciences, 22(14), 7349. https://doi.org/10.3390/ijms22147349

[2] Ryzhkova, A. I., Sazonova, M. A., Sinyov, V. V., Galitsyna, E. V., Chicheva, M. M., Melnichenko, A. A., Grechko, A. V., Postnov, A. Y., Orekhov, A. N., & Shkurat, T. P. (2018). Mitochondrial diseases caused by mtDNA mutationsA mini-review. Therapeutics and Clinical Risk Management, 14, 1933–1942. https://doi.org/10.2147/TCRM.S154863

[3] Zhang, Y., Qu, Y., Gao, K., Yang, Q., Shi, B., Hou, P., & Ji, M. (2015). High copy number of mitochondrial DNA (mtDNA) predicts good prognosis in glioma patients. American Journal of Cancer Research, 5(3), 1207–1216.

[4] Wei, W., Tuna, S., Keogh, M. J., Smith, K. R., Aitman, T. J., Beales, P. L., Bennett, D. L., Gale, D. P., Bitner-Glindzicz, M. A. K., Black, G. C., Brennan, P., Elliott, P., Flinter, F. A., Floto, R. A., Houlden, H., Irving, M., Koziell, A., Maher, E. R., Markus, H. S., … Chinnery, P. F. (2019). Germline selection shapes human mitochondrial DNA diversity. Science. https://doi.org/10.1126/science.aau6520

[5] Bris, C., Goudenege, D., Desquiret-Dumas, V., Charif, M., Colin, E., Bonneau, D., Amati-Bonneau, P., Lenaers, G., Reynier, P., & Procaccio, V. (2018). Bioinformatics Tools and Databases to Assess the Pathogenicity of Mitochondrial DNA Variants in the Field of Next Generation Sequencing. Frontiers in Genetics, 9, 632. https://doi.org/10.3389/fgene.2018.00632

[6] Rossignol, R., Faustin, B., Rocher, C., Malgat, M., Mazat, J.-P., & Letellier, T. (2003). Mitochondrial threshold effects. The Biochemical Journal, 370(Pt 3), 751–762. https://doi.org/10.1042/BJ20021594

[7] Zambelli, F., Vancampenhout, K., Daneels, D., Brown, D., Mertens, J., Van Dooren, S., Caljon, B., Gianaroli, L., Sermon, K., Voet, T., Seneca, S., & Spits, C. (2017). Accurate and comprehensive analysis of single nucleotide variants and large deletions of the human mitochondrial genome in DNA and single cells. European Journal of Human Genetics, 25(11), 1229–1236. https://doi.org/10.1038/ejhg.2017.129

