from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import utils
import tempfile
import shutil

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'sports-match-generator-secret-key')

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Global variables to store processed data
processed_data = {
    'article': None,
    'star_players': [],
    'faiss_index': None,
    'chunks': [],
    'embeddings': None
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html', 
                         article=processed_data['article'],
                         star_players=processed_data['star_players'])

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            flash('No file selected', 'error')
            return redirect(url_for('index'))
        
        file = request.files['file']
        if file.filename == '':
            flash('No file selected', 'error')
            return redirect(url_for('index'))
        
        if file and allowed_file(file.filename):
            # Check file size
            file.seek(0, os.SEEK_END)
            file_size = file.tell()
            file.seek(0)
            
            if file_size > MAX_FILE_SIZE:
                flash('File too large. Maximum size is 16MB', 'error')
                return redirect(url_for('index'))
            
            # Save file temporarily
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            
            # Process the PDF
            flash('Processing PDF...', 'info')
            
            # Extract text from PDF
            text = utils.extract_text_from_pdf(filepath)
            if not text.strip():
                flash('Could not extract text from PDF', 'error')
                os.remove(filepath)
                return redirect(url_for('index'))
            
            # Split text into chunks
            chunks = utils.split_text_into_chunks(text)
            
            # Create embeddings
            embeddings = utils.create_embeddings(chunks)
            
            # Build FAISS index
            faiss_index = utils.build_faiss_index(embeddings)
            
            # Generate article
            article = utils.generate_article(text)
            
            # Extract star players
            star_players = utils.extract_star_players(text)
            
            # Store in global variables
            processed_data['article'] = article
            processed_data['star_players'] = star_players
            processed_data['faiss_index'] = faiss_index
            processed_data['chunks'] = chunks
            processed_data['embeddings'] = embeddings
            
            # Clean up uploaded file
            os.remove(filepath)
            
            flash('PDF processed successfully!', 'success')
            return redirect(url_for('index'))
        
        else:
            flash('Invalid file type. Please upload a PDF file.', 'error')
            return redirect(url_for('index'))
            
    except Exception as e:
        flash(f'Error processing file: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        query = data.get('query', '').strip()
        
        if not query:
            return jsonify({'error': 'Please enter a question'}), 400
        
        if not processed_data['faiss_index'] or not processed_data['chunks']:
            return jsonify({'error': 'Please upload a PDF first'}), 400
        
        # Get relevant chunks using FAISS
        relevant_chunks = utils.get_relevant_chunks(
            query, 
            processed_data['faiss_index'], 
            processed_data['chunks']
        )
        
        # Generate response using LLM
        response = utils.generate_chat_response(query, relevant_chunks)
        
        return jsonify({'response': response})
        
    except Exception as e:
        return jsonify({'error': f'Chat error: {str(e)}'}), 500

@app.route('/clear')
def clear_data():
    # Clear all processed data
    processed_data['article'] = None
    processed_data['star_players'] = []
    processed_data['faiss_index'] = None
    processed_data['chunks'] = []
    processed_data['embeddings'] = None
    
    # Clear uploaded files
    try:
        shutil.rmtree(UPLOAD_FOLDER)
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    except:
        pass
    
    flash('All data cleared successfully!', 'success')
    return redirect(url_for('index'))

@app.errorhandler(413)
def too_large(e):
    flash('File too large. Maximum size is 16MB', 'error')
    return redirect(url_for('index'))

@app.errorhandler(500)
def internal_error(e):
    flash('Internal server error occurred', 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
