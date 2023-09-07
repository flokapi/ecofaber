

import numpy as np


import ecofaber
import ecofaber.basemodel as bm



@bm.register
class Model(bm.ModelElement):
    def __init__(self, data=None):
        super().__init__(data)

        self.angle = 0

    def update(self):
        self.angle += 0.1

    def getView(self):
        view = []

        view.append({
            "name": "b_cube_1",
            "pos": [10*np.cos(self.angle),10*np.sin(self.angle),0], 
            "color": [200,100,0],
        })

        view.append({
            "name": "b_ring_3",
            "pos": [0,0,0], 
            "color": [200,100,0],
        })

        return view

    def getObj(self, pos):
        return None


ecofaber.launch(Model)