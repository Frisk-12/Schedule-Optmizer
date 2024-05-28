# Employee Scheduling Optimization with Flask and OR-Tools

This Python code is a Flask web application designed to optimize employee scheduling using Google OR-Tools. The application allows users to input data regarding employees, their absences, and their shift preferences through a web interface. The OR-Tools Constraint Programming (CP) solver is then used to find an optimal solution that maximizes overall employee satisfaction while adhering to various constraints.

## Features:

- **Web Interface**: The application provides a simple web interface built with Flask, allowing users to interact with the scheduling system.
- **Input Data**: Users can input data such as a list of employees, their absences, and their shift preferences.
- **Optimization Problem**: The core of the application involves solving an optimization problem using OR-Tools CP solver. This problem includes assigning shifts to employees over a certain number of days and shifts per day, while considering their preferences and absences.
- **Constraints**: The optimization problem considers constraints such as the maximum number of working hours per week for each employee, as well as ensuring a minimum number of employees are assigned to each shift.
- **Maximization Objective**: The objective of the optimization problem is to maximize overall employee satisfaction, which is represented by a preference score calculated based on the assigned shifts.

## Code Overview:

- **Flask App Setup**: The code sets up a Flask web application, defining routes for serving HTML templates and handling POST requests.
- **Input Handling**: The `solve()` function retrieves input data from a JSON payload sent via a POST request.
- **Model Definition**: The OR-Tools CP model is defined, including decision variables for each employee, day, and shift, as well as constraints to enforce preferences, absences, and working hour limits.
- **Objective Function**: The preference score is defined as the objective function to be maximized using the CP solver.
- **Solver Invocation**: The CP solver is invoked to find the optimal solution to the scheduling problem.
- **Result Formatting**: If an optimal solution is found, the result is formatted as a JSON response and returned to the user.

## Usage:

1. Start the Flask web application by running the script.
2. Access the web interface in a browser and input the required data.
3. Submit the data to solve the optimization problem.
4. View the optimized schedule returned by the application.

