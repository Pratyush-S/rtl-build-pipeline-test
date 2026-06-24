# Simulator settings
SIM ?= ghdl
TOPLEVEL_LANG ?= vhdl

# VHDL source files
VHDL_SOURCES += $(PWD)/rtl/counter.vhd

# Top-level entity name in your VHDL
TOPLEVEL = counter

# Python test file name (without .py extension)
MODULE = test_counter

# Search path for Python testbenches
export PYTHONPATH := $(PWD)/tb:$(PYTHONPATH)

# Include cocotb's make rules
include $(shell cocotb-config --makefiles)/Makefile.sim

# Tell GHDL to dump waveforms to a file
SIM_ARGS += --wave=wave.ghw