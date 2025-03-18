import time
import json
import os
# from gemma3_inference import GemmaInference
from gemma3_inference_ollama import GemmaInferenceOllama  # Assuming the previous class is in gemma_inference.py

class CreateJSON_QA:
    FILE_PATH = "learning_json/pretrain_dataset.jsonl"
    OUTPUT_FILE = "learning_json/alpaca.jsonl"
    OUTPUT_DIR = "learning_json/alpaca_split"  # Subdirectory for split files

    def __init__(self, project_name='Warmduscher'):
        self.project_name = project_name
        self.gemma = GemmaInferenceOllama()

        self.intros = [
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
            """
        ]

    def run(self):
        os.makedirs(os.path.dirname(self.OUTPUT_FILE), exist_ok=True) #added to assure directory exists.

        with open(self.FILE_PATH, "r", encoding="utf-8") as file, open(self.OUTPUT_FILE, "w", encoding="utf-8") as output:
            for line in file:
                data = json.loads(line)
                raw_code = data["text"]
                
                for intro in self.intros:
                    question = f"{intro}\n\n{raw_code}"
                    start_time = time.time()
                    answer = self.gemma.inference(question)
                    generation_time = time.time() - start_time
                    
                    print(f"Q: {question[:500]}...\n")
                    print(f"A: {answer}...\n")
                    print(f"Generation time: {generation_time:.2f} seconds\n")
                    print("-" * 80, "\n")
                    
                    if answer is None:
                        print("Answer for question was None (Null), skipping...  question= \n {question} ß")
                        continue

                    job = f"You are a developer of project '{self.project_name}'. It's your task to implement according to the specification below"

                    output_entry = {
                        "instruction": job + answer,
                        "output": raw_code
                    }

                    output.write(json.dumps(output_entry) + "\n")
                    output.flush()

    def split_alpaca_file(self):
        os.makedirs(self.OUTPUT_DIR, exist_ok=True)  # Create split directory if it doesn't exist

        with open(self.OUTPUT_FILE, "r", encoding="utf-8") as alpaca_file:
            count = 1
            for line in alpaca_file:
                entry = json.loads(line)
                instruction = entry["instruction"]
                output_code = entry["output"]

                instruction_filename = os.path.join(self.OUTPUT_DIR, f"{count:06d}_instruction.md")
                output_filename = os.path.join(self.OUTPUT_DIR, f"{count:06d}_output.md")

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