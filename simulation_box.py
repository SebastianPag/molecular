import numpy as np

class Box():

    def __init__(self, dim=np.array([10,10,10]), pdb=True):
        self.dim = dim
        self.pdb = pdb
        self.molecule = []

    def set_dim(self, dim):
        self.dim = dim

    def get_dim(self):
        return self.dim

    def any_true(self, already_exists):
        is_any_true = False
        for i in already_exists:
            if i == True:
                is_any_true = True

        return is_any_true 

    def add_molecule(self, molecule):
        new_pos = molecule.get_position()
        already_exists = ["TRUE" for mol in self.molecule if new_pos.all() == mol.get_position]

        if "TRUE" in already_exists:
            pass
        else:
            self.molecule.append(molecule)        

    def get_molecules(self):
        return self.molecule