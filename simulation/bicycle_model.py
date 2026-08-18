import math
from pathlib import Path

import matplotlib.pyplot as plt


class BicycleModel:
    def __init__(
        self,
        x=0.0,
        y=0.0,
        yaw=0.0,
        v=0.0,
        wheelbase=0.3
    ):
        self.x = x
        self.y = y
        self.yaw = yaw
        self.v = v
        self.L = wheelbase

    def update(
        self,
        acceleration,
        steering_angle,
        dt
    ):
        self.x += (
            self.v
            * math.cos(self.yaw)
            * dt
        )

        self.y += (
            self.v
            * math.sin(self.yaw)
            * dt
        )

        self.yaw += (
            self.v
            / self.L
            * math.tan(steering_angle)
            * dt
        )

        self.v += acceleration * dt

    def state(self):
        return {
            "x": self.x,
            "y": self.y,
            "yaw": self.yaw,
            "v": self.v
        }


def run_simulation():
    car = BicycleModel(
        v=0.5,
        wheelbase=0.3
    )

    dt = 0.1
    simulation_steps = 100

    acceleration = 0.1

    steering_angle = math.radians(
        5
    )

    time_history = []
    x_history = []
    y_history = []
    yaw_history = []
    velocity_history = []

    for step in range(
        simulation_steps
    ):
        current_time = step * dt

        car.update(
            acceleration=acceleration,
            steering_angle=steering_angle,
            dt=dt
        )

        current_state = car.state()

        time_history.append(
            current_time
        )

        x_history.append(
            current_state["x"]
        )

        y_history.append(
            current_state["y"]
        )

        yaw_history.append(
            math.degrees(
                current_state["yaw"]
            )
        )

        velocity_history.append(
            current_state["v"]
        )

    return {
        "time": time_history,
        "x": x_history,
        "y": y_history,
        "yaw": yaw_history,
        "velocity": velocity_history
    }


def plot_results(history):
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
        exist_ok=True
    )

    # 차량 이동 경로 그래프
    plt.figure(
        figsize=(8, 6)
    )

    plt.plot(
        history["x"],
        history["y"],
        color="blue",
        linewidth=2,
        label="Vehicle trajectory"
    )

    plt.scatter(
        history["x"][0],
        history["y"][0],
        color="green",
        label="Start"
    )

    plt.scatter(
        history["x"][-1],
        history["y"][-1],
        color="red",
        label="End"
    )

    plt.xlabel(
        "X position [m]"
    )

    plt.ylabel(
        "Y position [m]"
    )

    plt.title(
        "Kinematic Bicycle Model Trajectory"
    )

    plt.axis("equal")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    trajectory_path = (
        plot_dir
        / "trajectory.png"
    )

    plt.savefig(
        trajectory_path,
        dpi=150
    )

    # 시간에 따른 속도와 방향각
    figure, axes = plt.subplots(
        2,
        1,
        figsize=(8, 7)
    )

    axes[0].plot(
        history["time"],
        history["velocity"],
        color="orange"
    )

    axes[0].set_xlabel(
        "Time [s]"
    )

    axes[0].set_ylabel(
        "Velocity [m/s]"
    )

    axes[0].set_title(
        "Vehicle Velocity"
    )

    axes[0].grid(True)

    axes[1].plot(
        history["time"],
        history["yaw"],
        color="purple"
    )

    axes[1].set_xlabel(
        "Time [s]"
    )

    axes[1].set_ylabel(
        "Yaw angle [deg]"
    )

    axes[1].set_title(
        "Vehicle Yaw Angle"
    )

    axes[1].grid(True)

    figure.tight_layout()

    state_history_path = (
        plot_dir
        / "state_history.png"
    )

    figure.savefig(
        state_history_path,
        dpi=150
    )

    print(
        "Trajectory plot saved:",
        trajectory_path
    )

    print(
        "State history plot saved:",
        state_history_path
    )

    plt.show()


if __name__ == "__main__":
    simulation_history = (
        run_simulation()
    )

    plot_results(
        simulation_history
    )
