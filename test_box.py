import unittest
import numpy as np
from simulation_box import Box
from molecule import Molecule

class testBox(unittest.TestCase):

    def setUp(self):
        self.box = Box()

    def test_set_dim(self):
        box_dim = np.array([20,20,20])
        self.box.set_dim(box_dim)
        self.assertEqual(box_dim.all(), self.box.get_dim().all())

    def test_add_molecule_to_box(self):
        molecule = Molecule()
        self.box.add_molecule(molecule)
        self.assertEqual([molecule], self.box.get_molecules())

    def test_molecule_in_box_if_not_added(self):
        molecule = Molecule()
        self.assertNotEqual([molecule], self.box.get_molecules())

    def test_if_molecule_already_in_pos_if_added_anyway(self):
        molecule = [Molecule(), Molecule()]
        self.assertNotEqual(molecule, self.box.get_molecules())

    def test_if_molecule_already_in_pos_and_not_if_added(self):
        mol1 = Molecule()
        mol2 = Molecule(pos=np.array([1,2,3]))
        self.box.add_molecule(mol1)
        self.box.add_molecule(mol2)
        self.assertEqual(len([mol1, mol2]), len(self.box.get_molecules()))