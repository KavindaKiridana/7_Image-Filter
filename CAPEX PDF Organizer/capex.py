"""
CAPEX PDF Organizer
Created for organizing IT Requisition PDF files.

Example PDF Names:

IT_Requisition_SWIT_2026_0058.pdf
IT_Requisition_SWIT_2026_0058 (1).pdf

The script:

1. Scans Downloads folder
2. Finds matching IT Requisition PDFs
3. Creates required folder structure
4. Moves/Copies files
5. Optionally removes originals
"""

import os
import re
import shutil

# ----------------------------------------------------------
# COMPANY MAPPING
# ----------------------------------------------------------

COMPANY_MAP = {
    "RAIT": "Renuka Agri Foods",
    "ROIT": "Renuka Agri Organics",
    "SWIT": "Shaw Wallace Ceylon",
    "RLIT": "Richlife Dairies",
    "KPIT": "Kandy Plantations",
    "GFIT": "Galle Face Properties",
    "CLIT": "Coco Lanka",
    "RTIT": "Renuka Teas Ceylon"
}

# ----------------------------------------------------------
# SETTINGS
# ----------------------------------------------------------

PDF_PATTERN = re.compile(
    r"^IT_Requisition_([A-Z]{4})_(\d{4})_(\d{4})(?: \(\d+\))?\.pdf$",
    re.IGNORECASE
)

# ----------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------

def get_downloads_folder():
    return os.path.join(os.path.expanduser("~"), "Downloads")


def get_desktop_folder():
    return os.path.join(os.path.expanduser("~"), "Desktop")


def create_base_folder():
    desktop = get_desktop_folder()

    base_folder = os.path.join(
        desktop,
        "Sankha's Doc",
        "CAPEX & Quotation"
    )

    os.makedirs(base_folder, exist_ok=True)

    return base_folder


def find_existing_company_folder(base_folder, expected_name):
    """
    Reuse an existing company folder if possible.

    Example:
        Expected:
            Shaw Wallace Ceylon

        Existing:
            Shaw Wallace Ceylon Ltd

        Use existing folder.
    """

    expected_words = expected_name.lower().split()

    for folder in os.listdir(base_folder):

        full_path = os.path.join(base_folder, folder)

        if not os.path.isdir(full_path):
            continue

        folder_lower = folder.lower()

        matches = sum(
            1 for word in expected_words
            if word in folder_lower
        )

        if matches >= max(1, len(expected_words) - 1):
            return full_path

    return None


def get_company_folder(base_folder, company_code):

    company_name = COMPANY_MAP.get(company_code)

    if not company_name:
        company_name = company_code

    existing = find_existing_company_folder(
        base_folder,
        company_name
    )

    if existing:
        return existing

    new_folder = os.path.join(
        base_folder,
        company_name
    )

    os.makedirs(new_folder, exist_ok=True)

    return new_folder


# ----------------------------------------------------------
# MAIN
# ----------------------------------------------------------

if __name__ == "__main__":

    print("\n========== CAPEX PDF ORGANIZER ==========\n")

    downloads_folder = get_downloads_folder()

    if not os.path.exists(downloads_folder):
        print("Downloads folder not found.")
        input("\nPress Enter to exit...")
        exit()

    answer = input(
        'Press "y" to REMOVE original files after moving.\n'
        'Press any other key to COPY only.\n\n'
        'Your choice: '
    ).lower()

    delete_original = answer == "y"

    base_folder = create_base_folder()

    processed_count = 0

    for file_name in os.listdir(downloads_folder):

        match = PDF_PATTERN.match(file_name)

        if not match:
            continue

        company_code = match.group(1).upper()
        year = match.group(2)
        serial = match.group(3)

        requisition_folder_name = (
            f"{company_code}_{year}_{serial}"
        )

        source_file = os.path.join(
            downloads_folder,
            file_name
        )

        company_folder = get_company_folder(
            base_folder,
            company_code
        )

        year_folder = os.path.join(
            company_folder,
            year
        )

        os.makedirs(year_folder, exist_ok=True)

        requisition_folder = os.path.join(
            year_folder,
            requisition_folder_name
        )

        os.makedirs(requisition_folder, exist_ok=True)

        destination_file = os.path.join(
            requisition_folder,
            file_name
        )

        try:

            if delete_original:

                shutil.move(
                    source_file,
                    destination_file
                )

                print(f"MOVED  : {file_name}")

            else:

                shutil.copy2(
                    source_file,
                    destination_file
                )

                print(f"COPIED : {file_name}")

            processed_count += 1

        except Exception as e:

            print(
                f"ERROR processing "
                f"{file_name}: {e}"
            )

    print("\n-----------------------------------")
    print(f"Processed Files : {processed_count}")
    print("Completed.")
    print("-----------------------------------\n")

    input("Press Enter to exit...")