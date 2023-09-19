
from typing import Dict, List, Tuple, Optional
import openai
import json

def validate_question_format(question_list: List) -> Tuple[bool, str]:
    # Check if input is a list
    if not isinstance(question_list, list):
        return (False, "Input is not a list.")
    
    for i, question_dict in enumerate(question_list):
        # Check if each entry is a dictionary
        if not isinstance(question_dict, dict):
            return (False, f"Element at index {i} is not a dictionary.")
        
        # Check if all required keys are present
        if not all(key in question_dict for key in ("q", "options", "a_index")):
            return (False, f"Element at index {i} is missing one or more required keys ('q', 'options', 'a_index').")
        
        # Check if 'q' is a string
        if not isinstance(question_dict["q"], str):
            return (False, f"Element at index {i} has a 'q' value that is not a string.")
        
        # Check if 'options' is a list of strings
        if not isinstance(question_dict["options"], list):
            return (False, f"Element at index {i} has an 'options' value that is not a list.")
        
        if not all(isinstance(option, str) for option in question_dict["options"]):
            return (False, f"Element at index {i} has an 'options' value that contains non-string elements.")
        
        # Check if 'a_index' is an integer and within the range of options
        if not isinstance(question_dict["a_index"], int):
            return (False, f"Element at index {i} has an 'a_index' value that is not an integer.")
        
        if question_dict["a_index"] < 0 or question_dict["a_index"] >= len(question_dict["options"]):
            return (False, f"Element at index {i} has an 'a_index' value that is out of range for the given options.")
    
    return (True, "")

EXAMPLE_QUIZ = [
    {
        "q": "What is the capital of France?", 
        "options": ["Paris", "Berlin", "London", "Madrid"],
        "a_index": 0
    },
    {
        "q": "Which of the following is not a programming language?", 
        "options": ["Python", "Java", "Banana", "TypeScript"],
        "a_index": 2
    },
    {
        "q": "What is 2+2?", 
        "options": ["34", "5", "15", "4"],
        "a_index": 3
    }
]

"""
result, message = validate_question_format(EXAMPLE_QUIZ)
print(result)  # Should print True
print(message)  # Should print ""
"""


def get_quiz_for_prompt(messages: List[Dict], openai_api_key: str, max_tries: int = 4) -> Tuple[Optional[Dict], List[Dict]]:
    """
    Prompts chatgpt until a proper json object representing a quiz is returned.

    returns: tuple (quiz_dict, new_messages)
    """
    openai.api_key = openai_api_key

    history = messages.copy()
    next_prompt = ""
    for i in range(max_tries):
        print(f"getting quiz from chatgpt attempt {i+1}/{max_tries}")
        #st.session_state.messages.append({"role": "user", "content": f"Give me the quiz with the answers as well and make it multiple choice please"})
        if not next_prompt:
            next_prompt = f"Give me the quiz on the topic above, including the answers. You're response must consist only of a list of valid json objects (starting with the char '[' and ending with ']') of a format like the following example valid response:\n{EXAMPLE_QUIZ}"
        print("next_prompt = ", next_prompt)
        history.append({"role": "user", "content": next_prompt})
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=history)
        msg = response.choices[0].message

        if "[" not in msg.content or "]" not in msg.content:
            next_prompt = "response does not contain '[' or ']'"
            continue
        raw_answer = msg.content[msg.content.index("["):msg.content.rindex("]")+1]

        # try to read as json and validate
        print("response = ", raw_answer)
        try:
            quiz_dict = json.loads(raw_answer)
            result, problem = validate_question_format(quiz_dict)
            if result:
                return (quiz_dict, history)
            history.append({"role": "assistant", "content": f"Invalid quiz format please try again: {problem}"})
        except json.decoder.JSONDecodeError as err:
            next_prompt = f"invalid json provided please try again. Respond only with valid json.\n{err}"
    
    print(f"Failed to get quiz from chatgpt after {max_tries} attempts :(")
    return (None, history)







