library ieee; 
use ieee.std_logic_1164.all; 
use std.textio.all; 
use ieee.numeric_std.all; 
 
entity counter is 
   port( 
      CLK, RESET : in std_logic; 
      Q : out unsigned(8 downto 0)
   ); 
end counter;

architecture arc of counter is 
   signal s : unsigned(8 downto 0) := (others => '0');
begin
   process(CLK, RESET)
   begin
       if RESET = '1' then
           s <= (others => '0');
       elsif rising_edge(CLK) then
               s <= s + 1;
       end if;
   end process;
   Q <= s;
end arc;
