from database import quizzes_collection
from quizzes_model import Quiz, QuizCreator, all_quizzes
from quizzes_routes import create_quiz, get_quizzes, delete_quiz, update_quiz_by_id


def build_quiz_creator():
    user_name = input("Enter your name: ")
    quiz_list_ = []
    # new_creator = None
    while True:
        question = input("Enter your question: ")
        list_size = int(input("How many choices would would add to your question? "))
        list_of_choices = []
        for i in range(list_size):
            first_ = input("Enter a Choice: ")
            list_of_choices.append(first_)

        new_quiz = {
            "question": question,
            "choices": list_of_choices
        }

        quiz_list_.append(new_quiz)

        new_creator = {
            "name": user_name,
            "quiz_list": quiz_list_
        }

        user_confirm2 = input("you have created your first quiz, would you like to add new one or no? "
                              "[add/no]: ")
        if user_confirm2 == "add":
            continue
        else:
            create_quiz(new_creator)
            print("Great Job!!, save your ID for later if you want to update you quiz, your ID: " +
                  f"{get_last_quiz_creator_id()}")
            break
    return new_creator


def get_last_quiz_creator_id():
    lists_ = all_quizzes(quizzes_collection.find())
    return lists_[-1].get("id")


def get_quizzes_id():
    lists_ = all_quizzes(quizzes_collection.find())
    return [quiz.get('id') for quiz in lists_]


if __name__ == '__main__':
    lists_ = all_quizzes(quizzes_collection.find())
    for x in lists_:
        print(x)

    print(get_quizzes_id())
    user_answ = input("Do you already have created a Quiz and have an ID? [y/n] ")
    user_answ = user_answ.lower()
    if user_answ == "n":
        print("Would you like to make your own quiz or to play?")
        user_confirm = input("Enter 'm' to make one, OR 'p' to play: ")
        user_confirm = user_confirm.lower()
        if user_confirm == "m":
            build_quiz_creator()
        else:
            print("Sorry! you will not be able to play cause the site is under construction")
    elif user_answ == "y":
        user_answ2 = input("Would you like to update or delete your quiz ? [u/d] ")
        user_answ2 = user_answ2.lower()
        if user_answ2 == "u":
            read_id = input("Typ your ID: ")
            if read_id in get_quizzes_id():
                # print("Warning you will get a new ID")
                print("HINT: IF YOU GET A NEW ID JUST IGNORE IT, YOU STILL HAVE THE SAME OLD ONE!!")
                new_quiz = build_quiz_creator()
                update_quiz_by_id(read_id, new_quiz)
                delete_quiz(get_last_quiz_creator_id())  # still need to change
            else:
                print("This ID not exist in the DataBase, try with another valid ID")
        elif user_answ2 == "d":
            read_id = input("Typ your ID: ")
            if read_id in get_quizzes_id():
                delete_quiz(read_id)
            else:
                print("This ID not exist in the DataBase, try with another valid ID")
        else:
            print("OPPS!!, undefined input, Try again")
    else:
        print("OPPS!!, undefined input, Try again")
