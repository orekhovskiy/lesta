# Задание
1. На языке Python реализовать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций.  
    `def isEven(value):return value%2==0`
2. На языке Python (2.7) реализовать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.
3. На языке Python реализовать функцию, которая быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить почему вы считаете, что функция соответствует заданным критериям.
# Ответы
## Задание 1
Я реализовал проверку на четность при помощи логического "И". 
- Этот способ очень узконаправлен и проверять на кратность без остатка можно только на степенях числа 2
+ Работает быстрее для больших чисел (больше чем длина слова на машине), так как на больших числах деление работает за O(n), где n - количество цифр
## Задание 2
### Очередь с использованием list
Данная реализация очень плоха, и по сути не является очередью с буфером, так как сохрянает все значения в памяти и не удаляет их, что может привести к утечке памяти.
* Добавление Элемента O(1)
* Удаление элемента O(1)
* Максимум используемой памяти - inf
### Очередь с использованием list + pop
Данная реализация удаляет элемент из листа при каждом pop(), но делает это за O(n)
* Добавление элемента O(1)
* Удаление элемента O(n)
* Максимум используемой памяти - n
### Очередь с использованием deque
Данная реализация построена на структуре deque
* Добавление элемента O(1)
* Удаление элемента O(1)
* Максимум используемой памяти - n
## Задание 3
Самые быстрые сортировки дают в среднем асимптотику O(n log n). Это справедливо как для merge, quick так и для tim сортировок. Но quick и tim сортировки падают в крайности на отсортированных массивах данных. Так для quicksort асимптотика будет O(n**2), а для tim - O(n). Стандартные методы list.sort() и sorted() используют именно timsort в python.  
Стоит отметить, что list.sort() работает быстрее, так как он сортирует данный массив, а sorted - его копию. Создание копии занимает время, а по тому сортировка методом list.sort() быстрее.  
Хотя следует помнить, что для того, чтобы отсортированный массив методом sorted() можно было использовать, на него необходимо иметь ссылку.