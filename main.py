import os
from PIL import Image

def collect_images_to_tiff(root_folder, folders_list, output_filename):
    images = []
    for folder_name in folders_list:
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.exists(folder_path):
            for file in os.listdir(folder_path):
                if file.endswith('.jpg') or file.endswith('.png'):
                    image_path = os.path.join(folder_path, file)
                    try:
                        images.append(Image.open(image_path))
                        print(f"Added image: {image_path}")
                    except Exception as e:
                        print(f"Failed to open image {image_path}: {e}")
        else:
            print(f"Folder not found: {folder_path}")

    if images:
        images[0].save(output_filename, save_all=True, append_images=images[1:])
        print(f"Saved {len(images)} images to {output_filename}")
    else:
        print("No images found to merge.")

root_folder = './Images'
folders_list = ['1388_12_Наклейки 3-D_3']
output_filename = 'Result.tif'
collect_images_to_tiff(root_folder, folders_list, output_filename)


