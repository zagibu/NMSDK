# Vector4f struct

from .Struct import Struct
from struct import pack


class Vector4f(Struct):
    def __init__(self, **kwargs):
        super(Vector4f, self).__init__()

        """ Contents of the struct """
        self.data['x'] = kwargs.get('x', 0.0)
        self.data['y'] = kwargs.get('y', 0.0)
        self.data['z'] = kwargs.get('z', 0.0)
        self.data['t'] = kwargs.get('t', 0.0)
        """ End of the struct contents"""

    def __bytes__(self):
        return pack('<ffff', self.data['x'], self.data['y'], self.data['z'], self.data['t'])

    def __str__(self):
        return 'Vector4f({0}, {1}, {2}, {3})'.format(self.data['x'],
                                                     self.data['y'],
                                                     self.data['z'],
                                                     self.data['t'])

    def __repr__(self):
        return str(self)
