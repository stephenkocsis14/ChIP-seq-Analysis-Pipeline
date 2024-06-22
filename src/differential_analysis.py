import pandas as pd
from pybedtools import BedTool

def load_peaks(peak_files):
    peaks = [BedTool(file) for file in peak_files]
    return peaks

def find_differential_peaks(peaks):
    common_peaks = peaks[0].intersect(peaks[1], u=True)
    specific_peaks_1 = peaks[0].subtract(peaks[1])
    specific_peaks_2 = peaks[1].subtract(peaks[0])
    
    return common_peaks, specific_peaks_1, specific_peaks_2

if __name__ == "__main__":
    peak_files = ["../data/peaks/sample1_peaks.narrowPeak", "../data/peaks/sample2_peaks.narrowPeak"]
    peaks = load_peaks(peak_files)
    
    common_peaks, specific_peaks_1, specific_peaks_2 = find_differential_peaks(peaks)
    
    common_peaks.saveas("../data/peaks/common_peaks.bed")
    specific_peaks_1.saveas("../data/peaks/specific_peaks_sample1.bed")
    specific_peaks_2.saveas("../data/peaks/specific_peaks_sample2.bed")
