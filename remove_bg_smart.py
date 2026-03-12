from PIL import Image, ImageDraw
import os

def remove_bg_smart(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    try:
        img = Image.open(input_path).convert("RGBA")
        width, height = img.size
        
        # Create a mask for flood filling
        # We'll use ImageDraw.floodfill to find connected white pixels from the corners
        # But Pillow's floodfill modifies the image directly. 
        # Strategy:
        # 1. Create a binary image where white pixels are 255 and others are 0
        # 2. Flood fill from corners (0,0) with black (0) on this binary image? 
        # Simpler approach manually:
        # standard BFS flood fill from (0,0), (w-1, 0), (0, h-1), (w-1, h-1)
        # if the pixel is "white" ( > threshold), make it transparent.
        
        # Let's implementation a custom BFS for control
        visited = set()
        queue = []
        
        # Seed points: corners
        seeds = [(0, 0), (width-1, 0), (0, height-1), (width-1, height-1)]
        
        pixels = img.load()
        
        # Add valid white seeds to queue
        for x, y in seeds:
            r, g, b, a = pixels[x, y]
            if r > 230 and g > 230 and b > 230: # Threshold for white
                queue.append((x, y))
                visited.add((x, y))
        
        processed_count = 0
        
        while queue:
            x, y = queue.pop(0)
            
            # Make transparent
            pixels[x, y] = (255, 255, 255, 0)
            processed_count += 1
            
            # Check neighbors
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < width and 0 <= ny < height:
                    if (nx, ny) not in visited:
                        r, g, b, a = pixels[nx, ny]
                        # If neighbor is also white, add to queue
                        if r > 230 and g > 230 and b > 230:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
                            
        img.save(output_path, "PNG")
        print(f"Successfully saved smart transparent logo to {output_path}")
        print(f"Processed {processed_count} pixels.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    remove_bg_smart("media/logo-unh.jpg", "media/logo-unh-smart.png")
