# Shopping cart
Basic restful json api to list the products A,B,C,D
● Api to add items to the basket/cart.
● Api which returns list items from the basket/cart(with individual price and
discount data),the total price and total discounts applied.
● Api to return the checked out items after applying discount
## Server
Python Flask and flask_restful is used on the server side for providing the API support.
This application uses MySQL server for the database
## Quick Start

### Basics

1. Activate a virtualenv(virtualenv -v env in ubuntu , venv env in windows)
1. Install the requirements (pip install -r requirements.txt)

### Set Environment Variables

Update *project/server/config.py*, and then run:

```sh
$ export APP_SETTINGS="project.server.config.DevelopmentConfig"
```

or

```sh
$ export APP_SETTINGS="project.server.config.ProductionConfig"
```

### Run the Application
Assuming Mysql is installed and available in the localhost
create the db for the first run
```sh
$ python manage.py create_db
```
## Run the script which contains some data to be present in the product and discount tables
mysql --login-path=local  < project/dbscripts/create.sql

```sh
$ python manage.py runserver
```
### Access the REST end points
## List the products
curl -i -H "Content-Type: application/json"  http://localhost:5000/products

## Add items to cart
curl -i -H "Content-Type: application/json" -X POST http://localhost:5000/cart -d "{\"items\":[{\"p_id\":1,\"quantity\":2}]                    }"

## View items in cart
curl -i -H "Content-Type: application/json"  http://localhost:5000/cart/1
##Checkout the cart- apply discount
curl -i -H "Content-Type: application/json"  http://localhost:5000/cart/checkout/1

Open [http://localhost:5000](http://localhost:5000) to view it in the browser.

### Testing

Without coverage:

```sh
$ python manage.py test
```

With coverage:

```sh
$ python manage.py cov
```
