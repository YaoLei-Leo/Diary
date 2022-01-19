# Short Tandem Repeat (STR)

## What is short tandem repeat ?
STRs are small sections of DNA, usually 2-6 nucleotides in length, that are repeated consecutively at a given locus [^chintalaphani_update_2021].

<center><img src="https://ib.bioninja.com.au/_Media/str_med.jpeg"></center>

STRs make up at leasts 6.77% of the human genome and are highly polymorphic [^chintalaphani_update_2021]. 

STR lengths are relatively unstable, it's lengths are prone to be altered during DNA replication, due to slippage events on misaligned strands, errors in DNA repair during synthesis and formation of secondary hairpin structures. STRs have mutation rate orders of magnitude higher than single nucleotide polymorphisms (SNPs) in non-repetitive contexts [^chintalaphani_update_2021].

## What STR will cause?
Large STR expansions may become pathogenic, underpinning various forms of primary neurological disease. There are currently 47 known STR genes that can cause disease when expanded. 37 of these exhibit primary neurological presentations while 10 present with development abnormalities. Furthermore, STR expansions have been linked to complex polygenic diseases such as heart disease, bipolar disoder, major depressive disorder and schizophrenia [^chintalaphani_update_2021].

For example:
- RFC1 could lead to Frontotemporal dementia and Amyotrophic lateral sclerosis.
- DMPK could lead to Myotonic dystrophy 1.
- CNBP (ZNF9) could lead to Myotonic dystrophy 2.
- Etc.

## Conventional approach to diagnosis STRs.
The established approach for molecular diagnosis of repeat expansion diseases involves genotyping STRs bt repeat-primed precise PCR (RP-PCR) and/or Southern blot assays for sizing large expansions [^chintalaphani_update_2021].

<center><img src="https://media.springernature.com/full/springer-static/image/art%3A10.1186%2Fs40478-021-01201-x/MediaObjects/40478_2021_1201_Fig3_HTML.png?as=webp"></center>
<center><p style="font-size:12px; color:grey">Current molecular diagnostic methods. Flow chart shows an example of two current diagnostic methods for diagnosing STR expansions: Southern blot and repeat-primed PCR. The sample analysis shown in both diagnostic methods was taken from a patient with Friedrich’s ataxia with a heterozygous ‘GAA’ expansion in the FXN gene (approximately 90 and 900 repeats). The RP-PCR graph shows the characteristic tailing/stuttering pattern of expanded alleles caused by the repeat-primed probes binding to more sites within the STR expansion. For sizing, Southern blot is performed. The larger 900-repeat ‘GAA’ allele cannot be seen using the Southern blot sizing ladder shown above  [^chintalaphani_update_2021]</p></center>

Limitation: As the phenotype of repeat expansion diseases are heterogeneous and overlapped between different disorders, the clinician must decide which STRs warrant testing for patients. Moreover, since both methods require separate primers/probes for each STR, parallel analysis of multiple candidates in single assay in not possible [^chintalaphani_update_2021].

## NGS in STR detection
STR expansions can be detected across the entire genome, using established short-read NGS platform and a growing number of bioinformatics tools. Such as ExpansionHunter, LobSTR, RepeatSeq, HipSTR and GangSTR [^chintalaphani_update_2021].

The major advantage of whole-genome sequencing is that, in theory, all STRs in the genome are profiled simutaneously, as well as STR contraction and non-STR mutations, which may also be implicated in disease [^chintalaphani_update_2021].

## NGS Calling of STR
- Expansion Hunter[^dolzhenko_detection_2017]
- LobSTR [^gymrek_lobstr_2012]

Limitations:
- Highly repetive and/or 'GC' rich genome regions are refractory to NGS library preparation, PCR amplification and sequencing , making is difficult to obtain sufficient coverage in many STR regions. PCR amplification during the library preparation can also introduce stutter errors, although this can be alleviated through the use of PCR-free library preparations [^chintalaphani_update_2021].
- The repetitive nature of STR regions can cause ambiguous alignment or misalignment of short NGS reads to the reference genome. More fundamentally, the short read length (~100bp-150bp) of established NGS techonologies is insufficient to span large STR expansions, making it impossible to precisely determine their length [^chintalaphani_update_2021].
- Standard NGS does not detect epigenetic modifications, such as 5-methylcytosine, which are diagnostically important in some cases [^chintalaphani_update_2021].

<center><img src="https://media.springernature.com/full/springer-static/image/art%3A10.1186%2Fs40478-021-01201-x/MediaObjects/40478_2021_1201_Fig4_HTML.png?as=webp"></center>
<center><p style="font-size:12px; color:grey">NGS and Long-read sequencing for diagnosing short tandem repeat expansions. Flow chart shows the use of short-read NGS and two long-read sequencing methods for genotyping STR expansions: PacBio single-molecule real-time (SMRT) sequencing and Oxford Nanopore Technology (ONT) long-read sequencing. The alignment of reads to the genome can be seen for all three methods; short-reads are ‘tiled’ together to estimate the repeat size and sequence, while long reads easily span repeat and flanking regions. Nanopore sequencing high error rates can be overcome via sufficient coverage [^chintalaphani_update_2021]</p></center>

# References:
[^chintalaphani_update_2021]: Chintalaphani, S. R., Pineda, S. S., Deveson, I. W., & Kumar, K. R. (2021). An update on the neurological short tandem repeat expansion disorders and the emergence of long-read sequencing diagnostics. Acta Neuropathologica Communications, 9(1), 98. https://doi.org/10.1186/s40478-021-01201-x

[^chintalaphani_update_2021]: Chintalaphani, S. R., Pineda, S. S., Deveson, I. W., & Kumar, K. R. (2021). An update on the neurological short tandem repeat expansion disorders and the emergence of long-read sequencing diagnostics. Acta Neuropathologica Communications, 9(1), 98. https://doi.org/10.1186/s40478-021-01201-x

[^dolzhenko_detection_2017]: Dolzhenko, E., van Vugt, J. J. F. A., Shaw, R. J., Bekritsky, M. A., van Blitterswijk, M., Narzisi, G., Ajay, S. S., Rajan, V., Lajoie, B. R., Johnson, N. H., Kingsbury, Z., Humphray, S. J., Schellevis, R. D., Brands, W. J., Baker, M., Rademakers, R., Kooyman, M., Tazelaar, G. H. P., van Es, M. A., … Eberle, M. A. (2017). Detection of long repeat expansions from PCR-free whole-genome sequence data. Genome Research, 27(11), 1895–1903. https://doi.org/10.1101/gr.225672.117

[^gymrek_lobstr_2012]: Gymrek, M., Golan, D., Rosset, S., & Erlich, Y. (2012). lobSTR: A short tandem repeat profiler for personal genomes. Genome Research, 22(6), 1154–1162. https://doi.org/10.1101/gr.135780.111

