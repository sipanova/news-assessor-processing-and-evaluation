# news-assessor-processing-and-evaluation
The project consist of all the python scripts that pre-process, post-process the input and output of the LLMs besides the evaluation scripts.

## Requirements
- Python 3.9+
- An IDE like VSCode

After generating the output files for the models (e.g. GPT-4o and Mistral-7b-instruct), those secrips are for generating the metric based on the referace file which is attached stored in the file "data/valid_test_final_file.csv"

To calculate validity, accuracy, precision, and recall, we have to excuate multiple jupyter cells in the file "output_validity_script.ipynb"
Comments are made in the cells for understanding.
