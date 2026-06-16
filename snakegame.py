import os
import random
import sys

try:
	import pygame
except Exception:
	print("Pygame is required. Install with: pip install pygame")
	sys.exit(1)

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 30, 30)
GREEN = (30, 200, 30)
BLUE = (30, 144, 255)
GRAY = (40, 40, 40)

HIGHSCORE_FILE = os.path.join(os.path.dirname(__file__), "highscore.txt")


def load_highscore() -> int:
	try:
		with open(HIGHSCORE_FILE, "r") as f:
			return int(f.read().strip() or 0)
	except Exception:
		return 0


def save_highscore(score: int) -> None:
	try:
		with open(HIGHSCORE_FILE, "w") as f:
			f.write(str(score))
	except Exception:
		pass


def draw_text(surface, text, size, color, pos, center=True):
	font = pygame.font.SysFont(None, size)
	text_surf = font.render(text, True, color)
	rect = text_surf.get_rect()
	if center:
		rect.center = pos
	else:
		rect.topleft = pos
	surface.blit(text_surf, rect)


class SnakeGame:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption("Snake — Professional Edition")
		self.clock = pygame.time.Clock()
		self.reset()

	def reset(self):
		self.direction = (1, 0)
		self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2), (GRID_WIDTH // 2 - 1, GRID_HEIGHT // 2)]
		self.spawn_food()
		self.score = 0
		self.speed = 8
		self.game_over = False
		self.paused = False
		self.highscore = load_highscore()

	def spawn_food(self):
		positions = set(self.snake)
		while True:
			pos = (random.randrange(0, GRID_WIDTH), random.randrange(0, GRID_HEIGHT))
			if pos not in positions:
				self.food = pos
				return

	def handle_input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)
			if event.type == pygame.KEYDOWN:
				if event.key in (pygame.K_UP, pygame.K_w):
					if self.direction != (0, 1):
						self.direction = (0, -1)
				elif event.key in (pygame.K_DOWN, pygame.K_s):
					if self.direction != (0, -1):
						self.direction = (0, 1)
				elif event.key in (pygame.K_LEFT, pygame.K_a):
					if self.direction != (1, 0):
						self.direction = (-1, 0)
				elif event.key in (pygame.K_RIGHT, pygame.K_d):
					if self.direction != (-1, 0):
						self.direction = (1, 0)
				elif event.key == pygame.K_p:
					self.paused = not self.paused
				elif event.key == pygame.K_r and self.game_over:
					self.reset()
				elif event.key == pygame.K_q:
					pygame.quit()
					sys.exit(0)

	def update(self):
		if self.game_over or self.paused:
			return
		head_x, head_y = self.snake[0]
		dx, dy = self.direction
		new_head = (head_x + dx, head_y + dy)
		if (
			new_head[0] < 0
			or new_head[0] >= GRID_WIDTH
			or new_head[1] < 0
			or new_head[1] >= GRID_HEIGHT
			or new_head in self.snake
		):
			self.game_over = True
			if self.score > self.highscore:
				self.highscore = self.score
				save_highscore(self.highscore)
			return
		self.snake.insert(0, new_head)
		if new_head == self.food:
			self.score += 1
			if self.score % 5 == 0:
				self.speed += 1
			self.spawn_food()
		else:
			self.snake.pop()

	def draw_grid(self):
		for x in range(0, WINDOW_WIDTH, GRID_SIZE):
			pygame.draw.line(self.screen, GRAY, (x, 0), (x, WINDOW_HEIGHT))
		for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
			pygame.draw.line(self.screen, GRAY, (0, y), (WINDOW_WIDTH, y))

	def draw(self):
		self.screen.fill(BLACK)
		self.draw_grid()
		for i, segment in enumerate(self.snake):
			r = pygame.Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
			color = GREEN if i == 0 else BLUE
			pygame.draw.rect(self.screen, color, r)
		fx, fy = self.food
		food_rect = pygame.Rect(fx * GRID_SIZE, fy * GRID_SIZE, GRID_SIZE, GRID_SIZE)
		pygame.draw.rect(self.screen, RED, food_rect)
		draw_text(self.screen, f"Score: {self.score}", 24, WHITE, (10, 10), center=False)
		draw_text(self.screen, f"Highscore: {self.highscore}", 24, WHITE, (WINDOW_WIDTH - 10, 10), center=False)
		if self.paused:
			draw_text(self.screen, "Paused", 72, WHITE, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
		if self.game_over:
			draw_text(self.screen, "Game Over", 64, RED, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 40))
			draw_text(self.screen, "Press R to restart or Q to quit", 28, WHITE, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20))
		pygame.display.flip()

	def show_main_menu(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit(0)
				if event.type == pygame.KEYDOWN:
					if event.key in (pygame.K_RETURN, pygame.K_SPACE):
						return
					if event.key == pygame.K_q:
						pygame.quit()
						sys.exit(0)
			self.screen.fill(BLACK)
			draw_text(self.screen, "Snake", 96, GREEN, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 60))
			draw_text(self.screen, "Press Enter/Space to start", 28, WHITE, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 10))
			draw_text(self.screen, "Arrows / WASD to move — P to pause — Q to quit", 20, WHITE, (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 40))
			pygame.display.flip()
			self.clock.tick(30)

	def run(self):
		self.show_main_menu()
		while True:
			self.handle_input()
			self.update()
			self.draw()
			self.clock.tick(self.speed)


def main():
	game = SnakeGame()
	game.run()


if __name__ == "__main__":
	main()

