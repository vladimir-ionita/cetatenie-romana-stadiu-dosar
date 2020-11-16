# About
A dossier web parser for `http://oldcetatenie.just.ro`.


## Motive
Based on the common history of Romania and the Republic of Moldova, the citizens of the Republic of Moldova can apply for, and obtain Romanian citizenship. Annually, circa 80.000-100.000 people apply for Romanian citizenship. 
Documents examination can take from half a year to 2-3 years and sometimes even more. People can check the status of their application, but the process is really tedious and error-prone.
The orders are published on `http://oldcetatenie.just.ro/index.php/ro/ordine/articol-11` as PDF files. A person must access this web address, and check every order for his dossier number.

This tool tends to make the process easier, by automating the whole process. 


# Installation
The project makes use of several libraries, some of which require some manual setup.

#### 1. The `pdf2image` library 
The `pdf2image` library requires `poppler` to be installed, according to its [README](https://github.com/Belval/pdf2image) file.

You can install it using homebrew: `brew install poppler`.

#### 2. The `pytesseract` library
The `pytesseract` library requires `tesseract` to be installed, according to its [README](https://github.com/madmaze/pytesseract) file.

You can install it using homebrew: `brew install tesseract`.

#### 3. Install dependencies
To install the project dependencies, you can use `pip` and the `requirements.txt` file:

`pip install -r requirements.txt`

# Usage

In the `main.py` search for the `lookups`. Set your dossier number according to the example and run the project.


# Configurations
#### The `pytesseract` library
For `tesseract` to properly read the PDF images, I've configured it's `page segmentation mode` to 4 (single column of text of variable sizes).

You can read more here: https://ai-facets.org/tesseract-ocr-best-practices.

#### Storage Path
The default storage path for the tools is set to `$HOME/dev/romanian-citizenship-status-files`.

You can change it by changing the `FILES_STORAGE_PATH` constant.


# Known Issues
Sometimes the PDF conversion to TXT results in badly formatted data. Unfortunately, I don't have much experience with `tesseract` and couldn't configure it better.

Solutions: Manually convert the malformatted files using `https://pdftotext.com/` or other tools.  


# Notes
I've also included all the PDF and TXT files until November 2020.

The tool can download and convert them by itself, but it might take a very long time, as there are more than 2000 files until now. This will help a lot.
