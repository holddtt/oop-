## Міністерство освіти на науки України
## Львівський Національний Університет Природокористування
### Факультет механіки та енергетики
### Кафедра Інформаційних систем та технологій

## Звіт про виконання практичної роботи №2
# "Структурні" паттерни.

### Мета роботи - освоїти роботу з "Структурні" паттернами в Python 2.

### Завдання
1. Дати теоретичний опис "Структурних" паттернів.
2. Дати теоретичний опис вибраного шаблону з групи паттернів



### Хід роботи
1. Група паттернів "Структурні" (Structural Patterns) - це одна з чотирьох основних груп паттернів проектування в області програмного проектування. Ця група паттернів спрямована на створення взаємодії між об'єктами та класами для формування більш складних структур та об'єктних систем.
Основні паттерни в групі "Структурні" включають такі:
    -	Адаптер (Adapter): Цей паттерн дозволяє об'єктам з різними інтерфейсами працювати разом, перетворюючи інтерфейс одного об'єкта в інший.
    -	Міст (Bridge): Міст розділяє абстракцію від реалізації, дозволяючи їм змінюватися незалежно. Цей паттерн використовується для забезпечення гнучкості та розширюваності системи.
    -	Склад (Composite): Паттерн "Склад" дозволяє об'єднувати об'єкти в деревоподібні структури для представлення складних ієрархій об'єктів.
    -	Декоратор (Decorator): Декоратор додає додаткову функціональність до об'єкта, не змінюючи його структури. Цей паттерн дозволяє динамічно надавати об'єктам нові можливості.
    -	Фасад (Facade): Фасад надає простий інтерфейс для складних систем або наборів об'єктів, що допомагає спростити їх використання та зменшити складність коду.
    -	Проксі (Proxy): Проксі дозволяє контролювати доступ до об'єкта, надаючи об'єкту-заміннику можливість виконувати додаткову логіку перед або після доступу до основного об'єкта.
    -	Компонувальник (Flyweight): Компонувальник допомагає оптимізувати використання пам'яті, дозволяючи багатьом об'єктам використовувати спільну частину стану.
Ця група паттернів спрямована на полегшення розширення та обслуговування програмного коду, розділення обов'язків між класами та об'єктами, а також на створення більш гнучких і розширюваних систем. Вона дозволяє розробникам створювати складні системи злегкістю та ефективністю, допомагаючи зберегти читабельність та гнучкість коду.

2. Паттерн "Фасад" (Facade) є структурним патерном проектування, який надає єдиний і простий інтерфейс до складного підсистеми об'єктів. Головна ідея паттерну фасаду полягає в тому, щоб забезпечити високорівневий інтерфейс, який упрощує використання підсистеми, надаючи зовнішній світ лише обмежений, але зручний набір функцій.
Основні учасники паттерна "Адаптер" включають такі елементи:
Підсистема (Subsystem): Це група класів або об'єктів, які виконують конкретні функції або виконують певні завдання. Підсистема складається з різних класів і компонентів, які працюють разом для досягнення певного функціоналу.
Клієнт (Client): Це об'єкт або клас, який використовує фасад для спрощення взаємодії з підсистемою. Клієнт взаємодіє лише з фасадом, не звертаючись безпосередньо до складних компонентів підсистеми.
Фасад (Facade): Це головний клас або об'єкт, який надає простий і високорівневий інтерфейс до підсистеми. Фасад взаємодіє з клієнтами і делегує їх запити до відповідних об'єктів підсистеми.
Основна ідея паттерна "Фасад" полягає в тому, щоб надати простий і єдинообразний інтерфейс до складної системи об'єктів, що дозволяє клієнтам взаємодіяти з системою без необхідності розуміти її внутрішню складність або безпосередньо взаємодіяти з багатьма її частинами.
Основні переваги паттерну фасаду спрощує взаємодію клієнта зі складною системою, надаючи простий і зрозумілий інтерфейс, зменшуючи залежності, покращуючи читабельність коду та полегшуючи управління складністю. 


### Висновок
Паттерн "Фасад" — це структурний паттерн проектування, який надає простий та єдинообразний інтерфейс до складної системи, спрощуючи взаємодію для клієнта, забезпечуючи зменшення залежностей, покращення читабельності коду та полегшення управління складністю системи.