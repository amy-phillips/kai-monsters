# Example file showing a basic pygame "game loop"
import pygame

BUTTON_WIDTH = 400
BUTTON_HEIGHT = 50
X_SPACING = BUTTON_WIDTH + 100
Y_SPACING = 30
STAMINA_PER_ATTACK = 30

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
    def __init__(self, name, strength, life, speed, stamina, y_offset):
        self.name : str = name
        self.strength : int = strength
        self.life : int = life
        self.speed : int = speed
        self.stamina : int = stamina
        self.max_stamina : int = stamina
        self.y_offset : int = y_offset

    def render(self, screen):
        font = pygame.font.Font(pygame.font.get_default_font(), 30)
        health_surface = font.render(f"{self.name} - Strength: {self.strength} Life: {self.life} Speed: {self.speed} Stamina: {self.stamina}", False, (0, 0, 0))
        screen.blit(health_surface, (0,self.y_offset))

    def do_attack(self) -> int:
        if(self.stamina > STAMINA_PER_ATTACK):
            self.stamina -= STAMINA_PER_ATTACK
            return self.strength #TODO this will depend on move selected etc
        return 0

    def receive_attack(self, damage):
        self.life -= damage

    def recharge(self):
        self.stamina = int(min(self.max_stamina, self.stamina+self.max_stamina/2))


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# setup attack buttons and monster stats
x_offset = 0
y_offset = 0
attacking_monster = Monster(name="Sensei Pandaken", strength=18800, life=246282, speed=10944, stamina=280, y_offset=y_offset)
y_offset += Y_SPACING
defending_monster = Monster(name="Rageaster", strength=42042, life=1157065, speed=24136, stamina=240, y_offset=y_offset)
y_offset += Y_SPACING
move_buttons = []
move_buttons.append(Button([BUTTON_WIDTH, BUTTON_HEIGHT], "Do Epic Move", [x_offset, y_offset]))
x_offset += X_SPACING
move_buttons.append(Button([BUTTON_WIDTH, BUTTON_HEIGHT], "Do Moar Epic Move", [x_offset, y_offset]))
x_offset = 0
y_offset += Y_SPACING + BUTTON_HEIGHT
move_buttons.append(Button([BUTTON_WIDTH, BUTTON_HEIGHT], "Do Ultimate Move", [x_offset, y_offset]))
x_offset += X_SPACING
move_buttons.append(Button([BUTTON_WIDTH, BUTTON_HEIGHT], "Do Smash Bros Move", [x_offset, y_offset]))
x_offset = X_SPACING/2
y_offset += Y_SPACING + BUTTON_HEIGHT
move_buttons.append(Button([BUTTON_WIDTH, BUTTON_HEIGHT], "Recharge", [x_offset, y_offset]))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    for move_button in move_buttons:
        move_button.render(screen)
        if move_button.clicked(events):
            print(f"Doing {move_button.text}...")
            if(move_button.text == "Recharge"): # urggggghhhh
                attacking_monster.recharge()
            else:
                damage = attacking_monster.do_attack()
                defending_monster.receive_attack(damage)

    attacking_monster.render(screen)
    defending_monster.render(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()