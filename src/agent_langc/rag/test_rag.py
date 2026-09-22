from agent_langc.rag.rag import retriever


def main():
   results = retriever.invoke("how many vacations days do employees get?")
   for doc in results:
       print(doc.page_content)
       print(doc.metadata)

if __name__ == "__main__":
    main()
