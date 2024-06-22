import os
import subprocess

def call_peaks(bam_file, output_dir, sample_name):
    macs2_cmd = f"macs2 callpeak -t {bam_file} -f BAM -n {sample_name} --outdir {output_dir}"
    subprocess.run(macs2_cmd, shell=True)

if __name__ == "__main__":
    input_dir = "../data/preprocessed"
    output_dir = "../data/peaks"
    
    for bam_file in os.listdir(input_dir):
        if bam_file.endswith("_sorted.bam"):
            sample_name = bam_file.split("_")[0]
            call_peaks(os.path.join(input_dir, bam_file), output_dir, sample_name)
