# 002. Vehicle Modeling

The first technical step of this project is to understand how a small wheeled vehicle can be represented as a mathematical model.

In real vehicles, motion is affected by many complex factors such as tire deformation, suspension dynamics, road friction, actuator delay, and sensor noise. However, for the first stage of this project, I will start with a simplified model.

A simple and useful model for studying basic vehicle motion is the kinematic bicycle model.

---

## Why Use a Bicycle Model?

A real car has four wheels, but modeling all four wheels from the beginning can make the problem unnecessarily complex.

The bicycle model simplifies the vehicle by combining the left and right front wheels into one virtual front wheel, and the left and right rear wheels into one virtual rear wheel.

This simplification makes it easier to study the relationship between:

* vehicle position
* heading angle
* velocity
* steering angle
* wheelbase

Although the model is simplified, it is still useful for understanding basic vehicle motion and path tracking control.

---

## State Variables

In the current Python implementation, the vehicle state is described using four main variables.

* `x`: vehicle position along the global x-axis
* `y`: vehicle position along the global y-axis
* `yaw`: heading angle of the vehicle
* `v`: vehicle velocity

The vehicle also has one important physical parameter:

* `L`: wheelbase, which is the distance between the front and rear wheels

---

## Control Inputs

The model uses two control inputs.

* `acceleration`: changes the vehicle velocity
* `steering_angle`: changes the vehicle direction

By changing these inputs over time, the vehicle trajectory can be simulated.

---

## Model Update

At each time step, the vehicle state is updated based on its current velocity and steering angle.

The current implementation updates the state using a simple time step `dt`.

The basic idea is:

* if velocity increases, the vehicle moves farther
* if steering angle is zero, the vehicle moves mostly straight
* if steering angle is not zero, the vehicle changes its heading angle
* if the wheelbase is longer, the vehicle turns more slowly
* if the wheelbase is shorter, the vehicle turns more sharply

---

## Current Python File

The first implementation is located in:

```txt
simulation/bicycle_model.py
```

This file defines a simple `BicycleModel` class and updates the vehicle state for 100 simulation steps.

The first version is intentionally simple.
The goal is not to build a perfect vehicle model immediately, but to create a foundation for future simulation and control experiments.

---

## Limitations of the Current Model

This first model does not include:

* tire slip
* road friction
* motor delay
* steering delay
* sensor noise
* lateral dynamics
* suspension effects

These limitations are acceptable at the beginning because the main purpose is to understand the basic relationship between steering, velocity, and vehicle motion.

Later, more realistic effects can be added step by step.

---

## Next Step

The next step is to visualize the vehicle trajectory using Python.

Instead of only printing numerical values, I will plot the vehicle path on a 2D graph and observe how the trajectory changes when steering angle, velocity, and wheelbase are changed.
