## Image Text Extractor Tool

This tool allows you to extract text from images using Python's `pytesseract` and `PIL` (Python Imaging Library). It leverages the Tesseract-OCR engine to process images and extract readable text.

### Features
- Extracts text from any image file
- Supports multiple languages (default is English)
- Easy to set up and use

### Prerequisites

Before using this tool, ensure that you have the following installed on your system:

- Python 3.x
- Tesseract-OCR

### Installation

#### Step 1: Clone the repository
```bash
git clone https://github.com/likithteki/TextExtractor
cd TextExtractor
```

#### Step 2: Set up a Python virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

#### Step 3: Install dependencies
```bash
pip3 install -r requirements.txt
```

#### Step 4: Install Tesseract OCR
- **macOS**: Install via Homebrew
  ```bash
  brew install tesseract
  ```
- **Linux**: Install via package manager
  ```bash
  sudo apt-get install tesseract-ocr
  ```
- **Windows**: Download and install from [Tesseract's official site](https://github.com/tesseract-ocr/tesseract/wiki).

### Usage

To extract text from an image, run the following command:

```bash
python3 script.py <image_path>
```

Replace `<image_path>` with the path to your image file.

### Commands 
To view help information about the script:

```bash
python3 script.py -h
```

or

```bash
python3 script.py --help
```

To save output in a seperate txt file:

```bash
python3 script.py /home/path/image.png -o output.txt
```

### Example
```bash
python3 script.py sample_image.png
```

```bash
python3 script.py sample_image.png -o output.txt
```

### Notes
- Ensure Tesseract OCR is correctly installed and added to your system's PATH.
- The default language is set to English. If you want to change the language, modify the `lang` parameter in the `pytesseract.image_to_string()` function call.
