import uuid
def generate_image_url(name, extension):
    return f"/static/images/{uuid.uuid4()}_{name}.{extension}"
def save_image(image_data):
    name: str = image_data.filename
    name, ext = name.rsplit(".", maxsplit=1)
    image_path = generate_image_url(name, ext)
    image_url = f'app/{image_path}'
    image_data.save(image_url)
    return image_path