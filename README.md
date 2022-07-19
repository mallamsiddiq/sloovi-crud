# DOCUMENTATION ON THE TEST APP



## Navigation

The app was built and hosted on heroku with functionality as described in the documentation. register as a new user at the endpoint: //sloovi-sodiq.herokuapp.com/register/, play with the api as a restful endpoint using you prefered client but for ease of navigation and better clarification and documentation, i have integrated a swagger UI with the app, kindly check https://sloovi-sodiq.herokuapp.com/swagger/ or https://sloovi-sodiq.herokuapp.com/redoc/. view all created templates at the endpoint https : //sloovi-sodiq.herokuapp.com/template with GET request, on this same endpoint use POSTrequest to create a new template. update, retrieve, and delete any unique template at the https://sloovi-sodiq.herokuapp.com/template/<template_id>/  with the unique template_id as the query parameter. please note: these endpoints requires that you're an authenticated user. register and login appropriately. the https://sloovi-sodiq.herokuapp.com/login/ and refresh token the https://sloovi-sodiq.herokuapp.com/login-refresh-token/. The 
https://sloovi-sodiq.herokuapp.com/users support a get request to fetch your details as a registered user. while https://sloovi-sodiq.herokuapp.com/users/<user_id>/  will support update, retrieve, and delete for your details. 

## running loclly

This app is built as a docker image for ease of environment conflicts. with docker installed kidly

		docker-compose up --build

And boom you have your app on port :5000

### without docker

if docker isn't installed on your machine, chill i have you covered. With python and pip installed. 

kindly run:

		pip install -r requirements.txt

		python manage.py migrate

		python manage.py runserver 0.0.0.0:8000

or at once run:

		pip install -r requirements.txt && python manage.py migrate && python manage.py runserver 0.0.0.0:8000

and boom!! again you have your app on port :5000. all navigation is as described in the navigation headline, just replace https://sloovi-sodiq.herokuapp.com http://localhost/5000 and you’re good to go.
  
# Note:

For the sake of this assessment and third party testing, I have created a test user and database called sloovi and sloovi-test-db respectively and exposed environment variables. freely playing around with api

  
For further enquiry : i am available @mallamsiddiq@gmail.com or https://www.linkedin.com/in/nutfa/ 

thanks 

SODIQ

