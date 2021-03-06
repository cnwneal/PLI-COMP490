# PLI-COMP490

An online module to allow non-attorneys to learn about legal processes and procedure in Cook County Illinois and to train non-lawyers
to provide legal information to the community. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
*basic understanding of python
*basic understanding of phpMyadmin
*basic understanding of html/css


### Installing
* Install the newest verion of python or 2.7
* Insatll XAMPP
* Install virtual enviorment with: pip install virtualenvwrapper-win
* cd into where the project will be created
* make a virtual enviorment with: mkvirtualenv and name it ex: mkvirtualenv test
* workon test
* then install django globally with pip install django
* create django application with: django-admin startproject test
* test that it works with python manage.py runserver
* set up database in settings file
* first install database in this case mysql with: pip install mysqlclient
*create models 
* create a database called pli if you don't have one in your phpmyadmin
*then run python manage.py makemigrations
* then migrate with python manage.py migrate
* create user with python manage.py createsuperuser --username=Name --email=email

## Common Issues and fixes



## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Djgango](https://docs.djangoproject.com) - The web framework used
* [Python](https://www.python.org/) - language
* [MySQL](https://www.mysql.com/) - database
* [PhpMyAdmin](https://www.phpmyadmin.net/) - database

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Online Resources
* https://scotch.io/tutorials/build-your-first-python-and-django-application
* https://python-forum.io/Thread-Basic-Part-1-Python-3-6-and-pip-installation-under-Windows
* https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database
* https://www.packtpub.com/mapt/book/web_development/9781784391911/10/ch10lvl1sec63/creating-models-for-diverse-content
* https://tutorial.djangogirls.org/en/django_views/
* http://www.effectivedjango.com/tutorial/views.html
* https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website
*https://chrisbartos.com/articles/what-do-you-do-when-makemigrations-is-telling-you-about-your-lack-of-default-value/

## Versioning



## Authors

* **Chlece Neal** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Chawn Neal
* Vaibhav R. Thakkar
* Participants in the Preventative Law Clinics 




