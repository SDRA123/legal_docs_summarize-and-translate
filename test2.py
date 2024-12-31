from groq import Groq
import re


# Now `lines` contains each line of the file as an element

# Open the file in read mode
with open("summary.txt", "r") as file:
    content = file.read()  # Reads the entire content of the file into a string




client = Groq(api_key="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")
completion = client.chat.completions.create(
    model="llama-3.1-70b-versatile",
    messages=[


        {
    "role": "user",
    "content": f"Combine the following text{content}, summarize it, and include only the key facts and clauses. 'Overview' which should be in points of key facts one word or one line answer, 'Clauses' includes important clauses also each clause have heading per context of the clause and each clause should be consice paragraph or line, and 'Summary'. Focus on the most important and crucial clauses (top 10). Keep the Overview comprehensive but concise. The Summary should be in 3-4 points."
}

        
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

with open('summary_formated.txt', "w") as file:
    file.write(pdf_summary_text)