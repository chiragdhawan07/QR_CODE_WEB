from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_generated = False
    if request.method == 'POST':
        data = request.form['data']
        if data.strip():
            qr = qrcode.QRCode(version=3, box_size=8, border=4)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            img.save('static/qr_code.png')
            qr_generated = True
    return render_template('index.html', qr_generated=qr_generated)

if __name__ == '__main__':
    app.run(debug=True)
