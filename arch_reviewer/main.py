import sys
import os
from openai import OpenAI
from arch_reviewer import img_encoder

api_key = os.getenv("OPEN_API_TOKEN")
client = OpenAI(api_key=api_key)

image_path = sys.argv[1]
base64_image = img_encoder.encode_image(image_path)


def format_and_output():
    output_path = image_path.rsplit('.', 1)[0] + "_security_report.md"
    report_content = response.choices[0].message.content

    start_marker = "```markdown"
    end_markers = "```"
    start_pos = report_content.index(start_marker) + len(start_marker)
    end_pos = report_content.index(end_markers, start_pos)
    markdown_table = report_content[start_pos:end_pos]

    with open(output_path, 'w') as file:
        file.write(markdown_table)


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

format_and_output()
