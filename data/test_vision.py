#!/usr/bin/env python3
"""
Simple test: Can Claude Vision read an image-based PDF?
Just tests the vision capability - no complex position metadata needed.
"""
import os
import sys
from pathlib import Path
import anthropic
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Import our PDF functions
try:
    from pdf2image import convert_from_path
    import base64
    from io import BytesIO
except ImportError:
    print("❌ Missing dependencies. Run: pip install pdf2image Pillow")
    sys.exit(1)

def encode_image_to_base64(image):
    """Encode PIL image to base64"""
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

def test_vision_on_pdf(pdf_path):
    """Test Claude Vision on a PDF"""

    # Check API key
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ No API key found!")
        print("\nTo fix:")
        print("  1. Copy .env.example to .env")
        print("  2. Add your Claude API key to .env")
        print("  3. Run this script again")
        return

    print(f"✅ API key found (starts with: {api_key[:15]}...)")

    # Convert PDF to images
    print(f"\n📄 Converting PDF to images: {pdf_path}")
    try:
        images = convert_from_path(pdf_path, dpi=150)
        print(f"✅ Converted {len(images)} pages")
    except Exception as e:
        print(f"❌ Error converting PDF: {e}")
        return

    # Just test first page
    print(f"\n🤖 Sending page 1 to Claude Vision...")

    image_base64 = encode_image_to_base64(images[0])

    client = anthropic.Anthropic(api_key=api_key)

    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "What text do you see in this image? Just extract and return the text content."
                        },
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/png",
                                "data": image_base64
                            }
                        }
                    ]
                }
            ]
        )

        extracted_text = response.content[0].text

        print(f"\n✅ SUCCESS! Claude Vision extracted text from the image PDF:")
        print("=" * 80)
        print(extracted_text)
        print("=" * 80)

    except Exception as e:
        print(f"❌ Error calling Claude API: {e}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 test_vision.py <path_to_pdf>")
        print("\nExample:")
        print("  python3 test_vision.py ../docs/resume.pdf")
        sys.exit(1)

    pdf_path = sys.argv[1]
    if not Path(pdf_path).exists():
        print(f"❌ File not found: {pdf_path}")
        sys.exit(1)

    test_vision_on_pdf(pdf_path)
