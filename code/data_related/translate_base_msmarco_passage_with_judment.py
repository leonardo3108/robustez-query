"""
Objetivo: criar base local msmarco-passage com julgamentos
"""
from tqdm import tqdm
from googletrans import Translator

translator = Translator()
texto_origem = 'eu te amo'
lingua_origem = 'en'
lingua_destino = 'pt'

w = open('data/tab_passage_with_judment.csv', 'w',  encoding="utf8")
w.write('cod_docto,language,text\n')
for ndx, passage in tqdm(enumerate(open('data/passages-with-judment.txt', encoding="utf8")), 'translation progress bar'):
    fields = passage.strip().split()
    docid = fields[0]
    text = ' '.join(fields[1:])
    translated_text = translator.translate(text,dest=lingua_destino,src=lingua_origem).text
    w.write(f'{docid},pt,{translated_text}\n')
    w.write(f'{docid},en,{text}\n')
    # print(f"\ndocid: {docid}")
    # print(f"\ntext: {text}")
    # print(f"\ntranslated_text: {translated_text.text}")
    if len(text)>(len(translated_text)+30):
        print(f'Maybe an error: more than 30 chars dif length docid: {docid} {len(text)} > {len(translated_text)} + 30')
w.close


exit()
data_carga_json = [
    {
        'content': passage[1],
        'id': passage[0],
        'meta': {
            'source': 'msmarco-passage-with-judment'
        }
    } for passage in passages
]

print(f"\nlen(data_carga_json) {len(data_carga_json)}")
print(f"Data_carga_json[0] {data_carga_json[0]}")

doc_store = ElasticsearchDocumentStore(
    host='localhost',
    username='', password='',
    index='robustez-query',
    similarity='dot_product'
)
doc_store.write_documents(data_carga_json)
