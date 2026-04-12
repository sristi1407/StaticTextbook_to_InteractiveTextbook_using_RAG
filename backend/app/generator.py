from openai import OpenAI

client = OpenAI()

def generate_answer(query, retrieved_docs):
    context_parts = []
    citations = []

    for doc in retrieved_docs:
        page = doc.metadata.get("page", "Unknown")
        content = doc.page_content
        context_parts.append(f"[Page {page}] {content}")
        citations.append(page)

    context = "\n\n".join(context_parts)

    prompt = f"""
You are an educational assistant.

Answer the user's question using ONLY the textbook context provided below.
Do not make up information.
If the answer is not in the context, say that the information was not found in the uploaded textbook.
At the end of the answer, include the relevant page number citations.

Context:
{context}

Question:
{query}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response.choices[0].message.content

    return {
        "answer": answer,
        "citations": sorted(list(set(citations)))
    }