# Andrew Katanakha | lesson 5
import math
import sys


def perimetr_round(radius_of_round):
    perimetr = 2 * math.pi * radius_of_round
    return '{0:.2f}'.format(perimetr)


def square_of_round(radius_of_round):
    square = math.pi * radius_of_round ** 2
    return '{0:.2f}'.format(square)


def radius_round_from_perimetr(perimetr_of_raund):
    radius_of_round = '{0:.2f}'.format(perimetr_of_raund / math.pi / 2)
    return radius_of_round


def radius_round_from_square(square_of_round):
    radius_of_round = '{0:.2f}'.format(math.sqrt(square_of_round / math.pi))
    return radius_of_round


def calculation_of_radius():
	radius = float(input('Enter radius of round: '))
	print('Periment of the round = ', perimetr_round(radius))
	print('Square of the round = ',square_of_round(radius))
	periment_to_calculation_radius = float(input('Enter perimetr of round: '))
	print('Radius (ñalculation from perimetr) = ', radius_round_from_perimetr(periment_to_calculation_radius))
	square_to_calculation_radius = float(input('Enter square of round: '))
	print('Radius (calculation from square) = ', radius_round_from_square(square_to_calculation_radius))


def end_of_program():
    print('Thank for visit, BUY!')
    sys.exit()


def get_zodiak():
	print(
		'1 - January',
		'2 - February',
		'3 - March',
		'4 - April',
		'5 - May',
		'6 - June',
		'7 - July',
		'8 - August',
		'9 - September',
		'10 - October',
		'11 - November',
		'12 - Decembre',
		sep='\n'
	)
	days_in_month = {
	    1 : 31,
	    2 : 29,
	    3 : 31,
	    4 : 30,
	    5 : 31,
	    6 : 30,
	    7 : 31,
	    8 : 31,
	    9 : 30,
	    10 : 31,
	    11 : 30,
	    12 : 31
	}
	month_of_birthday = input("enter your month of birthday: ") 
	while True:
	    if int(month_of_birthday) in days_in_month.keys():
	        break
	    else:
	        print('You entered uncorrect month!!! TRY AGAIN!')
	        month_of_birthday = input("enter your month of birthday: ") 
	    
	day_of_birthday = input('enter your day of birthday: ')

	while True:
	    correct_data = 1 <= int(day_of_birthday) <= days_in_month[int(month_of_birthday)]
	    if correct_data != True:
	        print('You entered uncorrect day!!! TRY AGAIN!')
	        day_of_birthday = input('enter your day of birthday: ')
	    else:
	        break
	    
	if int(day_of_birthday) < 10:
	    day_of_birthday = '0'+ day_of_birthday    

	date = int(month_of_birthday + day_of_birthday)
	zodiak = {
	    120 <= date <= 218: 'Aquarius',
	    219 <= date <= 302: 'Pisces',
	    321 <= date <= 419: 'Aries',
	    420 <= date <= 520: 'Taurus',
	    521 <= date <= 621: 'Gemini',
	    622 <= date <= 722: 'Cancer',
	    723 <= date <= 822: 'Leo',
	    823 <= date <= 922: 'Virgo',
	    923 <= date <= 1022: 'Libra',
	    1023 <= date <= 1122: 'Scorpius',
	    1123 <= date <= 1222: 'Sagittarius',
	    1223 <= date <= 1231 or 101 <= date <= 119: 'Capricornus'
	}
	if True not in zodiak.keys():
	    print('You entered uncorrect day of birthday! TRY AGAIN! ')

	print('Your item of zodiak is: ', zodiak[True])


def creation_of_list():
	my_list = []
	count_of_elements_in_list = int(input('Enter the number of items in the list: '))
	while count_of_elements_in_list != 0:
		elemen_of_list = input('Enter elemen of list: ')
		my_list.append(elemen_of_list)
		count_of_elements_in_list -= 1
	return my_list


def my_reverse_of_list(list_before_reversing):
    reversed_list = list_before_reversing[::-1]
    return reversed_list


def creation_of_dictionary():
    name_of_dictionary = {}
    name_of_dictionary[input('Enter name of key: ')] = input('Enter value of key: ')
    return name_of_dictionary


def printing_of_commad_menu():
    print('Commands menu:')
    print('1. View dictionary item')
    print('2. Add a new item')
    print('3. Delete the item from dictionary')
    print('4. Edit dictionary item')
    print("5. Delete the dictionary")


def users_answer(answer):
	answer = input('If you want continue => press "yes": ')


def command_of_view(name_of_dictionary):
    print(' 1. View dictionary item')
    for key in name_of_dictionary:
        print(key)
    print(name_of_dictionary.get(input('Enter name of key from the list: ')))
    users_answer()


def command_of_adding_new_item(name_of_dictionary):
    print((' 2. Add a new item'))
    name_of_dictionary[input('Enter name of key: ')] = input('Enter value of key: ')
    print('New key with value was added to dictionary')
    users_answer()


def deleting_of_item(name_of_dictionary):
    print('3. Delete the item from dictionary')
    deleted_elements = input('Enter name of key: ')
    name_of_dictionary.pop(deleted_elements)
    print('Element was deleted from dictionary!')
    users_answer()


def edition_of_dictionary(name_of_dictionary):
    print('Edit dictionary item')
    name_of_dictionary.update({input('Enter name of key: '): input('Enter value of key: ')})
    print('Element in dictuonary was edited!')
    print(name_of_dictionary)
    users_answer()


def deletion_of_dictionary(name_of_dictionary):
    del (name_of_dictionary)
    print('Dictionary has been deleted. Buy!')


def work_with_dictionary(name_of_dictionary):
    while True:
        printing_of_commad_menu()
        choosen_command = (input('Enter the commands number: '))
        user_answer = 'yes'
        if choosen_command == '1':
            command_of_view(name_of_dictionary)
        elif choosen_command == '2':
            command_of_adding_new_item(name_of_dictionary)
        elif choosen_command == '3':
            deleting_of_item(name_of_dictionary)
        elif choosen_command == '4':
            edition_of_dictionary(name_of_dictionary)
        elif choosen_command == '5':
            deletion_of_dictionary(name_of_dictionary)
            break
        else:
            print('You have chosen incorrect commands, please try again!!!')
        
        if user_answer.lower() != 'yes':
            print('Thaks for visit, see you latter!')
            break


def main():
	calculation_of_radius()
	get_zodiak()
	my_reverse_of_list(creation_of_list())
	work_with_dictionary(creation_of_dictionary())
	

if __name__ == "__main__"
	main()
	end_of_program()
