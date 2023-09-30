import pygame
class Dialogue:
    max_speed = 10
    def __init__(self,
                 font:pygame.font.Font,
                 text:str,
                 outline_color:tuple,
                 background_color:tuple,
                 padding_color:tuple,
                 text_color:tuple,
                 pos:tuple,
                 key:int=pygame.K_SPACE,
                 speed:int=8,
                 wraplimit:int=250,
                 h:int=75):
        self.font = font
        self.text = [char for char in text]
        self.string = text
        self.speed = Dialogue.max_speed-speed
        self.pos = pos
        self.wraplimit = wraplimit
        self.char = 0
        self.delay = 0
        self.text_surf = None
        self.bg_color = background_color
        self.padding_color = padding_color
        self.outline_color = outline_color
        self.text_color = text_color
        self.bg_rect = pygame.Rect(self.pos[0]-6, self.pos[1]-6, wraplimit+6, h+6)
        self.outline_rect = pygame.Rect(self.pos[0]-10, self.pos[1]-10, wraplimit+14, h+14)
        self.padding_rect = pygame.Rect(self.pos[0]-6, self.pos[1]-6, wraplimit+6, h+6)
        self.done = False
        self.written = False
        self.proceed_key = key
    def update(self, screen, dt=1):
        self.delay += 1
        if (self.delay % round(self.speed/dt) == 0) and self.char < len(self.text):
            self.char += 1
        if self.char >= len(self.text):
            self.written = True
        string = ""
        if self.outline_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.char = len(self.text)
                self.written = True
        if self.written and (pygame.key.get_pressed()[self.proceed_key]):
            self.done = True
        for i in range(0, self.char):
            string = string + self.text[i]    
        #[12, 245, 191] is just a random color for the covnenience of colorkeying the text, you can change it into whatever you want, just make sure not to set it to the color of the text
        self.text_surf = self.font.render(string, False, self.text_color, [12, 245, 191], self.wraplimit)
        self.text_surf.set_colorkey([12, 245, 191])
        
        pygame.draw.rect(screen, self.outline_color, self.outline_rect, 4)
        pygame.draw.rect(screen, self.bg_color, self.bg_rect)
        pygame.draw.rect(screen, self.padding_color, self.padding_rect, 4)
        screen.blit(self.text_surf, self.pos)
        
