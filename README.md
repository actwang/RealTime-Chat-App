## RealTimeChatApp with [Tailwind CSS](https://tailwindcss.com/)

#### Real Time Chat Application built with Django web Framework and Tailwind CSS
This is a Real time chatting application that allows admin to add Rooms for users to chat openly. 
The application includes login capability, and allows users to join and leave rooms on request. For development and leisure usage, each room has no limit in number of participants. 

This application provides a custom, modern looking UI with toggle password visibility. More importantly, it has a clean directory structure that is easy to navigate, suitable for understanding Django project file architechture.

#### Installation
To clone the repository code into your directory:

`git clone https://github.com/actwang/RealTime-Chat-App.git`

Go into the repository folder:

`cd RealTimeChatApp`

It is recommended to use a virtual environment for similar projects. To create a virtual environment call .venv inside the current directory, use this command:

`python3 -m venv .venv`

Alternatively, it's a better practice to use virtualenvwrapper to keep all virtual environments in one place: [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)

`pip install virtualenvwrapper`

and make a new virtual environment using:

`mkvirtualenv ChatAppVenv`

use `workon` to activate the project venv:

`workon ChatAppVenv`


#### Dependencies
The current project is built and tested with Python 3.9.10, but previous Python3 versions should also work.
The requirements.txt file specifies all other dependencies required, and can be installed by the following command.
To install the requirements after activating the virtual environment:

`pip install -r requirements.txt`

#### NOTE: DO NOT install the latest versions of django and channels using pip. 
The newer versions of django and channels installed through pip3 involves compatibility issues that will prevent the ASGI channel from successfully opening and listening for connection request. If you see your javascript developer tool logging webSocket connection failed, try verifying and installing the listed versions of channels and django in the requirements.txt file first. Namely: 

`pip install django==4.0.0`

`pip install django==4.0.1`

`pip install channels==3.0.4`

For details, check out this [stackoverflow](https://stackoverflow.com/questions/74091600/asgi-application-not-working-with-django-channels) post.

#### Future work
To add additional functionalities, in the future the task to create new rooms can be delegated to users or some selected group of authenticated users. To improve performance, use Redis as the channel_layer in this project and specify in settings.py. For performance scaling considerations, it's recommended to use a database more suitable and robust for higher consistency and scalability such as MySQL or POSTgreSQL. It's also recommended to use Redis for the channel_layers in this project, and specify it in settings.py of RealTimeChatApp directory.