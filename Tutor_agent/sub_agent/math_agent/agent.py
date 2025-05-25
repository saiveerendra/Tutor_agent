from google.adk.agents import Agent
import math

def calculator(expression: str) -> dict:
    """Returns the computed value of expression.

    Args:
        expression: A mathematical expression which has operations like addition, substraction, multiplication and division. 

    Returns:
        dict:returns result of expression
    """
    result = 0
    try:
        result = eval(expression)
    except Exception as e:
        print("error occurred while calculating",e)
        return {"result": e}
    return {"result":result}
def trignometric_calculator(expression:str)->dict:
    """Calculates the trignometric expressions like sin(90),cos(180)..

    Args:
        expression (str): Basic trignometric expressions.

    Returns:
        dict: Returns the value of trignometric expressions in dictionary format.
    """
    try:
        fn, val = expression.lower().strip().split("(")
        val = float(val.rstrip(")"))
        radians = math.radians(val)
        if fn=="sin":
            return {"result": math.sin(radians)}
        elif fn=="cos":
            return {"result": math.cos(radians)}
        elif fn=="tan":
            return {"result": math.tan(radians)}
        elif fn=="cot":
            return {"result": 1 / math.tan(radians)}
        elif fn=="sec":
            return {"result": 1 / math.cos(radians)}
        elif fn=="csc" | "cosec":
            return {"result": 1 / math.sin(radians)}
        else:
            return {"result": "Unsupported function"}
    except Exception as e:
        return {"result": f"Error: {str(e)}"}
    
    
math_agent = Agent(
    name="math_Agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions regarding maths questions."
    ),
    instruction=(
        """You are a helpful agent who can give accurate answers to the math questions.
           Use the following tools for different scenario:
           1.`calculator` for basic calculations like addition,substraction,multplication and division use tool calculator
              elif expressions like 2x+7=9 is given then convert it into x =(9-7)/2 give LHS part as expression to  the calculator tool then show the value in chat.
           2.`trigonometric_calculator` for sin(90), cos(30) — numeric with degrees.
           3.use both tools for expressions like sin(30)+cos(90) calculate trignometric expressions and pass the values to calculator
           4.for trignometric expressions like tan(90) ,1/cos(0) which are tending to very large number give it undefined tending to infinity (∞)
           use above mentioned tools only other wise give i cant give the answer.           
        """
    ),
    tools=[calculator,trignometric_calculator]
)