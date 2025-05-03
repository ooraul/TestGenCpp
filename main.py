import subprocess
import random
import shutil
import os
import os.path
import string

SOLUTION_FILENAME = "solution.cpp"
INPUT_FILENAME = "input.txt" # You can change these

def log(content):
    print(f"[TestGenCpp] {content}")

def main(num_test_cases):
    if not os.path.isfile(f"./{SOLUTION_FILENAME}"):
        log(f"Could not find the solution `{SOLUTION_FILENAME}`!")
        return
    
    log(f"Solution `{SOLUTION_FILENAME}` found!")

    if not os.path.isfile(f"./{INPUT_FILENAME}"):
        log(f"Could not find the input template `{INPUT_FILENAME}`!")
        return
    
    log(f"Input template `{INPUT_FILENAME}` found!")

    log("Compiling solution...")
    subprocess.run(f"g++ {SOLUTION_FILENAME} -o .solution", shell=True, executable="/bin/bash")
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
                range_min, range_max = [int(x) for x in arg[3:-1].split("-")]
                final_input = final_input.replace(arg, f"{random.randint(range_min, range_max)}", 1)

            if arg[1] == "f":
                range_min, range_max = [float(x) for x in arg[3:-1].split("-")]
                final_input = final_input.replace(arg, f"{random.uniform(range_min, range_max)}", 1)

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

        with open(f"./cases/{i}.in", "w") as file:
            file.write(final_input + "\n")

        log(f"Generating `{i}.out`...")

        with open(f"./cases/{i}.out", "w") as file:
            subprocess.run(f"(cat ./cases/{i}.in | ./.solution) >> ./cases/{i}.out", shell=True, executable="/bin/bash")

    os.remove("./.solution")
    log(f"Removed compiled solution.")

    log(f"{num_test_cases} test cases generated successfully! ({os.getcwd()}/cases)")

if __name__ == "__main__":
    num_test_cases = int(input("Enter the number of test cases to generate: "))
    
    main(num_test_cases)