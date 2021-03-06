# -*- coding: utf-8 -*-
"""
  displacements_comp_base.py generated by WhatsOpt 1.8.2
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: 
# analysis_id: 6


import numpy as np
from numpy import nan
from os import path
from importlib import import_module
from yaml import load, FullLoader
from openmdao.api import ExplicitComponent

class DisplacementsCompBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate DisplacementsComp discipline """

    def __init__(self, **kwargs):
        super(DisplacementsCompBase, self).__init__(**kwargs)
        self._impl = None
        dockconf = path.join(path.dirname(__file__), ".whatsopt_dock.yml")
        if path.exists(dockconf):
            with open(dockconf) as dockfile:
                dock = load(dockfile, Loader=FullLoader)
                impl = dock.get("displacements_comp")
                if impl:
                    module = import_module(impl['module'])
                    self._impl = getattr(module, impl['class'])()

    def setup(self):
        self.add_input('d_0', val=np.ones((104,)), desc='')
        self.add_input('d_1', val=np.ones((104,)), desc='')

        self.add_output('displacements_0', val=np.ones((102,)), desc='')

        self.add_output('displacements_1', val=np.ones((102,)), desc='')



        