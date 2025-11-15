from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

def main():
    loader = TextLoader("speech.txt")
    documents = loader.load()

    splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    chunks = splitter.split_documents(documents)
    print(f"Loaded {len(chunks)} chunks.")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma.from_documents(chunks, embeddings)
    retriever = db.as_retriever()

    llm = Ollama(model="mistral")

    rag_chain = (
        RunnableParallel({"context": retriever, "question": RunnablePassthrough()})
        | (lambda x: f"Context:\n{x['context']}\n\nQuestion:\n{x['question']}")
        | llm
        | StrOutputParser()
    )

    print("System is ready. Ask a question about the speech.\n")

    while True:
        q = input("Query (or 'exit'): ")
        if q.lower() == "exit":
            break

        ans = rag_chain.invoke(q)
        print("Answer:", ans)
        print("-" * 60)

if __name__ == "__main__":
    main()
