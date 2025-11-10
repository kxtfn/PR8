def main(): # Аксьонов Ігор 
    try:
        lastname = input("Введіть прізвище: ").strip()
        question = input("Введіть питання з Python: ").strip()
        with open("students.txt", "w", encoding="utf-8") as f:
            f.write(f"Прізвище: {lastname}\n")
            f.write(f"Питання: {question}\n")
            f.write("Відповідь:\n")
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
        

if __name__ == "__main__":
    main()
    append_second_student()
