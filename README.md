# Error Propagation Calculator
A web application (Developed with the Django framework, Tailwind CSS, and JQuery) for error propagation of any mathematical expression that has physical quantities with errors. The propagation follows the general formula for error propagation (the quadrature of partials multiplied with their uncertainties). I developed the web app because I had already written a python3 script for my physics senior lab that propagates error and wanted to expand on that and learn to develop websites using Django and Tailwind. 

# General Formula For Error Propagation
![Equation used in propagating errors](/assets/images/e-prop-eq.PNG)

# Running The Web App
The web app is not yet published but could be run with

1. `python3 manage.py runserver` 
2. and directing to `localhost:8000/epapp` on your favorite web browser. 

You also need to have the sympy and django libraries installed
# Picture Examples

![Form for inputting values](/assets/images/ex-picture-no-result.PNG)

![Form with input and Results](/assets/images/ex-pic-with-inp-and-res.PNG)


