from graphics import viewhandler

import tkinter as tk

class TkMenuView( viewhandler.ViewHandler ):
    ''' The in menu view.
    
    Member:
    backFromNewBtn -- The button which leads back to the main menu (Button).
    configBtn -- The button which opens the configuration menu (Button).
    helpBtn -- The button which opens the help menu (Button).
    levelList -- The list box containing all levels (ListBox).
    newGameBtn -- The new game button (Button).
    numLevelsInput -- Input field for number of levels to use (Entry).
    quitBtn -- The button to quit the game (Button).
    shuffleCheck -- A random check box to indicate if the level list should be shuffled (Checkbutton).
    startBtn -- The button to start the game (Button).
    _authorLabel -- The label containing the author (Label).
    _configMenuFrame -- The frame of the config menu (Frame).
    _dateLabel -- The label containing the date (Label).
    _descriptionLabel -- The label containing the description (Label).
    _frame -- The menu frame (Frame).
    _frames -- List of frames which are not needed later (Frame).
    _labels -- List of labels which are not needed later (Label).
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
        self._labels = []
        self.spacers = []
        
        self._frame = tk.Frame( window, height = data.configuration.windowHeight,
                                width = data.configuration.windowWidth )
        self._frame.config( background = 'white' )
        self._frame.pack_propagate( 0 )
        
        self.__initConfigMenu( data )
        self.__initMainMenu( data )
        self.__initNewGameMenu( data )
    
    def hide( self, data ):
        ''' Hides the menu. '''
        
        self._frame.pack_forget()
    
    def show( self, data ):
        ''' Shows the menu. '''
        
        self._frame.pack( side = tk.LEFT, fill = tk.BOTH, expand = 1 )
        
        if data.state is data.STATES.MENU_MAIN:
            self._configMenuFrame.pack_forget()
            self._newMenuFrame.pack_forget()
            self._mainMenuFrame.pack( side = tk.LEFT, fill = tk.X, expand = 1 )
            
        elif data.state is data.STATES.MENU_NEW:
            self._configMenuFrame.pack_forget()
            self._mainMenuFrame.pack_forget()
            self._newMenuFrame.pack( fill = tk.BOTH, expand = 1, padx = 10, pady = 10 )
                
            if data.level:
                self._authorLabel.config( text = 'Author: {}'.format(data.level.author) )
                self._dateLabel.config( text = 'Last Update: {}'.format(data.level.date) )
                self._descriptionLabel.config( text = '{}'.format(data.level.description) )
                self._timeLabel.config( text = 'Time Limit: {:.2f}s'.format(data.level.timeLimit / 1000) )
                self._titleLabel.config( text = '{}'.format(data.level.name) )
                self._versionLabel.config( text = 'Version: {}'.format(data.level.version) )
                
        elif data.state is data.STATES.MENU_CONFIG:
            self._configMenuFrame.pack( fill = tk.BOTH, expand = 1, padx = 10, pady = 10 )
            self._newMenuFrame.pack_forget()
            self._mainMenuFrame.pack_forget()
    
    def __initConfigMenu( self, data ):
        ''' Initialize config menu. '''
        self._configMenuFrame = tk.Frame( self._frame )
        self._configMenuFrame.config( background = 'white' )
                
    def __initMainMenu( self, data ):
        ''' Initialize main menu. '''
        self._mainMenuFrame = tk.Frame( self._frame )
        self._mainMenuFrame.config( background = 'white' )
        
        self.newGameBtn = tk.Button( self._mainMenuFrame, text = 'New Game' )
        self.newGameBtn.config( background = 'white', width = 20 )
        self.newGameBtn.pack()
        
        self.spacers.append( tk.Label(self._mainMenuFrame, background = 'white').pack() )
        
        self.configBtn = tk.Button( self._mainMenuFrame, text = 'Configuration' )
        self.configBtn.config( background = 'white', width = 20 )
        self.configBtn.pack()
        
        self.spacers.append( tk.Label(self._mainMenuFrame, background = 'white').pack() )
        
        self.helpBtn = tk.Button( self._mainMenuFrame, text = 'Help' )
        self.helpBtn.config( background = 'white', width = 20 )
        self.helpBtn.pack()
        
        self.spacers.append( tk.Label(self._mainMenuFrame, background = 'white').pack() )
        
        self.quitBtn = tk.Button( self._mainMenuFrame, text = 'Quit' )
        self.quitBtn.config( background = 'white', width = 20 )
        self.quitBtn.pack()
        
    def __initNewGameMenu( self, data ):
        ''' Initialize new game menu. '''
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
        
        optionsFrame = tk.Frame( levelFrame )
        optionsFrame.config( background = 'white' )
        optionsFrame.pack( anchor = tk.SW, fill = tk.X, expand = 1 )
        self._frames.append( optionsFrame )
        
        optionsLabel = tk.Label( optionsFrame, text = 'Options:' )
        optionsLabel.config( background = 'white', font = (None, 16, 'bold') )
        optionsLabel.pack( anchor = tk.W )
        self._labels.append( optionsLabel )
        
        self.shuffleCheck = tk.Checkbutton( optionsFrame, text = 'Shuffle Levels' )
        self.shuffleCheck.config( background = 'white' )
        self.shuffleCheck.select()
        self.shuffleCheck.pack( anchor = tk.W )
        
        self.numLevelsInput = tk.Entry( optionsFrame )
        self.numLevelsInput.config( background = 'white', width = 3 )
        self.numLevelsInput.pack( anchor = tk.W, side = tk.LEFT )
        
        numLevelsLabel = tk.Label( optionsFrame, text = 'Number of Levels (Used if shuffling is checked)' )
        numLevelsLabel.config( background = 'white' )
        numLevelsLabel.pack( anchor = tk.W, side = tk.LEFT )
        self._labels.append( numLevelsLabel )
        
        # Bottom Row
        self.spacers.append( tk.Label(self._newMenuFrame, background = 'white').pack() )
        
        self.backFromNewBtn = tk.Button( self._newMenuFrame, text = 'Back' )
        self.backFromNewBtn.config( background = 'white', width = 10 )
        self.backFromNewBtn.pack( side = tk.LEFT )
        
        self.startBtn = tk.Button( self._newMenuFrame, text = 'Start' )
        self.startBtn.config( background = 'white', width = 10 )
        self.startBtn.pack( side = tk.RIGHT )