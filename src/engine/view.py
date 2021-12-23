"""View class as part of MVC model"""
import pygame
from src.engine.event_types import QuitEvent


class PygameView:
    """Pygame UI class"""

    def __init__(self, ev_manager, model):
        """Constructor"""

        self.ev_manager = ev_manager
        ev_manager.register_listener(self)
        self.model = model

        self.initialised = False
        self.screen = None
        self.clock = None
        self.initialise()

    def initialise(self):
        """Create and initialise a pygame instance"""

        pygame.init()
        pygame.display.set_caption("Chess Engine")

        self.screen = pygame.display.set_mode((512, 512))
        self.smallfont = pygame.font.Font(None, 40)
        self.clock = pygame.time.Clock()
        self.initialised = True

    def render(self):
        """Render the screen"""
        if not self.initialised:
            return

        self.screen.fill((0, 0, 0))
        # draw some words on the screen
        somewords = self.smallfont.render(
            "The View is busy drawing on your screen", True, (0, 255, 0)
        )
        self.screen.blit(somewords, (0, 0))
        # flip the display to show whatever we drew
        pygame.display.flip()
        # Implement screen refresh/update/render here after return statement

    def notify(self, event):
        """Process the event and decide what to do"""
        if isinstance(event, QuitEvent):
            self.initialised = False
            pygame.quit()
        else:
            self.render()
        # Process all other events here
