import json
from nltk import agreement

def read_json(fn):
    lines=[]
    fh = open(fn)
    for line in fh:
        lines.append(json.loads(line))
        #break
    fh.close()
    return lines

def get_labels(json):
    labels_=[]
    spans_={}
    users_=[]
    for i in range(len(json)):
        for l in json[i]:
            if ("annotations" in list(json[i].keys())):
                text=json[i]["text"]
                labels=json[i]["annotations"]
                for label in labels:
                    user_=label["user"]
                    type_=str(label["label"])
                    token_=str(i)+"_"+str(label["start_offset"])+"_"+str(label["end_offset"])
                    if user_ not in users_:
                        users_.append(user_)
                    if token_ not in spans_.keys():
                        spans_[token_]={}
                    spans_[token_][user_]=type_
    for key, value in spans_.items():
        for u in users_:
            if (u in spans_[key].keys() ):
                labels_.append([str(u),key, spans_[key][u] ])
            else:
                labels_.append([str(u),key, "-1"])
    if len(labels_)==0:
        print ("no labels found")
    return labels_




def calc(file):
    json = read_json(file)
    d=get_labels(json)

    ratingtask = agreement.AnnotationTask(data=d)
    print("kappa " +str(ratingtask.kappa()))
    print("fleiss " + str(ratingtask.multi_kappa()))
    print("alpha " +str(ratingtask.alpha()))
    print("scotts " + str(ratingtask.pi()))
