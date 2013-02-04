from abc import ABCMeta, abstractmethod  

class Tickable(metaclass = ABCMeta):
    ''' This abstract class describes a module which will be executed in every step and can 
    manipulate the application data. '''

    @abstractmethod
    def tick( self, data ):
        ''' The derived class must implement this method. The parameter data is the application data 
        object. '''