import random
import pygame


class Button:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def clicked(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height


class RpsGame:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((960, 640))
        pygame.display.set_caption("RPS Smasher")

        self.bg = pygame.image.load("background.jpg")
        self.r_btn = pygame.image.load("rock (1).png").convert_alpha()
        self.p_btn = pygame.image.load("paper.png").convert_alpha()
        self.s_btn = pygame.image.load("scissors.png").convert_alpha()

        self.choose_rock = self.r_btn.copy()
        self.choose_paper = self.p_btn.copy()
        self.choose_scissors = self.s_btn.copy()

        self.rock_btn = Button(20, 500, 280, 140)
        self.paper_btn = Button(330, 500, 280, 140)
        self.scissors_btn = Button(640, 500, 280, 140)

        self.font = pygame.font.SysFont(None, 90)
        self.text = self.font.render(" ", True, (255, 255, 255))

        self.pl_score = 0
        self.pc_score = 0
        self.p_option = ""
        self.pc_random_choice = ""

        self.image_reset()

    def player(self):
        if self.rock_btn.clicked():
            self.p_option = "rock"
            self.screen.blit(self.choose_rock, (120, 200))
        elif self.paper_btn.clicked():
            self.p_option = "paper"
            self.screen.blit(self.choose_paper, (120, 200))
        elif self.scissors_btn.clicked():
            self.p_option = "scissors"
            self.screen.blit(self.choose_scissors, (120, 200))
        else:
            self.p_option = ""
        return self.p_option

    def computer(self):
        option = ["rock", "paper", "scissors"]
        pc_choice = random.choice(option)
        self.pc_random_choice = pc_choice

        if pc_choice == "rock":
            self.screen.blit(self.choose_rock, (600, 200))
        elif pc_choice == "paper":
            self.screen.blit(self.choose_paper, (600, 200))
        else:
            self.screen.blit(self.choose_scissors, (600, 200))

        return pc_choice

    def update_scores(self):
        pl = self.p_option
        pc = self.pc_random_choice

        if pl == pc:
            return

        winning_moves = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper",
        }

        if winning_moves[pl] == pc:
            self.pl_score += 1
        else:
            self.pc_score += 1

    def image_reset(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.r_btn, (20, 500))
        self.screen.blit(self.p_btn, (330, 500))
        self.screen.blit(self.s_btn, (640, 500))
        self.text = self.font.render(" ", True, (255, 255, 255))
        self.screen.blit(self.text, (330, 0))

    def game_loop(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.image_reset()
                    self.player()
                    self.computer()
                    self.update_scores()
                    self.text = self.font.render(f"{self.pl_score} : {self.pc_score}", True, (255, 255, 255))

            self.screen.blit(self.text, (330, 0))
            pygame.display.update()
            clock.tick(30)

        pygame.quit()


if __name__ == '__main__':
    game = RpsGame()
    game.game_loop()
       

