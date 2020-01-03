E9Xissues -- data centric project

This project was created to fulfill the data centric portion of my full stack web development program.

I came up with the idea of a forum type site that allows members to search, add and edit a database that has been publicly created. The database stores information regarding various common issues that people come across involving thier 2006 to 2012 BMW 3 series models.

UX

This website was created with the idea of allowing BMW owners to talk about and share questions they may be having regarding issues with thier car. By using the site, they can simply post a question/comment/issue and have people from accross different communities help them. I also made sure to use solid responsive design as use from a mobile device seems very helpful.

The app config was set using the port of 5000 as shown in the mini-project set up as well as the ip address set-up.
The db_uri setting was the most challenging for me to figure out. In the end, I was able to establish a way of hiding said username and password.


Features

Existing Features

View a database  - allows users to view, edit, add, and delete topics, by having them fill out a topic form.
Contact us  - allows users to fill out a contact form and send an email to site mediators.
Shop page  - provides links to various outside pages that provide auto parts as well as immediate dropdown options from the header.

...

Features Left to Implement

I would like to implement a search engine to sort and find issues. I would also like to possible create a notification system to alert users when someone has updated thier post.

I wouls also like to implement a way of having all additions pass through a check system of sorts. Maybe have an administrator review all post/edit requests.

Technologies Used

Framework
Bootstrap is the framework that I ended up using. I originally used materialize, however I couldn't get elements to render the way I wanted. So I simply switched to a framework that I am more familiar with.

JQuery
The project uses JQuery to simplify DOM manipulation.

Email
The contact form was put in place but not actually initialized as I felt it was unneccesary to have any actual emails be sent for the project


Testing

Edit issue form:
verify all edit, delete, and done buttons work

Add issue form:
From main page
Try to submit the empty form and verify that an empty issue is added to database list.

Edit issue form:
Ensure that all correct data is transferred to the form when clicking the task.
Edit all possible fields as well as not editing any to verifyform updates correctly on the main page.

Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
The site transitions from browser screen size and device screen size as desired. It holds its appearance and structure well.

I ran into several interesting bugs during development. The main issue that I addressed was actually occuring during attempted early deployment. When attempting to push to heroku, my build kept crashing due to unknown requirements being in my requirements.txt file. After much research and asking for help, I was able to determine that AWS Cloud9 environment was creating its own requirements to run the app internally and adding those requirements.

I struggled with getting the edit task function to work properly. I was unable to get the data from the database to actually bind to the form. Once I found out that my errors were in my python app routes and database structure, all functions worked correctly. 

Deployment
I used heroko to deploy my site. All parameters used were taken directly from the mini project instructions earlier in the unit.

The only major differences between production and final implementation was just basic CSS stylings that I thought just didn't look quite right, as well as changing the framework from materialize to bootstrap.

Credits
I recieved tutoring support from contacts I have in the tech field as well as help from the CodeInstitute tutor page.

Media
Background image borrowed from: https://i.pinimg.com/originals/59/40/a2/5940a279a83c46edf95e5ceb729eb855.jpg
Card images in shop.html are borrowed from: (Factory: https://i.pinimg.com/originals/30/7a/b3/307ab308010b03eb53696a168a0afc5a.jpg)
(Third Party: https://i.pinimg.com/originals/30/7a/b3/307ab308010b03eb53696a168a0afc5a.jpg) 
(Aftermarket: https://bimmertips.com/wp-content/uploads/2018/05/BMW_Style_219_M_E92_M3_Wheels.jpg)

Acknowledgements

email form from: http://reusableforms.com/d/a/contact-form-bootstrap

