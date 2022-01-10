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

Skeletal muscle is one of the most metabolically active tissue types with particularly high energetic demands, making it very susceptible to defects in mitochondrial function [^ignatieva_skeletal_2021].
## Introduction to Mitochondrial DNA

### 1. What is mitochondria DNA?
   In general, each human cell contains several hundred to 1,000 mitochondria, and each mitochondrion has 2 to 10 copies of mtDNA [^zhang_high_2015]. Mitochondrial DNA (mtDNA) is a 16,569 bp long, double-stranded supercoiled ring molecule, which does not contain histones. However, it forms a complex with >20 different proteins. Such a spherical nucleoprotein complex 100 nm in diameter is called a nucleoid and contain one or more copy of mtDNA [^ryzhkova_mitochondrial_2018].   Mitochondrial proteins are encoded both by the nuclear genome and their own genome (mtDNA), mitochondrial DNA (mtDNA) is primarily inherited from the maternal line [^bris_bioinformatics_2018]. 
   
   <p style="text-align:center"><img src="https://raw.githubusercontent.com/YaoLei-Leo/Diary/main/puppy_diary/mitochondrialGenetics/Mitochondrial%20DNA.jpg"></p>
   <p style="text-align:center">Mitochondrial in cell</p>
   
   Pedigree and phylogenetic analyses have estimated a de novo mtDNA nucleotide substitution rate of ~$10^{-8}$ substitutions per base pair per year. However, from 30,506 samples across the globe, only 2.4% of nucleotides (which is $16500*0.024=396$) show genetic variation with >1% frequency within a population. → The selection might contribute to the non-random distribution of common variants across the mitochondrial genome in the human population [^wei_germline_2019].

### 2. Macro-haplogroup of mtDNA ([cite from wikipedia](https://en.wikipedia.org/wiki/Macro-haplogroup_L_(mtDNA)))
  In human mitochondrial genetics, **L** is the mitochondrial DNA macro-haplogroup that is at the root of the anatomically modern human (*Homo sapiens*) mtDNA phylogenetic tree. As such, it represents the most ancestral mitochondrial lineage of all currently living modern humans, also dubbed "Mitochondrial Eve".

  <p style="text-align:center"><img src="https://raw.githubusercontent.com/YaoLei-Leo/Diary/main/puppy_diary/mitochondrialGenetics/Haplo%20group.png"></p>
  <p style="text-align:center">haplogroup of mitochondria</p>


### 3. Pathogenic variants in mtDNA
  Pathogenic varaints of the mitochondrial genome can affect either the protein codeing genes, tRNAs, rRNAs and rRNA genes. Hundreds of pathogenic mtDNA variants implicated in a variety of human diseases have now been reported in the continuously updated Human Mitochondrial Genome Database -- the Mitomap. But as of today (Jul 2018) only 84 variants have a confirmed status, whereas a total of 595 other variants classified as reported, awaiting a final confirmation of pathogenicity [^bris_bioinformatics_2018].

  As the percentage of heteroplasmy increases, the energy production declines until the energy output falls below the minimum necessary for the physiological maintenance of cellular functions, causing the appearance of sumptoms [^rossignol_mitochondrial_2003].

### 4. Homoplasmy and heteroplasmy
  Due to stochastic segregation of mtDNA, the percentage of mutant and normal mtDNAs may drift during cellular divisions, and the percentage of the mutaition load may vary drastically among the different tissues and organs, from 100% mutant load, defining homoplasmy, to the coexistence of mutant and wildtype copies, defining heteroplasmy [^bris_bioinformatics_2018].

  <p style="text-align:center"><img src="https://raw.githubusercontent.com/YaoLei-Leo/Diary/main/puppy_diary/mitochondrialGenetics/Graphical%20representation%20of%20human%20mitochondrial%20DNA%20variations.png"></p>
  <p style="text-align:center">Graphical representation of human mitochondrial DNA variations. The outer circle depicts the mitochondrial genome with annotated tRNAs (gray), rRNAs (purple), protein-coding genes, and non-coding regions (white).</p>

### 5. Conventional and validation techniques for mtDNA diagnosis
  Targeted Sanger sequencing for the detection of mutations, long-range PCR and Southern blotting for the detection of mtDNA rearrangements and depletions. fluorescent PCR restriction frament length polymorphism (RFLP) and pyrosequencing were used for the quantification of mtDNA variatns and rearrangements. These techniques are still useful as confirmatory and independent tools to ascertain the presence of a given mtDNA variant identified by NGS [^bris_bioinformatics_2018].

### 6. Difficulties of NGS on mitochondrial DNA.
  Interpretation of very low mutational loads, the discovery of variatns of unknown significance, and mutations unrelated to the patient phenotype [^bris_bioinformatics_2018].

### 7. Variants Calling
  There are a number of very good bioinformatic tools specifically designed for the SNV analysis of mtDNA MPS data, including MToolBox, MitoSeek, and mtDNA-server [^zambelli_accurate_2017].

 # References:
 [^ignatieva_skeletal_2021]: Ignatieva, E., Smolina, N., Kostareva, A., & Dmitrieva, R. (2021). Skeletal Muscle Mitochondria Dysfunction in Genetic Neuromuscular Disorders with Cardiac Phenotype. International Journal of Molecular Sciences, 22(14), 7349. https://doi.org/10.3390/ijms22147349

[^ryzhkova_mitochondrial_2018]: Ryzhkova, A. I., Sazonova, M. A., Sinyov, V. V., Galitsyna, E. V., Chicheva, M. M., Melnichenko, A. A., Grechko, A. V., Postnov, A. Y., Orekhov, A. N., & Shkurat, T. P. (2018). Mitochondrial diseases caused by mtDNA mutations: A mini-review. Therapeutics and Clinical Risk Management, 14, 1933–1942. https://doi.org/10.2147/TCRM.S154863

[^zhang_high_2015]: Zhang, Y., Qu, Y., Gao, K., Yang, Q., Shi, B., Hou, P., & Ji, M. (2015). High copy number of mitochondrial DNA (mtDNA) predicts good prognosis in glioma patients. American Journal of Cancer Research, 5(3), 1207–1216.

[^wei_germline_2019]: Wei, W., Tuna, S., Keogh, M. J., Smith, K. R., Aitman, T. J., Beales, P. L., Bennett, D. L., Gale, D. P., Bitner-Glindzicz, M. A. K., Black, G. C., Brennan, P., Elliott, P., Flinter, F. A., Floto, R. A., Houlden, H., Irving, M., Koziell, A., Maher, E. R., Markus, H. S., … Chinnery, P. F. (2019). Germline selection shapes human mitochondrial DNA diversity. Science. https://doi.org/10.1126/science.aau6520

[^bris_bioinformatics_2018]: Bris, C., Goudenege, D., Desquiret-Dumas, V., Charif, M., Colin, E., Bonneau, D., Amati-Bonneau, P., Lenaers, G., Reynier, P., & Procaccio, V. (2018). Bioinformatics Tools and Databases to Assess the Pathogenicity of Mitochondrial DNA Variants in the Field of Next Generation Sequencing. Frontiers in Genetics, 9, 632. https://doi.org/10.3389/fgene.2018.00632

[^bris_bioinformatics_2018]: Bris, C., Goudenege, D., Desquiret-Dumas, V., Charif, M., Colin, E., Bonneau, D., Amati-Bonneau, P., Lenaers, G., Reynier, P., & Procaccio, V. (2018). Bioinformatics Tools and Databases to Assess the Pathogenicity of Mitochondrial DNA Variants in the Field of Next Generation Sequencing. Frontiers in Genetics, 9, 632. https://doi.org/10.3389/fgene.2018.00632

[^bris_bioinformatics_2018]: Bris, C., Goudenege, D., Desquiret-Dumas, V., Charif, M., Colin, E., Bonneau, D., Amati-Bonneau, P., Lenaers, G., Reynier, P., & Procaccio, V. (2018). Bioinformatics Tools and Databases to Assess the Pathogenicity of Mitochondrial DNA Variants in the Field of Next Generation Sequencing. Frontiers in Genetics, 9, 632. https://doi.org/10.3389/fgene.2018.00632

[^rossignol_mitochondrial_2003]: Rossignol, R., Faustin, B., Rocher, C., Malgat, M., Mazat, J.-P., & Letellier, T. (2003). Mitochondrial threshold effects. The Biochemical Journal, 370(Pt 3), 751–762. https://doi.org/10.1042/BJ20021594

[^bris_bioinformatics_2018]: Bris, C., Goudenege, D., Desquiret-Dumas, V., Charif, M., Colin, E., Bonneau, D., Amati-Bonneau, P., Lenaers, G., Reynier, P., & Procaccio, V. (2018). Bioinformatics Tools and Databases to Assess the Pathogenicity of Mitochondrial DNA Variants in the Field of Next Generation Sequencing. Frontiers in Genetics, 9, 632. https://doi.org/10.3389/fgene.2018.00632

[^bris_bioinformatics_2018]: Bris, C., Goudenege, D., Desquiret-Dumas, V., Charif, M., Colin, E., Bonneau, D., Amati-Bonneau, P., Lenaers, G., Reynier, P., & Procaccio, V. (2018). Bioinformatics Tools and Databases to Assess the Pathogenicity of Mitochondrial DNA Variants in the Field of Next Generation Sequencing. Frontiers in Genetics, 9, 632. https://doi.org/10.3389/fgene.2018.00632

[^zambelli_accurate_2017]: Zambelli, F., Vancampenhout, K., Daneels, D., Brown, D., Mertens, J., Van Dooren, S., Caljon, B., Gianaroli, L., Sermon, K., Voet, T., Seneca, S., & Spits, C. (2017). Accurate and comprehensive analysis of single nucleotide variants and large deletions of the human mitochondrial genome in DNA and single cells. European Journal of Human Genetics, 25(11), 1229–1236. https://doi.org/10.1038/ejhg.2017.129

