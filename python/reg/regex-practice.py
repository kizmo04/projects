import re

story = '''Born to the prestigious Crownguards, the paragon family of Demacian service, Luxanna was destined for greatness. She grew up as the family's only daughter, and she immediately took to the advanced education and lavish parties required of families as high profile as the Crownguards. As Lux matured, it became clear that she was extraordinarily gifted. She could play tricks that made people believe they had seen things that did not actually exist. She could also hide in plain sight. Somehow, she was able to reverse engineer arcane magical spells after seeing them cast only once. She was hailed as a prodigy, drawing the affections of the Demacian government, military, and citizens alike.

As one of the youngest women to be tested by the College of Magic, she was discovered to possess a unique command over the powers of light. The young Lux viewed this as a great gift, something for her to embrace and use in the name of good. Realizing her unique skills, the Demacian military recruited and trained her in covert operations. She quickly became renowned for her daring achievements; the most dangerous of which found her deep in the chambers of the Noxian High Command. She extracted valuable inside information about the Noxus-Ionian conflict, earning her great favor with Demacians and Ionians alike. However, reconnaissance and surveillance was not for her. A light of her people, Lux's true calling was the League of Legends, where she could follow in her brother's footsteps and unleash her gifts as an inspiration for all of Demacia.'''


# 정규표현식 실습문제 1~4

r = re.findall(r'\ba\w{3}\b',story)

p1 = re.compile(r'\ba\w{3}\b')
print(re.findall(p1,story))

print(r)

r2 = re.findall(r'\w+r\b', story)
print(r2)

# '\b\w*r\b'



r3 = re.findall(r'\b\w*[abcde]{3}\w*\b',story)
print(r3)

#r4 = re.findall(r'\b\w+,\s*\w+',story)

#for m in r4:
#    r5 = re.sub(m, m.upper(), r4)
#    print(r5)

#p4 = re.compile(r'\b(?P<before>\w+),\s*(?P<after>\w+)')
#result = re.sub(p4, r'(?P=before)',story)
#print(result)

def replace_func(m):
    return '{}{}[{}]'.format(m.group('before').upper(),m.group('between'), m.group('after'))


p4 = re.compile(r'(?P<before>\w+)(?P<between>,\s*)(?P<after>\w+)')

#result = re.sub(p4, replace_func, story)

result = re.sub(p4, lambda m : '{}{}[{}]'.format(m.group('before').upper(), m.group('between'), m.group('after'), story))

print(result)

