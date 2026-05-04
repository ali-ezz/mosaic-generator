# Mosaic Generator

![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-experimental-orange)
![Language](https://img.shields.io/badge/language-Python-blue)

Mosaic Generator is an interactive Python CLI for generating image and video mosaics from local media.

## Features

- Generate image mosaics from photographs
- Generate video mosaics from local video files
- Interactive CLI selects media from `input/`
- Customizable mosaic density using number of copies
- Works with standard image and video file formats

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Place one or more image/video files in `input/`.
3. Run the CLI:
```bash
python main.py
```
4. Enter the number of copies or choose the default, then provide an output path.

## Usage examples

- Create a mosaic from an image in `input/` and save to `output/result.jpg`:
```bash
python main.py
```

- Create a mosaic from a video in `input/` and save to `output/result.mp4`:
```bash
python main.py
```

The script will list detected files from `input/` and prompt you to choose one.

## Project layout

```
.
├── main.py
├── README.md
├── requirements.txt
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── CODEOWNERS
├── CHANGELOG.md
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
├── input/          # Place source images or videos here
└── output/         # Generated mosaics are written here
```

## Contributing

See `CONTRIBUTING.md` for contribution guidelines and branch naming.

## License and policies

- License: `MIT`
- Code of conduct: `CODE_OF_CONDUCT.md`
- Security policy: `SECURITY.md`

## Notes

- `input/` should contain your source `.jpg`, `.png`, `.mp4`, `.mov`, or `.avi` files.
- The output file can be any valid image or video extension supported by OpenCV.
