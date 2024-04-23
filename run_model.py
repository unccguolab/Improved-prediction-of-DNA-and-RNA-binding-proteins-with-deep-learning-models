import re,os,sys
import numpy as np
import tensorflow as tf

path=sys.argv[1]
used_models=sys.argv[2]

##Sigmoid function
def sigmoid(x):
    return(1.0/(1+np.exp(-x)))

##Reading function
def reading(path):
    max_length=1500
    total_x={}
    path_list=os.listdir(path)
    for filename in path_list:
        if os.path.splitext(filename)[1]=='.pssm':
            lines=[]
            fp=open(path+filename,'r')
            for i in fp:
                i=re.sub('\n','',i)
                lines.append(i)
            fp.close()
            del lines[0:3]
            each=[]
            for x in lines:
                y=x.split()
                if len(y)==44:
                    tem=[]
                    for a in y[2:22]:
                        tem.append(sigmoid(int(a)))
                    each.append(tem)
            original_length=len(each)
            if len(each)<=max_length:
                pad=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
                for x in range(max_length-len(each)):
                    each.append(pad)
                each=list(map(list,zip(*each)))
                total_x[filename[:-8]]=each
    return(total_x)

x_test=reading(path)

##Prediction
fp=open('prediction.txt','w')
mymodel=tf.keras.models.load_model(used_models)
for x in x_test.keys():
    value=x_test[x]
    if used_models=='non-NABP_NABP.h5' or used_models=='DBP-RBP.h5' or used_models=='DBP-RBP-without-SSB.h5':
        predict=(mymodel.predict([value])>0.5).astype("int32").tolist()[0][0]
        if used_models=='non-NABP_NABP.h5':
            if predict==1:
                types='NABP'
            else:
                types='Non-NABP'
        else:
            if predict==1:
                types='DBP'
            else:
                types='RBP'
    else:
        predict=np.argmax(mymodel.predict([value]))
        if predict==0:
            types='RBP'
        elif predict==1:
            types='DBP'
        else:
            types='non-NABP'
    fp.write(x+'\t'+types+'\n')
fp.close()
