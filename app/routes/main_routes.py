from flask import Blueprint, render_template, request, jsonify
from app.services.downloader import download_instagram, download_audio

from flask import send_from_directory

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')


@main.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')


@main.route('/sitemap.xml')
def sitemap():
    return app.send_static_file('sitemap.xml')

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

