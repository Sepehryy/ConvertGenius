# ConvertGenius

[![Video Demo](https://img.shields.io/badge/Video%20Demo-Available-blue)](https://www.youtube.com/watch?v=UFWkUx-mKd0v=UFWkUx-mKd0)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Supported Formats](#supported-formats)
- [Usage](#usage)
- [Tech Stack](#tech-stack)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [Contact](#contact)

## Introduction

Welcome to **ConvertGenius**, a user-friendly web application that allows you to convert images, audio, and video files into various formats effortlessly. Whether you need to convert a video for a different platform, adjust image formats for a specific project, or convert audio files for compatibility, ConvertGenius has you covered.

## Features

- **Multiple Format Support**: Convert between a wide range of formats for videos, images, and audio files.
- **Easy to Use**: Simply upload your file, and ConvertGenius will provide download links for all supported formats.
- **Fast and Efficient**: Built with a focus on performance, ensuring quick conversions without compromising quality.
- **User-Friendly Interface**: Clean and intuitive interface for a seamless user experience.

## Supported Formats

### Video Formats:
- `.mp4`
- `.mkv`
- `.mov`
- `.avi`
- `.gif`

### Image Formats:
- `.jpeg`
- `.png`
- `.bmp`
- `.gif`
- `.ppm`
- `.tiff`
- `.jpg`

### Audio Formats:
- `.mp3`
- `.wav`
- `.ogg`
- `.flac`

## Usage

Here's how to use ConvertGenius once it's up and running:

### 1. Upload a File

- **Video Conversion**:
  - Go to the **Video Format Converter** page by clicking on the **Video** link from the homepage.
  - Click on the **Upload Video** button and select the video file you want to convert.
  - The application supports video formats like `.mp4`, `.mkv`, `.mov`, `.avi`, and `.gif`.

- **Image Conversion**:
  - Navigate to the **Image Format Converter** page by clicking on the **Image** link.
  - Click on the **Upload Image** button and select your image file.
  - Supported image formats include `.jpeg`, `.png`, `.bmp`, `.gif`, `.ppm`, `.tiff`, and `.jpg`.

- **Audio Conversion**:
  - Visit the **Audio Format Converter** page via the **Audio** link.
  - Use the **Upload Audio** button to choose your audio file.
  - Convert between audio formats such as `.mp3`, `.wav`, `.ogg`, and `.flac`.

### 2. Select Format

- Once the file is uploaded, ConvertGenius will automatically detect the current format and list the available formats for conversion.
- Select the desired format(s) for conversion from the options provided.

### 3. Download Converted File

- After conversion, download links for the new file formats will be available.
- Click on the links to download the converted files to your device.

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Bootstrap
- **Template Engine**: Jinja2

## File Structure

### Explanation:

- **`static/`**: Contains static files like CSS stylesheets.
  - **`style.css`**: Stylesheet for the application.
- **`templates/`**: Contains HTML templates for the web pages.
  - **`layout.html`**: The main layout template used across pages.
  - **`index.html`**: Homepage of the application.
  - **`video.html`**: Video conversion page template.
  - **`image.html`**: Image conversion page template.
  - **`audio.html`**: Audio conversion page template.
  - **`export.html`**: Template for displaying conversion results and download links.
- **`app.py`**: The main application file containing the Flask server code.
- **`requirements.txt`**: Lists the dependencies required to run the application.
- **`README.md`**: This file; contains information about the project.

## Contributing

We welcome contributions to ConvertGenius! To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

Please ensure your code follows the project's coding standards and includes appropriate tests.

## Contact

For questions or feedback, feel free to contact us:

- **Email**: sepehryavarzadeh@gmail.com
- **GitHub**: [Sepehryy](https://github.com/Sepehryy)
