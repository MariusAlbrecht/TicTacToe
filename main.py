import random

class TikTakToe:
  
    def __init__(self):
        self.fields = [None, None, None, None, None, None, None, None, None]
                        
    def getPrint(self, player, position):
            
        #     |     |     
        #  1  |  2  |  3  
        #-----|-----|-----
        #  4  |  5  |  6  
        #-----|-----|-----
        #  7  |  8  |  9  
        #     |     |     
        
        printDefault = "     |     |     \n  1  |  2  |  3  \n-----|-----|-----\n  4  |  5  |  6  \n-----|-----|-----\n  7  |  8  |  9  \n     |     |     "
        
        if(self.fields[int(position)] == None):
            self.fields[int(position)] = player
            printDefault = printDefault.replace(position, player)
            return printDefault
        else:
            return "This field is already in use"
        
class Game:
    player = random.choice(seq = ['X', 'O'])
    turn = 0
    won = False
    ttt = TikTakToe()
    
    def getInput(self):
        userInput = input("Where do y'wanna go " + self.player + " ? ")
        if(self.ttt.fields[int(userInput)] != None):
            self.getInput(self)
        else:
            return userInput
        
    def checkWin(self):
        if(self.ttt.fields[1] == self.ttt.fields[2] == self.ttt.fields[3]):
            return True
        elif(self.ttt.fields[4] == self.ttt.fields[5] == self.ttt.fields[6]):
            return True
        elif(self.ttt.fields[7] == self.ttt.fields[8] == self.ttt.fields[9]):
            return True
        elif(self.ttt.fields[1] == self.ttt.fields[4] == self.ttt.fields[7]):
            return True
        elif(self.ttt.fields[2] == self.ttt.fields[5] == self.ttt.fields[8]):
            return True
        elif(self.ttt.fields[3] == self.ttt.fields[6] == self.ttt.fields[9]):
            return True
        elif(self.ttt.fields[1] == self.ttt.fields[5] == self.ttt.fields[9]):
            return True
        elif(self.ttt.fields[3] == self.ttt.fields[5] == self.ttt.fields[7]):
            return True
    
    def switch(self):
        if(self.player == 'X'):
            self.player = 'O'
        else:
            self.player = 'X'
    
    def loop(self):
        while(self.won == False):
            print(self.ttt.getPrint(self.player, self.getInput(self)))
            #self.won = self.checkWin(self)
            self.switch(self)
            
g = Game
g.loop(g)