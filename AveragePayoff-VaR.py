from Visualization import RandomWalk
import numpy as np


def simulation(
    _n: int, _theta: float, _step_up: float, _step_down: float
) -> tuple[float, float]:
    """Return the final endpoint of 1 RandomWalk after <_n> steps."""

    rw = RandomWalk(_theta, _step_up, _step_down)
    rw.run(_n)
    return rw.path[-1]


def simulate(
    _n: int, _theta: float, _step_up: float, _step_down: float
) -> list[tuple[float, float]]:
    """Return a list of <_n> endpoints from different RandomWalks."""

    lst = []
    for _ in range(_n):
        lst.append(simulation(_n, _theta, _step_up, _step_down))
    return lst


def get_average_endpoint(
    _n: int, _endpoints: list[tuple[float, float]]
) -> tuple[float, float]:
    """Return the average of the endpoints in <endpoints>
    after <_n> simulations."""

    gross_endpoint = [0.0, 0.0]
    for endpoint in _endpoints:
        x, y = endpoint[0], endpoint[1]
        gross_endpoint[0] += x
        gross_endpoint[1] += y
    return (gross_endpoint[0] / _n), (gross_endpoint[1] / _n)


def get_average_pnl(
    _n: int, endpoints: list[tuple[float, float]], start: tuple[float, float] = (0, 0)
) -> float:
    """Return the average PNL in <endpoints> after <_n> simulations."""

    gross_pnl = 0.0
    for endpoint in endpoints:
        gross_pnl += endpoint[1] - start[1]
    return gross_pnl / _n


if __name__ == "__main__":
    # Precondition: n > 0, theta > 0
    n = 1000
    theta = 1 / 2
    step_up, step_down = 1.0, -1.0

    # Print average endpoint, pnl and VaR
    endpoints = simulate(n, theta, step_up, step_down)

    average_endpoint = get_average_endpoint(n, endpoints)
    print(f"Average Endpoint: {average_endpoint}")

    average_pnl = get_average_pnl(n, endpoints)
    print(f"Average PNL: {average_pnl}")

    var_95 = np.percentile([endpoint[1] for endpoint in endpoints], 95)
    print(f"VaR: {var_95}")
