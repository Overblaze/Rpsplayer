from MMJRPlayer import MMJRPlayer
player = MMJRPlayer()
print (player.play())
player.notify([4,0,0,0,2,0])#game end, p1,p2, pmove, op move, result
print(player.play())
player.notify([4,0,0,1,1,0])#game end, p1,p2, pmove, op move, result
print (player.play())
player.notify([4,player,0,0,2,0])#game end, p1,p2, pmove, op move, result
print(player.play())
