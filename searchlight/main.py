import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

prompt = '''
    Identify any OWASP concern in this terraform:

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


def llm_response(prompt):
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{'role':'user','content':prompt}],
        temperature=0
    )

    return response.choices[0].message.content


response = llm_response(prompt)
print(response)
