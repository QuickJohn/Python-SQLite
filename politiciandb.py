# John Quick
# Create politician db,
# Add & delete politicians from a SQLite database.
# Query & display db instances

import sqlite3
from politician import Politician

# --------------------------------- CREATE DB ---------------------------------- #
# Connection object representing the database
conn = sqlite3.connect('politician.db')

# Create db in memory to have new db evey time you run the program
conn = sqlite3.connect(':memory:')

# Create a cursor to allow for execution of sql commands
p = conn.cursor()

p.execute("""CREATE TABLE politicians (
   first text,
   last text,
   party text,
   years_in_office integer,
   crook int
   )""")

# ----------------------------------- PYTHON FUCNTIONS ------------------------------------ #
# Insert politician
def insert_pol(pol):
    with conn:
        p.execute("INSERT INTO politicians VALUES (:first, :last, :party, :years_in_office, :crook)", 
                {'first': pol.first,'last': pol.last,'party': pol.party, 'years_in_office': pol.years_in_office, 'crook': pol.crook})

# Search and return politician
def get_pols_by_name(lastname):
    p.execute("SELECT * FROM politicians WHERE last=:last", {'last':lastname})
    return p.fetchall()

# Update politician party
def update_party(pol, party):
    with conn:
        p.execute("""UPDATE politicians SET party = :party
        WHERE first = :first AND last = :last""",
        {'first':pol.first,'last': pol.last, 'party':party})

# Remove politician
def remove_pol(pol):
    with conn:
        p.execute("DELETE from politicians WHERE first =:first AND last = :last",
        {'first':pol.first,'last': pol.last})

# ------------------------------------ CREATE INSTANCES ------------------------------------- #
pol_1 = Politician('Harry', 'Balzak', 'Green', 6, 0)
pol_2 = Politician('Donald', 'Trump', 'Republican', 3, 1)
pol_3 = Politician('Bernie', 'Sanders', 'Independent', 40, 0)
pol_4 = Politician('Calvin', 'leCat', 'Feline', 1, 0)
pol_5 = Politician('John', 'Quick', 'Democrat', 2, 1)
pol_6 = Politician('Goober', 'Goombah', 'Snot', 10, 1)

# ------------------------------- INSERT INSTANCE INTO DB ----------------------------------- #
insert_pol(pol_1)
insert_pol(pol_2)
insert_pol(pol_3)
insert_pol(pol_4)
insert_pol(pol_5)
insert_pol(pol_6)
conn.commit()
# ----------------------------------- QUERY DB INSTANCES ------------------------------------ #
pols = get_pols_by_name("Quick")
print(pols)

pols = get_pols_by_name("leCat")
print(pols)

update_party(pol_5, "none")
remove_pol(pol_1)

pols = get_pols_by_name("Quick")
print(pols)


print(p.fetchall())

conn.close