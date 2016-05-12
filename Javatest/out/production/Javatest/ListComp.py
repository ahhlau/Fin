pokedex = []
f = open('pokemon.txt', 'r')
#load pokedex
for line in f:
    substring = line[1:-2]
    temp = substring.split(", ")
    pokedex.append(temp)
#change appropriate string to int
for item in pokedex:
    item[0] = int(item[0])
print pokedex

f.close()
f = open('strength.txt', 'r')
strengths = []
for line in f:
    substring = line[1:-2]
    temp = substring.split(", ")
    strengths.append(temp)
print strengths
print
print
#print pokemon number 1-10
print "SELECT id, name FROM pokedex WHERE id <= 10"
print [[i[0], i[1]] for i in pokedex if i[0]<=10]
print
#print all grass type pokemon
print "SELECT id, name FROM pokedex WHERE type1 or type2 == 'Grass'"
print [[i[0], i[1]] for i in pokedex if i[2]=="Grass" or i[3] == "Grass"]
print
#group by type 1 and sort the pokemon by name
#group by type and sort the pokemon by name
print "SELECT name from pokedex GROUP BY type1 ORDER BY name"
for type1 in sorted({p[2] for p in pokedex}): print (type1, sorted([p[1] for p in pokedex if p[2]==type1]))
print
#dept id = 9
#print "\nselect dept_id, avg(salary) from s_emp group by dept_id order by dept_id: "
#for department in sorted({ d[9] for d in s_emp[1::] }): print (department, (lambda l: round(sum(l) / len(l), 2))(map(float,[ e[7] for e in s_emp[1::] if e[9] == department ])))
#iterate through that list to gather pokemon names (type = type1)
#make a list of types


# for names in sorted([i[1]for i in pokedex]): print [names]
#print all pokemon who are strong against grass type pokemon, grouped by type
print "print all pokemon who are strong against grass type pokemon, grouped by type, sorted by name within the group"
print
#lambda function to go through strength and select types that are strong against grass
#lambda function to go through the types set and group together the pokemon by type
