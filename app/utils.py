import uuid
def generate_image_url(name, extension):
    return f"/static/images/{uuid.uuid4()}_{name}.{extension}"
