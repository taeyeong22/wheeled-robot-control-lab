import math
from pathlib import Path

import matplotlib.pyplot as plt


def generate_reference_path(
    length=20.0,
    step=0.1,
    amplitude=2.0,
    wavelength=10.0,
):
    if length <= 0:
        raise ValueError(
            "length must be greater than zero"
        )

    if step <= 0:
        raise ValueError(
            "step must be greater than zero"
        )

    if wavelength <= 0:
        raise ValueError(
            "wavelength must be greater than zero"
        )

    point_count = int(length / step) + 1

    x_history = []
    y_history = []
    yaw_history = []

    for index in range(point_count):
        x = index * step

        wave_angle = (
            2.0
            * math.pi
            * x
            / wavelength
        )

        y = amplitude * math.sin(
            wave_angle
        )

        slope = (
            amplitude
            * 2.0
            * math.pi
            / wavelength
            * math.cos(wave_angle)
        )

        yaw = math.atan2(
            slope,
            1.0,
        )

        x_history.append(x)
        y_history.append(y)
        yaw_history.append(yaw)

    return {
        "x": x_history,
        "y": y_history,
        "yaw": yaw_history,
    }


def plot_reference_path(path):
    project_dir = (
        Path(__file__)
        .resolve()
        .parents[1]
    )

    plot_dir = (
        project_dir
        / "assets"
        / "plots"
    )

    plot_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    plt.figure(
        figsize=(10, 5)
    )

    plt.plot(
        path["x"],
        path["y"],
        color="green",
        linewidth=2,
        label="Reference path",
    )

    plt.scatter(
        path["x"][0],
        path["y"][0],
        color="blue",
        label="Start",
    )

    plt.scatter(
        path["x"][-1],
        path["y"][-1],
        color="red",
        label="End",
    )

    plt.xlabel("X position [m]")
    plt.ylabel("Y position [m]")

    plt.title(
        "Reference Path for Path Tracking"
    )

    plt.axis("equal")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    output_path = (
        plot_dir
        / "reference_path.png"
    )

    plt.savefig(
        output_path,
        dpi=150,
    )

    print(
        "Reference path plot saved:",
        output_path,
    )

    plt.show()


if __name__ == "__main__":
    reference_path = (
        generate_reference_path()
    )

    plot_reference_path(
        reference_path
    )
