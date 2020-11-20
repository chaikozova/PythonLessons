import wikipedia


def main():
    language = input("Выберите язык для статей в Вкипедии: (en, de, ru)")
    wiki = wikipedia
    wiki.set_lang(language)
    while True:
        query = input("Что вам найти в википедии?")
        results = wiki.search(query)
        print()
        for key, result in enumerate(results):
            print(key, result)
        about = input("Выберите о чем вам найти краткую информацию\n")
        summary = wiki.summary(about)

        d = 0
        for i in range(0, len(summary), 50):
            try:
                print(summary[d:d+i], "-")
            except Exception:
                print(summary[d:])
            d += i
        #print(summary, "\n")

        ask_url = input("Хотите ли ссылку на статью в Википедии?")
        if ask_url.lower() == "да":
            article = wiki.page(about)
            print(article.url)




main()

