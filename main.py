import subprocess
import random
import shutil
import os
import os.path
import string
import time

SOLUTION_FILENAME = "solution.cpp"
INPUT_FILENAME = "input.txt" # You can change these

def log(content, error=False):
    print(f"{f"ERROR -" if error else "-"} {content}")

def main(num_test_cases, time_limit):
    time_start = time.time()

    if not os.path.isfile(f"./{SOLUTION_FILENAME}"):
        log(f"Could not find the solution `{SOLUTION_FILENAME}`!", True)
        return

    log(f"Solution `{SOLUTION_FILENAME}` found!")

    if not os.path.isfile(f"./{INPUT_FILENAME}"):
        log(f"Could not find the input template `{INPUT_FILENAME}`!", True)
        return

    log(f"Input template `{INPUT_FILENAME}` found!")

    log("Compiling solution...")

    try:
        subprocess.run(["g++", SOLUTION_FILENAME, "-o", ".temp_solution.out"], check=True)
    except subprocess.CalledProcessError as e:
        log(f"Error during compilation: {e}", True)
        return

    log("Solution compiled successfully!")

    if os.path.exists("./cases"):
        log("Removing existing `cases` directory...")
        shutil.rmtree("./cases")

    os.mkdir("cases")
    log("Directory `cases` created!")

    modelo = open(f"./{INPUT_FILENAME}").read()
    modelo_args = modelo.split()

    for i in range(1, num_test_cases + 1, 1):
        log(f"Generating `{i}.in`...")

        final_input = modelo

        for arg in modelo_args:
            if arg[1] == "i":
                range_min, range_max = [int(x) for x in arg[3:-1].split(":")]

                if range_max < range_min:
                    log(f"Cannot generate a random integer because {range_min} > {range_max}", True)
                    return os.remove("./.temp_solution.out")

                final_input = final_input.replace(arg, f"{random.randint(range_min, range_max)}", 1)

            if arg[1] == "f":
                options = arg[3:-1].split(":")

                range_min, range_max = map(float, options[:2])

                float_precision = 5

                if len(options) == 3:
                    float_precision = int(options[2])

                if range_max < range_min:
                    log(f"Cannot generate a random float because {range_min} > {range_max}", True)
                    return os.remove("./.temp_solution.out")

                final_input = final_input.replace(arg, f"{round(random.uniform(range_min, range_max), float_precision)}", 1)

            if arg[1] == "s":
                options = arg[3:-1].split(":")

                chars_whitelist = ""

                string_length = 0

                options_length_range = options[1].split("-")

                if len(options_length_range) == 1:
                    string_length = int(options_length_range[0])
                else:
                    range_min, range_max = [int(x) for x in options_length_range]
                    string_length = random.randint(range_min, range_max)

                if options[0][0] == '"':
                    chars_whitelist = options[0][1:-1]
                else:
                    options_choices = options[0].lower().split("/")

                    if "lower" in options_choices:
                        chars_whitelist += string.ascii_lowercase

                    if "upper" in options_choices:
                        chars_whitelist += string.ascii_uppercase

                    if "numbers" in options_choices:
                        chars_whitelist += string.digits

                final_input = final_input.replace(arg, "".join(random.choices(chars_whitelist, k=string_length)), 1)

        case_in_path = os.path.join("cases", f"{i}.in")
        with open(case_in_path, "w") as file:
            file.write(final_input + "\n")

        log(f"Generating `{i}.out`...")

        case_out_path = os.path.join("cases", f"{i}.out")
        try:
            with open(case_in_path, "r") as input_file:
                with open(case_out_path, "w") as output_file:
                    subprocess.run(
                        ["./.temp_solution.out"],
                        stdin=input_file,
                        stdout=output_file,
                        timeout=time_limit,
                        check=True
                    )
        except subprocess.TimeoutExpired:
            log(f"TLE on {i}.in (exceeded {time_limit} seconds limit)", True)
            os.remove("./.temp_solution.out")

    os.remove("./.temp_solution.out")
    log("Removed compiled solution.")

    time_end = time.time()

    log(f"Successfully generated {num_test_cases} test cases in {time_end-time_start:.5f}s! ({os.getcwd()}/cases)")

if __name__ == "__main__":
    num_test_cases = int(input("Enter the number of test cases to generate: "))
    time_limit = input("Enter the time limit in seconds (leave empty for default: 0.5 second): ")

    if len(time_limit) == 0:
        time_limit = 0.5
    else:
        time_limit = float(time_limit)

    if num_test_cases <= 0:
        log("Invalid number of test cases.", True)
    elif time_limit <= 0:
        log("Invalid time limit.", True)
    else:
        main(num_test_cases, time_limit)