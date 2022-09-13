import sys
import subprocess

xml = str(sys.argv[1])
samples = str(sys.argv[2])

base_name = 'https://genome.jgi.doe.gov'
sample_dict = {}
url_dict = {}

with open(samples, "r") as sample_file:
    for row in sample_file:
        row =row.strip().split()
        library = row[-1]
        sample_id = row[2]
        sample_dict[library] = sample_id

with open(xml, "r") as xml_file:
    for row in xml_file:
        row = row.split()
        library = row[19].split("=")
        library = library[1][1:].strip('"')
        url = row[17][5:].strip('"')
        url_dict[library] = url

for library in sample_dict:
    url = url_dict[library]
    url = url.split("amp;")
    url = url[0]+url[1]
    sample_id = sample_dict[library]
    sub_script = "Y_" + sample_id + "_download_reads.sh"
    with open(sub_script, "w") as script:
        script.writelines(

"#!/bin/bash\n\
#SBATCH --job-name=%s_download\n\
#SBATCH --partition=batch\n\
#SBATCH --ntasks=1\n\
#SBATCH --nodes=1\n\
#SBATCH --cpus-per-task=1\n\
#SBATCH --mem=20gb\n\
#SBATCH --time=2:00:00\n\
#SBATCH --output=%s_download.out\n\
#SBATCH --error=%s_download.err\n\
\n\
cd $SLURM_SUBMIT_DIR\n\
\n\
curl 'https://signon.jgi.doe.gov/signon/create' --data-urlencode 'login=richard.field@uga.edu' --data-urlencode 'password=Diztor10' -c cookies > /dev/null\n\
curl 'https://genome.jgi.doe.gov%s' -b cookies > Y_%s_%s.fasta.gz" % (sample_id, sample_id, sample_id, url, sample_id, library))
    cmd = str("sbatch " + sub_script)
    subprocess.run(cmd, shell=True)

#curl 'https://genome.jgi.doe.gov/portal/ext-api/downloads/get_tape_file?blocking=true&url=/YucfilEProfiling_4/download/_JAMO/627f3b78c2c506c5afe34156/52691.4.420703.TTGGACGT-TTGGACGT.filter-RNA.fastq.gz' -b cookies > YF_91_test.fasta.gz
