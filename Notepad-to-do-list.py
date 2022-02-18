"""
моя програма - записник
"""
print("вітаємо Вас у програмі - записнику від Юрія Іленкова!(версія 2.0)")

diary = {}

def add_deal(diary):
    """додаємо нову справу"""
    deal_date = input("Введіть дату (ДД-ММ-РРРР):")
    deal_description = input("Введіть справу, про яку Вам слід нагадати):")

    if deal_date not in diary:
        diary[deal_date] = [deal_description, ]
    else:
        diary[deal_date].append(deal_description)

def delete_all_deals_by_date(diary):
    """Видалення всіх справ за певну дату"""
    deal_date = input("Введіть дату: ")
    print(f"\tСправу за {deal_date} успішно видалено! ")
    diary.pop(deal_date)

def delete_deal_by_date(diary):
    """Видалення певної справи за конкретну дату"""
    deal_date = input("Введіть дату: ")
    num_deal = 0
    for deal in diary[deal_date]:
        print(num_deal, deal)
        num_deal += 1
    num_for_deleting = int(input(f"Введіть номер cправи за {deal_date} яку слід видалити: "))
    print(f"\tСправу за {deal_date} успішно видалено!")
    diary[deal_date].pop(num_for_deleting)

def show_all_deals_in_diary(diary):
    """Вивід повного списку справ на екран"""
    for deal_date in diary:
        print(deal_date)
        num_deal = 0
        for deal in diary[deal_date]:
            print(num_deal, deal)
            num_deal += 1
        print() #просто додаємо порожній рядкок після виводу в консоль

while True:

    answer = input ("Додати нову справу [add]\n"
                    # "Подивитись всі справи [show_all]\n"
                    # "Подивитись всі справи за певне число [show]\n"
                    "Видалити всі справи конкретної дати [delete_all]:\n"
                    "Видалити певну справу конкретного числа [delete_one]:\n"
                    "Вийти з програми (QUIT) [quit]:")

    # додаємо нову справу
    if answer == "add":
       add_deal(diary)
    elif answer == "delete_all":
        try:
            delete_all_deals_by_date(diary)
        except KeyError as error:
            print("!помилка! Ви ввели некоретну дату!", type (error), error)
    elif answer == "delete_one":
        try:
            delete_deal_by_date(diary)
        except KeyError as error:
            print("!помилка! Ви ввели некоретну дату!", type(error), error)

   # завершення роботи програми
    elif answer == "quit":
        print("Програма завершує роботу...")
        break

    show_all_deals_in_diary(diary)

print("Програма завершила свою роботу \nдякую, що скористались моєю програмою-записником)")