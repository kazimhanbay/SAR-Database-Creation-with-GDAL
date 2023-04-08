# TIFF-to-JPEG-Converter-and-Cropper



This script converts a TIFF image to a 3-band TIFF image and then to a JPEG image, and crops the JPEG image into 800x800 pixel squares.



### Dependencies



The script requires the following packages to be installed:



* `gdal`: This package provides access to a variety of geospatial data formats and allows for reading, writing, and manipulating geospatial data.

* `cv2`: This package is a part of the OpenCV library and provides support for image processing tasks such as reading, writing, and displaying images.

* `os`: This package provides functions for interacting with the operating system, such as creating directories and checking for the existence of files.

* `time`: This package provides functions for working with time, such as measuring elapsed time.

### Options

The script uses the following options to convert the TIFF image to a JPEG image:

   * -ot Byte: specifies the output data type as Byte (8-bit unsigned integer).
   * -of JPEG: specifies the output format as JPEG.
   * -b 1: specifies that band 1 (the grayscale band) should be included in the output image.
   * -b 2: specifies that band 2 (the green band) should be included in the output image.
   * -b 3: specifies that band 3 (the blue band) should be included in the output image.
   * -co QUALITY=100: sets the JPEG quality to 100%.
   * -outsize 24000 16000: sets the output image size to 24000x16000 pixels.
   * scale: sets the scale factor for the pixel values. The default is 1.0, but you can change this value to adjust the brightness and contrast of the output image.



### Usage



To use the script, run the following command in the terminal:



```python tiff_to_jpeg_converter_and_cropper.py```



The script will prompt the user for the following inputs:



* TIFF picture name: The name of the TIFF image to be converted.

* 3 band TIFF image name: The name to be given to the 3-band TIFF image created by the script.

* JPEG name: The name to be given to the JPEG image created by the script.



### The script will then perform the following steps:



1) Convert the TIFF image to a 3-band TIFF image using the convert_tiff_to_tree_band function. The options passed to the gdal.Translate function specify that the output data type should be unsigned 16-bit integer ('-ot UInt16'), and that all 3 bands ('-b 1', '-b 1', '-b 1') should be included in the output image.



2) Convert the 3-band TIFF image to a JPEG image using the convert_tiff_to_jpg function. The options passed to the gdal.Translate function specify that the output data type should be 8-bit unsigned integer ('-ot Byte'), and that all 3 bands ('-b 1', '-b 2', '-b 3') should be included in the output image. The output JPEG file will have a quality of 100 ('-co QUALITY=100') and the pixel values in the input image will be scaled by the specified scale factor ('65535').



3) Create a folder with the same name as the output TIFF image, if it doesn't already exist, using the create_folder function.



4) Use the crop function to crop the JPEG image into 800x800 pixel squares and save each cropped image in the folder created in step 3.



5) Print the elapsed time in seconds that it took for the script to run.



### Output



The script will generate the following output files:



* A 3-band TIFF image with the name specified by the user.

* A JPEG image with the name specified by the user.

* A folder with the same name as the output TIFF image, containing cropped versions of the JPEG image.



### Note



The script expects the TIFF image to be located in the current working directory. The output files will also be created in the current working directory.



### License



MIT License



Copyright (c) 2022 Taha Burak Özdemir



Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.



THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
