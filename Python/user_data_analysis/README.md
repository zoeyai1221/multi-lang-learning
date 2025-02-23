# UserAnalytics

A Python-based data analysis tool that processes user data to extract insights about language preferences and geographical distribution through email domain analysis.

## Overview
UserAnalytics demonstrates powerful data processing capabilities in Python, focusing on analyzing CSV data to generate statistical reports about user demographics. The tool specifically tracks:
- Language distribution among users
- Geographical distribution through email top-level domain analysis

## Key Features
- CSV data processing
- Dictionary-based data aggregation
- Regular expression pattern matching for email domain analysis
- Frequency calculation and statistical reporting
- Sorted output of results by frequency

## Technical Stack
- Python 3.x
- Regular Expressions (re module)
- CSV file handling
- Dictionary data structures

## File Structure
- `users.csv`: Input data file containing user information
- `data_analysis.py`: Core analysis implementation
- `report.py`: Report generation script

## Usage
```bash
python report.py users.csv
```

## Output Format
The tool generates a formatted report showing:
- Language distribution frequencies
- Top-level domain distribution frequencies

Each metric is sorted by frequency in descending order with normalized values.

## Skills Demonstrated
- Data parsing and cleaning
- Statistical analysis
- Pattern matching
- File I/O operations
- Data structure manipulation