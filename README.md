# ChIP-seq Data Analysis

## Project Overview

This project demonstrates a complete pipeline for ChIP-seq data analysis from raw FASTQ files to peak calling and differential peak analysis. The project uses tools like FastQC, BWA, SAMtools, MACS2, and PyBedTools to perform various steps of the analysis.

## Project Structure

- `data/`: Directory for storing data files.
- `notebooks/`: Jupyter notebooks for data preprocessing, peak calling, and differential peak analysis.
- `src/`: Source code for data preprocessing, peak calling, and differential analysis.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `README.md`: Project documentation.
- `requirements.txt`: List of Python dependencies.

## Getting Started

### Prerequisites

- Python 3.x
- Virtual environment (optional but recommended)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ChIPseq_Analysis.git
    cd ChIPseq_Analysis
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Preprocess the data:
    ```bash
    python src/preprocessing.py
    ```

2. Call peaks:
    ```bash
    python src/peak_calling.py
    ```

3. Perform differential peak analysis:
    ```bash
    python src/differential_analysis.py
    ```

4. Explore the Jupyter notebooks in the `notebooks/` directory for more details on each step of the analysis.

## License

This project is licensed under the MIT License.
