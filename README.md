# PYTHON CAMERA CLASSIFIER

This code uses your camera to identify objects in photos, such as a phone or book

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

```
python  ^3.8
Pillow  ^8.1.0
sklearn  ^0.0
numpy  ^1.19.4
opencv-python  ^4.5.1
```

### Installing

To install all that you will need

```
python -m poetry install
``` 
## Run

```
poetry run python main.py
```

This command will create one, and a popup in which you must enter the name of the first class of the object, for example cell, after clicking Ok another window will appear for the same function this time the name of the second class for example book.
After that, the larger window will gain some buttons.
And you will notice that your camera is now active.
One button with the name of the first class and another with the name of the second
Take a first-class object and place it in front of the camera and press the button a few times
Repeat the same process with the other object
After that, click on 'Train Model' to train object recognition
After that place the object in front of the camera and click on 'preview' to see the result.
If you click on 'Automatic preview' the code will automatically take pictures every 15 seconds trying to identify the object in front of the camera

Note: the more photos and the more angles you have, the more accurate the rating will be.

## Authors

* **Anderson F lima**

## Acknowledgments

* This code is for self-improvement only
