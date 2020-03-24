# Car part shopping list application

## Solo project due 24/03/2020 for QA Academy Devops.


## Assignment Brief

To create a CRUD application using flask incorporating all the methodologies and technologies covered in our core modules during our time at the academy. Application should manipulate through at least two tables.

## Solution

My solution is to create a car parts shopping application that allows the user to create cars and parts for that car, as well as modify and delete parts from their list.

I have created a one to many relationship between cars and parts. For example one car can have many parts.

The database is working and allows the user to add a car and add parts to the list for the specified car. It also allows us to add more cars and then parts related to that car. We can also delete the parts from table once we are done with the list.

## Architecture

## Entity relationship Diagrams:

![erd2](https://github.com/zedz65/myproject/blob/master/Documentation/erd2.jpg)

## Initial plan:

Initial plan was to create three tables, table 1 would be car, table 2 would be parts and table 3 would be a middle table called orders linking the 2.

![erd](https://github.com/zedz65/myproject/blob/master/Documentation/erd.jpg)

## Solution:

However the solution that was delivered was based on a 2 table solution, compromising of table 1 Car and table 2 Parts, with a one to many relationship. Therefore one car could have many parts which seemed a logically solution based on the conditions and time constraints we had.

### Deployment

For the build and deployment of the app  we are using Jenkins with a webhook to our git repo which is triggered during every build.

The app is running as a systemd service. Using a .service file in git and a build shell in Jenkins.

GCP is also used to run our flask app on a virtual machine and the sql database.

![ci](https://github.com/zedz65/myproject/blob/master/Documentation/ci.jpg)

Ci pipeline

### Testing

For testing pytest was used but not fully completed

### Technologies used:

Visual studio code – Source code

Version control system – Git

Project tracking – Trello

Testing – Pytest

CI server – Jenkins

VM SQL – GCP

## Front end design:

![home](https://github.com/zedz65/myproject/blob/master/Documentation/home1.jpg)

Home page with no entries

![car](https://github.com/zedz65/myproject/blob/master/Documentation/car1.jpg)

Car page with forms

![part](https://github.com/zedz65/myproject/blob/master/Documentation/part1.jpg)

Parts page with forms

![final](https://github.com/zedz65/myproject/blob/master/Documentation/final1.jpg)
final home page displaying car and parts for specific vehicle

![shell](https://github.com/zedz65/myproject/blob/master/Documentation/shell.jpg)
Build shell Jenkins

![trello](https://github.com/zedz65/myproject/blob/master/Documentation/trello.jpg)
shot of trello

## Improvements:

App has a lot of scope for improvement, currently it does not have update functionality fully working requires a bit work. This was the plan for the next sprint however working between a vm and windows is very time consuming.

For future sprints could also add specific delete functionality to each part or each car, at the moment it deletes all the parts in your list.

Another big improvement would be adding more drop down lists for parts or for cars instead of inserting strings, this was the original plan however was running low on time so couldn&#39;t see it through fully.

All in all great working on the project and searching for answers online instead of asking people, with a bit more time and better circumstances the project would be finished to a higher standard. However the support from trainers and trainees is great.


##AUTHOR: Zahid Ali
