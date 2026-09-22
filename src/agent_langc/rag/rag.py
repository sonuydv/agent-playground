from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

path = "data/documents/company.txt"

# 1: Load the documents
documents = TextLoader(path).load()


# 2: Split the documents into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200, # token size of each chunks
    chunk_overlap=10, # overlapping lines
)
chunks = splitter.split_documents(documents)


# 3: Generate the embeddings for the chunks
embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
# for manual embeddings , we get generate the embeddings then store in our store
#embeddings = embedder.embed_documents([chunk.page_content for chunk in chunks])

# 4: Now store the embeddings in vector database store , indexing the embeddings
vector_store = FAISS.from_documents(chunks,embedder)



# 5 : Create retriever to retrieve the embeddings
retriever = vector_store.as_retriever()
# Specify top k
retriever.search_kwargs = {"k":1}


# Helper function to format the returned result from retriever
def format_docs(docs):
    return "\n\n".join(
        doc.page_content
        for doc in docs
    )