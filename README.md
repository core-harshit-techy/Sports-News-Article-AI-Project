# 🏆 Sports Match Report Generator

A modern Flask web application that transforms match PDFs into professional sports articles with AI-powered insights.

## ✨ Features

- 📄 **PDF Processing**: Upload match scorecards and tournament summaries
- 🤖 **AI Article Generation**: Creates professional sports news articles
- ⭐ **Star Player Extraction**: Identifies top performers automatically
- 💬 **Interactive Chatbot**: Ask questions about the uploaded match
- 🎨 **Modern UI**: Responsive design with smooth animations
- 🔍 **Vector Search**: FAISS-powered similarity search for accurate responses

## 🚀 Quick Start

### 1. Clone/Download the Project

```bash
git clone <repository-url>
cd sports_match_report_generator
```

### 2. Set Up Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

1. Copy `.env` file and edit it:
   ```bash
   cp .env.example .env
   ```

2. Get your Hugging Face API token:
   - Go to https://huggingface.co/settings/tokens
   - Create a new token
   - Copy the token to your `.env` file:
   ```
   HUGGINGFACE_API_TOKEN=hf_your_token_here
   ```

### 5. Run the Application

```bash
python app.py
```

Visit http://127.0.0.1:5000 in your browser!

## 🎯 How to Use

1. **Upload PDF**: Click "Process PDF" and select your match scorecard
2. **View Article**: The AI will generate a professional sports article
3. **See Star Players**: Top performers will be highlighted in the sidebar
4. **Ask Questions**: Use the chatbot to get specific match insights

## 🏗️ Project Structure

```
Sports/
├── app.py                 # Main Flask application
├── utils.py              # PDF processing and AI utilities
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
├── .gitignore            # Git ignore file
├── README.md            # This documentation
├── run.bat              # Windows quick start script
├── test_setup.py        # Setup verification script
├── templates/
│   └── index.html       # Main UI template with animations
└── uploads/             # Temporary PDF storage (auto-created)
```

## 🔧 Technical Details

- **Backend**: Flask web framework
- **PDF Processing**: PyMuPDF for text extraction
- **AI Model**: Hugging Face Inference API
- **Vector Database**: FAISS for similarity search
- **Embeddings**: Sentence Transformers (all-MiniLM-L6-v2)
- **Frontend**: TailwindCSS + Custom animations

## 🛠️ Customization

### Change AI Model

Edit `utils.py` and modify the `model_id` in `call_huggingface_api()`:

```python
model_id = "tiiuae/falcon-7b-instruct"  # or your preferred model
```

### Adjust Chunk Size

Modify chunking parameters in `split_text_into_chunks()`:

```python
def split_text_into_chunks(text: str, chunk_size: int = 500, overlap: int = 50):
```

### UI Customization

The template uses TailwindCSS. Modify `templates/index.html` to customize the design.

## 📋 Requirements

- Python 3.8+
- Hugging Face API token
- 2GB+ RAM (for sentence transformers)
- Modern web browser

## 🔐 Security Notes

- Never commit your `.env` file to version control
- Use environment variables for sensitive data
- Consider rate limiting for production use
- Validate and sanitize all user inputs

## 🐛 Troubleshooting

### Common Issues

1. **"API token not found"**
   - Ensure your `.env` file has the correct token
   - Check token has proper permissions

2. **"Could not extract text from PDF"**
   - Ensure PDF is not password-protected
   - Try a different PDF file

3. **Long response times**
   - Hugging Face API can be slow for free tier
   - Consider using a local model for production

### Debug Mode

Enable debug mode in `.env`:
```
FLASK_DEBUG=True
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For issues or questions:
1. Check the troubleshooting section
2. Open an issue on GitHub
3. Review the code comments for implementation details

---

**Happy coding! 🏆⚽🏀🏈**
