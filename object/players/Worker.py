import time
from object.players.Player import Player
import pygame as pg


class Worker(Player):
    WORKER_COST = 1  # amount of resources to train a new worker
    WORKER_TRAIN = 10  # amount of turns to train a new worker
    WORKER_SPEED = 10  # distance covered in one turn by a running worker
    WORKER_PROD = 1  # amount of resources per turn mined by a worker in mine
    WORKER_REPAIR = 1  # amount of HP restored per turn by a worker in wall
    WORKER_HEALTH = 10


    PLAYER1_READY = "sprites/player1/sword/ready.png"
    PLAYER2_READY = "sprites/player2/sword/ready.png"
    PLAYER1_RUN = {"root": "sprites/player1/sword/run/run-", "extension": ".png"}
    PLAYER2_RUN = {"root": "sprites/player2/sword/run/run-", "extension": ".png"}
    PLAYER1_DIG = {"root": "sprites/player1/sword/attack/attack-", "extension": ".png"}
    PLAYER2_DIG = {"root": "sprites/player2/sword/attack/attack-", "extension": ".png"}


    def __init__(self, health, x, y, deploy, screen, type):
        super().__init__(health, x, y, deploy)
        self.turns = 0
        self.current_time = 0
        self.start_HP = 1
        self.digging = False
        self.repairing = True
        self.worker_added = False
        self.type = type
        match type:
            case"p1":
                self.animation = self.loadImage(self.PLAYER1_RUN.get("root"), self.PLAYER1_RUN.get("extension"), 11)
            case"p2":
                self.animation = self.loadImage(self.PLAYER2_RUN.get("root"), self.PLAYER2_RUN.get("extension"), 11)
        self.start_time = time.time()
        self.screen = screen
        self.rect = self.image.get_rect()



    def dig(self, player):
        if not self.repair and not self.digging:
            match player:
                case "p1":
                    self.image = pg.image.load(self.PLAYER1_READY)
                    if not self.digging:
                        self.digging = True
                        self.a_count = 0
                        self.load_work(self.PLAYER1_DIG.get("root"), self.PLAYER1_DIG.get("extension"))
                case "p2":
                    self.image = pg.image.load(self.PLAYER2_READY)
                    if not self.digging:
                        self.digging = True
                        self.a_count = 0
                        self.load_dig(self.PLAYER2_DIG.get("root"), self.PLAYER2_DIG.get("extension"))


    def repair(self, player):
        if not self.dig and not self.repairing:
            match player:
                case"p1":
                    self.image = pg.image.load(self.PLAYER1_READY)
                    if not self.repairing:
                        self.repairing = True
                        self.a_count = 0
                    self.load_attack(self.PLAYER1_REPAIR.get("root"), self.PLAYER1_REPAIR.get("extension"))
                case"p2":
                    self.image = pg.image.load(self.PLAYER2_READY)
                    if not self.repairing:
                        self.repairing = True
                        self.a_count = 0
                        self.load_attack(self.PLAYER2_REPAIR.get("root"), self.PLAYER2_REPAIR.get("extension"))


    def load_dig(self, image_path_root, img_extension):
        self.animation = self.loadImage(image_path_root, img_extension, 8)


    def load_repair(self, image_path_root, img_extension):
        self.animation = self.loadImage(image_path_root, img_extension, 8)


    def update(self):
        self.a_count += 1
        if self.a_count == len(self.animation):
            self.a_count = 0
        self.image = self.animation[self.a_count]


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))




    def move(self):
        if self.run:
            match self.type:
                case "p1":
                    self.x += self.SPEED
                case"p2":
                    self.x -= self.SPEED


    def train(self):
        if round(self.current_time - self.start_time) < self.TRAIN_TURNS:
            self.current_time = time.time()
        # we set ready to dispatch once the training time is done, then in the main when the dispatch order is issued, the dispatch variable gets set to True
        # and the soldiers gets deployed into the battle field
        else:
            self.ready_to_dispatch = True


    def rest(self):
        if self.REST > (self.current_time - self.start_shoot):
            self.current_time = time.time()
            # print("rest timer: " + str(self.current_time - self.start_shoot))
            return False
        else:
            return True

    def load_dead(self):
        if self.dead:
            match self.type:
                case "p1":
                    self.loadImage(self.PLAYER1_FALLEN.get("root"), self.PLAYER1_FALLEN.get("extension"), 6)
                case "p2":
                    self.loadImage(self.PLAYER2_FALLEN.get("root"), self.PLAYER2_FALLEN.get("extension"), 6)


