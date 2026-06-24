import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_adder_truth_table(dut):
    """Test all 8 possible combinations for a 1-bit full adder"""

    # Define the truth table: (A, B, Cin) -> (Sum, Cout)
    truth_table = [
        ((0, 0, 0), (0, 0)),
        ((0, 0, 1), (1, 0)),
        ((0, 1, 0), (1, 0)),
        ((0, 1, 1), (0, 1)),
        ((1, 0, 0), (1, 0)),
        ((1, 0, 1), (0, 1)),
        ((1, 1, 0), (0, 1)),
        ((1, 1, 1), (1, 1)),
    ]

    for inputs, outputs in truth_table:
        # Drive inputs
        dut.a.value = inputs[0]
        dut.b.value = inputs[1]
        dut.cin.value = inputs[2]

        # Use unit="ns" (singular) to satisfy newer cocotb versions
        await Timer(1, unit="ns")

        # Cast single-bit values directly to int
        expected_sum, expected_cout = outputs
        actual_sum = int(dut.sum.value)
        actual_cout = int(dut.cout.value)

        # Assertions
        assert actual_sum == expected_sum, \
            f"Inputs {inputs}: Expected Sum={expected_sum}, got {actual_sum}"
        assert actual_cout == expected_cout, \
            f"Inputs {inputs}: Expected Cout={expected_cout}, got {actual_cout}"

        dut._log.info(f"Passed: {inputs[0]} + {inputs[1]} + {inputs[2]} = Sum:{actual_sum} Cout:{actual_cout}")