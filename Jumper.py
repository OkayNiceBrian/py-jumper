from World import World


class Jumper:
    w = 100
    h = 200
    baseXspeed = 2
    baseJumpForce = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xspeed = 0
        self.jumpForce = Jumper.baseJumpForce
        self.yspeed = 0
        self.isJumping = False

    def update(self):
        self.x += self.xspeed
        self.y += self.yspeed

        if self.isJumping:
            self.yspeed += World.gravity

    def left(self):
        if not self.isJumping:
            self.xspeed = -Jumper.baseXspeed

    def right(self):
        if not self.isJumping:
            self.xspeed = Jumper.baseXspeed

    def stop(self):
        if not self.isJumping:
            self.xspeed = 0

    def jump(self):
        if not self.isJumping:
            self.isJumping = True
            self.yspeed = -self.jumpForce
