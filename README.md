# Morse Code Translator

## Overview
This project implements a Morse Code Translator using an **Arduino Uno**, a **breadboard**, **wires**, **push buttons**, a **buzzer**, **LED**, and **servo motors**. The translator supports both text-to-Morse and Morse-to-text conversion, providing visual, auditory, and mechanical feedback. The project leverages the **AADFramework** for Arduino component abstraction and control.

---

## Features

### Input and Output
- **Morse Input**: Enter Morse Code via a push button:
  - Short press for `.` (dot)
  - Long press for `-` (dash)
- **Text Input**: Convert text to Morse Code using pre-defined mappings.
- **Output Modes**:
  - Audible feedback via a buzzer for Morse signals.
  - Visual feedback with an LED.
  - Mechanical feedback via servo motors that represent the translated text characters.

### Components and Functionality
1. **Buzzer**: Emits sound for Morse Code signals (short or long).
2. **LED**: Lights up during buzzer activity for visual confirmation.
3. **Push Buttons**:
   - Morse button for entering dots and dashes.
   - Space button for text-to-Morse conversion.
   - Translate button to convert entered Morse to text.
   - Delete button to edit the input.
4. **Servo Motors**:
   - Four servo motors (`xMotor`, `yMotor`, `zMotor`, `dMotor`) represent letters, numbers, and spaces in the translated text using angular positions.
5. **Text-to-Morse and Morse-to-Text Conversion**:
   - Converts text into Morse Code with auditory and visual feedback.
   - Decodes Morse Code back into text using pre-mapped symbols.

### Other Features
- Input validation to ensure proper Morse Code formatting.
- Feedback for invalid or incomplete Morse sequences.
- Smooth servo motor transitions with home position resets.
- Support for special characters, numbers, and spaces.

---

## Components Used
- **Arduino Uno**: Microcontroller for managing input and output.
- **Breadboard and Wires**: Circuit connections.
- **Push Buttons**: Input devices for Morse and text conversion.
- **Buzzer and LED**: Provide audio-visual feedback.
- **Servo Motors**: Mechanically represent translated text characters.

---

## AADFramework Integration
This project utilizes the **AADFramework** for managing Arduino components:
- **DigitalInput**: For push button inputs.
- **DigitalOutput**: For controlling the buzzer and LED.
- **ServoMotor**: For handling servo motor actions with defined angular limits and home positions.

---

## Installation and Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/Cayden2606/morse-code-translator.git
   ```
2. Open the Arduino IDE and upload the project code to your Arduino Uno.
3. Connect the components to the Arduino Uno as per the pin configuration:
   - **Buzzer**: Pin 12
   - **LED**: Pin 5
   - **Push Buttons**: Pins 2, 3, 4, 6
   - **Servo Motors**: Pins 8, 9, 10, 11
4. Install the **AADFramework** and ensure it’s available in your Python environment.
5. Run the Python script:
   ```bash
   python Morse_Code_Translator.py
   ```

---

## Usage
1. **Morse Input Mode**:
   - Use the Morse button to input dots and dashes.
   - Press the Translate button to decode the input into text.
2. **Text-to-Morse Mode**:
   - Input text when prompted, and the program will output Morse Code.
3. Observe outputs via:
   - Buzzer and LED for Morse Code.
   - Servo motors for character representation.

---

## Contributing
Contributions are welcome! Feel free to fork the repository, open issues, or submit pull requests for additional features or bug fixes.

---

## License
This project is licensed under the [MIT License](LICENSE).

---
