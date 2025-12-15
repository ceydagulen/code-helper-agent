from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from prompts import SYSTEM_PROMPT


def create_agent(vector_store):
    llm = ChatOpenAI(
        model="gpt-4o-mini",   # CLI için daha hızlı/ucuz
        temperature=0
    )

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 4}
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", """
Soru:
{question}

Bağlam:
{context}
""")
    ])

    chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain
