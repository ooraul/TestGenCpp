# C++ Test Case Generator 🧪

A simple Python script to automatically generate input (`.in`) and output (`.out`) test cases for your C++ competitive programming solutions.

## 🤔 What it does

This script:

1.  Compiles your C++ solution using `g++`.
2.  Generates a specified number of `.in` files based on the template, replacing special placeholders with random values.
3.  Runs your compiled solution against each `.in` file to produce `.out` files.
4.  Organizes test cases into a `cases/` directory.

## 🛠️ Prerequisites

*   Python 3 🐍
*   `g++` (C++ compiler) installed and in your system's PATH. ⚙️
*   ⚠️ **Linux/Unix Environment Recommended**: This script uses shell commands (`cat`, `|`, `>>`) that are standard in Linux and macOS environments. While it might be adaptable for Windows (e.g., using WSL, Git Bash, or MinGW environments), it's **designed and tested primarily for Linux** and may not work out-of-the-box on Windows.

## 🚀 Quick Start

1.  **Get the script:**
    *   Download `main.py` directly.
    *   Or, clone the repository: `git clone https://github.com/ooraul/TestGenCpp`
2.  **Navigate to the script's directory.**
3.  **Prepare your files:**
    *   Place your C++ solution in `solution.cpp` in the same directory.
    *   Create an `input.txt` file in the same directory (see format below).
4.  **Run the script:**
    ```bash
    python3 main.py
    ```
5.  **Follow prompts:** Enter the number of test cases and the time limit (in seconds).
6.  **Done!** Check the `cases/` directory for your generated `.in` and `.out` files.

## 📝 Input Template Format (`input.txt`)

Create an `input.txt` file to define the structure of your test inputs. The script replaces special placeholders with random values.

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

Any text in `input.txt` not matching a placeholder format is copied directly.

➡️ **For a concrete example demonstrating how to structure your template with both placeholders and static text, please refer to the examples included in the root of this repository.**

## 🔧 Customization

*   You can change the default filenames (`SOLUTION_FILENAME`, `INPUT_FILENAME`) at the top of the `main.py` script if needed.

## 🔮 Future Ideas

*   Support for other programming languages.
*   Helpers for generating specific structures (e.g., graphs, trees).

## 🙏 Contributing

Contributions are welcome! Feel free to open an issue to report bugs or suggest features, or submit a pull request. ✨

## 📜 License

This project is licensed under the **MIT License**.
