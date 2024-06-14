from fastapi import FastAPI, Request, jsonify
from logging.config import fileConfig
from logging_config import LoggerSetup
from logs import log_info
import logging

logger_setup = LoggerSetup()

LOGGER = logging.getLogger(__name__)

app = FastAPI()

blog_posts = []

class BlogPost:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
    def __str__(self) -> str:
        return f'{self.id} - {self.title} - {self.content}'
    
    def toJson(self):
        return {'id': self.id, 'title': self.title, 'content': self.content}
    
@app.route('/blog', methods=['POST'])
def create_blog_post():
    try:
        data = Request.get_json()
        blog_posts.append(BlogPost(data['id'], data['title'], data['content']))
        LOGGER.info({"message": "Acessando a rota /blog", "method": "POST"})
        return jsonify({'status':'sucess'}), 201
    except KeyError:
        return jsonify({'error': 'Invalid request'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/blog', methods=['GET'])
async def get_blog_posts():
    LOGGER.info({"message": "Acessando a rota /blog", "method": "GET"})
    return jsonify({'posts': [blog.toJson() for blog in blog_posts]}), 200


@app.route('/blog/<int:id>', methods=['GET'])
async def get_blog_post(id):
    for post in blog_posts:
        if post.id == id:
            return jsonify({'post': post.__dict__}), 200
    LOGGER.info({"message": "Acessando a rota /blog/{int:id}", "method": "GET"})
    return jsonify({'error': 'Post not found'}), 404

@app.route('/blog/<int:id>', methods=['DELETE'])
async def delete_blog_post(id):
    for post in blog_posts:
        if post.id == id:
            blog_posts.remove(post)
            LOGGER.info({"message": "Acessando a rota /blog/{int:id}", "method": "DELETE", "id": id})
            return jsonify({'status':'sucess'}), 200
    return jsonify({'error': 'Post not found'}), 404

@app.route('/blog/<int:id>', methods=['PUT'])
async def update_blog_post(id):
    try:
        data = Request.get_json()
        for post in blog_posts:
            if post.id == id:
                post.title = data['title']
                post.content = data['content']
                LOGGER.info({"message": "Acessando a rota /blog/{int:id}", "method": "PUT", "id": id})
                return jsonify({'status':'sucess'}), 200
        return jsonify({'error': 'Post not found'}), 404
    except KeyError:
        return jsonify({'error': 'Invalid request'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)