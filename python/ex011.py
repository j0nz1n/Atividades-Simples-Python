largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metros: '))
area = largura * altura
tinta = area / 2
print('Sua parede mede {}X{} e sua área é de {}m^2.'.format(largura, altura, area))
print('para pintar essa parede, você precisará de {}L de tinta'.format(tinta))
