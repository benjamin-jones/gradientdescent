Gradient Descent
===============

This is a simple example of linear regression via gradient descent.
We develop a cost function that is the square error of data with an
assumed linear model. The model has two parameters, slope (m) and
a y-intercept (b). The gradient of the error function is descended
until a certain percision is met or a maximum number of iterations.
Several threads start at random locations in the field and perform
their own descent.

Point data and the correct m/b are stored in CSV files.

An error surface visualizer is provided.

