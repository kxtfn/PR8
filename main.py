def main():
    try:
        lastname = "Аксьонов"  # Фіксоване прізвище першого студента

        next_question = (
            "Питання для наступного студента:\n"
            "Як у Python відкрити і прочитати файл?\n"
        )
        
        with open("students.txt", "w", encoding="utf-8") as f:
            f.write(f"Прізвище: {lastname}\n")
            f.write(next_question)
            f.write("---\n")
        print("Файл успішно створено.")
    except Exception as e:
        print("Сталася помилка при роботі з файлом:", e)

        

def append_second_student(): # Денисенко Сергій

    filename = "students.txt"

    second_lastname = "Денисенко"

    answer_lines = [
        "Відповідь на питання першого студента:\n",
        "У Python файл відкривають за допомогою функції open(ім'я, режим).\n",
        "Найзручніше використовувати конструкцію with ... as, бо файл закриється автоматично.\n",
        "Основні режими: 'r' – читання, 'w' – перезапис, 'a' – дописування в кінець.\n",
        "Після відкриття можна використовувати write()/writelines() для запису або read()/readline() для читання.\n",
        "Помилки (немає файлу, немає прав) бажано ловити через try-except.\n",
    ]

    next_question = (
        "Питання для наступного студента:\n"
        "Як у Python перевірити існування файлу та прочитати його пострічково?\n"
        "Відповідь:\n"
    )

    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"Прізвище: {second_lastname}\n")
            for line in answer_lines:
                f.write(line)
            f.write(next_question)
            f.write("---\n")
        print("Дані другого студента успішно дописані.")
    except FileNotFoundError:
        print("Помилка: файл 'students.txt' ще не створений першим студентом.")
        

def append_third_student(): # Лихацький Денис
    filename = "students.txt"
    third_lastname = "Лихацький"
    answer_lines = [
        "Відповідь на питання другого студента:\n",
        "Для перевірки існування файлу в Python найчастіше використовують модуль os:\n",
        "import os\n",
        "if os.path.exists('ім\'я_файлу.txt'):\n",
        "    print('Файл існує')\n",
        "else:\n",
        "    print('Файл не знайдено')\n",
        "Щоб прочитати файл пострічково, найефективніше це зробити у циклі for:\n",
        "try:\n",
        "    with open('ім\'я_файлу.txt', 'r', encoding='utf-8') as f:\n",
        "        for line in f:\n",
        "            print(line.strip()) # .strip() прибирає зайві символи переносу рядка\n",
        "except FileNotFoundError:\n",
        "    print('Помилка: Файл для читання не знайдено.')\n"
    ]
    next_question = (
        "Питання для наступного студента:\n"
        "Яка різниця між методами `append()` та `extend()` при роботі зі списками в Python?\n"
        "Відповідь:\n"
    )
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"Прізвище: {third_lastname}\n")
            for line in answer_lines:
                f.write(line)
            f.write(next_question)
            f.write("---\n")
        print("Дані третього студента успішно дописані.")
    except (OSError, PermissionError) as e:
        print(f"Помилка: Не вдалося записати текст у файл '{filename}'. {e}")
    except Exception as e:
        print(f"Помилка: Сталася невідома помилка при дописуванні даних 3-го студента: {e}")

if __name__ == "__main__":
    main()
    append_second_student()
    append_third_student()
