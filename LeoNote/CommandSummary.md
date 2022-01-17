# Bash command daily usage
## bam convert to fastq
### 1. save fastq reads in separate R1 and R2 files ([samtools fasta](http://www.htslib.org/doc/samtools-fasta.html))
```Bash
samtools fastq -@ 8 SAMPLE_sorted.bam \
    -1 SAMPLE_R1.fastq.gz \
    -2 SAMPLE_R2.fastq.gz \
    -0 /dev/null -s /dev/null -n
```
### 2. save fastq read in same fastq file. ([samtools](http://www.htslib.org/doc/samtools.html))
```Bash
samtools bam2fq SAMPLE.bam > SAMPLE.fastq
```
### 3. split a single fastq file of paired-end reads into two separated files
```Bash
cat SAMPLE.fastq | grep '^@.*/1$' -A 3 --no-group-separator > SAMPLE_r1.fastq
cat SAMPLE.fastq | grep '^@.*/2$' -A 3 --no-group-separator > SAMPLE_r2.fastq
```

## bwa align single fastq file into sam
### 1.single fastq file
```bash
bwa mem -R "@RG\tID:${sample_ID}\tSM:${sample_ID}" ref.fa reads.fq > aln-se.sam
```
### 2.two fastq files
```Bash
bwa mem -R "@RG\tID:${sample_ID}\tSM:${sample_ID}" ref.fa read1.fq read2.fq > aln-pe.sam
```

## Samtools
### 1.sort
```Bash
samtools sort -o out.bam -O format -@ threads [in.sam|in.bam|in.cram]
```
**-O FORMAT:** Write the final output as sam, bam, or cram.
By default, samtools tries to select a format based on the -o filename extension; if output is to standard output or no format can be deduced, bam is selected.
### 2.extract chr
```Bash
samtools view -b in.bam chr1 > chr1.bam
```

## Bcftools
### 1.merge [bcftools merge link](https://samtools.github.io/bcftools/bcftools.html#merge)
**bcftools merge [OPTIONS] A.vcf.gz B.vcf.gz […]**

Example:
```Bash
bcftools merge A.vcf.gz B.vcf.gz -Oz -o merged.vcf.gz
```