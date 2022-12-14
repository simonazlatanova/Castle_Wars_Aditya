import random

import pygame as pg

from implementation import Function
from object.players.Archer import Archer
from object.players.SwordsMan import SwordMan

WIDTH, HEIGHT = 1000, 250

INITIAL_RESOURCE = 1000

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
BG = pg.transform.scale(pg.image.load("sprites/bakground/BG.jpg"), (WIDTH, HEIGHT))
pg.font.init()


def main():
    archers_p1 = []
    archers_p2 = []
    swordsmen_p1 = []
    swordsmen_p2 = []
    worker_p1 = []
    worker_p2 = []
    player1_resource = INITIAL_RESOURCE
    player2_resource = INITIAL_RESOURCE


    # counters
    archer_index_p1 = 0
    swordsman_index_p1 = 0
    worker_index_p1 = 0
    count_archer_p1 = 0
    num_archer_p1 = 0
    count_swordsmen_p1 = 0
    num_swordsmen_p1 = 0
    count_worker_p1 = 0
    num_worker_p1 = 0
    p1_total_soldiers = 0
    archer_index_p2 = 0
    swordsman_index_p2 = 0
    worker_index_p2 = 0
    count_archer_p2 = 0
    num_archer_p2 = 0
    count_swordsmen_p2 = 0
    num_swordsmen_p2 = 0
    count_worker_p2 = 0
    num_worker_p2 = 0
    p2_total_soldiers = 0

    # Fonts
    default_font = pg.font.SysFont("comicsans", 12)
    resource_font = pg.font.SysFont("comicsans", 20)

    def redraw_window():
        screen.blit(BG, (0, 0))

        ready_archers_label_1 = default_font.render(f"Ready Archers: {num_archer_p1}", True, (255, 0, 255))
        ready_swordsmen_label_1 = default_font.render(f"| Ready Swordsmen: {num_swordsmen_p1}", True, (255, 0, 255))
        ready_worker_label_1 = default_font.render(f"Ready Worker: {num_worker_p1}", True, (255, 0, 255))
        archers_in_training_1 = default_font.render(f"Issued archers: {count_archer_p1}", True, (255, 0, 255))
        swordsmen_in_training_1 = default_font.render(f"| Issued swordsmen: {count_swordsmen_p1}", True, (255, 0, 255))
        worker_in_training_1 = default_font.render(f"Issued worker: {count_worker_p1}", True, (255, 0, 255))
        player1_resource_label = resource_font.render(f"Resource: {player1_resource}", True, (255, 0, 0))
        tot_soldiers_p1_label = default_font.render(f"Total number of soldiers: {len(archers_p1) + len(swordsmen_p1) + len(worker_p1)}",
                                                    1, (0, 0, 0))
        ready_archers_label_2 = default_font.render(f"Ready Archers: {num_archer_p2}", True, (255, 0, 255))
        ready_swordsmen_label_2 = default_font.render(f"| Ready Swordsmen: {num_swordsmen_p2}", True, (255, 0, 255))
        ready_worker_label_2 = default_font.render(f"Ready Worker: {num_worker_p2}", True, (255, 0, 255))
        archers_in_training_2 = default_font.render(f"Issued archers: {count_archer_p2}", True, (255, 0, 255))
        swordsmen_in_training_2 = default_font.render(f"| Issued swordsmen: {count_swordsmen_p2}", True, (255, 0, 255))
        worker_in_training_2 = default_font.render(f"Issued worker: {count_worker_p2}", True, (255, 0, 255))
        player2_resource_label = resource_font.render(f"Resource: {player2_resource}", True, (255, 0, 0))
        tot_soldiers_p2_label = default_font.render(f"Total number of soldiers: {len(archers_p2) + len(swordsmen_p2) + len(worker_p1)}",
                                                    1, (0, 0, 0))

        screen.blit(player1_resource_label, (10, 5))
        screen.blit(ready_archers_label_1, (10, 35))
        screen.blit(ready_worker_label_1, (5, 30))
        screen.blit(ready_swordsmen_label_1, (ready_archers_label_1.get_width() + 15, 35))
        screen.blit(archers_in_training_1, (10, 45))
        screen.blit(worker_in_training_1, (5, 40))
        screen.blit(swordsmen_in_training_1, (archers_in_training_1.get_width() + 15, 45))
        screen.blit(tot_soldiers_p1_label, (10, 60))

        screen.blit(player2_resource_label, (WIDTH - player2_resource_label.get_width(), 5))
        screen.blit(ready_archers_label_2,
                    (WIDTH - ready_archers_label_2.get_width() - ready_swordsmen_label_2.get_width() - 5, 35))
        screen.blit(ready_swordsmen_label_2, (WIDTH - ready_archers_label_2.get_width() - 30, 35))
        screen.blit(archers_in_training_2,
                    (WIDTH - archers_in_training_2.get_width() - swordsmen_in_training_2.get_width() - 5, 45))
        screen.blit(swordsmen_in_training_2, (WIDTH - archers_in_training_2.get_width() - 30, 45))
        screen.blit(tot_soldiers_p2_label, (WIDTH - tot_soldiers_p2_label.get_width() - 5, 60))

        Function.draw(archers_p1, screen)
        Function.draw(archers_p2, screen)
        Function.draw(swordsmen_p1, screen)
        Function.draw(swordsmen_p2, screen)

        pg.display.update()

    loop = 1

    while loop:

        clock.tick(15)
        redraw_window()

        Functions = Function
        for event in pg.event.get():

            if event.type == pg.QUIT:
                loop = 0
            if event.type == pg.KEYDOWN:

                if event.key == pg.K_e:
                    if player1_resource >= 0:
                        player1_resource -= Archer.COST
                        count_archer_p1 += 1

                    else:
                        player1_resource = 0

                if event.key == pg.K_i:
                    if player2_resource >= 0:
                        player2_resource -= Archer.COST
                        count_archer_p2 += 1

                    else:
                        player2_resource = 0

                if event.key == pg.K_w:
                    if player1_resource > 0:
                        player1_resource -= SwordMan.COST
                        count_swordsmen_p1 += 1
                    else:
                        player1_resource = 0

                if event.key == pg.K_o:
                    if player2_resource > 0:
                        player2_resource -= SwordMan.COST
                        count_swordsmen_p2 += 1
                    else:
                        player2_resource = 0

                if event.key == pg.K_f:
                    if num_archer_p1 > 0:
                        archer_index_p1, num_archer_p1 = Function.attack(archers_p1, archer_index_p1, num_archer_p1)

                if event.key == pg.K_h:
                    if num_archer_p2 > 0:
                        archer_index_p2, num_archer_p2 = Function.attack(archers_p2, archer_index_p2, num_archer_p2)

                if event.key == pg.K_d:
                    if num_swordsmen_p1 > 0:
                        swordsman_index_p1, num_swordsmen_p1 = Function.attack(swordsmen_p1, swordsman_index_p1,
                                                                                num_swordsmen_p1)
                if event.key == pg.K_j:
                    if num_swordsmen_p2 > 0:
                        swordsman_index_p2, num_swordsmen_p2 = Function.attack(swordsmen_p2, swordsman_index_p2,
                                                                                num_swordsmen_p2)

                if event.key == pg.K_z:
                    Function.deploy_all(archers_p1)
                    Function.deploy_all(swordsmen_p1)
                    num_archer_p1 = 0
                    num_swordsmen_p1 = 0

        # PLAYER 1 ARCHERS
        Function.add_to_queue(archers_p1, count_archer_p1, "archers_p1", screen)
        num_archer_p1, count_archer_p1, total_archer_p1 = Function.check_added(archers_p1, num_archer_p1,
                                                                                count_archer_p1, "archers_p1",
                                                                                p1_total_soldiers)
        # PLAYER 2 ARCHERS
        Function.add_to_queue(archers_p2, count_archer_p2, "archers_p2", screen)
        num_archer_p2, count_archer_p2, total_archer_p2 = Function.check_added(archers_p2, num_archer_p2,
                                                                                count_archer_p2, "archers_p2",
                                                                                p2_total_soldiers)

        Function.add_to_queue(swordsmen_p1, count_swordsmen_p1, "swordsmen_p1", screen)
        num_swordsmen_p1, count_swordsmen_p1, p1_total_soldiers = Function.check_added(swordsmen_p1, num_swordsmen_p1,
                                                                                        count_swordsmen_p1,
                                                                                        "swordsmen_p1",
                                                                                        p1_total_soldiers)
        Function.add_to_queue(swordsmen_p2, count_swordsmen_p2, "swordsmen_p2", screen)
        num_swordsmen_p2, count_swordsmen_p2, p2_total_soldiers = Function.check_added(swordsmen_p2, num_swordsmen_p2,
                                                                                        count_swordsmen_p2,
                                                                                        "swordsmen_p2",
                                                                                        p2_total_soldiers)

        if count_archer_p1 <= 0:
            count_archer_p1 = 0
        if count_archer_p2 <= 0:
            count_archer_p2 = 0
        if count_swordsmen_p1 <= 0:
            count_swordsmen_p1 = 0
        if count_swordsmen_p2 <= 0:
            count_swordsmen_p2 = 0

        Function.training(archers_p1)
        Function.training(archers_p2)

        Function.training(swordsmen_p1)
        Function.training(swordsmen_p2)

        Function.deploy(archers_p1)
        Function.deploy(archers_p2)

        Function.deploy(swordsmen_p1)
        Function.deploy(swordsmen_p2)

        Function.collide(archers_p1, archers_p2)
        Function.collide(swordsmen_p1, swordsmen_p2)

        Function.check_health(archers_p1)
        Function.check_health(archers_p2)

        Function.check_dead(archers_p1)
        Function.check_dead(archers_p2)


if __name__ == '__main__':
    main()
