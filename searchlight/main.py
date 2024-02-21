import os
import google.generativeai as genai
import tf_import_gen
import tf_config_gen

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Set up the model
generation_config = {
    "temperature": 0,
    "top_p": 0,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

import_blocks_file = tf_import_gen.import_gen("sample/input.json")
tf_generated_config = tf_config_gen.config_gen(import_blocks_file)
with open(tf_generated_config, 'r') as file:
    # Read the content of the file into a string
    file_content = file.read()


prompt = f'''
Identify OWASP concerns in this terraform and generate a new Terraform code that addresses the concerns:

{file_content}
'''

response = model.generate_content(prompt)
print(response.text)
