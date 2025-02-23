# TextNGramAnalyzer

A Python tool for analyzing text data through n-gram frequency analysis, demonstrating advanced text processing and statistical analysis capabilities.

## Overview
TextNGramAnalyzer processes text documents to identify and analyze patterns in language usage through unigrams, bigrams, and trigrams. The tool showcases Python's powerful text processing and data analysis capabilities by implementing efficient dictionary-based frequency analysis.

## Key Features
- Multi-level n-gram analysis (unigrams, bigrams, trigrams)
- Intelligent text preprocessing
- Frequency calculation and statistical analysis 
- Modular design with separate concerns
- Comprehensive test coverage

## Components
- `NgramFrequencies`: Core class for n-gram processing
  - Frequency counting
  - Statistical analysis
  - Sorted frequency reporting
  
- `TextCleaner`: Text preprocessing module
  - Case normalization
  - Punctuation handling
  - Sentence boundary detection
  - Special token processing (e.g., abbreviations)

## Technical Capabilities
- Dictionary-based data structures for efficient counting
- Custom sorting algorithms for frequency analysis
- Unit testing infrastructure
- Modular object-oriented design

## Usage
```bash
python ngrams.py input_text.txt
```

## Output Format
Displays top 10 frequencies for:
- Unigrams (single words)
- Bigrams (word pairs)
- Trigrams (word triples)

Each n-gram is shown with its normalized frequency value.

## Project Structure
```
ngrams/
├── ngrams.py
├── frequencies_test.py
├── text_cleaner_test.py
├── ngram_frequencies.py
└── text_cleaner.py
```

## Skills Demonstrated
- Advanced text processing
- Statistical analysis
- Object-oriented programming
- Test-driven development
- Data structure optimization