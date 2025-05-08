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

*   `%i[min:max]`: Generates a random **integer** between `min` and `max` (inclusive).
    *   The `min` and `max` values are separated by a colon `:`.
    *   *Examples:*
        *   `%i[1:100]` (generates an integer between 1 and 100, e.g., `42`)
        *   `%i[0:0]` (always generates the integer `0`)
        *   `%i[-10:10]` (generates an integer between -10 and 10)

*   `%f[min:max]` or `%f[min:max:precision]`: Generates a random **float** between `min` and `max`.
    *   The `min` and `max` values are separated by a colon `:`.
    *   An optional `precision` (number of decimal places) can be specified after another colon. If omitted, `precision` defaults to 5.
    *   *Examples:*
        *   `%f[0.0:1.0]` (generates a float between 0.0 and 1.0, e.g., `0.73215`)
        *   `%f[1.5:10.5:2]` (generates a float between 1.5 and 10.5, rounded to 2 decimal places, e.g., `6.88`)
        *   `%f[-5.0:5.0:0]` (generates a float between -5.0 and 5.0, rounded to 0 decimal places, effectively an integer, e.g., `-2.0`)

*   `%s[charset_specifier:length_specifier]`: Generates a random **string**.
    *   The `charset_specifier` and `length_specifier` are separated by a colon `:`.
    *   **`charset_specifier`**: Defines the pool of characters to choose from.
        *   **Keywords**: Use predefined keywords `lower` (a-z), `upper` (A-Z), `numbers` (0-9). Multiple keywords can be combined, separated by a forward slash `/`. The keywords are case-insensitive.
            *   `lower` (generates from `abcdefghijklmnopqrstuvwxyz`)
            *   `upper/numbers` (generates from `ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`)
            *   `lower/upper/numbers` (generates from all alphanumeric characters)
        *   **Literal String**: Provide a specific string of allowed characters enclosed in double quotes.
            *   `"abcde"` (generates using only 'a', 'b', 'c', 'd', 'e')
            *   `"01"` (generates a binary string)
            *   `"!@#$"` (generates using only these special characters)
    *   **`length_specifier`**: Specifies the length of the generated string.
        *   **Fixed Length**: A single integer `N` for a string of exactly `N` characters.
            *   `:5` (generates a string of length 5)
        *   **Variable Length**: A range `min-max` (integers separated by a hyphen `-`) for a string whose length is a random integer between `min` and `max` (inclusive).
            *   `:10-20` (generates a string with length between 10 and 20)
    *   *Examples:*
        *   `%s[lower:10-20]` (lowercase string, length 10 to 20, e.g., `qwertzuiopasdf`)
        *   `%s[upper/numbers:5]` (uppercase letters and digits, fixed length 5, e.g., `A3B1Z`)
        *   `%s["aeiou":3]` (string of length 3 using only 'a', 'e', 'i', 'o', 'u', e.g., `eia`)
        *   `%s["01":1]` (a single random binary digit '0' or '1', e.g., `0`)
        *   `%s[lower/upper:1]` (a single random uppercase or lowercase letter)

All other text is copied exactly as it appears.

**See it in Action:**

➡️ **For a concrete example demonstrating how to structure your template with both placeholders and static text, please refer to the examples included in the root of this repository.**

## 🔧 Customization

*   You can change the default filenames (`SOLUTION_FILENAME`, `INPUT_FILENAME`) at the top of the `main.py` script if needed.

## 🔮 Future Plans

*   **Multi-Language Support:** Add support for Python, Java, C#, and potentially other languages.
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
