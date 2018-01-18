# python course 2017 final exam


## Subject

Our client is "You are not a human without IPhone" LTD.
We are asked to build an API for cell-phone ecommers website.

They can't decide about design of their pages, so we are only focusing on API right now. Later some other team will implement the frontend part.

We had a lot of discussions with their managers and product owners, they definitely know what they want.
After the requirements were clear for us, our architect [`@sobolevn`](https://github.com/sobolevn) made some tests headers in TDD style illustrating these requirements for other members of the engineering team.
These tests will guide you through the client's requirements.
There tests also recommends you a good testing strategy.

Our client happens to already have a good `django` team.
So, our project must use `python3.6` and `django=<1.12`.

But, our client is concerned about using the existing open-source ecommers technologies.
Because the client believes that they are not secure enough.

That's a very promising client, so, please, make sure your code meets the highest expectations!


## Requirements

Our application has four main endpoints, here's a detailed information about each of them.

`*` means that this action is only allowed for the authenticated user.

### Shop

`Shop` endpoint must do several things:

- Show all categories (currently there are only three categories: `Phones`, `Chargers`, `Cases`. But client said that there would be many categories in the nearest future)
- Show all products by category
- Search all products and show the result (search criteria: product's name, category and price. When multiple filters are applied, use logical `AND` operation)

### Cart

Cart is a collection of products.
Each customer creates a cart (with at least one product inside) before the actual checkout process starts.
`Cart` endpoint must do several things:

- Show current cart contents
- Add a product to the cart

### Profile

Each user has a profile.
It is impossible to checkout your order without a profile.
Login into the account should not clear the `Cart`.
This is also true for the logout process.
`Profile` endpoint must do several things:

- Create new profile
- Login into the existing profile (login must be performed with `email` and `password`, successful login must return a `jwt` token)
- `*` Show current profile (information about current user)
- `*` Show orders history for the current user

### Order

When the order is created then products from `Cart` are considered bought.
After that our client will send a courier to the customer to deliver the products and receive money from the customer.
`Order` endpoint must do several things:

- `*` Create new order


## Data model

Our application is focused on two models: `Product` and `Order`.

Our products have the following logic:

- There can be different versions of the same product, each version can possibly cost different amount of money. Example: `IPhone 8 32GB` costs less than `IPhone 8 64GB`, but `IPhone 8 32GB Black` and `IPhone 8 32GB White` cost the same
- Products can not run out of stock, our client has big supplies

### Model fields

Each user should have:

- email
- password (we only store hash!)
- full name

Each product should have:

- name
- category

Each product version should have:

- link to the base product (example: `IPhone 8 32GB` and `IPhone 8 64GB` have the same base product: `IPhone 8`)
- name
- description
- price

Each order should have:

- link to the customer
- delivery address
- delivery date and time
- what to deliver


## Administration

Our client will use built-in admin panel to create products, product versions.
This panel will also be used to receive information about new orders.

No specific logic, just some basics:

- Each model should be presented in the `django`'s admin panel
- Each model should have `list_fields` defined
- Each model should have `search_fields` defined


## Authentication

Our API is stateless.
Our application should use `jwt`.

This `jwt` token could be obtained in the `Profile` endpoint.
It should be passed as `Authorization` header.


## Criteria

See https://github.com/mos-polytech/2017#final-exam for full list of criteria.

Additional requirements:

- `python3.6` only
- `django=<1.12` only
- `djangorestframework`


## How to submit your work

`@sobolevn` will give you a flash drive to upload your project folder onto it.

If you are going for extra points (`heroku`, `travis`), make sure that you have also speicified all the required link in the `README.md`.

You can also upload your work to Github. 
It won't affect the result. 


## Blacklisted packages

You are not allowed to use any of these packages in your application:

- django-oscar
- django-shop
- django-cms
- django-cart
- Cartridge
- Lighting Fas Shop
- Saleor
- Satchless
- Satchmo
