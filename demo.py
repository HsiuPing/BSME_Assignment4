# project: BMSE Assignment 4
# filename: demo.py
# time: 201712
# editor: HsiuPing Lin

from person import Person
from load import Loading

def print_people(people):
    for p in people:
        print('\t', p)

# create a Person Joe, and store it in the variable 'joe'
joe = Person('Joe', 'male')
# check joe's name
assert joe.name == 'Joe'

print('Joe self'); print_people(joe.ancestors(0))
print('Joe parents None'); print_people(joe.ancestors(1))
# create a Person Mary, and make her Joe's mother
joe.mother = Person('Mary', 'F')
print('Joe parents mother'); print_people(joe.ancestors(1))

maternal_gm = joe.mother.mother = Person('Agnes', 'female')
# create a Person Joe Sr., and make him Joe's father
joe.father = Person('Joe Sr.', 'male')
print('joe parents(): Mary, Joe Sr.'); print_people(joe.parents())

# create joe's paternal grandfather
joe.father.father = Person('Old Joe', 'male')
# create joe's maternal grandmother
maternal_gm.mother = Person('Maternal ggm', 'female')
print('joe.grandparents_structured(), Agnes, Old Joe'); print_people(joe.grandparents_structured())
print('joe.grandparents(), Agnes, Old Joe'); print_people(joe.grandparents())
print('joe great-grandparents: Maternal ggm'); print_people(joe.great_grandparents())

# play with an infinite ancestry depth limit
inf = float('inf')
print('joes ancestors: Mary, Joe Sr., Agnes, Old Joe, Maternal ggm'); print_people(joe.all_ancestors())
print('joe and his ancestors'); print_people(joe.ancestors(0, inf))

# make Joe his mother's son
joe.set_mother(joe.mother)
print('joe.mother.sons():'); print_people(joe.mother.sons())

# create joe's kids
kid1 = Person('kid1', 'male', father=joe)
kid2 = Person('kid2', 'female', father=joe)
kid3 = Person('kid3', 'male', father=joe)

kid1.set_father(joe)
kid2.set_father(joe)
kid3.set_father(joe)
print('joe.children:'); print_people(joe.children)
print('joe.sons():'); print_people(joe.sons())

# create kid's and kid2's mother Penny
penny = Person('Penny', 'female')
kid1.set_mother(penny)
kid2.set_mother(penny)

# play with kid2's siblings and half-siblings
print('kid2.siblings():'); print_people(kid2.siblings())
print('kid2.half_siblings():'); print_people(kid2.half_siblings())

# create kid's kid
kid1kid = Person('kidkid', 'male', father=kid1)
kid1kid.set_father(kid1)

# play with Penny's descendants
print('Penny and her descendants'); print_people(penny.descendants(0, 1))

# play with an infinite descendant depth limit
inf = float('inf')
print('joe and his descendants'); print_people(joe.descendants(0, inf))

# demo by input name list and variants
people = Loading.load_people('name_input.txt')
for v in people.values():
    Person.get_variants(v)
    print(v)
    Person.print_variants(v)

# check Bob's variants
Person.print_variants(people["Bob"])