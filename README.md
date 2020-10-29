## Libraries
### pdf2image 
The `pdf2image` library requires `poppler` to be installed, according to its README file: https://github.com/Belval/pdf2image.

You can install it using homebrew: `brew install poppler`.

### pytesseract
The `pytesseract` library requires `tesseract` to be installed, according to its README file: https://github.com/madmaze/pytesseract.

You can install it using homebrew: `brew install tesseract`.

## Configurations
### pytesseract
In order for `tesseract` to properly read the PDF images, I've configured it's `page segmentation mode` to 4, which says the following: 
<i>Assume a single column of text of variable sizes</i>. For more configurations check https://ai-facets.org/tesseract-ocr-best-practices. 
