import pickle

person1 = {'Name': 'Rahul',
            'Age': 25}
person2 = {'Name': 'Raj',
            'Age': 23}

db = {}
db['person1'] = person1
db['person2'] = person2

pickle_object = pickle.dumps(db)

# load the object
loaded_pickle_object = pickle.loads(pickle_object)

print(type(pickle_object)) # <class 'bytes'>
print(loaded_pickle_object)