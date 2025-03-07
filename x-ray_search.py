class XRaySearchGenerator:
    def __init__(self):
        self.operators = {
            'site': 'site:',
            'inurl': 'inurl:',
            'intitle': 'intitle:',
            'filetype': 'filetype:',
            'intext': 'intext:',
            'exclude': '-',
            'or': 'OR',
            'and': 'AND',
            'not': '-',
        }
        
        # Обновленные шаблоны без лишних кавычек и скобок
        self.common_templates = {
            'резюме': 'site:hh.ru OR site:linkedin.com OR site:rabota.ru {keyword}',
            'документы': 'filetype:pdf OR filetype:doc OR filetype:docx {keyword}',
            'социальные_сети': 'site:facebook.com OR site:vk.com OR site:instagram.com {keyword}',
            'форумы': 'site:forum.* OR inurl:forum {keyword}',
            'github_clean': 'site:github.com/ {keyword} -inurl:topics|issues|projects|exchange|repositories|trending',
            'github_code': 'site:github.com {keyword} inurl:blob master',
            'linkedin_search': {
                'opentowork': 'site:linkedin.com/ inurl:opentowork-activity {keyword}',
                'jobs': 'site:linkedin.com/jobs {keyword}',
                'people': 'site:linkedin.com/in/ {keyword}',
                'posts': 'site:linkedin.com/posts/ {keyword}',
                'companies': 'site:linkedin.com/company/ {keyword}'
            }
        }

        # Списки сайтов по категориям
        self.job_sites = {
            'Работные сайты': [
                'hh.ru',
                'superjob.ru',
                'rabota.ru',
                'zarplata.ru',
                'career.habr.com',
                'job.ru',
                'trudvsem.ru',
                'avito.ru',
                'indeed.com'
            ],
            'Профессиональные сети': [
                'linkedin.com',
                'ru.linkedin.com',
                'vk.com/resume',
                'facebook.com/jobs',
                'moikrug.ru',
                'github.com'
            ],
            'Фриланс площадки': [
                'freelance.ru',
                'fl.ru',
                'freelancehunt.com',
                'kwork.ru',
                'weblancer.net'
            ],
            'Специализированные IT': [
                'career.habr.com',
                'stackoverflow.com/jobs',
                'djinni.co',
                'getmatch.ru',
                'hexlet.io/jobs',
                'geeklink.io',
                'github.io'
            ]
        }

    def format_keyword(self, keyword):
        """Форматирование ключевого слова: больше не добавляем кавычки"""
        return keyword

    def format_term(self, term):
        """Форматирование термина: просто возвращаем очищенный термин"""
        return term.strip('"')

    def generate_basic_query(self, keyword, search_type=None):
        keyword_query = self.format_keyword(keyword)
        if search_type and search_type in self.common_templates:
            return self.common_templates[search_type].format(keyword=keyword_query)
        return keyword_query

    def add_site_restriction(self, query, site):
        """Добавление ограничения по сайту"""
        if site in ['linkedin.com', 'github.com']:
            return f'site:{site}/ {query}'
        return f'site:{site} {query}'

    def add_file_type(self, query, file_type):
        return f'filetype:{file_type} {query}'

    def exclude_term(self, query, term):
        term_query = self.format_term(term)
        return f'{query} -{term_query}'

    def add_logical_operator(self, query, operator, term):
        term_query = self.format_term(term)
        if operator == "AND":
            return f'{query} {term_query}'
        elif operator == "OR":
            return f'{query} OR {term_query}'
        elif operator == "NOT":
            return f'{query} -{term_query}'
        return query

    def exclude_multiple_terms(self, query, terms_list):
        """Исключение нескольких терминов через оператор |"""
        if not terms_list:
            return query
        excluded_terms = '|'.join(terms_list)
        return f'{query} -inurl:{excluded_terms}'

    def generate_github_search(self):
        """Специальная функция для поиска по GitHub"""
        print("\nПоиск по GitHub:")
        keyword = input("Введите ключевое слово или фразу: ")
        keyword_query = self.format_keyword(keyword)
        
        print("\nВыберите тип поиска:")
        print("1. Чистый поиск (без служебных страниц)")
        print("2. Поиск в коде")
        print("3. Пользовательский поиск")
        
        choice = input("\nВаш выбор: ")
        
        if choice == "1":
            return f'site:github.com/ {keyword_query} -inurl:topics|issues|projects|exchange|repositories|trending'
        elif choice == "2":
            return f'site:github.com {keyword_query} inurl:blob master'
        elif choice == "3":
            exclude_sections = []
            print("\nВыберите секции для исключения (введите номера через запятую):")
            print("1. topics")
            print("2. issues")
            print("3. projects")
            print("4. exchange")
            print("5. repositories")
            print("6. trending")
            print("7. pulls")
            print("8. marketplace")
            
            sections = input("\nВыберите номера (например, 1,2,3): ").split(',')
            all_sections = ['topics', 'issues', 'projects', 'exchange', 
                          'repositories', 'trending', 'pulls', 'marketplace']
            
            for section in sections:
                try:
                    index = int(section.strip()) - 1
                    if 0 <= index < len(all_sections):
                        exclude_sections.append(all_sections[index])
                except:
                    continue
            
            query = f'site:github.com/ {keyword_query}'
            return self.exclude_multiple_terms(query, exclude_sections)

    def generate_linkedin_search(self):
        """Специальная функция для поиска на LinkedIn"""
        print("\n=== Поиск на LinkedIn ===")
        print("Выберите тип поиска:")
        print("1. Поиск людей открытых к работе (OpenToWork)")
        print("2. Поиск вакансий")
        print("3. Поиск профилей людей")
        print("4. Поиск в постах")
        print("5. Поиск компаний")
        
        choice = input("\nВаш выбор: ")
        keyword = input("Введите ключевое слово (например, 'java'): ")
        keyword_query = self.format_keyword(keyword)
        
        if choice == "1":
            return f'site:linkedin.com/ inurl:opentowork-activity {keyword_query}'
        elif choice == "2":
            return f'site:linkedin.com/jobs {keyword_query}'
        elif choice == "3":
            return f'site:linkedin.com/in/ {keyword_query}'
        elif choice == "4":
            return f'site:linkedin.com/posts/ {keyword_query}'
        elif choice == "5":
            return f'site:linkedin.com/company/ {keyword_query}'

    def generate_custom_query(self):
        print("\n=== Генератор X-Ray поисковых запросов ===")
        print("Введите ключевое слово или фразу для поиска")
        print("Примеры:")
        print("- java")
        print("- python developer")
        print("- devops engineer")
        
        keyword = input("\nВаш запрос > ")
        query = self.format_keyword(keyword)
        
        while True:
            print("\nВыберите действие:")
            print("1. Добавить ограничение по сайту")
            print("2. Добавить параметр URL (inurl)")
            print("3. Добавить исключение")
            print("4. Завершить и показать результат")
            
            choice = input("\nВаш выбор: ")
            
            if choice == "1":
                site = input("Введите домен сайта (например, linkedin.com): ")
                query = self.add_site_restriction(query, site)
            
            elif choice == "2":
                param = input("Введите параметр URL (например, opentowork-activity): ")
                query = f'{query} inurl:{param}'
            
            elif choice == "3":
                exclude = input("Введите термин для исключения: ")
                query = self.exclude_term(query, exclude)
            
            elif choice == "4":
                break
            
            print(f"\nТекущий запрос: {query}")
        
        return query

    def generate_job_search(self):
        """Специальная функция для поиска работников/вакансий"""
        print("\n=== Поиск работников/вакансий ===")
        
        print("\nВведите ключевые слова для поиска:")
        print("1. Добавить название должности на русском")
        print("2. Добавить название должности на английском")
        print("3. Добавить дополнительные навыки")
        print("4. Завершить ввод")
        
        keywords = []
        while True:
            choice = input("\nВыберите действие (1-4): ")
            
            if choice == "1":
                keyword_ru = input("Введите должность на русском: ")
                if keyword_ru:
                    keywords.append(self.format_keyword(keyword_ru))
            
            elif choice == "2":
                keyword_en = input("Введите должность на английском: ")
                if keyword_en:
                    keywords.append(self.format_keyword(keyword_en))
            
            elif choice == "3":
                skills = input("Введите дополнительные навыки через запятую: ")
                if skills:
                    for skill in skills.split(','):
                        skill = skill.strip()
                        if skill:
                            keywords.append(self.format_keyword(skill))
            
            elif choice == "4":
                if not keywords:
                    print("Нужно ввести хотя бы одно ключевое слово!")
                    continue
                break
            
            print("\nТекущие ключевые слова:", " OR ".join(keywords))

        # Выбор сайтов
        selected_sites = []
        while True:
            print("\nДоступные категории сайтов:")
            categories = list(self.job_sites.keys())
            for i, category in enumerate(categories, 1):
                print(f"{i}. {category}")
            print("5. Показать выбранные сайты")
            print("6. Продолжить с выбранными сайтами")
            
            category_choice = input("\nВыберите категорию (или 6 для продолжения): ")
            
            if category_choice == "6":
                if not selected_sites:
                    print("Вы не выбрали ни одного сайта. Хотите выбрать сайты?")
                    if input("Да/Нет: ").lower() != 'да':
                        break
                    continue
                break
            
            elif category_choice == "5":
                if selected_sites:
                    print("\nВыбранные сайты:")
                    for site in selected_sites:
                        print(f"- {site}")
                else:
                    print("Сайты еще не выбраны")
                continue
            
            try:
                index = int(category_choice) - 1
                if 0 <= index < len(categories):
                    category = categories[index]
                    sites = self.job_sites[category]
                    
                    print(f"\nДоступные сайты в категории '{category}':")
                    for i, site in enumerate(sites, 1):
                        print(f"{i}. {site}")
                    
                    site_choices = input("\nВыберите номера сайтов через запятую (или 'all'): ")
                    
                    if site_choices.lower() == 'all':
                        selected_sites.extend(sites)
                        print(f"Добавлены все сайты из категории '{category}'")
                    else:
                        try:
                            for num in site_choices.split(','):
                                site_index = int(num.strip()) - 1
                                if 0 <= site_index < len(sites):
                                    site = sites[site_index]
                                    if site not in selected_sites:
                                        selected_sites.append(site)
                                        print(f"Добавлен сайт: {site}")
                        except ValueError:
                            print("Неверный формат ввода")
            except ValueError:
                print("Неверный выбор категории")

        # Формирование запроса с сайтами
        if selected_sites:
            site_query = ' OR '.join([f'site:{site}' for site in selected_sites])
            keyword_query = ' OR '.join(keywords)
            final_query = f'{site_query} {keyword_query}'
        else:
            final_query = ' OR '.join(keywords)

        # Добавление города
        print("\nВыберите город:")
        print("1. Москва")
        print("2. Санкт-Петербург")
        print("3. Другой город")
        print("4. Вся Россия")
        
        city_choice = input("\nВаш выбор: ")
        if city_choice == "1":
            final_query += f' {self.format_keyword("Москва")}'
        elif city_choice == "2":
            final_query += f' {self.format_keyword("Санкт-Петербург")}'
        elif city_choice == "3":
            city = input("Введите название города: ")
            final_query += f' {self.format_keyword(city)}'

        # Дополнительные параметры
        print("\nДополнительные параметры:")
        print("1. Добавить уровень (junior/middle/senior)")
        print("2. Добавить зарплату")
        print("3. Добавить опыт работы")
        print("4. Продолжить без дополнительных параметров")
        
        params_choice = input("\nВыберите параметры (номера через запятую): ")
        
        if '1' in params_choice:
            level = input("Введите уровень (junior/middle/senior): ")
            final_query += f' {self.format_keyword(level)}'
        
        if '2' in params_choice:
            salary = input("Введите зарплату (например, '100000'): ")
            final_query += f' {salary}'

        if '3' in params_choice:
            experience = input("Введите опыт работы (например, '3 года'): ")
            final_query += f' {self.format_keyword(experience)}'

        return final_query

def main():
    generator = XRaySearchGenerator()
    
    while True:
        print("\n=== X-Ray Search Generator ===")
        print("1. Создать поисковый запрос")
        print("2. Поиск работников/вакансий")
        print("3. Специальный поиск по GitHub")
        print("4. Специальный поиск по LinkedIn")
        print("5. Информация о операторах")
        print("6. Выход")
        
        choice = input("\nВыберите действие: ")
        
        if choice == "1":
            query = generator.generate_custom_query()
            print("\nГотовый поисковый запрос:")
            print("-" * 50)
            print(query)
            print("-" * 50)
            
        elif choice == "2":
            query = generator.generate_job_search()
            print("\nГотовый поисковый запрос для поиска работников/вакансий:")
            print("-" * 50)
            print(query)
            print("-" * 50)
            print("\nЭтот запрос:")
            print("- Ищет по выбранным сайтам поиска работы")
            print("- Учитывает дополнительные параметры")
            
        elif choice == "3":
            query = generator.generate_github_search()
            print("\nГотовый поисковый запрос для GitHub:")
            print("-" * 50)
            print(query)
            print("-" * 50)
            print("\nЭтот запрос:")
            print("- Ищет на GitHub")
            print("- Исключает служебные страницы")
            print("- Фокусируется на основном контенте")
            
        elif choice == "4":
            query = generator.generate_linkedin_search()
            print("\nГотовый поисковый запрос:")
            print("-" * 50)
            print(query)
            print("-" * 50)
            print("\nЭтот запрос:")
            print("- Ищет на LinkedIn")
            print("- Использует правильные операторы")
            print("- Включает слеш где необходимо")
            
        elif choice == "5":
            print("\nОсновные операторы X-Ray поиска:")
            print("\nЛогические операторы:")
            print("AND - неявный оператор между словами (просто пробел)")
            print("OR - логическое ИЛИ (найти любой из терминов)")
            print("NOT (-) - исключение термина")
            print("\nСпециальные операторы:")
            print("site: - поиск на конкретном сайте")
            print("inurl: - поиск в URL страницы")
            print("intitle: - поиск в заголовке страницы")
            print("filetype: - поиск по типу файла")
            print("intext: - поиск в тексте страницы")
            print('Кавычки - используются только для фраз с пробелами')
            print("\nПримеры:")
            print('site:github.com python AND machine learning -javascript')
            print('filetype:pdf python OR java AND tutorial')
            input("\nНажмите Enter для продолжения...")
            
        elif choice == "6":
            print("Программа завершена")
            break

if __name__ == "__main__":
    main() 