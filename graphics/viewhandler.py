from abc import ABCMeta, abstractmethod  

class ViewHandler(metaclass = ABCMeta):
    ''' Base class for view classes. '''

    @abstractmethod
    def hide( self, data ):
        ''' The derived class must implement this method. Hides the view. '''

    @abstractmethod
    def show( self, data ):
        ''' The derived class must implement this method. Shows data in the view. '''
        
