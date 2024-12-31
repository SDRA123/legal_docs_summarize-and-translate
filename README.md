# Legal Document Summarization and Translation
# Project Overview
This project aims to summarize legal documents and translate the summaries into Urdu. The solution employs Python scripts to:

Perform Optical Character Recognition (OCR) on scanned legal documents to extract text.
Summarize the extracted text.
Translate the summary from English to Urdu.
Additionally, the project provides two modes of execution:

## Serial Execution: The scripts run one after another.
## Parallel Execution: The scripts run concurrently to optimize execution time.
Project Features
Summarization: Uses advanced algorithms to extract the most important points from legal documents.
Translation: Translates the summarized content into Urdu for easier comprehension.
Execution Modes: Includes both serial and parallel execution methods for benchmarking and optimizing performance.
# File Descriptions
1. test2.py
This script handles the process of summarizing individual pages of legal documents using a text extraction and summarization algorithm. It processes each page and stores the results as a text file.

2. translate.py
This script takes the summarized text from test2.py and translates it from English into Urdu using a translation API or library.

3. processor.py
This file contains the logic to run the project in both serial and parallel modes. It benchmarks the execution time for both modes and prints the results.

Serial Execution: The scripts (test2.py and translate.py) are run one after the other, which can take more time.
Parallel Execution: The scripts are executed concurrently, reducing the overall execution time.
Setup
# To run the project locally, follow these steps:

# 1. Clone the repository
bash
Copy code
git clone https://github.com/yourusername/legal-docs-summarize-translate.git
cd legal-docs-summarize-translate
2. Install dependencies
Make sure you have Python 3.x installed. Install the required libraries using pip:

# To Run
python processor.py 

# Results
Serial execution total time: 27.10 seconds

Parallel execution total time: 14.20 seconds

![image](https://github.com/user-attachments/assets/aa3317bc-fbf5-473a-bee3-ef71c9fe213d)

