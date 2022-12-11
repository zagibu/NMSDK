# TkAnimationData struct

from .Struct import Struct
from .List import List
from .TkAnimationGameData import TkAnimationGameData


class TkAnimationData(Struct):
    def __init__(self, **kwargs):
        super(TkAnimationData, self).__init__()

        """ Contents of the struct """
        self.data['Anim'] = kwargs.get('Anim', '')
        self.data['Filename'] = kwargs.get('Filename', '')
        self.data['AnimType'] = kwargs.get('AnimType', 'Loop')
        self.data['FrameStart'] = kwargs.get('FrameStart', 0)
        self.data['FrameEnd'] = kwargs.get('FrameEnd', 0)
        self.data['StartNode'] = kwargs.get('StartNode', '')
        self.data['ExtraStartNodes'] = kwargs.get('ExtraStartNodes', List())
        self.data['Priority'] = kwargs.get('Priority', 0)
        self.data['OffsetMin'] = kwargs.get('OffsetMin', 0)
        self.data['OffsetMax'] = kwargs.get('OffsetMax', 0)
        self.data['Delay'] = kwargs.get('Delay', 0)
        self.data['Speed'] = kwargs.get('Speed', 1)
        self.data['ActionStartFrame'] = kwargs.get('ActionStartFrame', 0)
        self.data['ActionFrame'] = kwargs.get('ActionFrame', -1)
        self.data['CreatureSize'] = kwargs.get('CreatureSize', 'AllSizes')
        self.data['Additive'] = kwargs.get('Additive', 'False')
        self.data['Mirrored'] = kwargs.get('Mirrored', 'False')
        self.data['Active'] = kwargs.get('Active', 'True')
        self.data['AdditiveBaseAnim'] = kwargs.get('AdditiveBaseAnim', '')
        self.data['AdditiveBaseFrame'] = kwargs.get('AdditiveBaseFrame', 0)
        self.data['GameData'] = kwargs.get('GameData', TkAnimationGameData())
        """ End of the struct contents"""
