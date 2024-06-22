# Differential_Peak_Analysis.ipynb

from src.differential_analysis import load_peaks, find_differential_peaks

# Define paths
peak_files = ["../data/peaks/sample1_peaks.narrowPeak", "../data/peaks/sample2_peaks.narrowPeak"]

# Load peaks
peaks = load_peaks(peak_files)

# Find differential peaks
common_peaks, specific_peaks_1, specific_peaks_2 = find_differential_peaks(peaks)

# Save results
common_peaks.saveas("../data/peaks/common_peaks.bed")
specific_peaks_1.saveas("../data/peaks/specific_peaks_sample1.bed")
specific_peaks_2.saveas("../data/peaks/specific_peaks_sample2.bed")
