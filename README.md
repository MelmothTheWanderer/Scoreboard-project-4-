# Scoreboard

***(Project 4)***

Scoreboard is a simple web app for keeping track of scores. Whether it is a quick game of cards, and you need to keep a running total of the points , or you are keeping track of who can fit the most marshmallows in their mouth, scoreboard can help you out. 



Users scores can be updated , and are stored in a database, so they are always there when the user logs in. 



They can also edit existing scores , and of course , delete them. 

---

[Link to the live project](https://project-4-scoreboard-f07086ca3a52.herokuapp.com/)

## Responsiveness: 

---

![Large login page](/readme_images/lg-login.png)

*Login on a large screen*

![Large scoreboard page](/readme_images/lg-scoreboard.png)

*Scoreboard on a large screen*

---

![Medium login page](/readme_images/md-login.png)

*Login on a medium screen*

![Medium scoreboard page](/readme_images/md-scoreboard.png)

*Scoreboard on a medium screen* 

---

![Small login page](/readme_images/sm-login.png)

*Login on a small screen*

![Small scoreboard page](/readme_images/sm-scoreboard(1).png)

*Scoreboard on a small screen*

---

## User Stories

---

### Login

As a user I should be able to register , and log in and out of the website.

AC1- 'When the user first visits the site, they are presented with the option of logging in, OR signing up"

AC2 - " If the user tries to signup with a username that is already in use , then they should be prompted to try again "

---

### Personalised message

As a user, I should be greeted with a personalised message.

AC1 - " The message should be the first thing that the user sees and should be hard to miss. "

AC2 - "The message should display the users username"

AC3- "The user name should have the first name capitalised, even if that isn't how they signed up"

---

### Input scores

As a user , I should be able to input some scores onto the scoreboard.

AC1 - " The user should be able to input both a name and a score"

AC2 - " The form should not submit without both fields being filled"

AC3 - " The number field should not accept letters"

---

### View Scores on the scoreboard

As a user , I should be able to view all of the score on the scoreboard.

AC1 - " It should be obvious to the user which is the score and which is the name"

AC2- "The user should be able to view multiple scores together"

---

### Edit the score 

As a user, I should be able to edit my score if I choose to

AC1 - "There should be an easy to recognise 'edit' button"

AC2 - " The button should direct the user to another page with a form where they can edit the entry"

AC3 - " The form should update the existing entry , and not create any new entries"

---

### Delete a score

As a user I should be able to delete a score.

AC1 - " Should be obvious which button is the delete button "
AC2 - " Should be coloured red for clarity"

---

### Scores are unique to the user

As a user I should only be able to see the scores that I have created as a logged in user , and nobody else . 

AC1 - " If I can only see , edit , create and delete the scores that I, the user have created, then that would this criteria would be met"

---

### View and delete users and scores.

As an admin , I should be able to create , edit , update , and delete registered users and score.

AC1 - " As an admin I should be able to log in and perform crud operations"

---


## Model Schema

---

![Model schema diagram](/readme_images/schema.jpg)

*Model schema diagram

I'm not ashamed to say that I kept my model simple. There is only one relationship , and that is the one between the out-of-the-box Django user model, and the custom model that I have decided to call the 'score' model.


The relationship is a 'one to many' relationship. The foreign key in the score model is the 'user' key, and the reason that it is used, is to keep track of which user owns which score. Without it , every user would be able to see every other users score , and things would quickly get out of hand. 

## Testing 

---

There were quite a few bugs when I was making the app , and some of them took me a while to fix. 



One of the worst bugs was one in which, when the user clicked on the 'edit' button, would create a new record instead of altering the current one. 



I had to refactor the code several times, and there was a lot of trial an error. 



At first I changed from a generic list view to a function based view, because I knew that this might give me more control over what was happening within the view.



After that, there was a lot of trouble, but eventually I found a solution by adding the private key (the id) of the data row to the button html tag, and then rendering a html form using the value (pk) that was stored in the button to populate the form with the correct instance to be edited.



I was very relieved when it worked!

---

## Deployment

Here are the steps required to deploy, but if you prefer the quick version , here is a [template](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf) from the Code Institute.

Now for the steps : 

### How to clone the repository: 

- Visit the repo [here](https://github.com/MelmothTheWanderer/Scoreboard-project-4-)

- On the top right of the screen, you should see a 'code' button, click 'HTTPS' and copy the link. 

- On your IDE , navigate to the directory that you would like to clone the project to. 

- In your terminal , type 'git clone' and paste the url that you copied. 

- If you want to go ahead and install all of the necessary packages, that can be done easily with the 'pip3 install -r requirements.txt' command. 

---

### How to deploy to Heroku

Here are the steps to deply to the Heroku hosting service: 

- Create an account on the [Heroku](https://www.heroku.com) website, or sign in if you already have one. 

- On the dashboard , you should see a "create new app" button. Click on it. 

- Enter name for your app. It needs to be unique, you might have to try a couple of times. 

- You might need to select a region. Just select whichever suits best. 

- Go to the settings tab of your app. Click on the button that says 'reveal config vars'

- Add a variable in all caps named 'DISABLE_COLLECTSTATIC' and set its value to ' 1 '. 

- Add another variable in all caps called 'SECRET_KEY' and assign it a value, anything you like, the more complicated the better though, I think. 

- If you go into your Django project now for a moment, the settings.py file ought to have the following variables set to : 

    - DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}

    - SECRET_KEY = os.environ.get('SECRET_KEY')

    - DEBUG = False

- In your IDE, take to the terminal window and initialise the data model in the postgres database with the following command 'python3 manage.py migrate' 

- After doing this follow up by keeping your requirements up to date with this command : 
    - 'pip3 freeze --local > requirements.txt' 

-Commit and push changes to your Github repo

-Make sure you add the values mentioned earlier , SECRET_KEY and DATABASE_URL to to your env.py file. 











