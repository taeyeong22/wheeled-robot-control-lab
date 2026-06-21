import math


class BicycleModel:
    def __init__(self, x=0.0, y=0.0, yaw=0.0, v=0.0, wheelbase=0.3):
        self.x = x
        self.y = y
        self.yaw = yaw
        self.v = v
        self.L = wheelbase

    def update(self, acceleration, steering_angle, dt):
        self.x += self.v * math.cos(self.yaw) * dt
        self.y += self.v * math.sin(self.yaw) * dt
        self.yaw += self.v / self.L * math.tan(steering_angle) * dt
        self.v += acceleration * dt

    def state(self):
        return {
            "x": self.x,
            "y": self.y,
            "yaw": self.yaw,
            "v": self.v
        }


if __name__ == "__main__":
    car = BicycleModel()

    dt = 0.1

    for step in range(100):
        car.update(
            acceleration=0.1,
            steering_angle=math.radians(5),
            dt=dt
        )

        print(step, car.state())
