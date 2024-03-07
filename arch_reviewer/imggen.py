import os
from openai import OpenAI

api_key = os.getenv("OPEN_API_TOKEN")
client = OpenAI(api_key=api_key)

response = client.images.generate(
    model="dall-e-3",
    prompt="Draw an architectural diagram with the following properties and incorporate threat mitigation strategies"
           "The diagram illustrates an event-driven data processing architecture using AWS services. The components "
           "involved in the process are:"
           "1. Data Source: An Amazon S3 bucket that contains data files in JSON format."
           "2. Amazon Eventbridge Rule: An event routing service that directs the data processing workflow."
           "3. Amazon SNS (Simple Notification Service): A messaging service for managing and delivering messages or "
           "notifications."
           "4. Amazon SQS (Simple Queue Service): A message queuing service that decouples and scales microservices, "
           "distributed systems, and serverless applications."
           "5. AWS Lambda: A serverless computing service that runs code in response to events and automatically "
           "manages the underlying compute resources."
           "6. Data Target: An Amazon S3 bucket where the processed data is stored in Parquet format.",
    n=1,
    size="1024x1024"
)

print(response.data[0].url)
