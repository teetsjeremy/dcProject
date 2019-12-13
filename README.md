E9Xissues -- data centric project

This project was created to fulfill the data centric portion of my full stack web development program.

I came up with the idea of a forum type site that allows members to search, add and edit a database that has been publicly created. The database stores information regarding various common issues that people come across involving thier 2006 to 2012 BMW 3 series models.

UX

Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:

As a user type, I want to perform an action, so that I can achieve a goal.
This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

Features

Existing Features

View a database  - allows users to view, edit and add topics, by having them fill out a topic form.
...
For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

Features Left to Implement

I would like to implement a search engine to sort and find issues

Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

JQuery
The project uses JQuery to simplify DOM manipulation.
Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

Edit issue form:
verify all edit, delete, and done buttons work

Add issue form:
From main page
Try to submit the empty form and verify that an empty issue is added to database list.


Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
The site transitions from browser screen size and device screen size as desired. It holds its appearance and structure well.

I ran into several interesting bugs during development. The main issue that I addressed was actually occuring during attempted early deployment. When attempting to push to heroku, my build kept crashing due to unknown requirements being in my requirements.txt file. After much research and asking for help, I was able to determine that AWS Cloud9 environment was creating its own requirements to run the app internally and adding those requirements.



Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.

Credits

Content

The text for section Y was copied from the Wikipedia article Z
Media

The photos used in this site were obtained from ...
Acknowledgements

I received inspiration for this project from X


email form from: http://reusableforms.com/d/a/contact-form-bootstrap

