import fitz  # PyMuPDF
import sys
import os
import glob
from datetime import datetime

def add_page_numbers(input_pdf_path, output_pdf_path):
    # Open the PDF file
    doc = fitz.open(input_pdf_path)
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        # Define the position for the page number
        rect = fitz.Rect(page.rect.width - 70, page.rect.height - 50, page.rect.width - 30, page.rect.height - 30)
        # Draw a hot pink rectangle to ensure the number is readable
        page.draw_rect(rect, color=(1, 0.41, 0.71), fill=1)
        
        # Center the text within the rectangle
        text = str(page_num + 1)
        # Calculate the center of the rectangle
        text_width = fitz.get_text_length(text, fontsize=12)
        text_height = 12  # Approximate height for fontsize=12
        center_x = rect.x0 + (rect.width - text_width) / 2
        center_y = rect.y0 + (rect.height - text_height) / 2 + text_height  # Adjust for baseline
        
        # Add the page number text
        page.insert_text((center_x, center_y), text, fontsize=12, fontname="helv", color=(0, 0, 0))

    # Save the modified PDF to a new file
    doc.save(output_pdf_path)

def print_help():
    help_message = """
    Usage: python add_page_numbers.py [-s] [-a] [-h] [<input_pdf_path>]
    This script adds page numbers to PDF files.

    Arguments:
    -s               Stitch all matching PDF files together, then add page numbers and export as a single file.
    -a               Process all PDF files in the current directory individually (adds page numbers to each).
    -h               Display this help message.
    <input_pdf_path> (Optional) Path to the input PDF file. If provided, only this file will be processed.

    The output file for individual processing will be named the same as the input file with '-n' appended before the file extension.
    For example, if the input file is 'somefile.pdf', the output file will be 'somefile-n.pdf'.

    The output file for stitching will be named with the current timestamp.

    Examples:
    # Add page numbers to a single PDF file:
    python add_page_numbers.py document.pdf
    -> Creates: document-n.pdf

    # Add page numbers to all PDF files in current directory:
    python add_page_numbers.py -a
    -> Creates: doc1-n.pdf, doc2-n.pdf, etc.

    # Combine all PDFs and add page numbers:
    python add_page_numbers.py -s
    -> Creates: stitched_20250111123456-n.pdf

    # Display this help message:
    python add_page_numbers.py -h
    """
    print(help_message)

def process_all_pdfs():
    for input_pdf_path in glob.glob("*.pdf"):
        if not input_pdf_path.endswith("-n.pdf"):
            file_name, file_extension = os.path.splitext(input_pdf_path)
            output_pdf_path = f"{file_name}-n{file_extension}"
            add_page_numbers(input_pdf_path, output_pdf_path)
            print(f"Page numbers added. Output file saved as '{output_pdf_path}'")

def stitch_and_process_pdfs():
    pdf_files = [f for f in glob.glob("*.pdf") if not f.endswith("-n.pdf")]
    if not pdf_files:
        print("No PDF files to stitch and process.")
        return

    # Create a new document to stitch all PDFs together
    stitched_doc = fitz.open()
    for pdf_file in pdf_files:
        doc = fitz.open(pdf_file)
        for page_num in range(len(doc)):
            stitched_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)
    
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    stitched_output_path = f"stitched_{timestamp}.pdf"
    stitched_doc.save(stitched_output_path)
    stitched_doc.close()
    
    # Add page numbers to the stitched PDF
    output_pdf_path = f"stitched_{timestamp}-n.pdf"
    add_page_numbers(stitched_output_path, output_pdf_path)
    os.remove(stitched_output_path)
    print(f"Stitched and page-numbered PDF saved as '{output_pdf_path}'")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # No arguments provided, show help message
        print_help()
        sys.exit(0)
        
    if len(sys.argv) > 2:
        print_help()
        sys.exit(1)

    if len(sys.argv) == 2:
        if sys.argv[1] == "-h":
            print_help()
        elif sys.argv[1] == "-s":
            stitch_and_process_pdfs()
        elif sys.argv[1] == "-a":
            process_all_pdfs()
        else:
            input_pdf_path = sys.argv[1]
            if not os.path.isfile(input_pdf_path):
                print(f"Error: File '{input_pdf_path}' not found.")
                sys.exit(1)
            
            file_name, file_extension = os.path.splitext(input_pdf_path)
            output_pdf_path = f"{file_name}-n{file_extension}"
            
            add_page_numbers(input_pdf_path, output_pdf_path)
            print(f"Page numbers added. Output file saved as '{output_pdf_path}'")
