## Порівняння алгоритмів сортування злиття, вставки та Timsort

сьогодня проводимо аналіз трьох алгоритмів сортування. Основною метою є порівняння швидкодії кожного з алгоритмів:

- Сортування злиттям (merge sort)
- Сортування вставками (insertion sort)
- Тімсорт (Timsort) - вбудований в Python алгоритм, який поєднує в собі методи злиття та вставки

Для порівняння використовувався модуль timeit, з допомогою цього модуля виміряємо час роботи кожного алгоритму. Для більш розгорнутого аналізу використовуємо випадкові масиви різного розміру: 50, 500 та 5000 елементів.

---

## Результати виконання

| Size            | Merge Sort      | Insertion Sort  | Timsort         |
-------------------------------------------------------------------------
| 50              | 0.000139        | 0.000074        | 0.000007        |
| 500             | 0.001473        | 0.015763        | 0.000078        |
| 5000            | 0.057015        | 1.437416        | 0.000672        |

_Примітка: при кожному новому запуску програми значення, що наведені в таблиці можуть відрізнятися від наведених в прикладі. Пояснюється це тим, що кожного разу маємо різні випадкові (рамдомні) масиви._

---

## Висновок

- навіть на для невеликих масивів (50 елементів) **Timsort** виконує сортування швидше по відношенню до інших алгоритмів, хоч вони теж працюють досить швидко.
- Із збільшенням розміру масивів (500, 5000) ефективність **Timsort** стає більш помітною.
- Сортування вставками є найповільнішим методом. В нашому випадку він більше ніж в 2000 разів повільніший від **Timsort** (якщо точно, то в 2139 разів).
 
Виходячи із вищенаведеного бачимо, що гібридний підхід **Timsort** робить його значно ефективнішим за інші алгоритми, особливо у випадках великих масивів. Власне це пояснює, чому розробники Python зупинили свій вибір на гібридному методі та добавили його до в вбудованих функцій сортування, зокрема таких як sorted().