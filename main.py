import os
import argparse
from pdftomd.pdftomd import pdf_to_markdown

def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='Convert PDF to Markdown')
    parser.add_argument('pdf_path', help='Path to the PDF file')
    parser.add_argument('-o', '--output', help='Path to save the output Markdown file')
    parser.add_argument('-u', '--url', help='Custom API URL (overrides environment variable)')
    
    args = parser.parse_args()
    
    try:
        # Convert PDF to Markdown
        md_content = pdf_to_markdown(
            pdf_path=args.pdf_path,
            output_path=args.output,
            url=args.url
        )
        
        # If no output file was specified, print to console
        if not args.output:
            print(md_content)
        else:
            print(f"Conversion complete. Output saved to {args.output}")
            
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    exit(main())
