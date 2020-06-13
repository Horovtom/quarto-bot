
import pygame as pg
import graphics.settings as settings

class Scene:
    def __init__(self, next_state=None):
        self.next = next_state
        self.done = False
        self.start_time = None

    def startup(self, now):
        """Set present time and take a snapshot of the display."""
        self.start_time = now

    def reset(self):
        """Prepare for next time scene has control."""
        self.done = False
        self.start_time = None

    def get_event(self, event):
        """Overload in child."""
        pass

    def update(self, now):
        """If the start time has not been set run necessary startup."""
        if not self.start_time:
            self.startup(now)