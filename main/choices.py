def get_nationality_from_file():
    nationality = []

    with open('files/nationalities.txt') as file:
        for line in file:
            option = line.strip()
            nationality.append((option, option))
    return nationality

def get_book_category_from_file():
    book_category = []

    with open('files/book_category.txt') as file:
        for line in file:
            option = line.strip()
            book_category.append((option, option))
    return book_category