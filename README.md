# Graphical Ball Motion Simulation

In this assignment, you are to implement a graphical motion simulation of
multiple ball objects, as shown.

![screen](docs/screen.png)


## Modules

Your application consists of five modules, three of which must be completed by
you.

### 1. Module `vector.py`

This module contains the `Vector` class for creating various vector
quantities used by the simulation.

The provided `vector.py` contains only some template code that you must
complete yourself.  Please look at `vector.py`'s
[documentation](docs/vector.md) for more details, including test cases that
will be used to grade this module.

### 2. Module `border.py`

This module contains the `Border` class for create a border surrounding
balls on the stage.

The provided `border.py` contains only some template code that you must
complete yourself.  Please look at `border.py`'s
[documentation](docs/border.md) for more details, including test cases that
will be used to grade this module.

### 3. Module `ball.py`
This module contains the `Ball` class for creating ball objects with
various physical properties such as position, velocity, and acceleration.
Each ball object knows how to update its own velocity and position.  When
surrounded by a border, the ball also knows when it hits a border's side and
updates its position and velocity accordingly.

The provided `ball.py` contains only some template code that you must
complete yourself.  Please look at `ball.py`'s
[documentation](docs/ball.md) for more details, including test cases that
will be used to grade this module.

### 4. Module `stage.py`
This module provides the `Stage` class for creating a `Stage` object that
incorporates a `Border` object and a list of `Ball` objects.  It is also
responsible for creating a graphical screen and a turtle-based painter object
to be used by the `Border` and `Ball` objects to draw themselves on the
screen.

This module is already completely implemented.  You don't have to add
anything.

### 5. Module `app.py`
This module implements an application that demonstrates the use of all the modules above
in a graphical window.

This module is already completely implemented.  You don't have to add
anything.


## Running Tests

Non-graphical tests can be performed by running each of the `vector.py`,
`border.py`, and `ball.py` directly.  They use the `doctest` to run all
examples found inside all the documentation files in the `docs` directory.

    python vector.py
    python border.py
    python ball.py


## Graphical Output

The graphical output elements is taken care of by the `stage.py` module.
However, you are required to implement the `draw` method in your `ball.py` and
`border.py`.  The `draw` method takes one `painter` argument which is a
`Turtle` object.  Consult [this
document](https://docs.python.org/3/library/turtle.html#turtle-methods) for
the list of turtle's drawing commands.

There is no definite rule on how you should draw your objects.  However, at
least the following is required:

* A `Ball` object must show with its current `color` property.
* A `Ball` object must show its movement trail, which keep track of the past
  10 positions of the ball.
* A `Border` object must clearly display its boundary.


