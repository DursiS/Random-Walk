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

    def expectation(self) -> float:
        """Return the expected final height given
        len(self.steps) steps were taken."""
        expt = self.theta * self.step_up + (1 - self.theta) * self.step_down
        return len(self.path) * expt

    def var(self) -> float:
        """Return the variance of this random walk"""
        c1 = self.theta * (self.step_up**2) + (1 - self.theta) * (self.step_down**2)
        c2 = (self.theta * self.step_up + (1 - self.theta) * self.step_down) ** 2
        return len(self.path) * (c1 - c2)

    def std(self) -> float:
        """Return the standard deviation of this random walk"""
        return self.var() ** (1 / 2)


def corr(w1: RandomWalk, w2: RandomWalk) -> float:
    """Return the correlation between <w1> and <w2>."""


def cov(w1: RandomWalk, w2: RandomWalk) -> float:
    """Return the covariance between <w1> and <w2>."""


if __name__ == "__main__":
    rw1 = RandomWalk(1 / 2, 1.0, -1.0)  # theta, step_up, step_down
    rw2 = RandomWalk(1 / 2, 0.5, -0.5)
    n = 300  # Number of steps

    # Graphs for both Random Walks
    rw1.run(n)
    x_rw1, y_rw1 = [item[0] for item in rw1.path], [item[1] for item in rw1.path]
    plt.plot(x_rw1, y_rw1)

    rw2.run(n)
    x_rw2, y_rw2 = [item[0] for item in rw2.path], [item[1] for item in rw2.path]
    plt.plot(x_rw2, y_rw2)

    # Root and Legend
    x2 = [i for i in range(n)]
    y2 = [200 ** (1 / 2) for i in range(n)]
    y3 = [-(200 ** (1 / 2)) for i in range(n)]
    plt.plot(x2, y2, c="#FF0000", label="Root(n)")
    plt.plot(x2, y3, c="#FF0000")

    # Expectation
    expt_rw1, expt_rw2 = rw1.expectation(), rw2.expectation()
    y4_rw1 = [expt_rw1 for i in range(n)]
    plt.plot(x2, y4_rw1, c="#00008B", label="Expectation RW1")
    y4_rw2 = [expt_rw2 for i in range(n)]
    plt.plot(x2, y4_rw2, c="#FF8C00", label="Expectation RW2")

    plt.legend()
    plt.show()
