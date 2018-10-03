from myapp import app
from models import Member

@app.route('/')
def index():
    firstMember = Member.query.first()
    return '<h1>You are on the index!' + firstMember.name + '</h1>'