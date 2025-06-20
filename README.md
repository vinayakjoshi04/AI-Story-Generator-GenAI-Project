# ✨ AI Story Generator

A beautiful, feature-rich web application that harnesses the power of Google's Gemini AI to create captivating stories based on your prompts. Built with Flask and featuring a stunning glassmorphic UI with animated particles.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-v2.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🌟 Features

### 🎨 **Beautiful User Interface**
- Modern glassmorphic design with animated particle effects
- Responsive layout that works on all devices
- Smooth animations and hover effects
- Dark gradient background with backdrop blur effects

### 🤖 **AI-Powered Story Generation**
- Integration with Google Gemini AI models
- Support for multiple Gemini model variants
- Intelligent story continuation feature
- Automatic title generation

### 📚 **Customizable Story Parameters**
- **Genres**: Adventure, Horror, Science Fiction, Fantasy, Romance, Mystery
- **Story Length**: Short (2-3 paragraphs), Medium (5-7 paragraphs), Long (10+ paragraphs)
- **Character Customization**: Define character names and types
- **Multi-language Support**: English, Hindi, Spanish, French, German

### 🔊 **Text-to-Speech Integration**
- Convert stories to audio using Google Text-to-Speech (gTTS)
- Multi-language audio support
- Built-in audio player with modern controls

### 💾 **Export Options**
- Download stories as TXT files
- Export as formatted PDF documents
- Preserve story titles and formatting

### ⚡ **Advanced Features**
- Story continuation functionality
- Real-time error handling
- Loading animations and feedback
- Responsive form validation

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google AI API key (Gemini)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-story-generator.git
   cd ai-story-generator
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create a .env file in the project root
   echo "GOOGLE_API_KEY=your_google_ai_api_key_here" > .env
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5000`

## 🛠️ Dependencies

```txt
Flask>=2.3.0
google-generativeai>=0.3.0
python-dotenv>=1.0.0
fpdf2>=2.7.0
gTTS>=2.4.0
```

## 📁 Project Structure

```
ai-story-generator/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Frontend template with UI
├── requirements.txt      # Python dependencies
├── .env                 # Environment variables (create this)
├── README.md           # Project documentation
└── .gitignore          # Git ignore file
```

## 🔧 Configuration

### Google AI API Setup

1. Visit the [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add the API key to your `.env` file:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Your Google AI (Gemini) API key | Yes |

## 🎯 Usage

1. **Choose Your Settings**
   - Select an AI model from the dropdown
   - Pick your preferred genre and story length
   - Define your character's name and type
   - Choose the language for your story

2. **Enter Your Prompt**
   - Write a creative prompt to start your story
   - Be specific about the setting, conflict, or theme

3. **Generate & Enjoy**
   - Click "Generate Story" and watch the magic happen
   - Continue your story with the "Continue Story" button
   - Listen to your story with text-to-speech (After Clicking on Listen to Story, it takes couple of minutes to convert to the audio, so wait for couple minutes and then it starts the audio.
   - Download in TXT or PDF format, U can also download the mp3 audio.

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main application page |
| `/generate` | POST | Generate a new story |
| `/continue` | POST | Continue an existing story |
| `/speak` | POST | Convert story to audio |
| `/download` | POST | Download story as file |

## 📱 Screenshots

### 🏠 Homepage - Story Generation Interface
![Screenshot 2025-06-20 190715](https://github.com/user-attachments/assets/84a86a9e-f82e-4915-8d10-fd6f8290df48)

### ✨ Story Generation in Action
![Screenshot 2025-06-20 185846](https://github.com/user-attachments/assets/41f3ef07-03f4-4a4d-926a-b51b1dce1acc)

![Screenshot 2025-06-20 202237](https://github.com/user-attachments/assets/7b1edec1-fe1d-4137-896a-17ed31647c6e)

### 📖 Generated Story Display
![Screenshot 2025-06-20 185932](https://github.com/user-attachments/assets/148a88b1-85fc-43ad-a511-de5015435ca1)

![Screenshot 2025-06-20 185956](https://github.com/user-attachments/assets/35de4b1c-4595-445a-a37b-1965ba9579de)

![Screenshot 2025-06-20 190014](https://github.com/user-attachments/assets/d4f217e1-dc4b-41e9-a6ca-99b003b04349)

![Screenshot 2025-06-20 190039](https://github.com/user-attachments/assets/ad0996a6-fd2b-4844-9653-9319104f8281)

### 🎵 Audio Playback Feature
![Screenshot 2025-06-20 190100](https://github.com/user-attachments/assets/f180de82-f83e-47ca-86de-ea27322e4203)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📋 Future Roadmap

- [ ] User authentication and story saving
- [ ] Story sharing functionality
- [ ] More AI model options
- [ ] Advanced story templates
- [ ] Story analytics and insights
- [ ] Mobile app version
- [ ] Collaborative story writing

## 🐛 Known Issues

- Audio playback may not work in some browsers due to autoplay policies
- PDF generation supports Latin-1 encoding (some special characters may not display correctly)
- Story length is limited by the AI model's context window

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Google Gemini AI](https://ai.google.dev/) for the powerful language model
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [gTTS](https://github.com/pndurette/gTTS) for text-to-speech functionality
- [FPDF](https://github.com/PyFPDF/fpdf2) for PDF generation
- Font Awesome for beautiful icons

## 📞 Support

If you encounter any issues or have questions, please:

1. Check the [Issues](https://github.com/yourusername/ai-story-generator/issues) page
2. Create a new issue with detailed information
3. Contact the maintainer at vinayakjoshi2004@gmail.com

---

⭐ **If you found this project helpful, please give it a star!** ⭐

Made with ❤️ by [Vinayak Vivek Joshi](https://github.com/vinayakjoshi04)
