from gamelib import*#import game library

#objects and initial settings
game = Game (1400,608,"Cave Runner")
bk = Image("bk.png",game)
bk.resizeTo(game.width, game.height)
dip= Animation("dip.png",10,game,840/5,470/2,4)
game.setBackground(bk)
bk2 = Image("bk2.png",game)
bk2.resizeTo(1400,608)
dip= Animation("dip.png",10,game,840/5,470/2,4)
dip.moveTo(250,300)
story  = Image("story.png",game)
story.moveTo(400,250)
storyt1 = Image("storyt1.png",game)
storyt1.moveTo(700,470)
game.setBackground(bk2)
#title screen
while not game.over:
    game.processInput()
    bk2.draw()
    dip.draw()
    
    story.draw()
    storyt1.draw()

    
    if mouse.collidedWith(story) and mouse.LeftClick:
        game.over=True
    



    game.update(60)
    
game.over =False
    

#Level 1 - game loop

while not game.over:
    game.processInput()
    game.scrollBackground("left",5)
    bk.draw()
    dip.draw()
    game.update(40)

game.over = False
#Level 2 - game loop

while not game.over:
    
    game.processInput()
    #game.scrollBackground("left",2)
    bk.draw()
    dip.Animate()
    game.update(30)

game.quit()
