# ZetaOne – User Manual

## Table of Contents
1. [Introduction](#introduction)
2. [System Requirements](#system-requirements)
3. [Installation](#installation)
4. [Shortcut Overview](#shortcut-overview)
5. [Button Overview](#button-overview)
9. [Support & Feedback](#support--feedback)

---

## Introduction
ZetaOne is a powerful calculator application offering advanced scientific functions. It is designed for both quick everyday calculations and complex scientific tasks. The user interface is intuitive, providing both novice and experienced users with optimal efficiency and precision.

---

## System Requirements
- **Operating System**: Windows 10 or later
- **Python Version**: Python 3.13 or later

### Libraries
All required libraries are documented in the [requirements](requirements.txt) file.


---

## Installation

Follow the steps below to install and launch ZetaOne on your system. These instructions assume you have Python 3.10 or later installed and available on your `PATH`.

### 1. Obtain the Source Code

- **Download ZIP:**  
  1. Navigate to the [ZetaOne GitHub repository](https://github.com/XenovaStudios/ZetaOne).  
  2. Click **Code → Download ZIP**, then extract the archive to a folder of your choice.

- **Or Clone with Git:**  
  ```bash
  git clone https://github.com/XenovaStudios/ZetaOne.git
  cd ZetaOne
  ```

### 2. Create and Activate a Virtual Environment

> It is recommended to isolate ZetaOne’s dependencies in a virtual environment.

- **Windows (PowerShell / Command Prompt):**  
  ```powershell
  cd ZetaOne
  python -m venv .venv
  .\.venv\Scripts\activate
  ```

- **macOS / Linux (bash, zsh):**  
  ```bash
  cd ZetaOne
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Install Dependencies

With the virtual environment activated, install all required packages:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Launch ZetaOne

From within the project directory and the activated virtual environment, start the application:

```bash
python main.py
```


---

Once these steps complete without error, ZetaOne is ready for use. Enjoy fast, accurate calculations in your new graphical calculator!

---

## Shortcut Overview
| Shortcut        | Function                  |
|-----------------|---------------------------|
| **Ctrl + C**    | Copy                      |
| **Ctrl + V**    | Paste                     |

---

## Button Overview
| Icon / Label | Function                                                                 |
|--------------|---------------------------------------------------------------------------|
| Copy         | Copy current entry to clipboard                                          |
| Paste        | Paste value from clipboard                                               |
| exp          | Enter scientific notation (e.g. `3E12` = 3 × 10<sup>12</sup>)            |
| Lock / Menu  | Open advanced features panel (if unlocked)                               |
| C            | Clear current entry                                                      |
| log          | Return base-10 logarithm of current entry                                |
| ln           | Return natural logarithm (base e) of current entry                       |
| \|x\|        | Return absolute value of current entry                                   |
| √            | Return square root of current entry                                      |
| ^            | Power operator                                                           |
| sin          | Compute sine of current entry                                            |
| cos          | Compute cosine of current entry                                          |
| tan          | Compute tangent of current entry                                         |
| π            | Insert constant π ≈ 3.14159                                              |
| e            | Insert constant e ≈ 2.71828                                              |
| ⌫           | Delete the last character of current entry                               |
| =            | Compute result                                                           |
| ±            | Toggle sign of current entry                                             |

---


## Tips & Notes
- **Unlock Advanced Features**: Enter the secret code and press Enter. Confirm the activation in the message box. The lock button icon should then change from '🔒' to '☰'. Pressing this button will open an additional panel with some advanced features. Feel free to try them out.
- **Clipboard Integration**: Use Copy and Paste to transfer values seamlessly between ZetaOne and other applications.  
- **Error Correction**: Use ⌫ to remove only the last character, avoiding the need to re-enter entire expressions.  
- **Sign Toggle**: Use ± to switch between positive and negative values quickly.

---

## Support & Feedback
This service is provided by Xenova Studios

**Contact:** Xenova@gmx.ch