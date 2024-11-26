import jiwer

# Define the file paths
reference_file_path = 'transcript.txt'
hypothesis_file_path = 'test.txt'

# Function to read and clean sentences from a file
def read_sentences(file_path):
    with open(file_path, 'r') as file:
        # Read lines, strip whitespace, and filter out empty lines
        return [line.strip() for line in file.readlines() if line.strip()]

# Read the reference and hypothesis sentences
reference_sentences = read_sentences(reference_file_path)
hypothesis_sentences = read_sentences(hypothesis_file_path)

# Check if either list is empty and handle accordingly
if not reference_sentences:
    raise ValueError("The reference sentences list is empty. Please check transcript.txt.")
if not hypothesis_sentences:
    raise ValueError("The hypothesis sentences list is empty. Please check test.txt.")

# Calculate WER
wer_result = jiwer.wer(reference_sentences, hypothesis_sentences)

# Print the WER result
print(f'Word Error Rate (WER): {wer_result:.2%}')