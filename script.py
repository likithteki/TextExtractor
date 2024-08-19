from PIL import Image
import pytesseract
import sys
import os

# New Logo and Author Name
LOGO = """
\033[95m\033[1m------------------------------
------------------------------
      Text Extractor          
------------------------------
------------------------------\033[0m
"""
AUTHOR = "Script by Likith"

# Adding colors for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# If tesseract is not in your PATH, specify the path to the executable
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang='eng')
        return text
    except Exception as e:
        print(f"{Colors.FAIL}Error processing {image_path}: {e}{Colors.ENDC}", file=sys.stderr)
        return None

def print_help():
    help_text = f"""        
    {Colors.OKCYAN}Options:{Colors.ENDC}
    {Colors.BOLD}-h, --help{Colors.ENDC}       Show this help message
    {Colors.BOLD}-o, --output{Colors.ENDC}     Specify output file to save the extracted text
    
    {Colors.OKCYAN}Example:{Colors.ENDC}
    {Colors.OKGREEN}python3 script.py /home/path/image.png -o output.txt{Colors.ENDC}
    """
    print(help_text)

def main():
    if len(sys.argv) < 2:
        print(f"{Colors.WARNING}Usage: python script.py <image_path> [-o output_file]{Colors.ENDC}", file=sys.stderr)
        sys.exit(1)

    # Display logo and author name
    print(f"{LOGO}")
    print(f"{Colors.UNDERLINE}{AUTHOR}{Colors.ENDC}\n")
    
    if sys.argv[1] in ('-h', '--help'):
        print_help()
        sys.exit(0)

    image_path = sys.argv[1]
    output_file = None

    if len(sys.argv) == 4 and sys.argv[2] in ('-o', '--output'):
        output_file = sys.argv[3]

    text = extract_text_from_image(image_path)
    
    if text:
        if output_file:
            try:
                with open(output_file, 'w') as f:
                    f.write(text)
                print(f"{Colors.OKGREEN}Text saved to {output_file}{Colors.ENDC}")
            except Exception as e:
                print(f"{Colors.FAIL}Error saving text to {output_file}: {e}{Colors.ENDC}", file=sys.stderr)
        else:
            print(f"{Colors.OKGREEN}Text from image {image_path}:{Colors.ENDC}")
            print(f"{Colors.OKBLUE}{text}{Colors.ENDC}")
            print(f"\n{Colors.HEADER}{'-'*50}{Colors.ENDC}\n")

if __name__ == "__main__":
    main()

