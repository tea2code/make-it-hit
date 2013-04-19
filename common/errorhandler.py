import sys
import time
import traceback as tb

class ErrorHandler():
    ''' Global error handler.
    
    Member:
    data -- List of objects with __str__() function. Will be dumped into error file in case of exception (List).
    '''
    
    def __init__( self ):
        ''' Initializes class and sets exception hook. '''
        self.data = [] 
        
    def exceptHook( self, extype, value, traceback ):
        ''' Exception handling method. Parameter are the exception class, exception instance, 
        and a trace back object.'''
        
        # Text
        error = ''.join( tb.format_exception(extype, value, traceback) )
        dump = 'Dumps:\n'
        for d in self.data:
            dump += '{0}\n'.format( str(d) )
          
        # Print to console.
        print( error )
        print( dump )
        
        # Log in file.        
        fileName = time.strftime( 'Error %Y-%m-%d-%H-%M-%S.txt' )
        with open( fileName, 'w' ) as file:
            file.write( error )
            file.write( dump )
            
    def register( self ):
        ''' Automatically registers class as global error handler. '''
        sys.excepthook = self.exceptHook