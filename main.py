from salary import calculate_salry
from db.people import get_employees
import datetime

if __name__ == '__main__':
    def main():
        while True:
            user_input = input('Введите:\n s для вывода salary\n p для вывода people\n d для вывода даты\n exit для выхода\n')
            if user_input == 's':
                calculate_salry()
            elif user_input == 'p':
                get_employees()
            elif user_input == 'd':
                today = datetime.date.today()
                print(today)
            elif user_input == 'exit':
                break

    main()