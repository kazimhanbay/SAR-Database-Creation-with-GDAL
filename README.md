# TIFF-to-JPEG-Converter-and-Cropper



This script converts a TIFF image to a 3-band TIFF image and then to a JPEG image, and crops the JPEG image into 800x800 pixel squares.

<p align="center">
  <img src="https://github.com/tburakozdemir/TIFF-to-JPEG-Converter-and-Cropper/assets/54362580/9c7bcce6-9bc4-443d-9414-b9ab58bd6d3f" style="border-radius: 50px;">
</p>


### Dependencies



The script requires the following packages to be installed:



* `gdal`: This package provides access to a variety of geospatial data formats and allows for reading, writing, and manipulating geospatial data.

* `cv2`: This package is a part of the OpenCV library and provides support for image processing tasks such as reading, writing, and displaying images.

* `os`: This package provides functions for interacting with the operating system, such as creating directories and checking for the existence of files.

* `time`: This package provides functions for working with time, such as measuring elapsed time.

![Python Version](https://img.shields.io/badge/Python-3.11-blue)
![GDAL Version](https://img.shields.io/badge/GDAL-3.8.2-brightgreen)


### Image Conversion Options 📸✨

Elevate your TIFF images to beautiful JPEGs with these fine-tuned options:

  * 🔍 Data Type - -ot Byte
     - Embrace precision with 8-bit unsigned integers. This choice ensures your images are stored in a compact and efficient format, perfect for both quality and practicality.


  * 🌟 Output Format - -of JPEG
     - Opt for JPEG, a format renowned for its balance between high-quality imaging and manageable file sizes. Ideal for web use and easy sharing!


   * 🔵🟢 Color Bands - -b 1, -b 2, -b 3
    Capture the full depth of your images by including:
       * -b 1: The grayscale band, adding depth and detail.
       * -b 2: The green band, highlighting nature's vibrant hues.
       * -b 3: The blue band, bringing in the cool and calm tones.


  * 💎 Pristine Quality - -co QUALITY=100
    - Ensure top-notch clarity by setting the JPEG quality to a perfect 100%. Ideal for when every detail matters and quality cannot be compromised.

  * 📐 Custom Size - -outsize 24000 16000
    - Define your canvas with custom dimensions of 24000x16000 pixels. This setting is perfect for capturing intricate details and expansive landscapes alike.

  * 🌓 Scale Adjustment - scale
    - Fine-tune your images with scale adjustments. Modify the brightness and contrast to suit your artistic vision, bringing a personalized touch to every pixel.

### 🚀 Usage

Unleash the power of image conversion right from your terminal! Here’s how to get started:
🖥️ Running the Script

Fire up the magic with a simple command:

 ``` python tiff_to_jpeg_converter_and_cropper.py ``` 

### 🧩 User Inputs

* The script will playfully ask you for:

   * TIFF Picture Name: Whisper the name of your TIFF image, ready to be transformed.
   * 3 Band TIFF Image Name: Dream up a name for your soon-to-be-created 3-band TIFF masterpiece.
   * JPEG Name: Conjure a name for the final JPEG image, your digital canvas.

### 🎨 The Transformation Journey

* Watch as your images undergo a magical metamorphosis:

    * Three-Band Conversion: Using convert_tiff_to_three_band, your TIFF is reborn with three bands (-b 1, -b 1, -b 1), shining in 16-bit unsigned integer glory (-ot UInt16).
    * JPEG Genesis: With convert_tiff_to_jpg, your image leaps into the JPEG realm. We talk 8-bit finesse (-ot Byte), a trio of bands (-b 1, -b 2, -b 3), impeccable quality (-co QUALITY=100), and a scaling adventure (scale factor 65535).
    * Folder Creation: Like a wizard, create_folder summons a new home for your TIFF, a cozy folder bearing its name.
    * Cropping Magic: The crop spell slices your JPEG into perfect 800x800 squares, each finding its place in the newly conjured folder.
    * Timekeeper's Tale: As the dust settles, you’ll see the time, in seconds, it took for this enchanting journey.

### 🌟 Glorious Output

* Behold the treasures you’ll uncover:

   * A 3-band TIFF image, proudly wearing the name you chose.
   * A JPEG image, radiant and crisp, also named by you.
   * A folder, echoing the name of your TIFF, filled with neatly cropped JPEG squares.



### Note



The script expects the TIFF image to be located in the current working directory. The output files will also be created in the current working directory.


### Referance 

For setup GDAL with wheel

* https://github.com/cgohlke/geospatial-wheels/releases
* https://opensourceoptions.com/how-to-install-gdal-for-python-with-pip-on-windows/


### License



MIT License



Copyright (c) 2022 Taha Burak Özdemir



Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.



THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
