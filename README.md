# projectSE2sem
ИИ-проект, ориентированный на реферирование текстов, по дисциплине "Программная инженерия".

## Состав команды:
* [Кожин Артём](https://github.com/ctakan4ik) - Тимлид, разработка функциональности приложения, описание проекта в github
* [Лихачев Денис](https://github.com/Liha4) - Разработка тестов
* [Пихтовникова Ирина](https://github.com/IraPikhtovnikova) - Разработка дизайна приложения
* [Чераева Олеся](https://github.com/rulthw) - Настройка github actions
* [Лебедева Дарья](https://github.com/dashleb33) - Развёртывание приложения в облаке

## Описание приложения
Цель данного приложения - реферирование (суммаризация) текстов.

Алгоритм работы:
1. Ввод исходного текста;
2. Суммаризация текста с помощью модели API Pipeline Hugging Face - этот API позволяет пользоваться моделями для автоматического реферирования текстов;
3. Вывод полученных результатов.


## Пример работы приложения (gif поменяется):
![Пример работы приложения](https://user-images.githubusercontent.com/38241217/212289700-8830462c-0840-4f60-a6e6-907f6f4f60da.gif)


## Почему мы пользуемся обучением без подготовки?
В последние годы обучение без подготовки стало популярным из-за того, что оно позволяет использовать эталонные NLP-модели без дополнительного обучения. Их эффективность — это нечто совершенно удивительное. Так, недавно специалисты из Big Science Research Workgroup выпустили модель T0pp (произносится как «Tи ноль плюс плюс»). Эта модель создавалась специально для исследования возможностей применения обучения без подготовки для решения различных задач. В бенчмарке BIG-bench эта модель во многих случаях обходит модели, которые в шесть раз больше её. Ещё она способна показать результаты, лучшие, чем показывает GPT-3 (которая в 16 раз больше её), в некоторых других NLP-бенчмарках.

## Подготовка инфраструктуры для использования ZSL-модели
Для того чтобы воспользоваться ZSL-моделями, мы можем прибегнуть к API Pipeline Hugging Face. Этот API позволяет пользоваться моделями для автоматического реферирования текстов, написав минимальный объём кода. API берёт на себя решение основных задач, связанных с обработкой данных в рамках NLP-модели:
* Осуществляет препроцессинг текста, преобразование его в формат, понятный модели.
* Передаёт модели текст, прошедший предварительную обработку.
* Производит пост-процессинг результатов, выдаваемых моделью, приводя их к виду, понятному человеку.

Этот API использует модели для автоматического реферирования текста, которые имеются в коллекции моделей Hugging Face.

