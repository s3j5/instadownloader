from flask import Blueprint, render_template, request, jsonify
from app.services.downloader import download_instagram, download_audio

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')


@main.route('/download/instagram', methods=['POST'])
def insta():
    data = request.get_json()
    url = data.get('url')
    return jsonify(download_instagram(url))



@main.route('/download/audio', methods=['POST'])
def audio():
    data = request.get_json()
    url = data.get('url')
    return jsonify(download_audio(url))

