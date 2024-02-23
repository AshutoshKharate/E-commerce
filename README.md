This is a simple eCommerce application built with Django Rest Frammework,Python,JWT Authentication to authentiate user,permissions, pagination etc.

step to Run application.
   1. git clone https://github.com/AshutoshKharate/E-commerce.git
   2. cd E-commerce
   3. cd ecommerce_project
   4. pip install -r requirements.txt
   5. python manage.py migrate
   6. python manage.py runserver

Api Endpoints:-
     "http://127.0.0.1:8000/api/createuser/"           # To create new user.
     "http://127.0.0.1:8000/api/category/"             # To create,retrive,update,delete category.
     "http://127.0.0.1:8000/api/product/"              # To create,retrive,update,delete product.           
     "http://127.0.0.1:8000/api/orderitem/"            #  To create,retrive,update,delete orderitem.

Features
       1. Product Management: Add,retrive,update and delete products.
              Sorting - sort product as per name, price.
              Filtering - Filter product by name, category and price.
              Searching - Search product by price.

        2. OrderItem Management: Add,retrive,update and delete orderitem.
              Sorting - sort ordeitem as per price.
              Filtering - Filter orderitem by name and price.
              Searching - Search orderitem by price.

        3. Category Management: Add,retrive,update and delete category.
              Sorting - sort Category as per name .
              Searching - Search Category by name .
              
        4. User Authentication: Secure user registration and login using JWT Authenticarion.

        5. view restricted with permission.

        6. Apply Page Number Pagination to split result set.

        7. Reffer requirement.txt

Usage
       Navigate to http://localhost:8000 in your web browser.
       Register a new account or log in with existing credentials.
       Create and Explore the product , category and orderitem doing operations to create, retrive, update,delete, sorting, filter and ordering.

Used tools:- 

       Language - Python
       Fremework - Django Rest Framework
       Authentication - JWT Authenticatio
       

Contact
      For questions or inquiries, please contact ashutoshkharate11@gmail.com/8668646229







        

        
        
        
