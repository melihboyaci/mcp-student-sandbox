import os

AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")

def connect():
    if AWS_SECRET_KEY:
        print("Connecting to AWS...")
    else:
        print("Error: AWS_SECRET_KEY environment variable not set")
