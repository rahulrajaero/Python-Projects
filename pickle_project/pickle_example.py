# pickle is a module in python which is used for serialization and de-serialization
# in python i.e. converts the python objects (list, tuple, dictionary, model, etc) into a
# character stream. 
# It has two main method - dump and load
# Let's see how it works.

import pickle

person1 = {'Name': 'Rahul',
            'Age': 25}
person2 = {'Name': 'Raj',
            'Age': 23}

db = {}
db['person1'] = person1
db['person2'] = person2

# save to dbfile 
dbfile = open('pickleobject', 'ab') # open in binary mode

# dump the db python object to dbfile
pickle.dump(db, dbfile)

# close the file
dbfile.close()

# Now load the dbfile 

loaded_dbfile = open('pickleobject', 'rb') 
loaded_db = pickle.load(loaded_dbfile)

# print both db and loaded_db to see wether they are same or not
if db == loaded_db:
    print("True")
print(db)
print(loaded_db)

# We can achieve the same without opening a file

# REf - GeeksForGeeks