# A00456020_djangorestapi

This is my repository for django rest api assignment for MCDA 5550.

I am Parth Tarak Vaidya, A00456020, MCDA Fall 2021 cohort, Saint Mary's University, Halifax.

The database used is MySQL database created using the following sql commands:

create database djangorestapi_db;
create user 'djangodbadmin'@'%' identified by "access";
grant all privileges on djangorestapi_db.* to 'djangodbadmin'@'%';

To get the list of all the hotels, use:

http://127.0.0.1:8000/hotels_list/  OR
GET Request to http://127.0.0.1:8000/hotels_list/ with empty body

To get a hotel by id, for example 7, use:

http://127..00.1:8000/hotels_list/7 OR
GET Request to http://127..00.1:8000/hotels_list/7 with empty body

to add new Hotel to database, use

POST Request to http://localhost:8080/hotels_list/ with Form data body containing:
(This will only work if the request body has follpwing key:value pairs in FORM DATA mode.)

id:5
name:AhmedabadGrand
website_url:ahmedabadinn.com
total_number_of_rooms:27
available_rooms:7

to delete hotel by any id, for example 7, use:

http://127..00.1:8000/delete_hotel/7 

----------OR-------------------

POST Request to http://127..00.1:8000/delete_hotel/7 with empty body

Thank you,
Parth Vaidya.
