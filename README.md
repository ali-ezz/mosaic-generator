# Mosaic Generator

A Python tool that creates mosaics from images or videos using small images or videos as tiles.

## Features

- **Image Mosaic**: Rebuild an image using small images as tiles
- **Video Mosaic**: Rebuild a video using small videos as tiles
- Color-based matching algorithm for optimal tile selection
- Support for various image and video formats
- Customizable tile sizes

## Project Structure

```
mosaic_project/
│
├── main.py            # Main script
├── requirements.txt   # Python dependencies
├── tiles_images/      # Folder with tiny images
├── tiles_videos/      # Folder with tiny videos
├── input/
│   ├── image.jpg      # Main image (optional)
│   ├── video.mp4      # Main video (optional)
├── output/            # Output folder for mosaics
```

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Image Mosaic

To create an image mosaic:
```bash
python main.py --mode image --main input/image.jpg --tiles tiles_images --output output/mosaic.jpg
```

### Video Mosaic

To create a video mosaic:
```bash
python main.py --mode video --main input/video.mp4 --tiles tiles_videos --output output/mosaic.mp4
```

### Custom Tile Size

You can specify a custom tile size (width height):
```bash
python main.py --mode image --main input/image.jpg --tiles tiles_images --output output/mosaic.jpg --tile_size 64 64
```

## How It Works

### Image Mosaic Process

1. Load the main image
2. Divide it into a grid based on tile size
3. Load all tile images and resize them to tile size
4. Calculate the average color of each grid cell and each tile image
5. For each grid cell, find the tile with the closest matching average color
6. Place the selected tiles in a new image to create the mosaic
7. Save the final mosaic image

### Video Mosaic Process

1. Load the main video frame by frame
2. Divide each frame into a grid based on tile size
3. Analyze all tile videos to calculate their average colors
4. For each grid cell in each frame, find the tile video with the closest matching average color
5. Create a new video by combining the selected tile videos in a grid
6. Save the final mosaic video

## Tips for Best Results

### Image Mosaics
- Use tile images with varied colors and patterns
- Ensure tile images are roughly the same aspect ratio as your desired tile size
- Higher resolution main images will produce better results with more tiles

### Video Mosaics
- Use tile videos that are the same length as your main video (or can be looped)
- Ensure tile videos have consistent visual content
- All tile videos should be in the same format for best compatibility

## Dependencies

- **OpenCV**: Image and video processing
- **NumPy**: Mathematical operations and array handling
- **MoviePy**: Video editing and processing
- **Pillow**: Image processing
- **tqdm**: Progress bars for long operations

## License

This project is open source and available under the MIT License.
