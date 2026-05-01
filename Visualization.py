import random
import matplotlib.pyplot as plt


class RandomWalk:
    """A position evolving step-by-step randomly.

    Public Attributes:
        - position: The net change of all steps from origin 0.0
        - theta: The probability of stepping up
        - step_up: How much to increment up by when stepping up
        - step_down: How much to increment down by when stepping down
        - path: A history of all positions, right-most being current position
    """

    position: tuple[float, float]
    theta: float
    step_up: float
    step_down: float
    path: list[tuple[float, float]]

    def __init__(self, theta: float, step_up: float, step_down: float) -> None:
        """Create a new random walk."""
        self.position = 0.0, 0.0
        self.theta = theta
        self.step_up = step_up
        self.step_down = step_down
        self.path = [(0, 0)]

    def step(self) -> None:
        """Move *one* step forward"""

        if random.random() < self.theta:
            step = self.step_up
        else:
            step = self.step_down

        new_pos = self.position[0] + 1.0, self.position[1] + step
        self.position = new_pos
        self.path.append(new_pos)

    def run(self, n: int) -> None:
        """Move <n> consecutive steps forward"""

        for i in range(n):
            self.step()


if __name__ == "__main__":
    rw = RandomWalk(1 / 2, 1.0, -1.0)
    n = 200

    rw.run(n)
    x, y = [item[0] for item in rw.path], [item[1] for item in rw.path]
    plt.plot(x, y)

    x2 = [i for i in range(n)]
    y2 = [200 ** (1 / 2) for i in range(n)]
    y3 = [-(200 ** (1 / 2)) for i in range(n)]
    plt.plot(x2, y2, c="#FF0000", label="Root(n)")
    plt.plot(x2, y3, c="#FF0000")

    plt.legend()
    plt.show()
