# End of 2nd year project: <br> Raspberry Pi 3 Coin Recognition System

> Created by [Dhouha GAOUD](https://github.com/Dhouhaga) and [Khalil OUALI](https://github.com/KhalilOuali).
Proposed and supervised by Prof. Kamel ECHAIEB.

## Context

This was our end-of-year project for the second year of our Computer Engineering degree (LCE-IOT 2) at the Faculty of Scicences of Tunis (FST).

## Objective

An embedded system which can take a photo of some coins, recognize the coins in the photo, calculate their sum, and inform the user of the sum. It is principally meant for use by the blind and the visually-impaired, but there are other potential applications.

## Methodology

1. Analyze and research the issue, as well as available solutions and their shortcomings.
2. Design the system and outline its specifications by defining the functional and non-functional requirements, detailing the necesssary hardware and software components, and modeling a potential solution.
3. Research and select adequate components and technologies.
4. Create a functional prototype using the selected components and techonlogies.
   1. Setup and configure the hardware and software environment.
   2. Build an image dataset and train a custom image-recognition model.
   3. Write a program which makes use of the model and delivers the desired fucntionality.

## Final Prototype

### Hardware

- Platform: Raspberry Pi 3 Model B+.
- Main peripherals: Raspberry Pi Camera, GPIO Button, Speaker, Power adapter.
- Additional peripherals: Display, Mouse, Keyboard.

### Software

- Language: Python.
- Image recognition library: Detecto / PyTorch.
- Main functionality: GPIO interrupt detection, Photo capture, Image recognition, TTS audio output.
- Additional functionality: Activity and performance logging.

### Operation

Once the system is on and the python script is launched, the user can aim the camera at the coins and press the button to begin the detection. After detecting the coins and calculating their sum, the program outputs the result via audio.

### Limitations and Prospects

Due to the lack of time and resources, the project has a few shortcomings.

- The prototype is not yet portable. It would need to be packaged and attached to a battery for portable use.
- The system's performance is utterly impractical as the program is slow and highly inaccurate. A TF Lite model trained on a better dataset would likely yield far improved results.

## Further Details

You can find more information in the presentation, report, and other files in the repo.
