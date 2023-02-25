## Installation of Django ##
24 January 2023    
                                                  Django 4.1.7


System required
----------------------
windows 10 Pro

Install
-------
   Firstly, you must download python, preferably a higher version
   Download and install, if you haven't done so already, see:
   www.python.org
   Pip is a package installer for python
   Check pip version in cmd by typing 
   python -mpip --version
   result> pip X.Y.Z from python version

   To download Apache
   You must first install the Visual C++ Redistributable for Visual Studio 2015-2019 x64. 
   Download and Install, if you have not done so already, see:

   https://www.apachelounge.com/download/

  Unzip the Apache24 folder to c:/Apache24 (that is the ServerRoot in the config).
  The default folder for your your webpages is DocumentRoot "c:/Apache24/htdocs"

  When you unzip to an other location: 
  change Define SRVROOT "c:/Apache24"  in httpd.conf, for example to "E:/Apache24"

Run and test
------------

  Open a command prompt window and cd to the c:\Apache24\bin folder.
  
  To Start Apache in the command prompt type:
  
    >httpd.exe
  
  Press Enter. If there are any errors it will tell you. 
  Warnings will not stop Apache from working, they do need to be addressed none the less. 
  If there are no errors the cursor will sit and blink on the next line. 
  
  You can test your installation by opening up your Browser and typing in the address:
  
     http://localhost
  
  You can shut down Apache by pressing Ctrl+C (It may take a few seconds)
  
  To Install mod-wsgi (i don't know)

  To install Django use the command 
  pip install Django
  
  To check if the Django has been installed type
  django-admin --version
   result> will give the version of Django you have.
   if nothing or an error appears then reinstall Django

   o verify that Django can be seen by Python, type python from your shell. Then at the Python prompt, try to import Django:

  import django
  print(django.get_version())
  4.1.7




   Divina
  



