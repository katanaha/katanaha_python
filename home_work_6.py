# Andrew Katanakha | lesson 6

class Work_with_dictionary:
    user_answer = 'yes'
    dictionary = {}

    def __init__(self, dictionary=None):
        if not dictionary:
            dictionary = self.dictionary
        else:
            self.dictionary = dictionary

    def printing_of_commad_menu(self):
        print('Commands menu:')
        print('1. View dictionary item')
        print('2. Add a new item')
        print('3. Delete the item from dictionary')
        print('4. Edit dictionary item')
        print("5. Delete the dictionary")

    def users_answer(self):
        self.user_answer = input('If you want continue => press "yes": ')

    def view_dictionary_elements(self):
        print(' 1. View dictionary item')
        for key in self.dictionary:
            print(key)
        print(self.dictionary.get(input('Enter name of key from the list: ')))
        self.users_answer()

    def command_of_adding_new_item(self):
        print((' 2. Add a new item'))
        self.dictionary[input('Enter name of key: ')] = input('Enter value of key: ')
        print('New key with value was added to dictionary')
        self.users_answer()

    def deleting_of_item(self):
        print('3. Delete the item from dictionary')
        for key in self.dictionary:
            print(key)
        deleted_elements = input('Enter name of key from the list: ')
        self.dictionary.pop(deleted_elements)
        print('Element of dictionary was deleted!')
        self.users_answer()

    def edition_of_dictionary(self):
        print('Edit dictionary item')
        for key in self.dictionary:
            print(key)
        self.dictionary.update({input('Enter name of key: '): input('Enter value of key: ')})
        print('Element in dictionary was edited!')
        print(self.dictionary)
        self.users_answer()

    def deletion_of_dictionary(self):
        try:
            print('Dictionary has been deleted. Buy!')
            del (self.dictionary)
        except AttributeError as massege:
            print('See you later')

    def work_with_dictionary(self):
        while True:
            self.printing_of_commad_menu()
            choosen_command = (input('Enter the commands number: '))
            if choosen_command == '1':
                self.view_dictionary_elements()
            elif choosen_command == '2':
                self.command_of_adding_new_item()
            elif choosen_command == '3':
                self.deleting_of_item()
            elif choosen_command == '4':
                self.edition_of_dictionary()
            elif choosen_command == '5':
                self.deletion_of_dictionary()
                break
            else:
                print('You have chosen incorrect commands, please try again!!!')

            if self.user_answer.lower() != 'yes':
                print('Thaks for visit, see you latter!')
                break


def main():
    random_dictionary = Work_with_dictionary()
    random_dictionary.work_with_dictionary()


if __name__ == "__main__":
    main()
