import os
from llama_index import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers import PDFReader


def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )

    return index


pdf_path = os.path.join("data", "Seoul.pdf")
pdf1_path = os.path.join("data", "japnese and korean companies in india.pdf")
seoul_pdf = PDFReader().load_data(file=pdf_path)
company_pdf = PDFReader().load_data(file=pdf1_path)
seoul_index = get_index(seoul_pdf, "seoul")
company_index = get_index(company_pdf, "company")
seoul_engine = seoul_index.as_query_engine()
company_engine = company_index.as_query_engine()