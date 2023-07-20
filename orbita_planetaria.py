import math
import pygame

# Parâmetros do programa
WIDTH, HEIGHT = 800, 600
FPS = 60

# Cores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Classe para representar um planeta
class Planet:
    def __init__(self, name, orbit_radius, orbit_speed, radius, color):
        self.name = name
        self.orbit_radius = orbit_radius
        self.orbit_speed = orbit_speed
        self.radius = radius
        self.color = color
        self.angle = 0

    def update(self):
        self.angle += self.orbit_speed

    def get_position(self):
        x = WIDTH // 2 + self.orbit_radius * math.cos(self.angle)
        y = HEIGHT // 2 + self.orbit_radius * math.sin(self.angle)
        return int(x), int(y)

# Função para desenhar informações dos planetas na tela
def draw_planet_info(screen, planet):
    font = pygame.font.Font(None, 24)
    text = font.render(planet.name, True, WHITE)
    screen.blit(text, (10, 10))

# Função principal da simulação
def simulate_orbits():
    # Inicialização do pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulação de Órbitas Planetárias")
    clock = pygame.time.Clock()

    # Criação dos planetas
    planets = [
        Planet("Mercury", 100, 0.03, 10, YELLOW),
        Planet("Venus", 150, 0.02, 15, (255, 165, 0)),
        Planet("Earth", 200, 0.01, 20, BLUE),
        Planet("Mars", 250, 0.008, 18, (255, 0, 0)),
        Planet("Jupiter", 350, 0.005, 40, (184, 134, 11)),
        Planet("Saturn", 450, 0.003, 35, (210, 180, 140)),
        Planet("Uranus", 550, 0.002, 30, (0, 191, 255)),
        Planet("Neptune", 650, 0.001, 28, (0, 0, 128))
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        for planet in planets:
            planet.update()
            x, y = planet.get_position()

            # Desenha a órbita
            pygame.draw.circle(screen, planet.color, (WIDTH // 2, HEIGHT // 2), planet.orbit_radius, 1)

            # Desenha o planeta
            pygame.draw.circle(screen, planet.color, (x, y), planet.radius)

            # Desenha a trajetória do planeta
            trajectory_points = [(WIDTH // 2 + planet.orbit_radius * math.cos(angle), HEIGHT // 2 + planet.orbit_radius * math.sin(angle)) for angle in
                                 [i / 100.0 * math.pi * 2 for i in range(101)]]
            pygame.draw.lines(screen, planet.color, False, trajectory_points, 1)

        # Desenha informações do planeta selecionado
        draw_planet_info(screen, planets[0])  # Neste exemplo, desenha informações do primeiro planeta da lista

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# Executa a simulação
simulate_orbits()
