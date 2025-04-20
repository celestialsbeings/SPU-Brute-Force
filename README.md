# 🔥 SPU CHECKER PRO 🔥

<div align="center">
  
![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000)
![Python](https://img.shields.io/badge/Python-3.7%2B-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Threading](https://img.shields.io/badge/Threading-Enabled-orange)

</div>

<p align="center">
  <img src="https://i.imgur.com/YourImageHere.png" alt="SPU Checker Pro Logo" width="200"/>
</p>

## ⚠️ DISCLAIMER

**IMPORTANT: READ BEFORE USING THIS SOFTWARE**

This tool is provided **STRICTLY FOR EDUCATIONAL PURPOSES ONLY**. The author (@info_celestialbeing) is **NOT RESPONSIBLE** for any misuse, illegal activities, or damages caused by this software. By using this tool, you agree to the following:

1. You will use this tool only for legitimate, ethical, and legal purposes
2. You will not use this tool to gain unauthorized access to any systems
3. You will not use this tool to violate any laws, regulations, or policies
4. You will not hold the author responsible for any consequences of your actions

**The author is not related to or responsible for any actions taken by users of this software.**

If you do not agree with these terms, do not use this software.

## 🚀 Features

- ✅ **Multi-threaded Processing**: Process multiple credentials simultaneously (1-10 threads)
- ✅ **Multiple Login Modes**: Support for Student, SPU Authority, and GDC Authority logins
- ✅ **Data Extraction**: Extract mobile numbers and email addresses from student accounts
- ✅ **Real-time Progress**: Live progress tracking with success rate display
- ✅ **User-friendly Interface**: Easy-to-use command-line interface with clear instructions
- ✅ **Detailed Reporting**: Comprehensive summary of results after completion

## 💻 System Requirements

- **Python 3.7 or higher**
- Internet connection
- Required libraries: `httpx`, `asyncio`

To check your Python version:
```bash
python --version
```

If you don't have Python installed, download it from: [Python.org](https://www.python.org/downloads/)
(Make sure to check "Add Python to PATH" during installation)

## 📥 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/spu-checker-pro.git
cd spu-checker-pro
```

### Step 2: Install Required Libraries
```bash
pip install httpx asyncio
```

If you encounter any errors, try:
```bash
python -m pip install httpx asyncio
```

### Step 3: Prepare Your Credentials File
Create a text file named `data.txt` in the same folder as the script with your credentials:
```
username1:password1
username2:password2
```

## 🔧 Usage

### Running the Script
```bash
python hit.py
```

### Available Options

#### Login Modes:
- **[S]** Student Login (Default): Extracts mobile numbers and emails
- **[A]** SPU Authority/Staff Login: Checks for valid SPU staff credentials
- **[G]** GDC Authority/Staff Login: Checks for valid GDC staff credentials

#### Performance Settings:
- **[T]** Thread Count: Set between 1-10 threads for faster processing
  - Higher thread counts process more credentials simultaneously
  - Use lower thread counts on slower computers or connections

### Output Files
Results will be saved to:
- Student mode: `hit.txt`
- Authority modes: `authority_hit.txt`

## ❓ Troubleshooting

### Common Issues:

1. **"ModuleNotFoundError: No module named 'httpx'"**
   - Solution: Run the command: `pip install httpx`

2. **"FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'"**
   - Solution: Make sure you've created the data.txt file in the same folder as hit.py

3. **"ValueError: not enough values to unpack"**
   - Solution: Check your data.txt file format. Each line must be in the format username:password

4. **Script crashes or freezes**
   - Solution: Check your internet connection. The script needs internet access to connect to the servers.

## 📞 Support & Contact

If you need further assistance or want to access premium tools:

1. Contact me directly on Telegram: [@info_celestialbeing](https://t.me/info_celestialbeing)
2. Join my channel for more tools and updates
3. Check out my premium tools for advanced features

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

<div align="center">
  <sub>Created with ❤️ by OG Celestial</sub>
</div>
