from groq import Groq
import re


# Open the file in read mode
with open("summary_formated.txt", "r") as file:
    content = file.read()  # Reads the entire content of the file into a string




client = Groq(api_key="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")
completion = client.chat.completions.create(
    model="llama-3.1-70b-versatile",
    messages=[


        {
            "role": "user",
            "content": f'''You’re a professional translator with a strong background in legal terminology and a deep understanding of both English and Urdu. Your expertise allows you to accurately convey the nuances of legal language while ensuring that the translated text remains clear and accessible.

Your task is to translate the provided summary into Urdu should not include unnessary words or commas or other this should be pure urdu  .

Please ensure that you use correct legal terms and maintain a glossary in Urdu for any specific legal terminology used in the summary dont use hindi words all headings should be maintained.

Here’s the summary you need to translate:{content} '''
        },
       
        
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)
pdf_summary_text=""
for chunk in completion:
        pdf_summary_text += chunk.choices[0].delta.content or ""  # Append streamed content

with open('summary_translated.txt', "w", encoding="utf-8") as file:
    file.write(pdf_summary_text)
