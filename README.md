# 🧠 Variable Name Generator

A simple web application that helps you generate meaningful variable names based on a description and selected format (e.g. camelCase, snake_case). It uses GigaChat from Sber to generate the names.

---

## 🔍 Description

You enter a description of the variable and select a naming style (like `camelCase`, `snake_case`, etc.), then the app sends a request to the GigaChat model, which returns a suitable variable name.

### Supported Styles:
- `camelCase`
- `PascalCase`
- `snake_case`
- `MACRO_CASE`
- `kebab-case`

---

## 🖥️ Technologies Used

- Python
- Flask — for building the web server
- LangChain — for working with LLMs
- GigaChat — for generating variable names
- HTML/CSS/JS — front-end logic
- Bootstrap — for UI styling

---

## 📁 Project Structure

```
.
├── static/
│   ├── script.js     # Client-side logic
│   └── style.css     # CSS styles
├── templates/
│   └── index.html    # Main HTML page
├── app.py            # Flask entry point
├── namer.py          # GigaChat interaction logic
└── README.md         # This file
```

---

## ⚙️ Installation and Setup

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/variable-namer.git
cd variable-namer
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables:

Create a `.env` file or export the variables manually:

```bash
export GIGACHAT_KEY="your_token"
export GIGACHAT_MODEL="GigaChat"  # or "GigaChat-Plus" if available
```

### 4. Run the server:

```bash
python app.py
```

Open your browser and go to: [http://localhost:8080](http://localhost:8080)

---

## 📦 Requirements

- Python 3.9+
- Active GigaChat subscription and API token
- Dependencies listed in `requirements.txt`

---

## 💡 Future Improvements

- Add support for saving history of requests
- Implement unit tests
- Switch to async mode for better scalability
- Add Docker support
- Support for other LLMs (e.g., OpenAI, YandexGPT)

---

## 🤝 Contributing

If you'd like to contribute to this project — you're welcome! Feel free to open issues and pull requests.

