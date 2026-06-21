# 001. Research Motivation

I am interested in wheeled machines because they are familiar, practical, and technically complex.

A car or a small mobile robot may look simple from the outside, but its motion depends on many physical and control-related factors:

- velocity
- steering angle
- wheelbase
- tire friction
- center of mass
- sensor noise
- control delay

The purpose of this project is to study how a small wheeled vehicle can be modeled, controlled, simulated, and tested.

At the beginning, I will focus on simple vehicle models and path tracking control algorithms. Later, I plan to connect the simulation results to a physical RC-car-based platform.

## Research Questions

- How can a wheeled vehicle follow a target path?
- How does steering angle affect the vehicle trajectory?
- What are the limitations of simple PID control?
- How are Pure Pursuit and Stanley Controller different?
- How can simulation results be validated with hardware experiments?

## First Goal

The first goal is to implement a simple vehicle model in Python and observe how the vehicle state changes with velocity and steering angle.
