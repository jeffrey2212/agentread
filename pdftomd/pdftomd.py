import os
import requests
import base64

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the API URL from environment variables
magic_pdf_url = os.getenv('magic_pdf_url')

def to_b64(file_path):
    """Convert a file to base64 encoding"""
    with open(file_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

def parse_file(file_path, url=None):
    """Parse a PDF file and return the JSON response"""
    # Use the provided URL or default to the environment variable
    if url is None:
        url = magic_pdf_url
        if url is None:
            raise ValueError("No API URL provided and 'magic_pdf_url' not found in environment variables")
    
    files = {
        'file': open(file_path, 'rb')
    }
    data = {
        'parse_method': 'auto',
        'return_layout': 'true',
        'return_content_list': 'true'
    }
    
    response = requests.post(url, files=files, data=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.text}")

def pdf_to_markdown(pdf_path, output_path=None, url=None):
    """Convert a PDF file to Markdown
    
    Args:
        pdf_path (str): Path to the PDF file
        output_path (str, optional): Path to save the Markdown output. If None, the output is not saved to a file.
        url (str, optional): API URL to use. If None, uses the URL from environment variables.
        
    Returns:
        str: The Markdown content
    """
    result = parse_file(pdf_path, url)
    md_content = result['md_content']
    
    # Save to file if output_path is provided
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
    
    return md_content

# Example usage (commented out so it doesn't run when imported)
# if __name__ == "__main__":
#     result = pdf_to_markdown('C:\\Users\\jeffr\\Downloads\\2504.12626v2.pdf', 'output.md')
#     print("Conversion complete. Output saved to output.md")