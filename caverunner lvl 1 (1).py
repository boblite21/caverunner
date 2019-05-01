


#atm.inc
#Cave Runner 
#Michael,Tionnah,Adolfo,Sheng
#two sentence explanation of the game's objective

from gamelib import*#import game library

#objects and initial settings
game = Game (1400,608,"Cave Runner")
bk2 = Image("bk2.png",game)
bk2.resizeTo(1400,608)
htp = Image("how to play.png",game)
htp.moveTo(400,150)
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
    htp.draw()
    story.draw()
    storyt1.draw()

    
    if mouse.collidedWith(story) and mouse.LeftClick:
        game.over=True
    



    game.update(60)
    
game.over =False
    


    
