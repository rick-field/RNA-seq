#!/bin/bash
#SBATCH --job-name=yfil_quant
#SBATCH --partition=batch
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=50gb
#SBATCH --time=12:00:00
#SBATCH --output=yfil_quant.out
#SBATCH --error=yfil_quant.err

cd $SLURM_SUBMIT_DIR

ml kallisto/0.46.1-foss-2019b

kallisto quant -i /home/rdf85141/genomes/Yfil/YfilamentosaC3.v2.1.prelim.annot/YfilamentosaC3v2.1.primaryTrs.idx \
-b 100 \
/scratch/rdf85141/RNA_analyses/final/data/reads/test/Y_filamentosa_84_4W_NAWWY_R1.fq \
/scratch/rdf85141/RNA_analyses/final/data/reads/test/Y_filamentosa_84_4W_NAWWY_R2.fq \
-o /scratch/rdf85141/RNA_analyses/data/
