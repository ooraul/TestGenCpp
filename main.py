import subprocess
import random
import shutil
import os
import os.path

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

        entrada_final = modelo

        for arg in modelo_args:
            if arg[1] == "i":
                range_min, range_max = [int(x) for x in arg[3:-1].split("-")]
                entrada_final = entrada_final.replace(arg, f"{random.randint(range_min, range_max)}", 1)

            if arg[1] == "f":
                range_min, range_max = [float(x) for x in arg[3:-1].split("-")]
                entrada_final = entrada_final.replace(arg, f"{random.uniform(range_min, range_max)}", 1)

        with open(f"./cases/{i}.in", "w") as file:
            file.write(entrada_final + "\n")

        log(f"Generating `{i}.out`...")

        with open(f"./cases/{i}.out", "w") as file:
            subprocess.run(f"(cat ./cases/{i}.in | ./.solution) >> ./cases/{i}.out", shell=True, executable="/bin/bash")

    os.remove("./.solution")

    log(f"{num_test_cases} test cases generated successfully! ({os.getcwd()}/cases)")

if __name__ == "__main__":
    num_test_cases = int(input("Enter the number of test cases to generate: "))
    
    main(num_test_cases)