#!/usr/bin/env python3
"""
Test script to verify the Sports Match Report Generator setup
"""

import os
import sys
from dotenv import load_dotenv

def test_environment():
    """Test environment setup"""
    print("🔍 Testing Environment Setup...")
    
    # Load environment variables
    load_dotenv()
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("❌ .env file not found!")
        return False
    
    # Check Hugging Face token
    token = os.environ.get('HUGGINGFACE_API_TOKEN')
    if not token:
        print("❌ Hugging Face API token not found!")
        print("   Please set HUGGINGFACE_API_TOKEN in your .env file")
        return False
    elif token == 'hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX':
        print("✅ Running in mock mode (no real API token needed)")
        return True
    else:
        print("✅ Environment variables configured correctly")
        return True

def test_imports():
    """Test if all required packages are installed"""
    print("\n🔍 Testing Package Imports...")
    
    required_packages = [
        ('flask', 'Flask'),
        ('fitz', 'PyMuPDF'),
        ('sentence_transformers', 'SentenceTransformer'),
        ('faiss', 'FAISS'),
        ('numpy', 'NumPy'),
        ('requests', 'Requests'),
        ('dotenv', 'python-dotenv')
    ]
    
    failed_imports = []
    
    for package, name in required_packages:
        try:
            __import__(package)
            print(f"✅ {name} imported successfully")
        except ImportError as e:
            print(f"❌ {name} import failed: {e}")
            failed_imports.append(name)
    
    if failed_imports:
        print(f"\n❌ Failed imports: {', '.join(failed_imports)}")
        print("   Run: pip install -r requirements.txt")
        return False
    
    return True

def test_utilities():
    """Test utility functions"""
    print("\n🔍 Testing Utility Functions...")
    
    try:
        import utils
        
        # Test sentence transformer model loading
        print("✅ Utils module imported successfully")
        
        # Test basic functionality
        test_text = "This is a test match report. Player John scored 50 runs."
        chunks = utils.split_text_into_chunks(test_text)
        print(f"✅ Text chunking works: {len(chunks)} chunks created")
        
        # Test embeddings (this will download the model if not cached)
        print("📥 Testing embeddings (may download model first time)...")
        embeddings = utils.create_embeddings(chunks)
        print(f"✅ Embeddings created: shape {embeddings.shape}")
        
        # Test FAISS index
        faiss_index = utils.build_faiss_index(embeddings)
        print("✅ FAISS index created successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ Utility test failed: {e}")
        return False

def test_huggingface_api():
    """Test Hugging Face API connection"""
    print("\n🔍 Testing Hugging Face API Connection...")
    
    try:
        import utils
        
        # First verify API token
        is_valid, message = utils.verify_api_token()
        if not is_valid:
            print(f"❌ API token validation failed: {message}")
            return False
        
        print("✅ API token is valid")
        
        # Test API connection
        print("🔄 Testing API response...")
        test_response = utils.call_huggingface_api("Write a short sentence about sports:", max_tokens=50)
        
        if test_response.startswith("Error:"):
            print(f"❌ API test failed: {test_response}")
            return False
        
        print("✅ Hugging Face API connection successful")
        print(f"   Response: {test_response[:100]}...")
        return True
        
    except Exception as e:
        print(f"❌ API test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Sports Match Report Generator - Setup Test\n")
    
    tests = [
        ("Environment Setup", test_environment),
        ("Package Imports", test_imports),
        ("Utility Functions", test_utilities),
        ("Hugging Face API", test_huggingface_api)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test crashed: {e}")
            results.append((test_name, False))
    
    print("\n" + "="*50)
    print("📊 TEST RESULTS SUMMARY")
    print("="*50)
    
    all_passed = True
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name:<25} {status}")
        if not result:
            all_passed = False
    
    print("="*50)
    
    if all_passed:
        print("🎉 ALL TESTS PASSED! Your setup is ready.")
        print("   Run: python app.py")
        print("   Then visit: http://127.0.0.1:5000")
    else:
        print("⚠️  Some tests failed. Please fix the issues above.")
        print("   Check the README.md for troubleshooting tips.")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
