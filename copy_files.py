import os
import shutil
import sys

# Функція для рекурсивного читання директорій і копіювання файлів
def copy_and_sort_files(src_dir, dst_dir):
    try:
        # Перевіряємо, чи існує директорія призначення, якщо ні - створюємо її
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        
        # Перебираємо всі елементи у вихідній директорії
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)
            
            # Якщо це директорія, викликаємо функцію рекурсивно
            if os.path.isdir(src_path):
                new_dst_dir = os.path.join(dst_dir, item)
                copy_and_sort_files(src_path, new_dst_dir)
            # Якщо це файл, обробляємо його
            elif os.path.isfile(src_path):
                # Отримуємо розширення файлу
                file_extension = os.path.splitext(item)[1][1:].lower()
                if not file_extension:  # Якщо файл без розширення
                    file_extension = 'no_extension'
                
                # Створюємо папку для файлів з цим розширенням у директорії призначення
                extension_dir = os.path.join(dst_dir, file_extension)
                if not os.path.exists(extension_dir):
                    os.makedirs(extension_dir)

                # Копіюємо файл до відповідної папки
                shutil.copy2(src_path, extension_dir)
                print(f"Скопійовано файл {item} до {extension_dir}")

    except Exception as e:
        print(f"Помилка: {e}")

# Парсинг аргументів командного рядка
def main():
    try:
        if len(sys.argv) < 2:
            print("Необхідно вказати шлях до вихідної директорії.")
            return

        src_dir = sys.argv[1]
        dst_dir = sys.argv[2] if len(sys.argv) > 2 else 'dist'

        if not os.path.exists(src_dir):
            print(f"Директорія {src_dir} не існує.")
            return

        # Виклик функції для копіювання та сортування файлів
        copy_and_sort_files(src_dir, dst_dir)
        print("Копіювання завершено.")
    
    except Exception as e:
        print(f"Помилка в основній функції: {e}")

if __name__ == '__main__':
    main()

