import time
import json
import os
import re
from gemma3_inference_ollama import GemmaInferenceOllama

class CreateJSON_QA:
    FILE_PATH = "learning_json/pretrain_dataset.jsonl"
    OUTPUT_FILE = "learning_json/alpaca.jsonl"
    OUTPUT_DIR = "learning_json/alpaca_split"

    def __init__(self, project_name='Warmduscher'):
        self.project_name = project_name
        self.gemma = GemmaInferenceOllama()

        self.intros = [

             ######################## QUESTION 1 ########################
            f"""
            Your task is to write an IT specification for the given source code class below, which is part of the project '{self.project_name}'. 
            The IT specification shall follow the structure below. If an item of the spec is not applicable just leave it empty.

            # IT Specification

            ## 1. Summary
            Provide a clear summary of the code purpose and functionality.

            ## 2. File Information
            - **File Location:** (Specify the file path)
            - **Class Name(s):** (List relevant class names)

            ## 3. Functional Requirements
            This section defines the expected behavior and core functionalities of the code. Functional requirements should specify:
            - **Primary Operations**: What the code is designed to do.
            - **User Inputs & Outputs**: Expected inputs and corresponding outputs.
            - **Workflow/Logic**: Steps or processes involved.
            - **External Interactions**: API calls, database queries, file operations, or UI interactions.
            - **Edge Cases Handling**: Expected behavior in different scenarios, including errors.

            ## 4. Non-Functional Requirements
            This section defines the quality attributes and constraints of the system, including:
            - **Performance**: Expected execution time, response time, or memory usage.
            - **Scalability**: How well the system handles increased load.
            - **Security**: Authentication, encryption, data protection.
            - **Maintainability**: Code structure, modularity, ease of modification.
            - **Reliability & Availability**: Expected uptime and fault tolerance.
            - **Usability**: How easy it is to use or integrate.
            - **Compliance**: Industry standards or legal requirements.

            ## 5. Key Components
            Break down the main components of the code, including:
            - Functions: Give a quick description of what each function is doing
            - Important logic flows
            - Error handling
            - Classes: are there any subclasses defined?
            - Modules

            ## 6. Dependencies

            ### 6.1 Core Language Features
            List the built-in language features and standard libraries used, e.g.:
            - Data structures (lists, maps, sets, etc.)
            - File handling
            - Concurrency/threading

            ### 6.2 External Frameworks & Libraries
            List external dependencies along with their purpose, e.g.:
            - **Spring Boot** - Used for dependency injection and web service handling.
            - **Lodash** - Provides utility functions for array and object manipulation.

            ### 6.3 Internal Project Dependencies
            List internal project dependencies with explanations, e.g.:
            - **`com.myproject.utils.StringHelper`** - Provides string manipulation functions.
            - **`myproject.database.DbConnector`** - Handles database connectivity.

            ## 7. Potential Improvements
            Suggest improvements or optimizations, such as:
            - **Performance Enhancements:** Identify possible bottlenecks.
            - **Code Readability:** Refactor large functions into smaller, reusable units.
            - **Security Improvements:** Highlight potential security risks.
            - **Scalability Considerations:** Recommend changes for future scalability.

            Source code below:
            """, 

             ######################## QUESTION 2 ########################
            f"""
            For the source code below. Write 5 questions for a developer interview.  Focus on different areas on the code...
            
            The questions must always begin with: For Project '{self.project_name}' considering file in path '{{FILE_LOCATION}}' with name '{{FILE_NAME}}'... 
            {{QUESTION}}...

            Replace FILE_LOCATION and FILE_NAME with the given below... then directly write the best answer you can imagine to the question... 
            now, for your response: directly response. no introduction. format each question and answer pair using the following syntax:
            ***** MY_QUESTION
            {{QUESTION}}
            ***** MY_ANSWER
            {{ANSWER}}
            """,

             ######################## QUESTION 3 ########################
            f"""
            For the source code below: Write 5 questions for a developer interview. The candidate is given a quick overview. Then the questions itself shall cover different areas of the code. The question itself contains a part of the code (e.g. a method, or partial method, or some other partials) which are shown..
            
            The questions must always begin with: For Project '{self.project_name}' considering file in path '{{FILE_LOCATION}}' with name '{{FILE_NAME}}'... 
            {{QUESTION}}...

            Replace FILE_LOCATION and FILE_NAME with the given below... then directly write the best answer you can imagine to the question... 
            now, for your response: directly response. no introduction. format each question and answer pair using the following syntax:
            ***** MY_QUESTION
            {{QUESTION}}
            ***** MY_ANSWER
            {{ANSWER}}
            """,

             ######################## QUESTION 4 ########################
            f"""
            For the source code below: You pick a relevant part of the code. And you create 3 questions of different parts of the code. The question always shows a part of the source code and has a question to it... 
            
            The questions must always begin with: For Project '{self.project_name}' considering file in path '{{FILE_LOCATION}}' with name '{{FILE_NAME}}' where below a part of it is displayed... 
            {{QUESTION}}...

            Replace FILE_LOCATION and FILE_NAME with the given below... then directly write the best answer you can imagine to the question... 
            now, for your response: directly response. no introduction. format each question and answer pair using the following syntax:
            ***** MY_QUESTION
            {{QUESTION}}
            ***** MY_ANSWER
            {{ANSWER}}
            """,

             ######################## QUESTION 5 ########################            
            """
           For the source code below we want to challenge for a senior developer of the project. The person claims to know each and every part of the code. Hence, as a question we take any method of the code below and summarize it up. The aim of the person is to exactly write the code based on our explanation here... In total we want 3 questions of that type...  For you to figure the question I pasted the code below... 
            The questions must always begin with: For Project '{self.project_name}' considering file in path '{{FILE_LOCATION}}' with name '{{FILE_NAME}}' we have the following question: 
            {{QUESTION}}...

            Replace FILE_LOCATION and FILE_NAME with the given below... then directly write the best answer you can imagine to the question... 
            now, for your response: directly response. no introduction. format each question and answer pair using the following syntax:
            ***** MY_QUESTION
            {{QUESTION}}
            ***** MY_ANSWER
            {{ANSWER}}
            """
        ]

    def extract_qa_from_llm_output(self, llm_output):
        qa_pairs = []
        question_pattern = re.compile(r'\*{5} MY_QUESTION\n(.*?)\n\*{5} MY_ANSWER', re.DOTALL)
        answer_pattern = re.compile(r'\*{5} MY_ANSWER\n(.*?)(?=\n\*{5} MY_QUESTION|\Z)', re.DOTALL)

        questions = question_pattern.findall(llm_output)
        answers = answer_pattern.findall(llm_output)

        for q, a in zip(questions, answers):
            qa_pairs.append({"instruction": q.strip(), "output": a.strip()})

        return qa_pairs

    def run(self):
        os.makedirs(os.path.dirname(self.OUTPUT_FILE), exist_ok=True)

        with open(self.FILE_PATH, "r", encoding="utf-8") as file, open(self.OUTPUT_FILE, "w", encoding="utf-8") as output:
            for line in file:
                data = json.loads(line)
                raw_code = data["text"]
                
                for i, intro in enumerate(self.intros):
                    question = f"{intro}\n\n{raw_code}"
                    start_time = time.time()
                    answer = self.gemma.inference(question)
                    generation_time = time.time() - start_time

                    print(f"Q: {question[:500]}...\n")
                    print(f"A: {answer}...\n")
                    print(f"Generation time: {generation_time:.2f} seconds\n")
                    print("-" * 80, "\n")

                    if answer is None:
                        print(f"Answer for question {i+1} was None (Null), skipping...  question= \n {question} ß")
                        continue

                    job = f"You are a developer of project '{self.project_name}'. It's your task to implement according to the specification below"

                    if i == 0:  # Question 1
                        output_entry = {
                            "instruction": job + answer,
                            "output": raw_code,
                            "questionType": i
                        }
                        output.write(json.dumps(output_entry) + "\n")
                        output.flush()
                    elif i in [1, 2, 3, 4]:  # Question 2,3, 4
                        qa_pairs = self.extract_qa_from_llm_output(answer)
                        for qa in qa_pairs:
                            qa["questionType"] = i
                            output.write(json.dumps(qa) + "\n")
                        output.flush()

    def split_alpaca_file(self):
        os.makedirs(self.OUTPUT_DIR, exist_ok=True)

        with open(self.OUTPUT_FILE, "r", encoding="utf-8") as alpaca_file:
            count = 1
            for line in alpaca_file:
                entry = json.loads(line)
                instruction = entry["instruction"]
                output_code = entry["output"]
                question_type = entry.get("questionType", "unknown")

                instruction_filename = os.path.join(self.OUTPUT_DIR, f"{count:06d}_instruction_Q{question_type}.md")
                output_filename = os.path.join(self.OUTPUT_DIR, f"{count:06d}_output_Q{question_type}.md")

                print(f"Write split file {instruction_filename} and {output_filename}.")

                with open(instruction_filename, "w", encoding="utf-8") as instruction_md, \
                     open(output_filename, "w", encoding="utf-8") as output_md:
                    instruction_md.write(instruction)
                    output_md.write(output_code)

                count += 1

if __name__ == "__main__":
    creator = CreateJSON_QA(project_name="Warmduscher")
    creator.run()
    creator.split_alpaca_file()