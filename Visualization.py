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


def cov(w1: RandomWalk, w2: RandomWalk) -> float:
    """Return the covariance between <w1> and <w2>."""
    w1_expt, w2_expt = w1.expectation(), w2.expectation()

    c1 = (w1.theta * w2.theta) * (w1.step_up * w2.step_up)
    c2 = (w1.theta * (1 - w2.theta)) * (w1.step_up * w2.step_down)
    c3 = ((1 - w1.theta) * w2.theta) * (w1.step_down * w2.step_up)
    c4 = ((1 - w1.theta) * (1 - w2.theta)) * (w1.step_down * w2.step_down)

    return (c1 + c2 + c3 + c4) - (w1_expt * w2_expt)


def corr(w1: RandomWalk, w2: RandomWalk) -> float:
    """Return the correlation between <w1> and <w2>."""
    w1_var, w2_var = w1.var(), w2.var()
    return cov(w1, w2) / ((w1_var * w2_var) ** (1 / 2))


def visualize(w: RandomWalk) -> None:
    """Plot the <number>th RandomWalk"""
    x1, y1 = [item[0] for item in w.path], [item[1] for item in w.path]
    plt.plot(x1, y1)


def visualize_stats(w: RandomWalk, number: int, n: int) -> None:
    """Plot the stats for the <number>th RandomWalk after <n> steps."""
    # Mean
    x1 = [item[0] for item in w.path]
    expt = w.expectation()
    y2 = [expt for i in range(n)]
    plt.plot(x1[:-1], y2, c="#00008B", label=f"Mean {number}")

    # Root and Legend
    x2 = [i for i in range(n)]
    y2 = [n ** (1 / 2) for i in range(n)]
    y3 = [-(n ** (1 / 2)) for i in range(n)]
    plt.plot(x2, y2, c="#FF0000", label="Root(n)")
    plt.plot(x2, y3, c="#FF0000")


if __name__ == "__main__":
    rw1 = RandomWalk(1 / 2, 1.0, -1.0)  # theta, step_up, step_down
    rw2 = RandomWalk(1 / 2, 0.5, -0.5)
    n = 1000  # Number of steps, n > 0

    # RandomWalk #1
    rw1.run(n)
    visualize(rw1)
    visualize_stats(rw1, 1, n)

    # RandomWalk #2
    rw2.run(n)
    visualize(rw2)
    visualize_stats(rw2, 2, n)

    # Corr and plotting
    plt.plot(0, 0, label=f"Correlation = {corr(rw1, rw2)}")
    plt.legend()
    plt.show()
