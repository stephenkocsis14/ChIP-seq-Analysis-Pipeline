import os
import subprocess

def run_fastqc(input_dir, output_dir):
    fastqc_cmd = f"fastqc {input_dir}/*.fastq -o {output_dir}"
    subprocess.run(fastqc_cmd, shell=True)

def run_bwa_alignment(fastq_file, reference_genome, output_file):
    bwa_cmd = f"bwa mem {reference_genome} {fastq_file} > {output_file}"
    subprocess.run(bwa_cmd, shell=True)

def convert_sam_to_bam(sam_file, bam_file):
    samtools_view_cmd = f"samtools view -Sb {sam_file} > {bam_file}"
    subprocess.run(samtools_view_cmd, shell=True)

def sort_bam_file(bam_file, sorted_bam_file):
    samtools_sort_cmd = f"samtools sort {bam_file} -o {sorted_bam_file}"
    subprocess.run(samtools_sort_cmd, shell=True)

if __name__ == "__main__":
    raw_fastq_dir = "../data/raw_fastq"
    output_dir = "../data/preprocessed"
    reference_genome = "../data/reference_genome/genome.fa"
    
    run_fastqc(raw_fastq_dir, output_dir)
    
    for fastq_file in os.listdir(raw_fastq_dir):
        if fastq_file.endswith(".fastq"):
            sample_name = fastq_file.split(".")[0]
            sam_file = os.path.join(output_dir, f"{sample_name}.sam")
            bam_file = os.path.join(output_dir, f"{sample_name}.bam")
            sorted_bam_file = os.path.join(output_dir, f"{sample_name}_sorted.bam")
            
            run_bwa_alignment(os.path.join(raw_fastq_dir, fastq_file), reference_genome, sam_file)
            convert_sam_to_bam(sam_file, bam_file)
            sort_bam_file(bam_file, sorted_bam_file)
