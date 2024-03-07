import os
import base64
from openai import OpenAI

api_key = os.getenv("OPEN_API_TOKEN")
client = OpenAI(api_key=api_key)


# Function to encode the image
def encode_image(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


image_path = "data/sample_diagram.png"
base64_image = encode_image(image_path)

response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text",
                 "text": "Consider the architecture diagram in this picture and generate a threat modeling report as "
                         "a markdown table with 'Component','Threat','Likelihood','Mitigation Strategy' columns"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                },
            ],
        }
    ],
    max_tokens=1000
)

output_path = image_path.rsplit('.', 1)[0] + "_security_report.md"
report_content=response.choices[0].message.content

start_marker = "```markdown"
end_markers = "```"
start_pos = report_content.index(start_marker) + len(start_marker)
end_pos = report_content.index(end_markers, start_pos)
markdown_table = report_content[start_pos:end_pos]

with open(output_path, 'w') as file:
    file.write(markdown_table)
