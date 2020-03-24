# Car part shopping list application

### Solo project due 24/03/2020 for QA Academy Devops.

Index



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

Initial plan was to create three tables, table 1 would be car, table 2 would be parts and table 3 would be a middle table called orders linking the 2 as they would be many to many.

![erd](https://github.com/zedz65/myproject/blob/master/Documentation/erd.jpg)

## Solution:

However the solution that was delivered was based on a 2 table solution, compromising of table 1 Car and table 2 Parts, with a one to many relationship. Therefore one car could have many parts which seemed a logically solution based on the conditions and time constraints we had.
