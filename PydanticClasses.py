from pydantic import BaseModel 
# this serves the formatting of the GPT output
class interestEnjoyment(BaseModel):
    explanation: str
    question1 : int
    question2 : int
    question3 : int
    question4 : int
    question5 : int
    question6 : int
    question7 : int

class PerceivedCompetence(BaseModel):
    explanation: str
    question1 : int
    question2 : int
    question3 : int
    question4 : int
    question5 : int
    question6 : int

class EffortImportance(BaseModel):
    explanation: str
    question1 : int
    question2 : int
    question3 : int
    question4 : int
    question5 : int
    question6 : int

class PressureTension(BaseModel):
    explanation: str
    question1 : int
    question2 : int
    question3 : int
    question4 : int
    question5 : int

class PerceivedChoice(BaseModel):
    explanation: str
    question1 : int
    question2 : int
    question3 : int
    question4 : int
    question5 : int
    question6 : int
    question7 : int

class ValueUsefulness(BaseModel):
    explanation: str
    question1 : int
    question2 : int
    question3 : int
    question4 : int
