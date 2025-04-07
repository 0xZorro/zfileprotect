# ============================================
# zfileprotect - File Protection Tool
# ============================================
# Author: 0xZorro
# Created: 2025-04-07
# Description: A Python tool to protect Word, PDF, and Excel files with a password.
#              Supports manual and automatic password generation, and can process
#              multiple files or entire directories.
#
# License: MIT License (see LICENSE file for details)
# Version: 1.0
# Repository: https://github.com/0xZorro/zfileprotect
# ============================================


import os
import win32com.client as win32
from argparse import ArgumentParser
from PyPDF2 import PdfReader, PdfWriter
import string
import secrets


# Function to protect a Word document with a password
# This function opens the specified Word file, applies password protection,
# and saves it with the specified password. The resulting file is saved 
# with the suffix '.crypted.docx'.
def protectWORD(filePath, pwd):
  word = win32.gencache.EnsureDispatch('Word.Application')
  word.Visible = False
  document = word.Documents.Open(filePath)
  document.SaveAs(f"{filePath}.crypted.docx", Password=pwd)
  print("Protection completed.")
  document.Close()
  word.Application.Quit()

# Function to protect a PDF document with a password
# This function opens the specified PDF file and applies password protection.
# The resulting file is saved as a new PDF with password protection.
# Libraries such as PyPDF2 or pikepdf could be used to implement PDF encryption.
def protectPDF(filePath,pwd):
    pdfReader = PdfReader(filePath)
    pdfWriter = PdfWriter()
    for page in range(len(pdfReader.pages)):
       pdfWriter.add_page(pdfReader.pages[page])
    pdfWriter.encrypt(user_password=pwd,use_128bit=True)
    output = filePath + ".protected.pdf"
    with open(output, "wb") as out:
       pdfWriter.write(out)
    print("Protection completed.")

# Function to protect an Excel file with a password
# This function opens the specified Excel file and applies password protection.
# The resulting file is saved with the specified password protection.
# Libraries like openpyxl or xlsxwriter can be used to apply password protection for Excel files.
def protectExcel(filePath,pwd):
    excel = win32.gencache.EnsureDispatch("Excel.Application")
    excel.Visible = False
    workbook = excel.Workbooks.Open(filePath)
    workbook.SaveAs(f"{filePath}.protected.xlsx",Password=pwd)
    print("Protection completed")
    workbook.Close
    excel.Application.Quit()

# Function to generate automatically a password
def generatePassword(length):
    # ----------  Prepare character list ----------
    all_chars = string.ascii_letters + string.digits + string.punctuation
    filtered_chars = []
    for c in all_chars:
        if c != '"':
            filtered_chars.append(c)
    characters = ''.join(filtered_chars)
    # ----------------------------------------------
    pwd = ""
    while len(pwd) < length:
        pwd += secrets.choice(characters)
    return pwd


def protect_file(file_path, pwd):
    # Determine the file type and call the appropriate function
    file_extension = os.path.splitext(file_path)[1].lower() # Check file extension
    if file_extension == '.docx':
        print(f"Protecting Word file: {file_path} ...")
        # Get the current working directory
        # This is needed because we're working with the Windows API, 
        # which requires the absolute file path for file operations.
        prefix = os.getcwd()
        # Protect the Word document by calling the protectWORD function
        # The file path is combined with the current working directory to form the absolute path
        protectWORD(f'{prefix}\\{file_path}', pwd)
    elif file_extension == '.pdf':
        print(f"Protecting PDF file:  {file_path} ...")
        protectPDF(file_path, pwd)
    elif file_extension == '.xlsx':
        print(f"Protecting Excel file: {file_path} ...")
        prefix = os.getcwd()
        protectExcel(f'{prefix}\\{file_path}', pwd)
    else:
         print("Unsupported file type. Please provide a .docx, .pdf, or .xlsx file.")


def process_directory(directory, pwd):
    # Go through all files in the directory
    for root, dir,  files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            protect_file(file_path, pwd)

def main():
    parser = ArgumentParser(description = "Protect files with a password.")
    parser.add_argument("filePath", nargs="+", help="Path to the file(s) to be protected")
    parser.add_argument("-p", "--password", action="store_true", help="Automatically generate a password")  # No argument for -p
    parser.add_argument("--pwd", type=str, help="Password to protect the file(s) with")
    args = parser.parse_args()

    # If the user provides the '-p' option, generate a password
    if args.password:
        print("Generating password automatically...")
        password = generatePassword(10)  # Example: generate_password()
        print(f"Generated password: {password}")
    elif args.pwd:
        password = args.pwd  # If user provides a password directly, use it
        print(f"Using provided password: {password}")
    else:
        print("Error: No password provided and no key for automatic generation.")
        return

     # Process the specified file(s)
    for file_path in args.filePath:
        # Check if it is a directory
        if os.path.isdir(file_path):  # If directory
            process_directory(file_path, password)
        else:  # If single file
            protect_file(file_path, password)


if __name__ == "__main__":
   main()