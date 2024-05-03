library ieee; 
use ieee.std_logic_1164.all; 
use std.textio.all; 
use ieee.numeric_std.all; 
 
entity counter_tb is

end counter_tb;

architecture Behavioral of counter_tb is
 component counter is
   port( 
      CLK, RESET : in std_logic; 
      Q : out unsigned(8 downto 0)
   ); 
 end component;
    signal CLK_tb : std_logic;
    signal RESET_tb : std_logic;
    signal Q_tb : unsigned(8 downto 0); 
begin

  C1 : counter 
      PORT MAP(
        CLK => CLK_tb,
        RESET => RESET_tb,
        Q => Q_tb
      ); 
   -- simulation de l'horloge (CLK)
   clk_process: process
   begin
           CLK_tb <= '1';
           wait for 5 ns;
           CLK_tb <= '0';
           wait for 5 ns;
   end process;
   -- semilation de (RESET)
   reset_process: process
   begin
       RESET_tb <= '1';
       wait until falling_edge(CLK_tb);
       RESET_tb <= '0';
       wait until Q_tb = to_unsigned(210, 9) and rising_edge(CLK_tb);
   end process;
-- mettre les resultat dans un fichier
outpute_file_process : process (CLK_tb)
   file outpute_file : text open write_mode is "/home/bilal/VHDL/counter_gen/output_file.txt";
   variable ligne : line;
begin
   if rising_edge(clk_tb) then
       write(ligne, to_integer(Q_tb));
       writeline(outpute_file, ligne);
   end if;
   end process;
end Behavioral;
