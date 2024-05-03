GHDL=ghdl

all:
	@$(GHDL) -a counter.vhd counter_tb.vhd
	@$(GHDL) -e counter_tb
	@$(GHDL) -r counter_tb --wave=wave.ghw --stop-time=10ms