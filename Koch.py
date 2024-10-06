import turtle

# Функція для малювання одного сегмента кривої Коха
def koch_curve(length, level):
    if level == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch_curve(length, level - 1)
        turtle.left(60)
        koch_curve(length, level - 1)
        turtle.right(120)
        koch_curve(length, level - 1)
        turtle.left(60)
        koch_curve(length, level - 1)

# Функція для малювання сніжинки Коха
def koch_snowflake(length, level):
    for _ in range(3):
        koch_curve(length, level)
        turtle.right(120)

# Головна функція для ініціалізації графіки і побудови фракталу
def main():
    # Вказати користувачем рівень рекурсії
    level = int(input("Введіть рівень рекурсії: "))
    
    # Ініціалізуємо екран turtle
    turtle.speed(0)  # Максимальна швидкість малювання
    turtle.penup()
    turtle.goto(-200, 100)  # Перемістимося в лівий верхній кут
    turtle.pendown()

    # Малюємо сніжинку Коха
    length = 400  # Початкова довжина сторони сніжинки
    koch_snowflake(length, level)
    
    # Завершення
    turtle.done()

if __name__ == "__main__":
    main()
