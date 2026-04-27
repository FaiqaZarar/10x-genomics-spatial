# Assignment #2 — Genetic Disorders & Rare Diseases: Variant Analysis

## Objective
Analyze three genetic disorders and rare diseases by identifying their most relevant pathogenic variants using bioinformatics databases including ClinVar, OMIM, UCSC Genome Browser, and Ensembl VEP.

---

## Diseases Selected

| # | Disease | Type | Gene | Variant |
|---|---------|------|------|---------|
| 1 | Cystic Fibrosis | Genetic Disorder | CFTR | NM_000492.4(CFTR):c.1521_1523delCTT (p.Phe508del) |
| 2 | Sickle Cell Anemia | Genetic Disorder | HBB | NM_000518.5(HBB):c.20A>T (p.Glu7Val) |
| 3 | Huntington's Disease | Rare Disease | HTT | NM_002111.8(HTT):c.53CAG[>35] (CAG Repeat Expansion) |

---

## Tools & Databases Used

- **ClinVar** — https://www.ncbi.nlm.nih.gov/clinvar/
- **OMIM** — https://www.omim.org
- **UCSC Genome Browser** — https://genome.ucsc.edu
- **Ensembl VEP** — https://asia.ensembl.org/Tools/VEP
- **GitHub** — https://github.com

---

## Steps to Reproduce

### Step 1 — ClinVar Variant Search
1. Go to https://www.ncbi.nlm.nih.gov/clinvar/
2. Search each disease name (e.g., "Cystic Fibrosis")
3. Filter by **Pathogenic** clinical significance
4. Select the most relevant variant record
5. Record: Gene, Variant ID, Chromosome position, Clinical significance, HGVS name

### Step 2 — Read Studies (Explanation Field)
1. On the ClinVar variant page scroll to **Submissions** and **Publications**
2. Read clinical observations and research summaries
3. Summarize findings in the explanation field of the Excel sheet

### Step 3 — OMIM Phenotype
1. Go to https://www.omim.org
2. Search the gene name (e.g., CFTR, HBB, HTT)
3. Navigate to **Clinical Features** section
4. Copy phenotype description into the Excel sheet

### Step 4 — UCSC Genome Browser (AlphaMissense & REVEL)
1. Go to https://genome.ucsc.edu
2. Enter chromosome position:
   - Cystic Fibrosis: `chr7:117,548,620-117,548,650`
   - Sickle Cell Anemia: `chr11:5,226,925-5,227,100`
   - Huntington's Disease: `chr4:3,074,677-3,074,920`
3. Scroll down to **Phenotypes, Variants, and Literature** section
4. Set **AlphaMissense** to "full" → Refresh
5. Set **REVEL Scores** to "full" → Refresh
6. Screenshot and paste into Excel

### Step 5 — ACMG/AMP Classification
1. Review ClinVar submissions for criteria codes
2. Apply ACMG/AMP 2015 guidelines (Richards et al.)
3. Record classification and criteria met

### Step 6 — VCF File Creation
```
##fileformat=VCFv4.2
##reference=GRCh38/hg38
#CHROM  POS         ID           REF  ALT       QUAL  FILTER  INFO
7       117548628   rs113993960  CTT  .         .     PASS    GENE=CFTR;DISEASE=Cystic_Fibrosis
11      5227002     rs334        A    T         .     PASS    GENE=HBB;DISEASE=Sickle_Cell_Anemia
4       3074877     rs193922927  CAG  CAGCAGCAG .     PASS    GENE=HTT;DISEASE=Huntingtons_Disease
```

### Step 7 — VCF Annotation using Ensembl VEP
1. Go to https://asia.ensembl.org/Tools/VEP
2. Select Species: **Homo sapiens**, Assembly: **GRCh38**
3. Upload `variants.vcf`
4. Click **Run** and view annotated results

---

## Files in This Repository

| File | Description |
|------|-------------|
| `Assignment2.xlsx` | Main Excel sheet with all variant data, explanations, phenotypes, screenshots, and ACMG classifications |
| `variants.vcf` | VCF file with all 3 pathogenic variants in VCFv4.2 format |
| `README.md` | Full documentation and reproduction steps |

---

## Key Findings Summary

### Cystic Fibrosis — CFTR F508del
- Most common CF mutation (~70% of alleles worldwide)
- Causes misfolding and degradation of CFTR protein
- **ACMG: Pathogenic** (PVS1, PS3, PP5, PM3)
- Position: chr7:117,548,628 (GRCh38)

### Sickle Cell Anemia — HBB Glu7Val
- Single nucleotide change causes HbS polymerization
- Protective against malaria in heterozygotes
- **ACMG: Pathogenic** (PS1, PS3, PS4, PM1, PP5)
- Position: chr11:5,227,002 (GRCh38)

### Huntington's Disease — HTT CAG Repeat Expansion
- ≥40 CAG repeats cause full-penetrance neurodegeneration
- Autosomal dominant with anticipation
- **ACMG: Pathogenic** (PVS1, PS4, PS3, PP1, PP5)
- Position: chr4:3,074,877 (GRCh38)

---

## References
- Richards et al. 2015 — ACMG/AMP variant interpretation guidelines (Genet Med)
- Riordan et al. 1989 — CFTR gene identification (Science)
- Ingram 1956 — Sickle cell hemoglobin (Nature)
- The HD Collaborative Research Group 1993 — HTT gene (Cell)
