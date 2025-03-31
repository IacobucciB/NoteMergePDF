from PyPDF2 import PdfMerger
import logging

def merge_pdfs(pdf_files, output_filename="out.pdf"):
    if not pdf_files:
        logging.error("No PDF files provided for merging.")
        return None
    merger = PdfMerger()
    try:
        for pdf in pdf_files:
            merger.append(pdf)
            logging.info(f"Added {pdf} to the merger.")
        merger.write(output_filename)
        logging.info(f"Merged PDF saved as {output_filename}.")
        return output_filename
    except Exception as e:
        logging.error(f"An error occurred while merging PDFs: {e}")
        return None
    finally:
        merger.close()