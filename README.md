# 🔳 QR Code Generator (Python + Flask)

This is a simple yet stylish QR Code Generator web application built using Python, Flask, and HTML/CSS. Enter any text or link, and instantly generate a downloadable QR code image.

---

## 🚀 Features

- 🔸 Generate QR code for any text or link.  
- 🔸 Clean and responsive web UI.  
- 🔸 Built with Flask (Python backend).  
- 🔸 Lightweight — no frontend JavaScript.  
- 🔸 QR image saved and served from the `/static` folder.

---

## 📸 How It Works

1. User inputs text or a URL in the field.
2. On clicking Generate QR, a POST request is sent to Flask.
3. The backend generates the QR image and saves it as **static/qr_code.png**.
4. The image is rendered on the page via **Jinja2 templating**.

---

## 🧠 Technologies Used

- Python
- Flask
- HTML/CSS (No JS)
- qrcode (Python library)
- Pillow (image processing)

---

## 🛠️ Installation & Setup

```bash
git clone https://github.com/yourusername/qr-code-generator.git
cd qr-code-generator
pip install flask qrcode pillow
```

## ▶️ Run the App

```bash
python app.py
```

## Then open your browser and go to:

```bash
http://127.0.0.1:5000
```




