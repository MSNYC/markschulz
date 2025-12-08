#!/usr/bin/env python3
"""
Quick test script to verify PDF detection (text-based vs image-based)
"""
import sys
from pathlib import Path

# Import the functions from extract_and_load
sys.path.insert(0, str(Path(__file__).parent))
from extract_and_load import is_image_based_pdf, read_pdf_file

def test_pdf(filepath):
    """Test a PDF to see if it's detected as image-based"""
    filepath = Path(filepath)

    if not filepath.exists():
        print(f"❌ File not found: {filepath}")
        return

    print("=" * 80)
    print(f"Testing: {filepath.name}")
    print("=" * 80)

    # Test detection
    is_image = is_image_based_pdf(filepath)
    print(f"\n🔍 Detection Result: {'IMAGE-BASED PDF' if is_image else 'TEXT-BASED PDF'}")

    # Test reading
    print("\n📖 Attempting to read PDF...")
    try:
        result = read_pdf_file(filepath)
        if result == 'IMAGE_PDF':
            print("✅ PDF correctly identified as IMAGE_PDF marker")
            print("   → Would trigger Claude Vision processing")
        else:
            char_count = len(result)
            print(f"✅ Extracted {char_count:,} characters of text")
            print(f"\nFirst 200 characters:")
            print("-" * 80)
            print(result[:200])
            print("-" * 80)
    except Exception as e:
        print(f"❌ Error reading PDF: {e}")

    print("\n" + "=" * 80)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python test_pdf_detection.py <path_to_pdf>")
        print("\nExample:")
        print("  python test_pdf_detection.py ../docs/resume.pdf")
        sys.exit(1)

    test_pdf(sys.argv[1])
