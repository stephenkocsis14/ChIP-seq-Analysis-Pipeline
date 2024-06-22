# Data_Preprocessing.ipynb

from src.preprocessing import run_fastqc, run_bwa_alignment, convert_sam_to_bam, sort_bam_file

# Define paths
raw_fastq_dir = "../data/raw_fastq"
output_dir = "../data/preprocessed"
reference_genome = "../data/reference_genome/genome.fa"

# Run FastQC
run_fastqc(raw_fastq_dir, output_dir)

# Align and process sequences
for fastq_file in os.listdir(raw_fastq_dir):
    if fastq_file.endswith(".fastq"):
        sample_name = fastq_file.split(".")[0]
        sam_file = os.path.join(output_dir, f"{sample_name}.sam")
        bam_file = os.path.join(output_dir, f"{sample_name}.bam")
        sorted_bam_file = os.path.join(output_dir, f"{sample_name}_sorted.bam")

        run_bwa_alignment(os.path.join(raw_fastq_dir, fastq_file), reference_genome, sam_file)
        convert_sam_to_bam(sam_file, bam_file)
        sort_bam_file(bam_file, sorted_bam_file)
