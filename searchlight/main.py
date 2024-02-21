import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Set up the model
generation_config = {
    "temperature": 0,
    "top_p": 1,
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

prompt = '''
Identify OWASP concern in this terraform:

provider "aws" {
  region = "us-west-2"
}
                
resource "aws_msk_cluster" "example_cluster" {
  cluster_name = "example-msk-cluster"
  kafka_version = "2.8.0"
                
  number_of_broker_nodes = 3
                
  encryption_info {
    encryption_at_rest_kms_key_arn = "arn:aws:kms:us-west-2:123456789012:key/abcd1234-a123-456a-a12b-a123b4cd5678"
  }
                
  client_authentication {
    sasl {
      scram {
        enabled = true
      }
    }
  }
                
  logging_info {
    broker_logs {
      cloudwatch_logs {
        enabled = true
        log_group = "msk-logs"
      }
    }
  }
}
'''

response = model.generate_content(prompt)
print(response.text)
