#!/usr/bin/env python
import sys
import math
import numpy as np
from sklearn.neighbors import KNeighborsRegressor


# This function creates a dictionary with the reference sequence identifiers as keys and a list as values, being this list --> [tc score, [list of the pairwise identity]]
def hd(listid, sp, identity):
	d={}
	for i in listid:
		# Now s is a float instead of a list
		s=float(sp.get(i,0))
		pid=[]
		for j in listid:
			pid.append((100.0-identity.get((i,j),100)))
		d[i]=[s,pid]
	return d


def mach_learn(listid,d, k):
	predictions={}
	# for i in range(len(listid)):
	# 	#forloop for the reference
	for j in range(len(listid)):
		#forloop for the target
		# if i !=j:
			# R=listid[i]#reference
		T=listid[j]#target
		# rsp=d[T][0]#real sp of the target with respect to the reference
		X=[]
		Y=[]
		X_test=[]
		# psop=[]				
		for z in range(len(listid)):
			# if z!=i and z!=j:
			if z!=j:
				#for loop to define the space
				sop=d[listid[z]][0]#the sp score of the coord z with respect to the reference
				listina=[]
				x_test=[]
				for c in range(len(listid)):
					#for loop to fill the training vectors
					# if c!=i and c!=j:
					if c!=j:
						listina.append(d[listid[z]][1][c])
						x_test.append(float(d[T][1][c]))
				X.append(listina) # X will be the coordinates in the n-dimensional space
				Y.append(sop)	  # Y will be the tc/sop score asociated to each point
		X_test.append(x_test)
		X=np.asarray(X, dtype='float')
		Y=np.asarray(Y)
		#X_test=np.asarray(X_test)
		neigh=KNeighborsRegressor(n_neighbors=int(k), weights='distance')
		neigh.fit(X,Y)#training using R as reference to compute the sp and T to be predicted
		pred=neigh.predict(X_test)#prediction of T with R as reference
		dist=neigh.kneighbors(X_test)
		dis=dist[0][0][0]
		# num=dist[1][0][0]
		#dis=sum(dist[0][0])/float(k)
		#predictions[(R,T)]=[float(pred), float(dis), int(num)]
		# predictions[(R,T)]=[float(pred), float(dis)]
		predictions[T]=[float(pred), float(dis)]
	return predictions

def final_measure(sp, predictions, listid):
	delta=0.0
	for i in listid:
		# for j in listid:
			# if i!=j:
		delta=delta+(sp[i]-predictions[i][0])**2
	N=len(sp.keys())
	#print N
	return math.sqrt(delta)/N


def outputfilewriting(outfile,sp, predictions, listid):
	out=open(outfile, 'w+')
	# out.write('#reference'+'\t'+'target'+'\t'+'real sp'+'\t'+'predicted sp'+'\t'+'|delta|'+'\n')
	out.write('#target'+'\t'+'real_tc'+'\t'+'predicted_tc'+'\t'+"distance_cl_kneighbor"+"\t"+'|delta|'+'\n')
	for i in listid:
		# for j in listid:
		# 	if i!=j:
		D= abs(sp[i]-predictions[i][0])
		out.write(str(i)+'\t'+str(sp[i])+'\t'+str(predictions[i][0])+'\t'+str(predictions[i][1])+'\t'+str(D)+'\n')
		#out.write(str(i)+'\t'+str(j)+'\t'+str(sp[(i,j)])+'\t'+str(predictions[(i,j)][0])+'\t'+str(predictions[(i,j)][1])+'\t'+str(predictions[(i,j)][2])+'\t'+str(D)+'\n')
	fin=final_measure(sp, predictions, listid)
	out.write('\n'+'\n'+'\n'+'FINAL MEASURE: SQRT(DELTA^2)/#MODELS OBTAINED='+'\t'+str(fin)+'\n')
	out.close()



if __name__=='__main__':
	lid=sys.argv[1]
	spfile=sys.argv[2]
	pidfile=sys.argv[3]
	k=sys.argv[4]
	outfile=sys.argv[5]

	#wrong_seqs={"1bd7a","1bqqm"} # Misleading structures (want to remove them)
	wrong_seqs={}

##	ONLY FOR LOCAL!!!!!!!!!!!  ###########
	# cwd=os.getcwd()
	# os.chdir(cwd+"/scripts")
##########################################
	listid=[]
	sp={}
	identity={}
	for i in open(lid):
		i=i.rstrip()
		if str(i[1:]) not in wrong_seqs:
			listid.append(str(i[1:]))
	for i in open(spfile):
		i=i.rstrip().split('\t')
		# sp[(str(i[0]),str(i[1]))]=sp[(str(i[1]),str(i[0]))]=float(i[2])          
# -----------------------------------------------------------------------------------------------
		sp[str(i[0])]=float(i[1])
# -----------------------------------------------------------------------------------------------
	for i in open(pidfile):
		i=i.rstrip().split(' ')
		identity[(str(i[0]),str(i[1]))]=identity[(str(i[1]),str(i[0]))]=float(i[2])
	d=hd(listid, sp, identity)
	#print d
	predictions=mach_learn(listid,d, k)
	#print predictions
	#print final_measure(sp, predictions, listid)
	outputfilewriting(outfile,sp, predictions, listid)
