import os
from flask import Flask, render_template, request, send_from_directory
from flask_session import Session
from moviepy.editor import VideoFileClip, AudioFileClip
from PIL import Image

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['VIDEO_FOLDER'] = '/workspaces/131765527/final/videos'
app.config['IMAGE_FOLDER'] = '/workspaces/131765527/final/images'
app.config['AUDIO_FOLDER'] = '/workspaces/131765527/final/audios'
Session(app)

os.makedirs(app.config['VIDEO_FOLDER'], exist_ok=True)
os.makedirs(app.config['IMAGE_FOLDER'], exist_ok=True)
os.makedirs(app.config['AUDIO_FOLDER'], exist_ok=True)

def save_file(file, folder):
    filename_with_extension = file.filename
    filename, file_format = os.path.splitext(filename_with_extension)
    file_path = os.path.join(folder, filename_with_extension)
    file.save(file_path)
    return filename, file_format.lower(), file_path

def convert_video(file_path, filename, file_format, formats, folder):
    clip = VideoFileClip(file_path)
    fps = clip.fps
    filenames = []
    for format in formats:
        output_path = os.path.join(folder, f"{filename}{format}")
        if format == '.mkv':
            codec = 'libvpx'
        else:
            codec = 'libx264'
        if format == '.gif':
            clip.write_gif(output_path, fps=fps)
        else:
            clip.write_videofile(output_path, fps=fps, codec=codec)
        filenames.append(f"{filename}{format}")
    clip.close()
    return filenames

def convert_image(file_path, filename, file_format, formats, folder):
    image = Image.open(file_path)
    filenames = []
    for format in formats:
        output_format = format[1:].upper()
        if output_format == 'JPG':
            output_format = 'JPEG'

        elif output_format == 'WEBP':
            output_format = 'WEBP'

        output_path = os.path.join(folder, f"{filename}.{format[1:]}")

        if image.mode == 'RGBA' and output_format in ['JPEG', 'BMP']:
            image = image.convert('RGB')

        image.save(output_path, output_format)
        filenames.append(f"{filename}.{format[1:]}")
    image.close()
    return filenames

def convert_audio(file_path, filename, file_format, formats, folder):
    audio = AudioFileClip(file_path)
    filenames = []
    for format in formats:
        output_path = os.path.join(folder, f"{filename}{format}")
        if format == '.ogg':
            codec = 'libvorbis'
        elif format == '.flac':
            codec = 'flac'
        else:
            codec = None
        audio.write_audiofile(output_path, codec=codec)
        filenames.append(f"{filename}{format}")
    audio.close()
    return filenames

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/video", methods=["GET", "POST"])
def video():
    if request.method == "POST":
        if not request.files['file']:
            return render_template("video.html", error="please upload your video file")

        file = request.files['file']
        filename, file_format, file_path = save_file(file, app.config['VIDEO_FOLDER'])
        formats = [".mp4", ".mkv", ".mov", ".avi", ".gif"]
        if file_format not in formats:
            return render_template("video.html", error="your file format is not supported")
        formats.remove(file_format)
        filenames = convert_video(file_path, filename, file_format, formats, app.config['VIDEO_FOLDER'])
        return render_template("export.html", filenames=filenames, route='/download/videos')
    else:
        return render_template("video.html")

@app.route("/image", methods=["GET", "POST"])
def image():
    if request.method == "POST":
        if not request.files['file']:
            return render_template("image.html", error="please upload your image file")

        file = request.files['file']
        filename, file_format, file_path = save_file(file, app.config['IMAGE_FOLDER'])
        formats = [".jpeg", ".png", ".bmp", ".gif", ".ppm", ".tiff", ".jpg", ".webp"]  # Added .webp to supported formats
        if file_format not in formats:
            return render_template("image.html", error="your file format is not supported")
        formats.remove(file_format)
        filenames = convert_image(file_path, filename, file_format, formats, app.config['IMAGE_FOLDER'])
        return render_template("export.html", filenames=filenames, route='/download/images')
    else:
        return render_template("image.html")

@app.route("/audio", methods=["GET", "POST"])
def audio():
    if request.method == "POST":
        if not request.files['file']:
            return render_template("audio.html", error="please upload your audio file")

        file = request.files['file']
        filename, file_format, file_path = save_file(file, app.config['AUDIO_FOLDER'])
        formats = [".mp3", ".wav", ".ogg", ".flac"]
        if file_format not in formats:
            return render_template("audio.html", error="your file format is not supported")
        formats.remove(file_format)
        filenames = convert_audio(file_path, filename, file_format, formats, app.config['AUDIO_FOLDER'])
        return render_template("export.html", filenames=filenames, route='/download/audios')
    else:
        return render_template("audio.html")

@app.route('/download/<filetype>/<filename>')
def download_file(filetype, filename):
    if filetype == 'videos':
        directory = app.config['VIDEO_FOLDER']
    elif filetype == 'images':
        directory = app.config['IMAGE_FOLDER']
    elif filetype == 'audios':
        directory = app.config['AUDIO_FOLDER']

    return send_from_directory(directory, filename)

if __name__ == "__main__":
    app.run(debug=True)
