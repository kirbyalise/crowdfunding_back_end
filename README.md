# Crowdfunding Back End
Kirby Thomson

## Planning:
### Concept/Name
CrumbFund

### Intended Audience/User Stories

Baker’s Story:
    As a passionate baker and product innovator, I want to raise funds to grow my business or develop new tools that can help other bakers. I’ll launch a project on BakeFund, offering exciting rewards like custom treats or early access to my innovations for backers who support my journey.

Backer’s Story:
    As a dedicated baking enthusiast, I want to support emerging bakers and creative innovators. By backing a project on BakeFund, I can enjoy delicious rewards like boxes of cookies or cupcakes, and even have the chance to try out new baking tools or ingredients before they hit the market.

### Front End Pages/Functionality
<!-- - {{ A page on the front end }}
    - {{ A list of dot-points showing functionality is available on this page }}
    - {{ etc }}
    - {{ etc }}
- {{ A second page available on the front end }}
    - {{ Another list of dot-points showing functionality }}
    - {{ etc }} -->


Home page:
  - Link to my user profile
  - List of projects to donate to 
  - Create account
  - Search projects 

Profile page:
  - List of all my pledges
  - My personal details- Name and email 
  - Delete account link  

Project page:
  - Name and project details with pictures/videos 
  - List of current pledges 
  - If I am the owner I can edit the project
  - If I am not the owner I can add a pledge  

### API Spec
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL              | HTTP Method | Purpose               | Request Body         | Success Response Code | Authentication/Authorisation |
| ---              | ----------- | -------               | ------------         | --------------------- | ---------------------------- |
| /users           | POST        | Create a user         | User object          | 201                   | N/A                          |
| /users           | GET         | Get all users         | User objects         | 302                   | Admin                        |
| /users           | PUT         | Edit user details     | Username and password| 200                   | Must be logged in            |
| /users/<pk>/     | GET         | Get specific user     | User object          | 302                   | Admin                        |
| /users/<pk>/     | DELETE      | Delete a user         | N/A                  | 204                   | Must be logged in            |
| /projects        | POST        | Post a project        | Project object       | 201                   | Must be logged in            |
| /projects        | GET         | Find all projects     | N/A                  | 302                   | Must be logged in            |
| /projects/<pk>/  | GET         | Find a project        | Project object       | 302                   | Must be logged in            |
| /projects/<pk>/  | PUT         | Edit a project        | Project object       | 200                   | User only                    |
| /projects/<pk>/  | DELETE      | Delete a project      | N/A                  | 204                   | Must be logged in            |
| /api-token-auth/ | POST        | Gets user token       | Username and password| 302                   | User only                    |
| /pledges         | POST        | Posts a pledge        | Pledge object        | 200                   | Must be logged in            |
| /pledges/<pk>/   | GET         | Find a pledge         | Pledge object        | 302                   | Must be logged in            |
| /pledges/        | GET         | Find all pledges      | Pledge object        | 302                   | Must be logged in            |
| /pledges         | PUT         | Edit a pledge         | Pledge object        | 200                   | Must be logged in            |
| /pledges/<pk>/   | DELETE      | Delete a pledge       | Pledge object        | 204                   | User only- Time period       |










### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )



<!-- Project Requirements
Your crowdfunding project must:

 Be separated into two distinct projects: an API built using the Django Rest Framework and a website built using React.
 Have a cool name, bonus points if it includes a pun and/or missing vowels. See https://namelix.com/ for inspiration. (Bonus Points are meaningless)
X Have a clear target audience.

 Have user accounts. A user should have at least the following attributes:
 Username
 Email address
 Password

 Ability to create a “project” to be crowdfunded which will include at least the following attributes:
 Title
 Owner (a user)
 Description
 Image
 Target amount to fundraise
 Whether it is currently open to accepting new supporters or not
 When the project was created

 Ability to “pledge” to a project. A pledge should include at least the following attributes:
 An amount
 The project the pledge is for
 The supporter/user (i.e. who created the pledge)
 Whether the pledge is anonymous or not
 A comment to go along with the pledge
 Implement suitable update/delete functionality, e.g. should a project owner be allowed to update a project description?
 Implement suitable permissions, e.g. who is allowed to delete a pledge?
 Return the relevant status codes for both successful and unsuccessful requests to the API.
 Handle failed requests gracefully (e.g. you should have a custom 404 page rather than the default error page).
 Use Token Authentication, including an endpoint to obtain a token along with the current user's details.
 Implement responsive design.

Additional Notes
No additional libraries or frameworks, other than what we use in class, are allowed unless approved by the Lead Mentor.

Note that while this is a crowdfunding website, actual money transactions are out of scope for this project.

Submission
To submit, fill out this Google form, including a link to your Github repo. Your lead mentor will respond with any feedback they can offer, and you can approach the mentoring team if you would like help to make improvements based on this feedback!

Please include the following in your readme doc:

 A link to the deployed project.
 A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
 A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
 A screenshot of Insomnia, demonstrating a token being returned.
 Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).
 Your refined API specification and Database Schema. -->