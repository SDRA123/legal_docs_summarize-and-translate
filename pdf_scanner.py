import os
import PyPDF2
from groq import Groq
from multiprocessing import Pool, Manager

# Function to process a single page
def process_page(args):
    page_num, page_text, api_key = args
    
    client = Groq(api_key=api_key)
    pdf_summary_text = ""

    try:
        # Send text to Llama model for summarization
        completion = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": f"Summarize this: {page_text} and give summary in this format format(clauses: should be highly accurate if any not more than 3 - Overview: which includes key facts and answers of key facts in one word or line - summary short 50-word summary of entirety)"
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        # Collect streamed chunks
        for chunk in completion:
            pdf_summary_text += chunk.choices[0].delta.content or ""

    except Exception as e:
        pdf_summary_text = f"Error processing page {page_num}: {str(e)}"

    return page_num, pdf_summary_text

# Main function
def main():
    # Directory and file path
    pdf_dir = r"E:\fpy\oldcodes\old code"
    pdf_file_name = "A_RES_45_116_ModelTreatyExtradition.pdf"
    pdf_file_path = os.path.join(pdf_dir, pdf_file_name)

    # Open the PDF file
    pdf_file = open(pdf_file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Initialize the Groq client with the API key
    api_key = "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"

    # Prepare data for multiprocessing
    tasks = [(page_num, pdf_reader.pages[page_num].extract_text().lower(), api_key) for page_num in range(len(pdf_reader.pages))]

    # Use a multiprocessing Pool to process pages in parallel
    with Pool(processes=4) as pool:  # Adjust the number of processes based on your system
        results = pool.map(process_page, tasks)

    # Combine results and sort by page number
    results.sort(key=lambda x: x[0])
    pdf_summary_text = "\n".join([result[1] for result in results])

    # Save the summary to a new file
    summary_file_path = os.path.join(pdf_dir, "summary.txt")
    with open(summary_file_path, "w", encoding="utf-8") as file:
        file.write(pdf_summary_text)

    # Close the PDF file
    pdf_file.close()

    print(f"Summary saved to {summary_file_path}")

if __name__ == "__main__":
    main()
