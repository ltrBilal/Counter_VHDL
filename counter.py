import sys
import math

class Counter:
    def __init__(self) -> None:
        if(len(sys.argv) != 2):
            print("Please provide only one argument.")
            sys.exit(-1)
        self.frequency = int(sys.argv[1])
    
    def generate_vhdl(self):
        # calculates number of bits
        number_of_bits = int(math.ceil(math.log2(self.frequency)))
        #number_of_bits -= 1

        # libraries
        library = "library ieee; \n"
        library += "use ieee.std_logic_1164.all; \n"
        library += "use std.textio.all; \n"
        library += "use ieee.numeric_std.all; \n \n"

        # porte for both files
        port = "   port( \n"
        port += "      CLK, RESET : in std_logic; \n"
        port += f"      Q : out unsigned({number_of_bits} downto 0)\n   ); \n"

        with open('counter.vhd', 'w') as f, open('counter_tb.vhd', 'w') as f_tb:
            # library
            f.write(library)
            f_tb.write(library)

            # entity counter
            f.write("entity counter is \n")
            f.write(port)
            f.write("end counter;\n\n")

            # entity counter_tb
            f_tb.write("entity counter_tb is\n\nend counter_tb;\n\n")

            # architecture for counter
            f.write("architecture arc of counter is \n")

             # a signal
            f.write(f"   signal s : unsigned({number_of_bits} downto 0) := (others => '0');\n")
            f.write("begin\n")
            f.write(
                "   process(CLK, RESET)\n"
                "   begin\n"
                "       if RESET = '1' then\n"
                "           s <= (others => '0');\n"
                "       elsif rising_edge(CLK) then\n"
                "               s <= s + 1;\n"
                "       end if;\n"
                "   end process;\n"
                "   Q <= s;\n"
            )
            f.write("end arc;\n")      

            # architecture for counter_tb
            f_tb.write(
                "architecture Behavioral of counter_tb is\n"
                " component counter is\n"
                f"{port}"
                " end component;\n"
                "    signal CLK_tb : std_logic;\n"
                "    signal RESET_tb : std_logic;\n"
                f"    signal Q_tb : unsigned({number_of_bits} downto 0); \n"
                "begin\n\n"
                "  C1 : counter \n"
                "      PORT MAP(\n"
                "        CLK => CLK_tb,\n        RESET => RESET_tb,\n        Q => Q_tb\n"
                "      ); \n"
            )
            f_tb.write(
                "   -- simulation de l'horloge (CLK)\n"
                "   clk_process: process\n"
                "   begin\n"
                "           CLK_tb <= '1';\n"
                "           wait for 5 ns;\n"
                "           CLK_tb <= '0';\n"
                "           wait for 5 ns;\n"
                "   end process;\n"
            )

            f_tb.write(
                "   -- semilation de (RESET)\n"
                "   reset_process: process\n"
                "   begin\n"
                "       RESET_tb <= '1';\n"
                "       wait until falling_edge(CLK_tb);\n"
                "       RESET_tb <= '0';\n"
                f"       wait until Q_tb = to_unsigned({self.frequency}, {number_of_bits + 1}) and rising_edge(CLK_tb);\n"
                "   end process;\n"
            )

            f_tb.write(
                "-- mettre les resultat dans un fichier\n"
                "outpute_file_process : process (CLK_tb)\n"
                "   file outpute_file : text open write_mode is \"/home/bilal/VHDL/counter_gen/output_file.txt\";\n"
                "   variable ligne : line;\n"
                "begin\n"
                "   if rising_edge(clk_tb) then\n"
                "       write(ligne, to_integer(Q_tb));\n"
                "       writeline(outpute_file, ligne);\n"
                "   end if;\n"
                "   end process;\n"
            )

            f_tb.write("end Behavioral;\n")
    print(f"VHDL code generation is done for n = {sys.argv[1]}")

count = Counter()
count.generate_vhdl()       