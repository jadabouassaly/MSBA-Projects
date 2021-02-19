# Streamlit & Heroku

## This is a tutorial for developping a simple streamlit app and deploy it via Heroku

Create a Heroku account\
Install Heroku CLI\
Install GIT

1-Needed Files:\
requirements.txt : 
File contains all the libraries that need to be installed for the project to work. This file can be created manually by going through all files and looking what libraries are used or automatically using something like pipreqs.

setup.sh (replace your email inside it)\
Procfile (replace it your app name inside it)

2-Create A git repositry where you have saved your .py app and the above files (using git init)\ 
3-Open terminal, go to your repository and write the following commands:\
  heroku login\
  heroku create (to create the app)\
  git add .\
  git commit -m "some message"\
  git push heroku master
    
Copy the URL and paste it in your browser
  
