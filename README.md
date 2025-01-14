# Robotic Camera Man

This project combines computer vision with Arduino-based hardware control to create an automated camera operator.

## Overview

This system uses OpenCV to detect and track colored objects in real-time video feed. Based on the object's position, it sends commands to an Arduino-controlled servo motor to adjust the camera's position, creating a smooth tracking effect.

## Features

- Real-time color-based object detection
- Automatic servo control for camera positioning
- Configurable HSV color range for object detection
- Buffer-based position tracking
- Adjustable detection sensitivity
- Live video feed display with object highlighting
- Serial communication with Arduino

## Prerequisites

- Python 3.x
- OpenCV
- NumPy
- pySerial
- imutils
- Arduino board with servo motor setup

## Installation

1. Clone this repository
2. Install required Python packages:
```bash
pip install opencv-python numpy pyserial imutils
```
3. Connect your Arduino board and update the serial port in the code:
```python
ser = serial.Serial('/dev/cu.usbmodem143301', 9600)  # Update with your port
```

## Usage

Run the script using:
```bash
python robotic_cameraman.py [-v VIDEO] [-b BUFFER]
```

Arguments:
- `-v`, `--video`: Path to input video file (optional, defaults to webcam)
- `-b`, `--buffer`: Maximum buffer size for position tracking (default: 32)

Press 'q' to quit the application.

## Configuration

The color detection range can be adjusted by modifying the HSV bounds:
```python
lowerBound = np.array([29, 86, 6])
upperBound = np.array([64, 255, 255])
```

Servo movement thresholds can be adjusted in the main loop:
```python
if x1 < 75:  # Left threshold
    pos += 2
if x1 > 105:  # Right threshold
    pos -= 2
```

## Technical Details

- The system uses HSV color space for more robust color detection
- Object tracking is implemented using contour detection
- Servo position is updated based on the object's X-coordinate
- The camera position is adjusted when the object moves beyond defined thresholds
- Implements erosion and dilation for noise reduction

## Author

Created by Zak Mineiko
- Initial Creation: February 4, 2021
- Last Modified: October 22, 2022



## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
