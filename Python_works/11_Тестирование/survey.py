class AnonymousSurvey():
    """Сбор анонимных ответов на опросы."""

    def __init__(self, question):
        """Сохраняет вопрос и готовиться к сохранению ответов."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Выводит вопрос"""
        print(self.question)

    def store_response(self, new_response):
        """Сохраняет один отвт на опрос"""
        self.responses.append(new_response)

    def store_results(self):
        """Выводит все полученные ответы"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")