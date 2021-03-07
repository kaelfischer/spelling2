from text_to_speech import speak

from lists import lists

def get_list():
    """Ask user for name and get the number of the list they are studying.

    :return: list of words
    """

    kids = lists.keys()
    kid = input("What's your name? ")

    number_of_lists = len(lists[kid.upper()]) + 1
    list_number = int(input("Hi %s! What list do you want? (1-%s) "
                         % (kid,number_of_lists)))

    return lists[kid.upper()][list_number-1].split()

def main(word_list):
    """Speak each word in turn. Repeat or continue after user input.

    :param word_list:
    :return: None
    """
    for word in word_list:
        choice = 'R'
        while len(choice) > 0:
            speak(word, slow=False)
            choice = input("R to repeat word, <ENTER> to continue. ")


if __name__ == '__main__':
    """CLI"""
    main(get_list())

