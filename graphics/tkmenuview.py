from graphics import viewhandler

import tkinter as tk

class TkMenuView( viewhandler.ViewHandler ):
    ''' The in menu view.
    
    Member:
    backBtn -- The button which leads back to the main menu (Button).
    configBtn -- The button which opens the configuration menu (Button).
    helpBtn -- The button which opens the help menu (Button).
    levelList -- The list box containing all levels (ListBox).
    newGameBtn -- The new game button (Button).
    quitBtn -- The button to quit the game (Button).
    shuffleCheck -- A random check box to indicate if the level list should be shuffled (Checkbutton).
    startBtn -- The button to start the game (Button).
    _authorLabel -- The label containing the author (Label).
    _dateLabel -- The label containing the date (Label).
    _descriptionLabel -- The label containing the description (Label).
    _frame -- The menu frame (Frame).
    _frames -- List of frames which are not needed later (Frame).
    _mainMenuFrame -- The frame of the main menu (Frame).
    _newMenuFrame -- The frame of the new game menu (Frame).
    _scrollbar -- The scroll bar for the level list (Scrollbar).
    _spacers -- List of empty spacer labels (Label).
    _timeLabel -- The label containing the time (Label).
    _titleLabel -- The label containing the title (Label).
    _versionLabel -- The label containing the version (Label).
    ''' 
    
    def __init__( self, data, window ):
        ''' Add menu to given window. '''
        
        self._frames = []
        self.spacers = []
        
        self._frame = tk.Frame( window, height = data.windowHeight,
                                     width = data.windowWidth )
        self._frame.config( background = 'white' )
        self._frame.pack_propagate(0)
        
        # Main Menu ================================
        self._mainMenuFrame = tk.Frame( self._frame )
        self._mainMenuFrame.config( background = 'white' )
        
        self.newGameBtn = tk.Button( self._mainMenuFrame, text = 'New Game' )
        self.newGameBtn.config( background = 'white', width = 20 )
        self.newGameBtn.pack()
        
        self.spacers.append( tk.Label(self._mainMenuFrame, background = 'white').pack() )
        
        self.configBtn = tk.Button( self._mainMenuFrame, text = 'Configuration', state = tk.DISABLED )
        self.configBtn.config( background = 'white', width = 20 )
        self.configBtn.pack()
        
        self.spacers.append( tk.Label(self._mainMenuFrame, background = 'white').pack() )
        
        self.helpBtn = tk.Button( self._mainMenuFrame, text = 'Help', state = tk.DISABLED )
        self.helpBtn.config( background = 'white', width = 20 )
        self.helpBtn.pack()
        
        self.spacers.append( tk.Label(self._mainMenuFrame, background = 'white').pack() )
        
        self.quitBtn = tk.Button( self._mainMenuFrame, text = 'Quit' )
        self.quitBtn.config( background = 'white', width = 20 )
        self.quitBtn.pack()
        
        # New Game Menu ================================
        self._newMenuFrame = tk.Frame( self._frame )
        self._newMenuFrame.config( background = 'white' )
        
        # Level Selection
        levelFrame = tk.Frame( self._newMenuFrame )
        levelFrame.config( background = 'white' )
        levelFrame.pack( anchor = tk.W, fill = tk.Y, expand = 1 )
        self._frames.append( levelFrame )
        
        levelSelectionFrame = tk.Frame( levelFrame )
        levelSelectionFrame.config( background = 'white' )
        levelSelectionFrame.pack( side = tk.LEFT, 
                                  fill = tk.Y, expand = 1 )
        self._frames.append( levelSelectionFrame )
        
        self._scrollbar = tk.Scrollbar( levelSelectionFrame, orient = tk.VERTICAL )
        self.levelList = tk.Listbox( levelSelectionFrame, selectmode = tk.MULTIPLE, 
                                           width = 70, yscrollcommand = self._scrollbar.set )
        self._scrollbar.config( command = self.levelList.yview )
        self.levelList.pack( side = tk.LEFT, fill = tk.Y, expand = 1 )
        self._scrollbar.pack( fill = tk.Y, expand = 1 )

        for level in data.levelList:
            self.levelList.insert( tk.END, level )
        self.levelList.selection_set( 0, self.levelList.size() - 1 )
        
        spacerFrame = tk.Frame( levelFrame )
        spacerFrame.config( background = 'white', width = 30 )
        spacerFrame.pack( side = tk.LEFT )
        self._frames.append( spacerFrame )
        
        # Detail Info of Level
        self._titleLabel = tk.Label( levelFrame )
        self._titleLabel.config( background = 'white', font = (None, 16, 'bold') )
        self._titleLabel.pack( anchor = tk.W )
        
        self._descriptionLabel = tk.Label( levelFrame )
        self._descriptionLabel.config( background = 'white' )
        self._descriptionLabel.pack( anchor = tk.W )
        
        self.spacers.append( tk.Label(levelFrame, background = 'white').pack() )
        
        self._authorLabel = tk.Label( levelFrame )
        self._authorLabel.config( background = 'white' )
        self._authorLabel.pack( anchor = tk.W )
        
        self._dateLabel = tk.Label( levelFrame )
        self._dateLabel.config( background = 'white' )
        self._dateLabel.pack( anchor = tk.W )
        
        self._versionLabel = tk.Label( levelFrame )
        self._versionLabel.config( background = 'white' )
        self._versionLabel.pack( anchor = tk.W )
        
        self._timeLabel = tk.Label( levelFrame )
        self._timeLabel.config( background = 'white' )
        self._timeLabel.pack( anchor = tk.W )
        
        # Bottom Row
        self.spacers.append( tk.Label(self._newMenuFrame, background = 'white').pack() )
        
        self.backBtn = tk.Button( self._newMenuFrame, text = 'Back' )
        self.backBtn.config( background = 'white', width = 10 )
        self.backBtn.pack( side = tk.LEFT )
        
        self.startBtn = tk.Button( self._newMenuFrame, text = 'Start' )
        self.startBtn.config( background = 'white', width = 10 )
        self.startBtn.pack( side = tk.RIGHT )
        
        self.shuffleCheck = tk.Checkbutton( self._newMenuFrame, text = 'Shuffle Levels' )
        self.shuffleCheck.config( background = 'white', width = 20 )
        self.shuffleCheck.select()
        self.shuffleCheck.pack( side = tk.RIGHT )
    
    def hide( self, data ):
        ''' Hides the menu. '''
        
        self._frame.pack_forget()
    
    def show( self, data ):
        ''' Shows the menu. '''
        
        self._frame.pack( side = tk.LEFT, fill = tk.BOTH, expand = 1 )
        
        if data.state is data.STATES.MENU_MAIN:
            self._newMenuFrame.pack_forget()
            self._mainMenuFrame.pack( side = tk.LEFT, fill = tk.X, expand = 1 )
            
        elif data.state in [data.STATES.MENU_NEW, data.STATES.MENU_NEW_DETAILS]:
            self._mainMenuFrame.pack_forget()
            self._newMenuFrame.pack( fill = tk.BOTH, expand = 1, padx = 10, pady = 10 )
                
            if data.level:
                self._authorLabel.config( text = 'Author: {}'.format(data.level.author) )
                self._dateLabel.config( text = 'Last Update: {}'.format(data.level.date) )
                self._descriptionLabel.config( text = '{}'.format(data.level.description) )
                self._timeLabel.config( text = 'Time Limit: {:.2f}s'.format(data.level.timeLimit / 1000) )
                self._titleLabel.config( text = '{}'.format(data.level.name) )
                self._versionLabel.config( text = 'Version: {}'.format(data.level.version) )