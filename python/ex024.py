'''
c = str(input('Em que cidade você nasceu? '))
c.strip()
c.upper()
print(c.count('SANTO'))
'''

c = str(input('Em que cidade você nasceu? ')).strip()

print(c[:5].upper() == 'SANTO')
