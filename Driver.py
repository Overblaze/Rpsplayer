from MMJRPlayer import MMJRPlayer
from Message import Message
player = MMJRPlayer()
print (player.play())
player.notify([Message.Match_End,player,0,0,1,0])#game end, p1,p2, pmove, op move, result
print(player.play())
player.notify([Message.Match_End,0,0,1,1,0])#game end, p1,p2, pmove, op move, result
print (player.play())
player.notify([Message.Match_End,player,0,0,1,0])#game end, p1,p2, pmove, op move, result
print(player.play())

