from phonebook import phonebook
from answers import get_class_average, get_class_median
from TextExample import ChapterOne as chapter_one


def main() -> None:
    # exercise #01
    students = {
        "Jeff": 34.5,
        "Tammy":  87.3,
        "Esethu": 65.4,
        "Oscar": 60.9,
        "Pierre": 56.7,
        "Sarah": 91.7,
        "Tim":	 43.5,
        "Theunis": 73.1,
        "Marc": 69.2,
        "Jessica": 53.6,
    }

    # Average score
    average: float = get_class_average(students)
    print(f"Class average: {average}")

    # median
    median: float = get_class_median(students)
    print(f"Class median: {median}")

    # exercise #02
    # 2.1 Change number
    print(f"Laura Moore current number is: {phonebook['Laura Moore']}")
    phonebook['Laura Moore'] = '555-0153'
    print(f"Laura Moore new number is: {phonebook['Laura Moore']}")

    # 2.2 Remove Noah Delgado
    phonebook.pop('Noah Delgado', None)
    print(f"Noah Delgado removed: {'Noah Delgado' not in phonebook}")

    # 2.3 Append new contacts
    contacts = {
        "Alice Johnson": "555-0134",
        "Bob Smith": "555-0912",
        "Carol Lee": "555-8675",
        "David Wright": "555-1357",
        "Emma Davis": "555-2468",
        "Frank Brown": "555-3321",
        "Grace Miller": "555-6472",
        "Helen Clark": "555-0246",
        "Ian Walker": "555-1597",
        "Julia Turner": "555-8635",
        "Kevin Harris": "555-7843",
        "Laura Young": "555-2580",
        "Mark Allen": "555-9876",
        "Nina Scott": "555-2134",
        "Oscar King": "555-3498",
        "Paula Baker": "555-0751",
        "Quentin Reed": "555-6382",
        "Rachel Green": "555-4317",
        "Sam Carter": "555-8923",
        "Tina Perez": "555-6048"
    }
    phonebook.update(contacts)
    print(f"Phonebook updated. Total contacts: {len(phonebook)}")

    # 2.4 Spam
    spam_number = '555-0129'
    # You can use .items() to get both the name and number
    # Or you can just iterate through the dictionary and use the name to get the number
    for name in phonebook:
        if phonebook[name] == spam_number:
            print(f"The spam call from {name} with number {phonebook[name]}")

    # Exercise #03
    countries = {
        "Algeria": {"capital": "Algiers",
                    "language": ["Arabic"]},
        "Angola": {"capital": "Luanda",
                   "language": ["Portuguese"]},
        "Benin": {"capital": "Porto-Novo",
                  "language": ["French"]},
        "Botswana": {"capital": "Gaborone",
                     "language": ["English"]},
        "Burkina Faso": {"capital": "Ouagadougou",
                         "language": ["French"]},
        "Burundi": {"capital": "Bujumbura",
                    "language": ["French", "Kirundi"]},
        "Cameroon": {"capital": "Yaoundé",
                     "language": ["French"]},
        "Cape Verde": {"capital": "Praia",
                       "language": ["Portuguese"]},
        "Central African Republic": {"capital": "Bangui",
                                     "language": ["French"]},
        "Chad": {"capital": "N'Djamena",
                 "language": ["French", "Arabic"]},
        "Comoros": {"capital": "Moroni",
                    "language": ["Shikomoro", "French", "Arabic"]},
        "Congo": {"capital": "Brazzaville",
                  "language": ["French"]},
        "Ivory Coast": {"capital": "Yamoussoukro",
                        "language": ["French"]},
        "Djibouti": {"capital": "Djibouti",
                     "language": ["French", "Arabic"]},
        "Egypt": {"capital": "Cairo",
                  "language": ["Arabic"]},
        "Equatorial Guinea": {"capital": "Malabo",
                              "language": ["Spanish", "French"]},
        "Eritrea": {"capital": "Asmara",
                    "language": ["Tigrinya", "Arabic", "Tigre"]},
        "Ethiopia": {"capital": "Addis Ababa",
                     "language": ["Amharic"]},
        "Gabon": {"capital": "Libreville",
                  "language": ["French"]},
        "Gambia": {"capital": "Banjul",
                   "language": ["English"]},
        "Ghana": {"capital": "Accra",
                  "language": ["English"]},
        "Guinea": {"capital": "Conakry",
                   "language": ["French"]},
    }

    # The solution will depend on how you structured the data.
    french_countries = []
    for country, info in countries.items():
        for language in info['language']:
            if language == 'French':
                french_countries.append(country)
                break  # No need to check other languages for this country
    print(f"Countries where French is spoken: {', '.join(french_countries)}")

    # Exercise #04
    # We use a dictionary with the word as the key and the count as the value
    search_words = {
        "the": 0,
        "at": 0,
        "and": 0,
        "island": 0,
        "man": 0
    }
    full_text:str = chapter_one
    # Remove punctiuation and split the text into words
    full_text = full_text.replace(',', '').replace('.', '').replace('\'', '').\
                        replace('\"', '').replace('!', '').replace('?', '').\
                        replace(':', '').replace(';', '')
    # Convert to lowercase for case-insensitive search
    full_text = full_text.lower()
    # Split the text into individual words
    chapter_one_words = full_text.split()
    for word in chapter_one_words:
        # Check if the word is in our search words dictionary
        if word in search_words:
            search_words[word] += 1

    print("Word counts:")
    for word, count in search_words.items():
        print(f"{word}: {count}")

    # .2 ===========================
    # The list will look as follows: [['a', 5], ['b', 3], ['c', 2], ...]
    # where the first element is the letter and the second element is the count
    letters_list: list  = []
    full_text = chapter_one
    # Remove punctiuation and split the text into words
    full_text = full_text.replace(',', '').replace('.', '').replace('\'', '').\
                        replace('\"', '').replace('!', '').replace('?', '').\
                        replace(':', '').replace(';', '')
    # Convert to lowercase for case-insensitive search
    full_text = full_text.lower()
    for letter in full_text:
        # Check if the character is a letter
        if letter.isalpha():
            # This boolean is used to check if the letter is already in the list
            # If it is, we increment the count, if not, we add it to the
            is_in_list = False
            for letter_count in letters_list:
                if letter == letter_count[0]:
                    is_in_list = True
                    letter_count[1] += 1
                    break
            if not is_in_list:
                # If the letter is not in the list, we add it with a count of 1
                letters_list.append([letter, 1])
    print("Letter counts:")
    for letter_count in letters_list:
        print(f"{letter_count[0]}: {letter_count[1]}")

    # .3 ===========================
    letters: dict = {}
    full_text = chapter_one
    # Remove punctiuation and split the text into words
    full_text = full_text.replace(',', '').replace('.', '').replace('\'', '').\
                        replace('\"', '').replace('!', '').replace('?', '').\
                        replace(':', '').replace(';', '')
    # Convert to lowercase for case-insensitive search
    full_text = full_text.lower()
    for letter in full_text:
        # Check that the character is a letter
        if letter.isalpha():
            # Get the value of the letter, default to 0 if not found
            letters[letter] = letters.get(letter, 0) + 1
    print("Letter counts:")
    for letter, count in letters.items():
        print(f"{letter}: {count}")

    # Exercise #05
    african_countries: dict = {
        "Algeria"                     : "Arabic",
        "Angola"                      : "Portuguese",
        "Benin"                       : "French",
        "Botswana"                    : "English",
        "Burkina Faso"                : "French",
        "Burundi"                     : "French",
        "Cameroon"                    : "French",
        "Cape Verde"                  : "Portuguese",
        "Central African Republic"    : "French",
        "Chad"                        : "French and Arabic",
        "Comoros"                     : "Arabic and French",
        "Congo"                       : "French",
        "Ivory Coast"                 : "French",
        "Djibouti"                    : "French and Arabic",
        "Egypt"                       : "Arabic",
        "Equatorial Guinea"           : "Spanish and French",
        "Eritrea"                     : "Tigre and Arabic",
        "Ethiopia"                    : "Amharic",
        "Gabon"                       : "French",
        "Gambia"                      : "English",
        "Ghana"                       : "English",
        "Guinea"                      : "French"
    }
    # Declare the new dictionary
    language_by_country: dict = {}
    # Create a new dictionary with languages as keys and empty lists as values
    for language in african_countries.values():
        # Split the languages by 'and' to handle multiple languages
        languages = language.split(' and ')
        # Add each language to the new dictionary if not already present
        for language in languages:
            language_by_country[language] = []

    # Add each country to the new dictionary under the appropriate language
    for country, language in african_countries.items():
        languages = language.split(' and ')
        for lang in languages:
            language_by_country[lang].append(country)
    # Print the new dictionary
    print("Countries by language:")
    for language, countries in language_by_country.items():
        print(f"{language}: {', '.join(countries)}")

if __name__ == "__main__":
    main()
