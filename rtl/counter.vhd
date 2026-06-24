library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity counter is  -- Keeping the name 'counter' so you don't have to change your Makefile
    port (
        a    : in  std_logic;
        b    : in  std_logic;
        cin  : in  std_logic;
        sum  : out std_logic;
        cout : out std_logic
    );
end entity counter;

architecture rtl of counter is
begin
    sum  <= a xor b xor cin;
    cout <= (a and b) or (cin and (a xor b));
end architecture rtl;