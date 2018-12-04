import unittest
import numpy as np
from molecule import Molecule


class testMolecule(unittest.TestCase):

    def setUp(self):
        self.molecule = Molecule()

    def test_add_position(self):
        pos_xyz = np.array([1,1,1.1])
        self.molecule.set_position(pos_xyz)
        self.assertEqual(np.array([1,1,1.1]).all(), self.molecule.get_position().all())

    def test_add_velocity(self):
        vel_xyz = np.array([1,1,1.1])
        self.molecule.set_velocity(vel_xyz)
        self.assertEqual(np.array([1,1,1.1]).all(), self.molecule.get_velocity().all())