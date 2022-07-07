<h1 align="center">Venture-Press---Full-Stack-Frameworks-With-Django-Milestone-Project (Milestone Project #4)</h1>
<h1 align="center">Olly Lomax</h1>
<h2 align="center"><img src="media/readme/readmeheader.png"></h2>

![Responsive Visuals]()

# Venture Press Website

I built this website using my knowledge of HTML5, CSS3, JavaScript, jQuery, Bootstrap, Python, PostgresSQL and Django which I have learned from Code Institute during my Diploma in Full Stack Software Development. Venture Press is an imaginary brand that I have created to showcase my knowledge and skills in the aforementioned languages and frameworks with the intention of completing my Full Stack Frameworks with Django Milestone Project.

The website’s purpose is to deliver an E-Commerce platform for a domestic printing company, offering a wide range of print services which are all purchasable through a cart and checkout flow.

View the live project [here](https://venture-press.herokuapp.com/)

## UX STRATEGY

### Goals
- To expand upon my knowledge of HTML5, CSS3, JavaScript, jQuery and Python.
- To showcase my new knowledge of Django and PostgresSQL.
- To provide a responsive website fulfilling the UX Design philosophy.
- To provide a website showcasing customisable print services for sale.
- To provide a website with means to contact the company with queries and/or custom quotations.
- To provide a website with full cart and checkout functionality for purchasing print services.
- To provide a website with user registration, profile page and order history.
- To provide a website with notification feedback through email for registration, purchases and contact form.
- To provide a website with admin functionality for adding new print services.
- To provide a website with superuser functionality for managing backend operations.

### User Stories

- As a user, I want to easily understand the purpose of the site.

- As a user, I want to clearly view the website and content on any device.

- As a user, I want to easily navigate the website so that I can find content quickly.

- As a user, I want to be able to see what print services are available and how much they are.

- As a user, I want to be able to search the website for services I may be interested in.

- As a user, I want to be able to filter the print services by category.

- As a user, I want to be able to customise my chosen service and then add it to my cart.

- As a user, I want to be able to view all services I have added to my cart before deciding whether to proceed to payment.

- As a user, I want to be able to proceed to purchasing the contents of my cart, input my card details and make the purchase.

- As a user, I want to be able to contact the company about any queries or custom quotations I might need.

- As a user, I want to be able to easily return to the website if I encounter a page error.

- As a user, I want to be able to register on the website.

- As a registered user, I want to be able to log in to my account on the website.

- As a registered user, I want to be able to log out of my account on the website.

- As a registered user, I want to be able to view my profile, edit my details and change my password.

- As a registered user, I want to be able to see a list of my order history.

- As an admin user, I want to be able to create, edit and delete print services. 

- As the superuser, I want to be able to create, edit and delete categories and services.

- As the superuser, I want to be able to create, edit and delete user details and emails.

- As the superuser, I want to be able to create, edit and delete orders.

## UX SCOPE

- ### Planned Features

    -   Creating and storing User, Category, Service, Cart and Order information inside a PostgresSQL database.
    -   Adopting UX Design Philosophy.
    -   Navigation links on all pages.
    -   Cart info on all pages.								
    -   Website title and description clearly stating intended purpose.			
    -   CRUD Functionality.							
    -   Login/Logout Functionality.	
    -   Home page with introduction, hero image and a set of example services on offer.
    -   Profile page viewable and editable by registered users.
    -   Order history page viewable by registered users.
    -   Change password page, separate from edit profile page, for users to securely change their password with validation.
    -   Print services page viewable, searchable and filterable by all users.
    -   Add/Edit Service pages for registered users to add or edit print services.
    -   Service detail pages with images, descriptions and prices viewable and purchasable by all users.
    -   Cart page with total amount of order and a list of services and their respective images, quantities and details that a user has added.
    -   Mini cart pop-up when users scroll over their cart at top right of nav menu displaying a reduced version of the same page above.
    -   Checkout page with delivery information form and stripe card input for users to process their orders.
    -   Order confirmation page showing full details of the processed order and all line items.
    -   Toast notifications for many site actions including adding items to cart, processing orders and submitting contact form.
    -   Email notifications when registering, confirming email, submitting contact form requests and processing orders.
    -   Map access to full backend functionality packaged with Django.
    -   404 and 500 error pages caught Django error handling to direct user back to website.