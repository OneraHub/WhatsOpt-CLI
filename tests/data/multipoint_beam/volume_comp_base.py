# -*- coding: utf-8 -*-
"""
  volume_comp_base.py generated by WhatsOpt 1.8.2
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: https://ether.onera.fr/whatsopt
# analysis_id: 4


import numpy as np
from numpy import nan
from os import path
from importlib import import_module
from yaml import load, FullLoader
from openmdao.api import ExplicitComponent

class VolumeCompBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate VolumeComp discipline """

    def __init__(self, **kwargs):
        super(VolumeCompBase, self).__init__(**kwargs)
        self._impl = None
        dockconf = path.join(path.dirname(__file__), ".whatsopt_dock.yml")
        if path.exists(dockconf):
            with open(dockconf) as dockfile:
                dock = load(dockfile, Loader=FullLoader)
                impl = dock.get("volume_comp")
                if impl:
                    module = import_module(impl['module'])
                    self._impl = getattr(module, impl['class'])()

    def setup(self):
        self.add_input('h', val=np.ones((1, 50)), desc='')

        self.add_output('volume', val=np.ones((1,)), desc='')



        