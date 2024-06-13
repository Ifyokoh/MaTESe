from datasets import load_dataset
import os

def save_samples_to_files(dataset, num_samples_per_lp=10):
    # Create text files if they do not exist
    files = {
        "src": "sources.txt",
        "mt": "candidates.txt",
        "ref": "references.txt",
        "annotations": "annotations.txt",
        "lp": "language_pairs.txt"
    }
    file_handles = {key: open(filename, 'a') for key, filename in files.items()}

    # Get unique language pairs
    language_pairs = set(dataset['lp'])
    
    # Process each language pair
    for lp in language_pairs:
        # Filter dataset by language pair
        filtered_dataset = dataset.filter(lambda example: example['lp'] == lp)
        # Take up to num_samples_per_lp samples
        samples = filtered_dataset.select(range(min(num_samples_per_lp, len(filtered_dataset))))

        # Write each sample to the respective files
        for sample in samples:
            file_handles['src'].write(sample['src'] + '\n')
            file_handles['mt'].write(sample['mt'] + '\n')
            file_handles['ref'].write(sample['ref'] + '\n')
            file_handles['annotations'].write(str(sample['annotations']) + '\n')
            file_handles['lp'].write(sample['lp'] + '\n')

    # Close all file handles
    for handle in file_handles.values():
        handle.close()

if __name__ == "__main__":
    dataset = load_dataset("RicardoRei/wmt-mqm-error-spans", split="train")
    save_samples_to_files(dataset)
