from osgeo import gdal
import cv2
import os
import time

''' 
This command uses the following options:
    -of JPEG specifies the output format as JPEG.
    -ot Byte specifies the output data type as Byte (8-bit unsigned integer).
    -b 1 specifies that band 1 (the grayscale band) should be included in the output image.
    -colorinterp gray specifies that the color table should be interpreted as a grayscale ramp.
    -expand rgb specifies that the output image should be a true color image with 3 bands (red, green, and blue).
    NOTE: This command will convert the TIFF image to a JPEG image with 3 bands, each with 8-bit depth, 
    resulting in a total of 3 x 8 = 24 bits per pixel. The color table will be interpreted as a grayscale ramp, 
    which will be used to map the pixel values in the input image to colors in the output image.

    Python Version: 3.11
    GDAL Version: 3.4.3
'''


def convert_tiff_to_three_band(picture_name, output_name, base_path):
    options_list = [
        '-ot UInt16',
        '-b 1',
        '-b 1',
        '-b 1',
    ]
    options_string = " ".join(options_list)

    input_path = os.path.join(base_path, f"{picture_name}.tiff")
    output_path = os.path.join(base_path, f"{output_name}.tiff")

    gdal.Translate(output_path, input_path, options=options_string)


def convert_tiff_to_jpg(output_name, output_jpg, base_path):
    #scale = "65535"
    options_list = [
        '-ot Byte',
        '-of JPEG',
        '-b 1',
        '-b 2',
        '-b 3',
        '-co QUALITY=100',
        '-outsize 24000 16000',
        '-scale 65535',
    ]
    options_string = " ".join(options_list)

    input_path = os.path.join(base_path, f"{output_name}.tiff")
    output_path = os.path.join(base_path, f"{output_jpg}.jpg")

    gdal.Translate(output_path, input_path, options=options_string)


def create_folder(folder_name, base_path):
    path = os.path.join(base_path, folder_name)
    if not os.path.exists(path):
        os.makedirs(path)


def crop(picture_name, output_jpg, base_path):
    img_path = os.path.join(base_path, f"{output_jpg}.jpg")
    img = cv2.imread(img_path)

    if img is None:
        print(f"Error: Unable to load image at {img_path}")
        return

    crop_folder = os.path.join(base_path, output_jpg)

    for r in range(0, img.shape[0], 800):
        for c in range(0, img.shape[1], 800):
            crop_path = os.path.join(crop_folder, f"{picture_name}_{r}_{c}.jpg")
            cv2.imwrite(crop_path, img[r:r + 800, c:c + 800, :])


def timer(start_time):
    elapsed_time = time.time() - start_time
    print(f"It took {elapsed_time:.2f} seconds to run")


if __name__ == '__main__':
    start_time = time.time()

    base_path = "C:\\example\\example\\example\\example"
    picture_names = input("Enter the TIFF picture names separated by commas: ").split(',')
    picture_names = [name.strip() for name in picture_names]

    for picture_name in picture_names:
        if not os.path.isfile(os.path.join(base_path, f"{picture_name}.tiff")):
            print(f"Image not found: {picture_name}.tiff")
            continue

        output_name = f"{picture_name}ConvertTo3BandTiff"
        output_jpg = f"{picture_name}LastJPGV"

        convert_tiff_to_three_band(picture_name, output_name, base_path)
        convert_tiff_to_jpg(output_name, output_jpg, base_path)
        create_folder(output_jpg, base_path)
        crop(picture_name, output_jpg, base_path)

    timer(start_time)
