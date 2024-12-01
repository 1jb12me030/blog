# blog

git clone <repository_url>  
cd <repository_folder>  
python -m venv venv  
source venv/bin/activate      # Linux/Mac  
venv\Scripts\activate         # Windows  
pip install -r requirements.txt  
python manage.py migrate  
python manage.py runserver  


# apply token 

Authorization: Token <your_token>  

# Example of API requests

POST /api/posts/  
Content-Type: application/json  
Authorization: Token <your_token>  

{  
    "title": "My First Blog Post",  
    "content": "This is the content of my first blog post.",  
    "author": 1  
}  
# Response

{  
    "id": 1,  
    "title": "My First Blog Post",  
    "content": "This is the content of my first blog post.",  
    "author": 1,  
    "published_date": "2024-12-01T12:00:00Z"  
}  
# URLS 

http://127.0.0.1:8000/api/posts/
http://127.0.0.1:8000/api/posts/<int:pk>/
http://127.0.0.1:8000/api/posts/<int:post_id>/comments/


