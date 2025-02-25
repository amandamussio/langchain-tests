from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
load_dotenv()

# Load the PDF file
loader = PyPDFLoader("term.pdf")

# Split the PDF file into chunks
text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200)
chunks = loader.load_and_split(text_splitter)
# chunks = text_splitter.split_documents(loader.load())
print(chunks)

for chunk in chunks:
    print(chunk.page_content)
    print("-"*100)
