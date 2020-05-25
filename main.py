import json

from questcheck import QuestCheck
from answer_questions.bert import QA


def main():
    # print("Loading json")
    # qa = QA(model_path="answer_questions/models")
    # doc = "Says the CDC now says that the coronavirus can survive on surfaces for up to 3 days."
    # q = "How long does it take the coronavirus to survive on surfaces?"
    # print(qa.predict(doc, q)['answer'])
    with open('data/data.json') as f:
        data = json.load(f)
        # print("json loaded")
        for instance in data['instances']:
            qc = QuestCheck()
            # print("settings params for instance")
            unverified = instance['unverified']['text']
            sources = instance['sources']
            questions = instance['questions']
            # print("params set, prediting...")
            result = qc.predict(unverified, sources, questions)
            print("FINAL SCORE", result)
            print("------predictin for instance completed... ---------")
    print("PROGRAM COMPLETE")


if __name__ == "__main__":
    main()
