# Script: split_child_forms.py
# Purpose: This script automates the splitting of a single multi-page intake PDF
#          into individual forms based on known page numbers. Each child's forms
#          are saved in a uniquely named folder.

import os
from PyPDF2 import PdfReader, PdfWriter

# Define which pages belong to which form.
# The keys are form titles; the values are lists of page indexes (starting from 0).
form_map = {
    "MEDIA RELEASE AND CONSENT FOR MINORS": [0],
    "PLACEMENT AGREEMENT": [1, 2, 3],
    "BEHAVIOR MANAGEMENT PRACTICE AND POLICY": [4, 5],
    "MEDICAL CONSENT": [6],
    "MEDICATION CONSENT": [7],
    "OTHER CONSENTS": [8, 9],
}

# Define the input folder where original PDFs are stored
input_folder = r"C:\Users\NicoleGilbert\Documents\input_forms"

# Define the output folder where split PDFs will be saved
output_folder = r"C:\Users\NicoleGilbert\Documents\output_forms"
os.makedirs(output_folder, exist_ok=True)  # Create it if it doesn't exist

# Loop through all PDF files in the input folder
for file in os.listdir(input_folder):
    if file.endswith(".pdf"):
        input_path = os.path.join(input_folder, file)
        reader = PdfReader(input_path)

        # Get the child’s name from the file name (everything before the first dot)
        child_name_raw = file.split(".")[0]
        child_name = " ".join(word.capitalize() for word in child_name_raw.split())

        # Create a folder for this child's forms
        child_output_folder = os.path.join(output_folder, child_name)

        # Skip this file if already processed
        if os.path.exists(child_output_folder):
            print(f"Skipping {child_name}, already processed.")
            continue

        os.makedirs(child_output_folder, exist_ok=True)

        # Split and save each form into its own PDF
        for form_title, pages in form_map.items():
            writer = PdfWriter()

            for page_num in pages:
                # Avoid adding non-existent pages
                if page_num < len(reader.pages):
                    writer.add_page(reader.pages[page_num])

            # Build the output filename and path
            output_filename = f"{child_name}.{form_title}.pdf"
            output_path = os.path.join(child_output_folder, output_filename)

            # Write the new split PDF file
            with open(output_path, "wb") as out_file:
                writer.write(out_file)

        print(f"Processed: {child_name}")

print("All PDFs have been processed and saved into child-specific folders.")
