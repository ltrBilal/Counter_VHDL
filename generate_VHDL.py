import subprocess
from functions import *

# scripts
script_path = "./counter.py" # script to generate VHDL file
expected_results = "./expected_results.py" # script to generate expected results

# files
results_file = "./output_file.txt"
expected_file = "./expected_file.txt"


i = 0
while i < 200:
    args = [f"{i + 35}"] # parametre
    i = i + 25
    # generate VHDL code
    result = subprocess.run(["python3", script_path] + args, capture_output=True, text=True)
    print(result.stdout)

    # generate the expected results
    expected = subprocess.run(["python3", expected_results] + args, capture_output=True, text=True)
    print(expected.stdout)

    # execute VHDL code
    subprocess.run(["make"], check=True) # GHDL Makefile
    
    # compare results
    difference_position = find_first_difference(results_file, expected_file)
    if difference_position is not None:
        print("Error, test FAILED. First difference at line:", difference_position)
    else:
        print("test PASSED.")
    print("************************************\n")

