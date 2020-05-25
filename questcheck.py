import statistics

from answer_questions.bert import QA
from text_similarity.text_similarity import sim
# from text2text.text_generator import TextGenerator


class QuestCheck():
    """
    """

    source_answers = []
    unverified_answers = []

    def __init__(self):
        # qg = TextGenerator(output_type="question")
        self.qa = QA(model_path="answer_questions/models")

    def __generate_questions(self):
        # print("Inside generate questions")
        # no_of_questions = self.unverified.split()
        # results = qg.predict(no_of_questions * [self.unverified])
        # this.questions = [q for q, a in results]
        # print("Question generation complete")
        # print("Questions: ", self.questions)
        pass

    def __predict_answers(self):
        print("Inside predict answers")
        print("Predicting answers")
        self.source_answers = []
        self.unverified_answers = []
        for question in self.questions:
            temp = []
            for source in self.sources:
                source_answer = self.qa.predict(source, question)
                temp.append(source_answer['answer'])
            self.source_answers.append(temp)
            unverified_answer = self.qa.predict(self.unverified, question)
            self.unverified_answers.append(unverified_answer['answer'])
            # print("Question: ", question, "---unverified_answer:",
            #       unverified_answer['answer'], "---source_answers:", temp)

        print("Predict answers complete")

    def __calculate_score(self):
        print("Inside calculate score")
        scores = []
        for i in range(len(self.questions)):
            temp = []
            for answer in self.source_answers[i]:
                similarity = sim(answer, self.unverified_answers[i])
                # print("srcanswer-{}---unv-{}---sim-{}".format(answer,
                #                                               self.unverified_answers[i], similarity))
                temp.append(similarity)

            score = min(temp)
            # print("question:", self.questions[i],
            #       "---temp:", temp, "---score:", score)
            scores.append(score)

        return statistics.mean(scores)

    def __evaluate_result(self, result):

        if result < 1 / 3:
            return "incorrect"
        elif 1 / 3 < result < 2 / 3:
            return "inconclusive"
        else:
            return "correct"

    def predict(self, unverified, sources, questions):
        # print("Inside predict")
        self.unverified = unverified
        self.sources = sources
        self.questions = questions
        print("Received params", self.unverified, self.sources, self.questions)
        self.__generate_questions()
        self.__predict_answers()
        result = self.__calculate_score()
        return result
