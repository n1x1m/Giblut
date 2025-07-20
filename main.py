from flask import Flask, request, send_file
from PIL import Image
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Avatar Hair Renderer is running!'

@app.route('/generate')
def generate():
    hair = request.args.get('hair', 'black_png')
    base_path = 'assets/base.png'
    hair_path = f'assets/{hair}.png'
    output_path = 'static/output.png'

    if not os.path.exists(base_path) or not os.path.exists(hair_path):
        return 'Missing image files', 404

    base = Image.open(base_path).convert('RGBA')
    hair_img = Image.open(hair_path).convert('RGBA')
    result = Image.alpha_composite(base, hair_img)
    result.save(output_path)

    return send_file(output_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)