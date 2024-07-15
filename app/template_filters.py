from app import app
from app.models import Like


@app.template_filter("is_like")
def post_like(post_id, user_id):
    like = Like.query.filter_by(user_id=user_id, post_id=post_id).first()
    if like:
        return True
    else:
        return False
