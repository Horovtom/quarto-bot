import abc


class Scene(abc.ABC):
    def __init__(self, next_state=None, next_args=None):
        self.next = next_state
        self.next_args = next_args
        self.done = False
        self.initialized = False

    def reset(self):
        """Prepare for next time scene has control."""
        self.done = False
        self.initialized = False

    def get_event(self, event):
        """Overload in child."""
        pass

    def update(self, now):
        """If the start time has not been set run necessary startup."""

    def initialize(self, *args):
        self.initialized = True

    @abc.abstractmethod
    def draw(self, surface):
        pass
