# Example file showing a basic pygame "game loop"
import pygame

class Button:
    def __init__(self, size, text, pos, bgColor=(0, 255, 0), textColor=(0, 0, 0)):
        self.pos  = pos
        self.size = size
        self.text = text
        self.font = pygame.font.Font(pygame.font.get_default_font(), size[1])
        self.textSurf = self.font.render(f"{text}", True, textColor)
        self.button = pygame.Surface((size[0], size[1])).convert()
        self.button.fill(bgColor)

    def render(self, window):
        window.blit(self.button, (self.pos[0], self.pos[1]))
        window.blit(self.textSurf, (self.pos[0]+1, self.pos[1]+5))

    def clicked(self, events):
        mousePos = pygame.mouse.get_pos()#  get the mouse position
        for event in events:
            if self.button.get_rect(topleft=self.pos).collidepoint(mousePos[0], mousePos[1]):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return True
        return False

class Monster:
    def __init__(self, name, health, might, y_offset):
        self.name = name
        self.health = health
        self.might = might
        self.y_offset = y_offset

    def render(self, screen):
        font = pygame.font.Font(pygame.font.get_default_font(), 30)
        health_surface = font.render(f"{self.name} - Health: {self.health} Might: {self.might}", False, (0, 0, 0))
        screen.blit(health_surface, (0,self.y_offset))

    def calculate_attack_damage(self):
        return self.might #TODO this will depend on move selected etc
    def sustain_attack_damage(self, damage):
        self.health -= damage

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

move_button = Button([350, 50], "Do Epic Move", [50, 50])
attacking_monster = Monster("attack", 1000, 30, 0)
defending_monster = Monster("defend", 1000, 30, 30)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    move_button.render(screen)
    if move_button.clicked(events):
        print("Doing epic move...")
        damage = attacking_monster.calculate_attack_damage()
        defending_monster.sustain_attack_damage(damage)

    attacking_monster.render(screen)
    defending_monster.render(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()