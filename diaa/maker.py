import json
from nltk import agreement
from urllib import request, parse
import json,urllib.request

def get_docs_from_json(fn):
    lines=[]
    fh = open(fn)
    for line in fh:
        lines.append(json.loads(line))
        #break
    fh.close()
    return lines


def get_docs_from_doccano(url_,project_):

    ##getting token
    #http post http://tc.qu.tu-berlin.de/v1/auth-token username=vinicius password=nopassword

    auth_url=url_+"/v1/auth-token"
    #print (auth_url)
    data = {'username': 'vinicius', 'password': 'nopassword'}
    req = request.Request(auth_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(data)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    result = request.urlopen(req, jsondataasbytes).read()
    token=json.loads(result)["token"]
    header = {'Content-Type': 'application/json; charset=utf-8','Authorization': 'Token '+str(token)}
    #print (token)

    #http://tc.qu.tu-berlin.de/v1/projects/4/docs/download?q=json

    data_url=url_+"/v1/projects/"+str(project_)+"/docs/download?q=json&format=json"
    #print (data_url)
    req =  request.Request(data_url, headers=header)
    webURL = request.urlopen(req)

    data=[]
    for line in webURL:
        data.append(json.loads(line.decode("utf-8")))

    return data


def get_labels(docs):
    labels_=[]
    spans_={}
    users_=[]
    for i in range(len(docs)):
        doc=docs[i]
        if ("annotations" in list(doc.keys())):
            text=doc["text"]
            labels=doc["annotations"]
            for label in labels:
                user_=label["user"]
                type_=str(label["label"])
                token_=str(i)+"_"+str(label["start_offset"])+"_"+str(label["end_offset"])
                if user_ not in users_:
                    users_.append(user_)
                if token_ not in spans_.keys():
                    spans_[token_]={}
                spans_[token_][user_]=type_
        else:
            print("did not find annotations in record "+str(i))

    for key, value in spans_.items():
        for u in users_:
            if (u in spans_[key].keys() ):
                labels_.append((str(u),key, int(spans_[key][u]) ))
            else:
                labels_.append((str(u),key, 0))
    if len(labels_)==0:
        print ("no labels found")

    print (labels_)
    return labels_




def calc(labels):
    metrics={}
    ratingtask = agreement.AnnotationTask(data=labels)
    metrics["kappa"]=ratingtask.kappa()
    metrics["fleiss"]=ratingtask.multi_kappa()
    metrics["alpha"]=ratingtask.alpha()
    metrics["scotts"]=ratingtask.pi()
    return metrics

