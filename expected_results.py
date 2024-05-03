import sys
import time

n = int(sys.argv[1])
# ces resultat sont pour une simulation de 10 ms
with open('/home/bilal/VHDL/counter_gen/expected_file.txt', 'w') as f:
    i = 0
    p = 0
    while  p < 1000000: # 10 ms / 10 ns
        f.write(f"{i}\n")
        if i == n:
            i = 0
        else:
            i += 1
        p += 1

print("Expected results are generated")