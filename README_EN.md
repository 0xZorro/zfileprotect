# zfileprotect

**zfileprotect** is a Python tool designed to protect Word, PDF, and Excel files with a password. It supports both manual password input and automatic password generation. This tool also allows you to process multiple files and entire directories in one go.

## Features

- Protect Word (`.docx`), PDF (`.pdf`), and Excel (`.xlsx`) files with a password.
- Automatically generate a strong password with the `-p` flag.
- Support for multiple files and directories.
- Simple command-line interface using `argparse`.

## Motivation

This project was created as a learning exercise in **cybersecurity**.  
Inspired by the book **"Ethical Hacking" by Florian André Dalwick**, the goal was to practice building practical tools that improve data protection — with a particular focus on **file encryption** and **password-based security**.

## Requirements

- Python 3.x
- `pywin32` (for Word and Excel protection)
- `PyPDF2` (for PDF protection)

### Installation

To install the required libraries, you can use `pip`:

```bash
pip install pywin32 PyPDF2
```

## Usage

### Protect a file with a manually provided password:

```bash
python zfileprotect.py "Test.pdf" --pwd=yourpassword
```

### Protect multiple files with a manually provided password:

```bash
python zfileprotect.py "file1.pdf" "file2.docx" "file3.xlsx" --pwd=yourpassword
```

### Automatically generate a password and protect files:

```bash
python zfileprotect.py "Test.pdf" -p
```

### Process all files in a directory:

```bash
python zfileprotect.py "C:\path\to\directory" -p
```

The tool will automatically process all supported files in the directory and protect them with a generated password.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

**zfileprotect** is a tool for educational and personal use only. By using this tool, you agree not to use it for any illegal activities. You should only protect files you own or have explicit permission to protect. **The author is not responsible for any misuse or damage caused by this tool.**

---

## Contributing

Feel free to contribute to this project by forking it, making changes, and creating a pull request. 

Please ensure that any contributions follow the code of conduct and project standards.

---

## Author

Created by Jose Luis Ocana

Cybersecurity Learner | Python & C++ Tools 

GitHub: [0xZorro](https://github.com/0xZorro)

TryHackMe: [https://tryhackme.com/p/0xZorro](https://tryhackme.com/p/0xZorro)
  
Contact: zorro.jose@gmx.de

