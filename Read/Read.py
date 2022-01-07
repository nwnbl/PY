pi_string=''

with open('Pi.txt') as file:
    for line in file:
        pi_string+=line.strip()

if '926' in pi_string:
    print('found')
else:
    print("not found")