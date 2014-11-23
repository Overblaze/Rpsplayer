#################################################
# 
# RPSPlayer designed to work with RPSFramework
# Created by Matt Martorana + Justin Read
#
#################################################
import Player
from Message import Message

class MMJRPlayer(Player.Player): # took ,Observer out
    #global name
    #global rock
    #global scissors
    #global paper
    #global listOfMoves
    def __init__(self):
        Player.Player.__init__(self)
        self.name = "MattMJustinR"
        self.rock = 0
        self.scissors = 1
        self.paper = 2
        self.listOfMoves=[2]
    #c = rpyc.connect(serverAddress, 12345)

    def notify(self, message):
        #if (message[0] == Message.MatchStart)
            
        if (message[0] == Message.Match_End):
            if (message[1] == self): # if we are player 1, we want player 2's move
                self.listOfMoves.append(message[3])
            else:
                self.listOfMoves.append(message[4]) #otherwise get other move

    def play(self):
        return my_rps_play_strategy.play(self.listOfMoves)

    def set_history(self,listPastMoves):
        self.listOfMoves = listPastMoves

    def get_name(self):
        return name

class my_rps_play_strategy(object):


    @staticmethod
    def play(listOfMoves):
        result = 0
        rock = 0
        scissors = 1
        paper = 2
        for i in range(len(listOfMoves)):
            result = result + (listOfMoves[i])
        result = result % 3
        return result
    
#def main():
    
#    player = MMJRPlayer()
#    player.set_history (['rock','scissors', 'paper', 'rock'])
#    print(player.play())

#if  __name__ =='__main__':
#    main()
