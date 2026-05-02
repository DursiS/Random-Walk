from Visualization import RandomWalk


def simulate(
    _n: int, _theta: float, _step_up: float, _step_down: float
) -> tuple[float, float]:
    """Return the final endpoint of 1 RandomWalk after <v> steps."""

    rw = RandomWalk(_theta, _step_up, _step_down)
    rw.run(_n)
    return rw.path[-1]


def get_average_endpoint(
    _n: int, _theta: float, _step_up: float, _step_down: float
) -> tuple[float, float]:
    """Return the average endpoint of a RandomWalk after <n> stimulation's."""

    gross_endpoint = [0.0, 0.0]
    for _ in range(_n):
        x, y = simulate(_n, _theta, _step_up, _step_down)
        gross_endpoint[0] += x
        gross_endpoint[1] += y
    return (gross_endpoint[0] / _n), (gross_endpoint[1] / _n)


if __name__ == "__main__":
    # Precondition: n > 0, theta > 0
    n = 100
    theta = 1 / 2
    step_up, step_down = 1.0, -1.0

    average = get_average_endpoint(n, theta, step_up, step_down)
    print(f"Average Endpoint: {average}")



# pnl = endpoints - paths[0, :]  # profit/loss
# losses = -pnl
# var_95 = np.percentile(losses, 95)
