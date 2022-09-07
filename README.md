# usersCR

<p>This is a practice assignment for Coding Dojo<p>
<p>✔️= task completed</p>
<p>❌ = task not complete</p>
<h2>Goals for this assignment:</h2>
<ul>
  <li>✔️Use the users_schema created in the MySQL course</li>
  <li>✔️Create a new Flask project</li>
  <li>✔️Create 2 html pages, Read(All) and Create</li>
  <li>✔️Display all users from the database on the Read(All) page</li>
  <li>✔️Display form to create new users on the Create page</li>
  <li>✔️When the form is submited, a new user should be inserted into the database</li>
  <li>✔️Redirect to Read(All) page after creating a new users, and the user just created should appear in the table</li>
  <li>✔️Use the same flask project from the usersCR project</li>
  <li>✔️On the Read(All) page create an actions column</li>
  <li>✔️Show link will render the Users Read (One) page</li>
  <li>✔️Delete link will delete the User from the database, and redirect to the Read(all) page</li>
  <li>✔️After successful creation of a new User, redirect to Read(One)page</li>
  <li>✔️Read(One) page will display the user information</li>
  <li>✔️Edit page will have a form with pre-populated with the users information</li>
  <li>✔️Update the updated_at field when editing the users information</li>
  <li>❌After successful update of the user, reidrect to the Read(One) page and display the updated information</li>
  <li>✔️All home links should redirect to the Read(All) page</li>
</ul>

***

## Email Validation with DB

- [x] 1 Add the following to your users assignment:
  - A validator method to your user class that
    - accepts input data as a dictionary
    - adds flash messages and returns true or false
- [x] 2 Validate that there are no fields left blank
- [ ] 3 Validate that the email is in the correct format
- [ ] 4 Be sure to add messages to flash if there are any errors
  - be sure to utilize flash message categories for clarity
- [ ] 5 Handle the following logic in your controller:
  - if invalid, send the user back to the create page
    - show the error messages in the page
  - if valid, carry on creating the new user and redirect to the dashboard
- [ ] NINJA Bonus: Also validate that the email being added is unique
- [ ] NINJA Bonus: Make it so the data the user input isn't lost when they have an error so they don't have to re-input form data each time they make a mistake
  - HINT: *How do you persist data temporarily from route to route? (probably session[])*