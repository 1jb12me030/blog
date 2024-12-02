## blog

git clone <repository_url>  
cd <repository_folder>  
python -m venv venv  
source venv/bin/activate      # Linux/Mac  
venv\Scripts\activate         # Windows  
pip install -r requirements.txt  
python manage.py migrate  
python manage.py runserver  


## apply token 

Authorization: Token <your_token>  

## Example of API requests

# this is applicable for GET and Post.

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

# Request

GET /api/posts/  
Content-Type: application/json  
Authorization: Token <your_token>  

# Response

    {
        "id": 1,
        "title": "stall",
        "content": "qwe",
        "author": 1,
        "published_date": "2024-11-30T06:47:41.111474Z",
        "comments": [
        {
                "id": 1,
                "author": 1,
                "text": "qwertyu",
                "created_date": "2024-11-30T06:48:41.942158Z"
            }
        
]

# Request # it's applicable for GET,Update and Delete.

GET /api/posts/<int:pk>/  
Content-Type: application/json  
Authorization: Token <your_token>  

# Response

{
    "id": 2,
    "title": "qwe",
    "content": "qas",
    "author": 2,
    "published_date": "2024-11-30T06:48:23.608548Z",
    "comments": [
        {
            "id": 2,
            "author": 2,
            "text": "agsiskjskksckcsnih",
            "created_date": "2024-11-30T06:50:34.944717Z"
        }

       ] 

    }

# Request # it's applicable for GET and Post.

GET /api/posts/<int:pk>/comments/  
Content-Type: application/json  
Authorization: Token <your_token>  

# Response
    [
    {
        "id": 2,
        "author": 2,
        "text": "agsiskjskksckcsnih",
        "created_date": "2024-11-30T06:50:34.944717Z"
    }
]

# Request

Post /api/posts/<int:pk>/comments/  
Content-Type: application/json  
Authorization: Token <your_token>  

{
  "author" : 5,
  "text":"this is first text"
 }
 
# Response
{
    "id": 9,
    "author": 1,
    "text": "this is first text",
    "created_date": "2024-12-02T07:23:41.086515Z"
}
  
  

# URLS 

http://127.0.0.1:8000/api/posts/
http://127.0.0.1:8000/api/posts/<int:pk>/
http://127.0.0.1:8000/api/posts/<int:post_id>/comments/


