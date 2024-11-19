import pygame
import random
def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mol_pos=mole_image.get_rect(topleft=(0,0))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if mol_pos.collidepoint(event.pos):
                        xx = random.randrange(0,640,32)
                        yy= random.randrange(0, 512, 32)
                        mol_pos.topleft=(xx, yy)

            screen.fill("light blue")
            screen.blit(mole_image, mole_image.get_rect(topleft=(mol_pos.x, mol_pos.y)))
            for x in range(0, 640, 32):
                for y in range(0, 512, 32):
                    pygame.draw.line(screen, "dark blue", (640,y),(x,y))
                    pygame.draw.line(screen, "dark blue", (x,512), (x,y))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
