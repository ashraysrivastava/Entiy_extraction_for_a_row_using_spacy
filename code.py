import pandas as pd
import spacy
a=[]
b=[]
def entity_extraction(text):#function for entity extraction
    nlp=spacy.load('en_core_web_sm')
    doc=nlp(text)
    x=''
    y=''
    
    for entity in doc.ents:
        if entity.text != '\n':
            x = "".join(entity.text)
            y="".join(spacy.explain(entity.label_))
            a.append(x)
            b.append(y)
    return (x+"---> "+y)
    

df=pd.read_csv('D://ZZ Ashray(698306)//remedytickets//outlook1.csv')
data=df.SRV_MGT_SRV_RQST_DESC

for line in data:
    print(entity_extraction(line))
    
# df1 = pd.DataFrame(a,b)
# df1.to_csv('list.csv', index=False)
    
