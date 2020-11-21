Init_hours = (input('Qual o horário inicial: '))
Finish_hours = (input('Qual o horário final: '))
H1 = Init_hours.split(':')
H2 = Finish_hours.split(':')
print('Qual o inicio do atendimento{}: '.format(H1))
print('Qual o final do atendimento{}: '.format(H2))

#Horario inicial
integer = int(H1[0])
integermin = int(H1[1])
integeseg = int(H1[2])
#horario final
integer_finish = int(H2[0])
integerminf = int(H2[1])
integersegf = int(H2[2])
duration_hours = integer - integer_finish
duration_hoursf = abs(integermin - integerminf)
durantion_foursff = integeseg - integersegf
print('Qual a duração do atendimento:{}h:{}m:{}s'.format(duration_hours,duration_hoursf,durantion_foursff))



