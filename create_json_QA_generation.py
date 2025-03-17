import time
import json
import os
from gemma3_inference import GemmaInference

class CreateJSON_QA:
    def __init__(self, 
                 file_path="learning_json/pretrain_dataset.jsonl", 
                 output_file="learning_json/alpaca.jsonl", 
                 project_name='Warmduscher'
                 ):
        self.file_path = file_path
        self.output_file = output_file
        self.project_name = project_name  # Store project name
        self.gemma = GemmaInference()

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
            - Classes
            - Functions
            - Modules
            - Important logic flows

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
        with open(self.file_path, "r", encoding="utf-8") as file, open(self.output_file, "w", encoding="utf-8") as output:
            for line in file:
                data = json.loads(line)
                raw_code = data["text"]  # Extract raw source code
                
                responses = []
                for intro in self.intros:
                    question = f"{intro}\n\n{raw_code}"
                    start_time = time.time()
                    answer = self.gemma.inference(question)
                    generation_time = time.time() - start_time
                    
                    # print(f"Intro: {intro[:100]}...\n")  # Print only first 100 chars for readability
                    print(f"Q: {question[:500]}...\n")  # Print only first 500 chars for readability
                    print(f"A: {answer}...\n")  
                    print(f"Generation time: {generation_time:.2f} seconds\n")
                    print("-" * 80, "\n")
                    
                    job = "You are a developer of project '{self.project_name}'. It's your task to implement according to the specification below"

                    output_entry = {
                        "instruction": job + answer,  # The LLM's response as the instruction
                        "output": raw_code  # The raw source code as the answer
                    }
                    output.write(json.dumps(output_entry) + "\n")
                    output.flush()
                
                # Save output in Alpaca format
                output_entry = {
                    "instruction": raw_code,
                    "responses": responses
                }
                output.write(json.dumps(output_entry) + "\n")
                output.flush()

if __name__ == "__main__":
    creator = CreateJSON_QA(project_name="Warmduscher")
    creator.run()
