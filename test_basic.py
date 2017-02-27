#!/usr/bin/env python3
####-----------------------------------------------------------------------
#### Unit Test exposed to test takers
#### 2017-02-25: KYK
####-----------------------------------------------------------------------
import unittest
import DigitalCircuitAnalysis


class TestBasicDCAnalysis(unittest.TestCase):

    def test_nand2(self):
        nl = DigitalCircuitAnalysis.Netlist()
        nl.add_spice("""
            MN1   n A VSS VSS nmos
            MN2 out B   n VSS nmos
            MP1 out A VDD VDD pmos
            MP2 out B VDD VDD pmos
            """)
        table = nl.truth_table(['A','B'], ['out'])
        s = "\n".join(table)
        self.assertEqual(s, "001\n011\n101\n110")


    def test_nor2(self):
        nl = DigitalCircuitAnalysis.Netlist()
        nl.add_spice("""
            MN1 out A VSS VSS nmos
            MN2 out B VSS VSS nmos
            MP1 out A   n VDD pmos
            MP2   n B VDD VDD pmos
            """)
        table = nl.truth_table(['A','B'], ['out'])
        s = "\n".join(table)
        self.assertEqual(s, "001\n010\n100\n110")



if __name__ == '__main__':
     unittest.main()
