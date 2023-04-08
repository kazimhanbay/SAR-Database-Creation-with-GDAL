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


def convert_tiff_to_tree_band(picture_name, output_name):
    options_list = [
        '-ot UInt16',
        '-b 1',
        '-b 1',
        '-b 1',
    ]
    options_string = " ".join(options_list)

    # Set the file path
    input_path = f"C:\\Users\\example\\example\\example\\{picture_name}.tiff"
    output_path = f"C:\\Users\\example\\example\\example\\{output_name}.tiff"

    gdal.Translate(output_path, input_path, options=options_string)


def convert_tiff_to_jpg(output_name, output_jpg):
    scale = "65535"
    options_list = [
        '-ot Byte',
        '-of JPEG',
        '-b 1',
        '-b 2',
        '-b 3',
        '-co QUALITY=100',
        '-outsize 24000 16000',
        scale,
    ]
    options_string = " ".join(options_list)

    input_path = f"{output_name}.tiff"
    output_path = f"{output_jpg}.jpg"

    gdal.Translate(output_path, input_path, options=options_string)


def create_folder(folder_name):
    path = f"{folder_name}"
    if not os.path.exists(path):
        os.makedirs(path)


def crop(output_jpg):
    img = cv2.imread(f"{output_jpg}.jpg")
    for r in range(0, img.shape[0], 800):
        for c in range(0, img.shape[1], 800):
            cv2.imwrite(f"{output_jpg}\\img{r}_{c}.jpg",
                        img[r:r + 800, c:c + 800, :])


if __name__ == '__main__':
    start_time = time.time()

    picture_name = input("What is the TIFF picture name? ")

    # Automated naming of output files
    output_name = f"{picture_name}ConvertTo3BandTiff"
    output_jpg = f"{picture_name}LastJPGV"

    convert_tiff_to_tree_band(picture_name, output_name)
    convert_tiff_to_jpg(output_name, output_jpg)
    create_folder(output_jpg)
    crop(output_jpg)
    
    #Timer
    elapsed_time = int(float(time.time() - start_time))
    print(f"It took {elapsed_time} seconds to run")

