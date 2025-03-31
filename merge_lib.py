from PyPDF2 import PdfMerger, PdfReader, PdfWriter
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

def get_pdf_page_counts(pdf_files):
    result = []
    for pdf in pdf_files:
        try:
            reader = PdfReader(pdf)
            num_pages = len(reader.pages)
            result.append((pdf, num_pages))
            logging.info(f"{pdf} has {num_pages} pages.")
        except Exception as e:
            logging.error(f"Failed to read {pdf}: {e}")
    return result

def merge_selected_pages(selected_pages, output_filename="merged_pages.pdf"):
    writer = PdfWriter()
    try:
        for page_info in selected_pages:
            file_name, page_str = page_info.rsplit(" - Page ", 1)
            page_number = int(page_str) - 1
            reader = PdfReader(file_name)
            writer.add_page(reader.pages[page_number])
            logging.info(f"Added {file_name} - Page {page_number + 1} to the writer.")
        
        with open(output_filename, "wb") as output_file:
            writer.write(output_file)
        logging.info(f"Merged pages saved as {output_filename}.")
        return output_filename
    except Exception as e:
        logging.error(f"An error occurred while merging selected pages: {e}")
        return None