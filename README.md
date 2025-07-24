<<<<<<< HEAD
# 🏆 Sports Match Report Generator

A modern Flask web application that transforms match PDFs into professional sports articles with AI-powered insights.

## ✨ Features

- 📄 **PDF Processing**: Upload match scorecards and tournament summaries
- 🤖 **AI Article Generation**: Creates professional sports news articles
- ⭐ **Star Player Extraction**: Identifies top performers automatically
- 💬 **Interactive Chatbot**: Ask questions about the uploaded match
- 🎨 **Modern UI**: Responsive design with smooth animations
- 🔍 **Vector Search**: FAISS-powered similarity search for accurate responses
![WhatsApp Image 2025-07-17 at 12 00 18_72faa44d](https://github.com/user-attachments/assets/16f3a22a-a722-424d-8b79-670ba3c4c01b)


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
=======
# harshitsrivastavajps-project



## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/topics/git/add_files/#add-files-to-a-git-repository) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.com/harshitsrivastavajps-group/harshitsrivastavajps-project.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://gitlab.com/harshitsrivastavajps-group/harshitsrivastavajps-project/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Set auto-merge](https://docs.gitlab.com/user/project/merge_requests/auto_merge/)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing (SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thanks to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README

Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
>>>>>>> cecffc45bc808e3343e0f77cf3ba626494c1658c
