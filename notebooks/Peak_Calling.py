# Peak_Calling.ipynb

from src.peak_calling import call_peaks

# Define paths
input_dir = "../data/preprocessed"
output_dir = "../data/peaks"

# Call peaks
for bam_file in os.listdir(input_dir):
    if bam_file.endswith("_sorted.bam"):
        sample_name = bam_file.split("_")[0]
        call_peaks(os.path.join(input_dir, bam_file), output_dir, sample_name)
