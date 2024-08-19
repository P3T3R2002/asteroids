import random
from circleshape import*
from constants import*


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)
        
    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vel1 = self.velocity.rotate(angle)
        vel2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        aster1 = Asteroid(self.position[0], self.position[1], new_radius)
        aster1.velocity = vel1*1.2
        aster2 = Asteroid(self.position[0], self.position[1], new_radius)
        aster2.velocity = vel2*1.2

