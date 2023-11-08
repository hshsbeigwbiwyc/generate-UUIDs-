import uuid

def generate_uuid():
    return str(uuid.uuid4())

# Generate a UUID in the format you specified
formatted_uuid = '-'.join(generate_uuid().split('-'))
print(formatted_uuid)
