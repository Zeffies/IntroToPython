aliens = ['Blarg', 'Starg', 'Marg', 'Rarg', 'Darg', 'Larg', 'Aarg', 'Clarg', \
          'Garg', 'Harg']
red = 5
green = 10
blue = 20
alien_colors = [blue, green, red, red, blue, green, blue, red, blue, green]
total = 0
for alien in aliens:
    total = total + alien_colors[aliens.index(alien)]
print(total)
