import pgzrun
import random

WIDTH=1200
HEIGHT=600

WHITE=(255,255,255)

ship=Actor('ship')
bug=Actor('bug')

ship.pos = (WIDTH // 2,HEIGHT - 60)

speed=5

#define a list for bullets
bullets = []

#defining a list of enemies
enemies = []

score = 0
direction = 1

ship.dead=False
ship.countdown=90


for x in range (8):
    for y in range (4):
        enemies.append(Actor('bug'))
        enemies[-1].x=100+50* x #150,200,250
        enemies[-1].y=80+50* y

def displayScore():
    screen.draw.text(str(score),(50,30))
    
def gameOver():
    screen.draw.text("GAME OVER", (250, 300))

def on_key_down(key):
    if ship.dead == False:
        if key == keys.SPACE:
            bullets.append(Actor('bullet'))
            bullets[-1].x = ship.x
            bullets[-1].y = ship.y - 50

def update():
    global score
    global direction
    moveDown = False

    if ship.dead == False:
        if keyboard.right:
            ship.x += speed
            if ship.x > 1162:
                ship.x = 1162
        elif keyboard.left:
            #ship.x = ship.x-speed
            ship.x -= speed
            if ship.x <38:
                ship.x = 38

    for bullet in bullets:
        if bullet.y <= 0: #goes outside the screen
            bullets.remove(bullet)
        else:
            bullet.y -= 10

    if len(enemies) == 0:
        gameOver()

    if len(enemies) > 0  and (enemies[-1].x > WIDTH-80 or enemies[0].x < 80):
        moveDown = True
        direction = direction*-1

    for enemy in enemies:
        enemy.x += 5*direction
        if moveDown == True:
            enemy.y += 100
        if enemy.y >HEIGHT:
            enemies.remove(enemy)
        for bullet in bullets:
            if enemy.colliderect(bullet):
                score+=10
                bullets.remove(bullet)
                enemies.remove(enemy)
                if len(enemies) == 0:
                    gameOver()
        
        if enemy.colliderect(ship):
            ship.dead = True
    
    if ship.dead:
        ship.countdown -=1
    if ship.countdown == 0:
        ship.dead = False #respawn
        ship.countdown = 90

def draw():
    screen.clear()
    screen.fill("cadetblue")

    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    if ship.dead == False:
        ship.draw()
    if len(enemies) == 0:
        gameOver()

    displayScore()
pgzrun.go()