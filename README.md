# PDF-Splitter
# 🧾 PDF Intake Splitter for Consent Packets

This Python script automates the process of splitting a signed intake packet (multi-page PDF) into individual form files. It was developed for a nonprofit agency to streamline uploading documentation into Salesforce CRM, but it can be adapted for any organization that collects and processes signed form packets.

## 📘 Background & Purpose

At our agency, parents receive a single electronically signable PDF packet containing multiple required forms (e.g. medical consent, placement agreement, media release). Once completed, these signed packets need to be:

1. Split into individual forms
2. Properly renamed to reflect the child’s name and form title
3. Uploaded into our Salesforce CRM under the correct program enrollment

Manually doing this for every intake packet was time-consuming and prone to error. This script automates that process, cutting down on administrative work and ensuring consistency in file naming and structure.

---

## ✨ Features

- Automatically splits a multi-page signed PDF into individual form documents
- Renames each file with the child’s name and the specific form title
- Organizes outputs into folders by child for ease of upload into CRM
- Reduces manual work and human error

---

## 🔧 Technologies Used

- Python 3
- [PyPDF2](https://pypi.org/project/PyPDF2/) – for PDF reading/writing
- [pycryptodome](https://pypi.org/project/pycryptodome/) – to handle encrypted PDFs (required by some e-signing tools)

---

## 📦 Installation

Make sure you have Python 3 installed, then install the required libraries:

```bash
pip install PyPDF2 pycryptodome


**🚀 How to Use**

1. Place all signed intake PDFs in an input_forms folder. Filenames should begin with the child’s name:
          jane_doe.intake.pdf
          john_smith.intake.pdf

2. Update these paths in the Python script:
input_folder = r"C:\path\to\input_forms"
output_folder = r"C:\path\to\output_forms"

3. Run the script:
python split_child_forms.py

4. Each child’s folder will be created in output_forms/, containing:
/output_forms/
└── Jane Doe/
    ├── Jane Doe.MEDIA RELEASE AND CONSENT FOR MINORS.pdf
    ├── Jane Doe.PLACEMENT AGREEMENT.pdf
    ├── ...

5. These files can now be easily matched to Salesforce records and uploaded accordingly.

**🧠 How It Works**
The script uses a form_map dictionary to define which pages in the packet correspond to which forms. Example:
form_map = {
    "MEDIA RELEASE AND CONSENT FOR MINORS": [0],
    "PLACEMENT AGREEMENT": [1, 2, 3],
    ...
}
This mapping reflects the static layout of the PDF packet. You can easily edit it if your agency changes the packet format in the future.

