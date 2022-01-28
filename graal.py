# class State:
#     def __init__(self, perso, graal):
#         self.perso = perso
#         self.graal = graal


# state = State(
#     perso=Perso(#blabla), 
#     graal=(x_graal, y_graal)
# )

# class RogueGame(Game):
#     def process_events(self, events):
#         perso = state.perso
#         for event in events:
#             if (
#                 event.type == pg.QUIT
#                 or event.type == pg.KEYDOWN
#                 and event.key == pg.K_q
#             ):
#                 self.quit()
#             elif event.type == pg.KEYDOWN:
#                 if event.key == pg.K_DOWN:
#                     perso.direction = DIRECTIONS["DOWN"]
#                 elif event.key == pg.K_UP:
#                     perso.direction = DIRECTIONS["UP"]
#                 elif event.key == pg.K_RIGHT:
#                     perso.direction = DIRECTIONS["RIGHT"]
#                 elif event.key == pg.K_LEFT:
#                     perso.direction = DIRECTIONS["LEFT"]
#                 elif event.key == pg.K_RIGHTPAREN:
#                     perso.ramasser()
#         try:
#             perso.move()
#         except SystemExit as error:
#             message = error.args[0]
#             self.quit(error=message)

#     def draw(self):
#         perso = state.perso
#         graal_x, graal_y = state.graal
#         draw_background(self.screen)
#         for x, y in objets.geometry:
#             draw_tile(self.screen, x, y, SNAKE_COLOR)
#         draw_tile(self.screen, fruit_x, fruit_y, FRUIT_COLOR)


# while True:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             pygame.quit()
#             sys.exit()

# if __name__ == "__main__":
#     snake_game = SnakeGame(size=(X * W, Y * H), fps=FPS)
#     snake_game.start()