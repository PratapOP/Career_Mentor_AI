"""
Placeholder fine-tuning script for Career Mentor AI.

This script describes where a fine-tuning workflow would be integrated and prints example dataset entries.
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / 'dataset.json'


def main():
    if not DATA_FILE.exists():
        print(f'No dataset file found at {DATA_FILE}. Create one before fine-tuning.')
        return

    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        dataset = json.load(file)

    print('Dataset loaded successfully.')
    print('Example dataset entries:')
    for item in dataset[:2]:
        print('-', item.get('input', 'N/A'))
    print('\nThis script does not perform actual model training by default.')
    print('Use this file as a starting point to add your own fine-tuning pipeline.')


if __name__ == '__main__':
    main()
