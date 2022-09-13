#!/bin/bash
#SBATCH --job-name=yfil_index
#SBATCH --partition=batch
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=50gb
#SBATCH --time=12:00:00
#SBATCH --output=yfil_index.out
#SBATCH --error=yfil_index.err

cd $SLURM_SUBMIT_DIR

ml kallisto/0.46.1-foss-2019b

kallisto index -i /home/rdf85141/genomes/Yalo/YaloifoliaYa24Inokov2.1.primaryTrs.idx \
/home/rdf85141/genomes/Yfil/Yalo/YaloifoliaYa24Inokov2.1.primaryTrs.fasta
