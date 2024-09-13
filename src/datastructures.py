
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members =  [
            {
                "first_name": "Tommy",
                "id": 3443,
		        "age": 23,
		        "lucky_numbers": [34,65,23,4,6]
            },
        ]
    
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    
    def add_member(self, member):
        if 'id' not in member:  
            member['id'] = self._generate_id()
        member['last_name'] = self.last_name  
        print("este es el add member member:", member) 
        self._members.append(member)

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True  
        return False  

    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member
        return None
    
    def get_all_members(self):
        return self._members
