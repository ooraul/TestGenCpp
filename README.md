# C++ Test Case Generator 🧪

A simple Python script to automatically generate input (`.in`) and output (`.out`) test cases for your C++ competitive programming solutions. ✨ Streamline your testing process! 🚀

## 🤔 What it does

This script takes your C++ solution file and an input template file, then:

1.  Compiles your C++ solution using `g++`.
2.  Reads the `.txt` template.
3.  Generates a specified number of `.in` files based on the template, replacing special placeholders with random values.
4.  Runs your compiled C++ solution against each generated `.in` file.
5.  Captures the output and saves it to corresponding `.out` files.
6.  Organizes all generated test cases into a `cases/` directory.

## ✨ Why Use This Script?

*   **⚡️ Save Time:** Instantly generate dozens or hundreds of test cases instead of creating them manually.
*   **📝 Easy Configuration:** Use a straightforward `.txt` file to specify the format and random ranges for your inputs.
*   **🎲 Versatile Randomization:** Supports both random integers and floats to cover different scenarios.
*   **⚙️ Seamless Workflow:** Integrates compilation (`g++`) and execution of your C++ solution directly into the generation process.
*   **✅ Guaranteed Correctness (Based on your solution):** Generates `.out` files by running *your* trusted solution, ensuring outputs match the expected logic.

## 🛠️ Prerequisites

*   Python 3 🐍
*   A C++ compiler (specifically `g++`) installed and accessible in your PATH. ⚙️
*   ⚠️ **Linux/Unix Environment Recommended**: This script uses shell commands (`cat`, `|`, `>>`) that are standard in Linux and macOS environments. While it might be adaptable for Windows (e.g., using WSL, Git Bash, or MinGW environments), it's **designed and tested primarily for Linux** and may not work out-of-the-box on Windows.

## 🚀 Usage

1.  **Clone or Download:** Get the `main.py` script into your project directory.
    ```bash
    git clone https://github.com/ooraul/TestGenCpp
    cd TestGenCpp
    # Or just download main.py
    ```
2.  **Prepare Your C++ Solution:** Place your correct C++ solution code in a file named `solution.cpp` in the same directory as `main.py`.
3.  **Create an Input Template:** Create a file named `input.txt` in the same directory. This file will define the structure of your input files and specify where random values should be inserted.
4.  **Define Placeholders in `input.txt`**.
5.  **Run the Script:** Execute the Python script from your terminal:
    ```bash
    python3 main.py
    ```
6.  **Enter Number of Test Cases:** The script will prompt you:
    ```
    Enter the number of test cases to generate:
    ```
    Type the desired number (e.g., `10`) and press Enter.
7.  **Check the Results:** The script will output logs as it works. Once finished, you'll find a `cases/` directory containing the generated `N.in` and `N.out` files. 🎉

## 📝 Input Template Format (`input.txt`)

The `input.txt` file serves as the blueprint for your generated `.in` files. The script reads this file and intelligently replaces special placeholders with random values while copying static text directly.

**Placeholders:**

Use these tags to insert random data:

*   `%i[min-max]`: Generates a random **integer** between `min` and `max` (inclusive).
    *   *Examples:*
        *   `%i[1-100]` (integer between 1 and 100)
        *   `%i[0-0]` (always generates the integer 0)
*   `%f[min-max]`: Generates a random **float** between `min` and `max`.
    *   *Examples:*
        *   `%f[0.0-1.0]` (float between 0.0 and 1.0)
*   `%s[charset:length]`: Generates a random **string**.
    *   `charset`: Specifies the pool of characters to choose from.
        *   Use keywords `upper` (A-Z), `lower` (a-z), `numbers` (0-9), separated by `/`. (e.g., `upper/lower`, `lower/numbers`)
        *   Alternatively, provide a specific string of allowed characters in double quotes (e.g., `"abc123"`, `"01"`).
    *   `length`: Specifies the length of the generated string.
        *   A single integer `N` for a fixed length (e.g., `:6`).
        *   A range `min-max` for a variable length (e.g., `:10-50`).
    *   *Examples:*
        *   `%s[lower:10-20]` (lowercase string, length 10 to 20)
        *   `%s[upper/numbers:5]` (uppercase letters and digits, fixed length 5)
        *   `%s["aeiou":3]` (string of length 3 using only 'a', 'e', 'i', 'o', 'u')
        *   `%s["01":1]` (a single random binary digit '0' or '1')

All other text is copied exactly as it appears.

**See it in Action:**

➡️ **For a concrete example demonstrating how to structure your template with both placeholders and static text, please refer to the examples included in the root of this repository.**

## 🔧 Customization

*   You can change the default filenames (`SOLUTION_FILENAME`, `INPUT_FILENAME`) at the top of the `main.py` script if needed.

## 🔮 Future Plans

*   **Multi-Language Support:** Add support for Python, Java, C#, and potentially other languages.
*   **Float Formatting Control:** Specify precision for generated floats (e.g., `%f[0-1, prec=5]`).
*   **Time Limit Enforcement:** Kill the solution if it runs too long and report a Time Limit Exceeded (TLE) status.
*   **Specific Structure Generation:** Helpers for common structures like generating valid graphs (e.g., number of nodes/edges, ensuring connectivity or acyclicity if needed) or trees.

## 🙏 Contributing

Want to help improve this script? Contributions are welcome!

*   **Report Bugs:** If something isn't working right, please [open an issue](https://github.com/ooraul/TestGenCpp/issues).
*   **Suggest Features:** Have ideas for making it better? [Open an issue](https://github.com/ooraul/TestGenCpp/issues) to share them.
*   **Submit Code:**
    1.  Fork the repo.
    2.  Create a branch.
    3.  Make your changes.
    4.  Submit a Pull Request.

Your help is appreciated! ✨

## 📜 License

This project is licensed under the **MIT License**.

This means you are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, provided that the original copyright notice and this permission notice are included in all copies or substantial portions of the Software.
