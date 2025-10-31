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

if __name__ == "__main__":
    main()
