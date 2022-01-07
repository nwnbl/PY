class Survey:
    def __init__(self, question):
        self.question = question
        self.responses=[]

    def show_question(self):
        print(f"{self.question}")
    
    def store_response(self, new):
        self.responses.append(new)
    
    def show_results(self):
        print("Results: \n")
        for res in self.responses:
            print(f"{res}")