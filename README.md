# QR Code Access Control

This project demonstrates a QR code-based access control system using OpenCV and the `pyzbar` library. The script reads webcam input, detects QR codes, and checks if the decoded value is in a predefined list of access codes. If the value is found, it displays "Access Granted" along with the decoded string and draws a bounding box around the QR code; otherwise, it displays "Access Denied".

## Project Structure

- `qr_code_access.py`: Main script to read webcam input, detect and decode QR codes, and display access control messages.
- `requirements.txt`: List of dependencies required to run the project.

## Setup

1. **Clone the repository**
   ```bash
   https://github.com/sairam-penjarla/QR-Code.git
   ```

2. **Install the required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script**
   ```bash
   python qr_code_access.py
   ```

## Usage

1. **Launch the script**:
   ```bash
   python qr_code_access.py
   ```
   This will start your webcam and open a window displaying the video feed.

2. **Center Square**:
   - A blue square will appear in the middle of the video feed. Position your QR code within this square for best results.

3. **Access Control**:
   - If the QR code is successfully decoded and the value is found in the predefined access codes list, "Access Granted" along with the decoded string will be displayed above the QR code, and a green bounding box will be drawn around the QR code.
   - If the value is not found in the access codes list, "Access Denied" will be displayed, and a red bounding box will be drawn around the QR code.

4. **Exit**:
   - Press the 'q' key to exit the webcam feed and close the window.

## Predefined Access Codes

The list of access codes can be modified in the script. By default, it includes:
```python
access_codes = ["12345", "67890", "ABCDE"]
```

## Dependencies

The project requires the following dependencies, which are listed in the `requirements.txt` file:
- `opencv-python==4.5.3.56`
- `pyzbar==0.1.8`
- `numpy==1.21.2`

To install the dependencies, run:
```bash
pip install -r requirements.txt
```

## Notes

- Ensure you have a working webcam connected to your computer.
- Adjust the size and position of the center square if necessary, depending on your webcam's resolution and QR code size.

## References

- OpenCV: https://opencv.org/
- Pyzbar: https://github.com/NaturalHistoryMuseum/pyzbar

This project can be further extended to include additional features such as logging access attempts, integrating with a database, or using more advanced QR code detection and decoding techniques.