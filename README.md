# Crowdfunding Back End
Kirby Thomson

## Planning:
### Concept/Name
CrumbFund

### Intended Audience/User Stories

Baker’s Story:
    As a passionate baker and product innovator, I want to raise funds to grow my business or develop new tools that can help other bakers. I’ll launch a project on BakeFund, offering exciting rewards like custom treats or early access to my innovations for backers who support my journey.

Backer’s Story:
    As a dedicated baking enthusiast, I want to support emerging bakers and creative innovators. By backing a project on BakeFund, I    can enjoy delicious rewards like boxes of cookies or cupcakes, and even have the chance to try out new baking tools or ingredients before they hit the market.

### Front End Pages/Functionality
- {{ A page on the front end }}
    - {{ A list of dot-points showing functionality is available on this page }}
    - {{ etc }}
    - {{ etc }}
- {{ A second page available on the front end }}
    - {{ Another list of dot-points showing functionality }}
    - {{ etc }}


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
| /users           | GET         | Get all users         | User objects         | 200                   | Admin                        |
| /users/<pk>/     | GET         | Get specific user     | User object          | 200                   | Admin                        |
| /users/<pk>/     | DELETE      | Delete a user         | ???                  | 200                   |                              |
| /projects        | POST        | Post a project        | Project object       | 201                   | Must be logged in            |
| /projects/<pk>/  | GET         | Find a project        | Project object       | 200                   | Must be logged in            |
| /projects/<pk>/  | DELETE      | Delete a project      | ???                  | ???                   | ---------------------------- |
| /api-token-auth/ | POST        | Gets user token       | Username and password| 200                   | User only                    |



### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )