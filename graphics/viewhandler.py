from abc import ABCMeta, abstractmethod  
from formulary import screenconvert

class ViewHandler(metaclass = ABCMeta):
    ''' Base class for view classes. '''

    @abstractmethod
    def show( self, data ):
        ''' The derived class must implement this method. Shows data in the view. '''
        
