from langchain_community.document_loaders import OnlinePDFLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.retrievers import BM25Retriever

def retriever():

    loader1 = PyPDFLoader(file_path='files/Cartilha_de_Estágio')

    data = loader1.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=100, separators=["\n", " ", ""]
    )
    texts = text_splitter.split_documents(data)

    retriever = BM25Retriever.from_documents(texts)
    return retriever
