#Zoo Sensor Event System

A simulation project that models a zoo monitoring system using virtual sensors and employees. The goal is to simulate how different types of sensors trigger events, and how employees with different roles respond based on their responsibilities.

---

##Purpose

In real-world animal facilities like zoos or wildlife parks, various environmental and security sensors are used to monitor animal safety and living conditions. This project mimics that logic using Python by:

- Simulating **motion**, **temperature**, and **humidity** sensors.
- Generating **random events**.
- Assigning **employees** to handle events based on their roles.
- Printing realistic logs to simulate live responses.

---

##Technologies

- Python 3.x
- OOP (Object-Oriented Programming)
- Randomized simulation
- Role-based logic

---

##Roles & Responsibilities

| Sensor Type  | Triggered Event              | Responsible Role |
|--------------|------------------------------|------------------|
| `motion`     | Motion sensor triggered       | `guard`          |
| `humidity`   | Humidity sensor triggered     | `zookeeper`      |
| `temperature`| Temperature sensor triggered  | `cleaner`        |

Employees only respond to events related to their defined role. Also there are some other roles that you can define their jobs.

---

This project is open-source and free to use.


