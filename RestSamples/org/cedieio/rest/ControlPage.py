from flask import Flask
import uuid
from sys import path
from flask import request
path.append('.')
print(path)
from org.cedieio.model.Person import Person as Person

app = Flask(__name__)

stack = []
@app.route('/', methods=['GET'])
def index():
    return print_person_to_readable(stack)

@app.route('/persons', methods=['GET'])
def get_persons():
    return print_person_to_readable(stack)

@app.route('/persons', methods=['POST'])
def insert_persons():
    person = Person()
    json_post = request.get_json()
    person.set_first_name(json_post['first_name'])
    person.set_last_name(json_post['last_name'])
    stack.append(person)   
    return print_person_to_readable(stack)



@app.route('/persons', methods=['DELETE'])
def delete_person():
    json_post = request.get_json()
    for i in range(len(stack)):
        if str(stack[i].get_person_id()) == str(json_post['person_id']):
            print('Deleteing object')
            del stack[i]
    return print_person_to_readable(stack)
    
@app.route('/persons', methods=['PUT'])
def update_person():
    json_post = request.get_json()
    for i in range(len(stack)):
        if str(stack[i].get_person_id()) == str(json_post['person_id']):
            person = stack[i]
            person.set_first_name(json_post['first_name'])
            person.set_last_name(json_post['last_name'])
            stack[i] = person
    return print_person_to_readable(stack)
    


def print_person_to_readable(persons):
    val = ""
    for person in persons:
        val = val  + 'Firstname: {} Lastname: {} Person Id: {}\n'.format(person.get_first_name(), person.get_last_name(), person.get_person_id())
    return val
    
if __name__ == '__main__':
    app.run()