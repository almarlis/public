# Thank you https://github.com/GeorgioArmani/TestRepository.git
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('money = '))
deposit = []
for key in per_cent:
    deposit.append(per_cent[key] * money / 100)
max_deposit = max(deposit)
print('deposit = ' + str(deposit))
str(per_cent.items())
print('Примечание - ' + str(per_cent.items()))
print('Максимальная сумма, которую вы можете заработать - ' + str(max_deposit))
