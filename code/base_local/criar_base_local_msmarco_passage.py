"""
A ser construído, se necessário
"""
import gzip




for i, line in enumerate(gzip.open('temp\collection.tar.gz', mode='rt')):
    fields = line.strip().split()
    if i > 10: break
    pid = fields[0]
    text = ' '.join(fields[1:])
    print(pid, text)

data_json = []
for i, line in enumerate(gzip.open('collection.tar.gz', mode='rt')):
    fields = line.strip().split()
    if i == 0: # pula primeiro registro
      pid = 0
      text = 'The presence of communication amid scientific minds was equally important to the success of the Manhattan Project as scientific intellect was. The only cloud hanging over the impressive achievement of the atomic researchers and engineers is what their success truly meant; hundreds of thousands of innocent lives obliterated.'
    else:
      pid = fields[0]
      text = ' '.join(fields[1:])
    json_docto = {
        'text': text,
        'id':pid,
        'meta': {
            'source': 'msmarco-passage'
        }
    }
    data_json.append(json_docto)
    if i <= 4:
        print(pid, 'text', text)

