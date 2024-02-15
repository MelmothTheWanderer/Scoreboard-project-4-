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








