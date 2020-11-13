#The code 
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # buildXY a "fence" 20 meters to enemy's left.
        hero.buildXY("fence", enemy.pos.x - 15, enemy.pos.y)
        pass
    else:
        # moveXY down 10 meters.
        hero.moveXY(hero.pos.x, hero.pos.y - 10)
        pass
