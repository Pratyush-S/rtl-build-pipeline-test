# RTL Build Pipeline Test
Scaffolding for build pipelines
Project: A simple 1-bit full adder verified using VHDL (GHDL) and cocotb.
## 1. Prerequisites
Install the simulator and Python tools on the host system:
```
sudo apt update && sudo apt install ghdl python3 python3-pip python3-venv make gtkwave -y
```
## 2. Launch env
```
python3 -m venv .venv
source .venv/bin/activate
pip install cocotb
make
```
## 3. View wave form
```
gtkwave wave.ghw
```
## 4. Optional
Close the env
```
deactivate
```