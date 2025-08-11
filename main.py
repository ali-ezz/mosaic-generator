import os
import cv2
import numpy as np
from PIL import Image
import glob
from tqdm import tqdm
import math

def load_video_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    cap.release()
    return frames

def create_image_mosaic(main_image_path, output_path, num_copies=None):
    main_image = Image.open(main_image_path).convert('RGB')
    width, height = main_image.size
    
    if num_copies is None:
        grid_w = max(1, width // 64)
        grid_h = max(1, height // 64)
    else:
        grid_w = int(math.sqrt(num_copies))
        grid_h = int(math.sqrt(num_copies))

    tile_w = width // grid_w
    tile_h = height // grid_h
    
    output_image = Image.new('RGB', (width, height))
    
    tile = main_image.resize((tile_w, tile_h))

    for j in tqdm(range(grid_h), desc="Processing image rows"):
        for i in range(grid_w):
            region = main_image.crop((i * tile_w, j * tile_h, (i + 1) * tile_w, (j + 1) * tile_h))
            avg_color = np.mean(np.array(region), axis=(0, 1)).astype(int)
            
            color_overlay = Image.new('RGB', (tile_w, tile_h), tuple(avg_color))
            tinted_tile = Image.blend(tile, color_overlay, 0.5)
            
            output_image.paste(tinted_tile, (i * tile_w, j * tile_h))
            
    output_image.save(output_path)
    print(f"Image mosaic saved to {output_path}")

def create_video_mosaic(main_video_path, output_path, num_copies=None):
    frames = load_video_frames(main_video_path)
    if not frames:
        print("No frames found in video.")
        return

    height, width, _ = frames[0].shape
    
    if num_copies is None:
        grid_w = max(1, width // 64)
        grid_h = max(1, height // 64)
    else:
        grid_w = int(math.sqrt(num_copies))
        grid_h = int(math.sqrt(num_copies))
        
    num_cells = grid_w * grid_h
    total_frames = len(frames)

    tile_w = width // grid_w
    tile_h = height // grid_h
    
    tile_video = [cv2.resize(frame, (tile_w, tile_h)) for frame in frames]
    
    cell_offsets = [(i * (total_frames // num_cells)) % total_frames for i in range(num_cells)]

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, 30.0, (width, height))

    for frame_idx in tqdm(range(total_frames), desc="Processing video frames"):
        output_frame = np.zeros((height, width, 3), dtype=np.uint8)
        for cell_idx in range(num_cells):
            r = cell_idx // grid_w
            c = cell_idx % grid_w
            
            offset = cell_offsets[cell_idx]
            tile_frame_index = (frame_idx + offset) % total_frames
            tile_frame = tile_video[tile_frame_index]
            
            original_region = frames[frame_idx][r*tile_h:(r+1)*tile_h, c*tile_w:(c+1)*tile_w]
            avg_color = np.mean(original_region, axis=(0, 1))
            
            color_overlay = np.full((tile_h, tile_w, 3), avg_color, dtype=np.uint8)
            tinted_tile = cv2.addWeighted(tile_frame, 0.5, color_overlay, 0.5, 0)
            
            output_frame[r*tile_h:(r+1)*tile_h, c*tile_w:(c+1)*tile_w] = tinted_tile
        
        out.write(cv2.cvtColor(output_frame, cv2.COLOR_RGB2BGR))
    
    out.release()
    print(f"Video mosaic saved to {output_path}")

def cli_menu():
    print("Welcome to the Mosaic Generator")
    input_files = glob.glob("input/*.*")
    if not input_files:
        print("No files found in the 'input' folder.")
        return

    print("Available files:")
    for i, f in enumerate(input_files):
        print(f"{i+1}. {f}")
    
    choice = int(input("Choose a file by number: ")) - 1
    main_path = input_files[choice]
    
    use_default = input("Use default number of copies? (y/n): ").strip().lower()
    if use_default == 'y':
        num_copies = None
    else:
        num_copies = int(input("Enter number of copies (e.g., 64): "))
    
    output_path = input("Enter output file path (e.g., output/result.mp4): ")

    if main_path.lower().endswith(('.mp4', '.mov', '.avi')):
        create_video_mosaic(main_path, output_path, num_copies)
    elif main_path.lower().endswith(('.jpg', '.jpeg', '.png')):
        create_image_mosaic(main_path, output_path, num_copies)
    else:
        print("Unsupported file type.")

if __name__ == "__main__":
    cli_menu()
