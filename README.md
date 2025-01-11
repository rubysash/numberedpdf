# PDF Page Numbering Tool

A Python script that adds page numbers to PDF files. The script can process single PDFs, multiple PDFs individually, or combine multiple PDFs into a single numbered document.

## Features

- Add page numbers to a single PDF file
- Process multiple PDF files in a directory individually
- Combine multiple PDFs and add page numbers to the combined document
- Page numbers are displayed in a hot pink background rectangle for readability
- Numbers are centered within the rectangle
- Output files preserve original files by creating new ones with '-n' suffix

## Installation

### Setting up a Virtual Environment

It's recommended to use a virtual environment to avoid conflicts with other Python packages. Here's how to set it up:

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

The main requirement is PyMuPDF, but using the requirements.txt file will ensure all dependencies are properly installed.

## Usage

The script can be run in several ways depending on your needs:

```bash
python add_page_numbers.py [-s] [-a] [-h] [<input_pdf_path>]
```

### Arguments

- `-s` Stitch all matching PDF files together, then add page numbers and export as a single file
- `-a` Process all PDF files in the current directory individually (adds page numbers to each)
- `-h` Display the help message
- `<input_pdf_path>` (Optional) Path to the input PDF file. If provided, only this file will be processed

### Examples

1. Add page numbers to a single PDF file:
   ```bash
   python add_page_numbers.py document.pdf
   ```
   Creates: `document-n.pdf`

2. Add page numbers to all PDF files in current directory:
   ```bash
   python add_page_numbers.py -a
   ```
   Creates: `doc1-n.pdf`, `doc2-n.pdf`, etc.

3. Combine all PDFs and add page numbers:
   ```bash
   python add_page_numbers.py -s
   ```
   Creates: `stitched_20250111123456-n.pdf`

4. Display help message:
   ```bash
   python add_page_numbers.py -h
   ```

## Output File Naming

- For individual files: The output file will be named the same as the input file with '-n' appended before the file extension
  - Example: `document.pdf` → `document-n.pdf`
- For stitched files: The output file will be named with a timestamp
  - Example: `stitched_20250111123456-n.pdf`

## Page Number Format

- Location: Bottom right corner of each page
- Background: Hot pink rectangle for visibility
- Text: Black numbers, centered in the rectangle
- Font: Helvetica, 12pt

## Error Handling

The script includes error handling for:
- File not found
- Invalid file paths
- Missing input arguments

## Notes

- Original PDF files are never modified
- Files ending in '-n.pdf' are skipped when using the -a option to prevent processing already numbered files
- When using -s (stitch) option, temporary files are automatically cleaned up

## License

MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contributing

Feel free to submit issues and enhancement requests!
