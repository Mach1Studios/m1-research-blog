#!/usr/bin/env python3
"""
Script to convert Apple Spatial Audio diagrams to dark-theme friendly versions.
This script converts black lines and text to light colors while preserving white fills.
"""

import os
import sys

def install_pillow():
    """Install Pillow if not available"""
    try:
        import subprocess
        print("Installing Pillow...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
        print("Pillow installed successfully!")
        return True
    except Exception as e:
        print(f"Failed to install Pillow: {e}")
        return False

def process_image(input_path, output_path):
    """Convert black lines/text to light colors for dark theme compatibility"""
    try:
        from PIL import Image, ImageOps
        
        # Open the image
        img = Image.open(input_path)
        img = img.convert("RGBA")
        
        # Get image data
        data = img.getdata()
        new_data = []
        
        for item in data:
            r, g, b, a = item
            
            # If pixel is black or very dark (lines/text), make it light gray
            if r < 50 and g < 50 and b < 50 and a > 200:
                # Convert black to light gray (#CCCCCC)
                new_data.append((204, 204, 204, a))
            # If pixel is white or very light (fills), keep it white
            elif r > 200 and g > 200 and b > 200:
                new_data.append((255, 255, 255, a))
            # For other colors (like red arrows), keep them as is
            else:
                new_data.append(item)
        
        # Update image data
        img.putdata(new_data)
        
        # Save the modified image
        img.save(output_path, "PNG")
        print(f"Processed: {input_path} -> {output_path}")
        return True
        
    except ImportError:
        print("PIL/Pillow not available. Attempting to install...")
        if install_pillow():
            # Retry after installation
            return process_image(input_path, output_path)
        else:
            return False
    except Exception as e:
        print(f"Error processing {input_path}: {e}")
        return False

def main():
    """Main function to process Apple Spatial Audio diagrams"""
    base_dir = "content/posts/resources/observations-limitations-of-atmos-for-spatial"
    
    images_to_process = [
        "atmos-panningspace-1.png",
        "atmos-panningspace-2.png"
    ]
    
    for image_name in images_to_process:
        input_path = os.path.join(base_dir, image_name)
        
        # Create dark theme version with suffix
        name_parts = image_name.rsplit('.', 1)
        output_name = f"{name_parts[0]}-dark.{name_parts[1]}"
        output_path = os.path.join(base_dir, output_name)
        
        if os.path.exists(input_path):
            success = process_image(input_path, output_path)
            if success:
                print(f"✓ Created dark theme version: {output_name}")
            else:
                print(f"✗ Failed to process: {image_name}")
        else:
            print(f"✗ Image not found: {input_path}")

if __name__ == "__main__":
    main()