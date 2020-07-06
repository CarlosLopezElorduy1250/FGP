#!/usr/bin/env python
import sys, os
from scipy.stats.stats import pearsonr
#from scipy.stats.stats import spearmanr
import math

def bin_corr(sp1, sp2, pid, outfile):
	out= open(outfile, 'w')
	for i in range(0,100,1):
		u=i+1
		c=0
		L1=[]
		L2=[]
		for p in range(len(pid)):
			if pid[p]>=i and pid[p]<u:
				L1.append(sp1[p])
				L2.append(sp2[p])
				c=c+1
		ro=pearsonr(L1,L2)
		#ro1=spearmanr(L1,L2)
		out.write(str(i)+'-'+str(u)+' '+str(ro[0])+' '+str(c)+'\n')
	out.close()
		
def comun_corr(sp1,sp2,pid, outfile):
	out= open(outfile, 'w')
	for i in range(int(math.floor(min(pid))),int(math.floor(max(pid))),1):
		c=0
		L1=[]
		L2=[]
		for p in range(len(pid)):
			if pid[p]>=i:
				L1.append(sp1[p])
				L2.append(sp2[p])
				c=c+1
		ro=pearsonr(L1,L2)
		out.write(str(i)+' '+str(ro[0])+' '+str(c)+'\n')
	out.close()
		
def both(sp1,sp2,pid,outfile):
	out= open(outfile, 'w')
	# out.write("Threshold_dist"+' '+"Cumulative"+' '+"Sample_c"+' '+"Bin"+' '+"Sample_b"+"\n")
	out.write("Threshold_dist"+' '+"Cumulative"+' '+"Sample_c"+"\n")
	for i in range(int(math.floor(min(pid))),int(math.floor(max(pid))),1): # From the smallest distance to c_neighbour to the highest
		u=i+1
		b=0
		c=0
		B1=[]
		B2=[]
		C1=[]
		C2=[]
		for p in range(len(pid)):
			if pid[p]<=i: #######################################
				C1.append(sp1[p])
				C2.append(sp2[p])
				c=c+1
			if  pid[p]>=i and pid[p]<u:
				B1.append(sp1[p])
				B2.append(sp2[p])
				b=b+1
		if len(C1)>=1:
			# bro=pearsonr(B1,B2)
			cro=pearsonr(C1,C2)
			# if str(bro[0])!="nan" and str(cro[0])!="nan":
			# 	towrite=str(i)+' '+str(cro[0])+' '+str(c)+' '+str(bro[0])+' '+str(b)+'\n'
			if str(cro[0])=="nan":
				towrite=str(i)+' NA '+str(c)+'\n'
			else:
				towrite=str(i)+' '+str(cro[0])+' '+str(c)+'\n'

		# CHANGE SO THAT IT PRINTS "NA" WHEN EITHER C1 OR B1 ARE LOWER LENGTH THAN 2 (print just the corresponding column).
		# if len(C1)>=2 and len(B1)>=2:
		# 	bro=pearsonr(B1,B2)
		# 	cro=pearsonr(C1,C2)
		# 	if str(bro[0])!="nan" and str(cro[0])!="nan":
		# 		towrite=str(i)+' '+str(cro[0])+' '+str(c)+' '+str(bro[0])+' '+str(b)+'\n'
		# 	elif str(cro[0])!="nan":
		# 		towrite=str(i)+' NA '+str(c)+' '+str(bro[0])+' '+str(b)+'\n'
		# 	else:
		# 		towrite=str(i)+' '+str(cro[0])+' '+str(c)+' NA '+str(b)+'\n'
		
				
				
#		elif len(C1)<2:
#			bro=pearsonr(B1,B2)
#			if str(bro[0]=="nan"):
#				towrite=str(i)+' NA '+str(c)+' NA '+str(b)+'\n'
#			else:
#				towrite=str(i)+' NA '+str(c)+' '+str(bro[0])+' '+str(b)+'\n'
#		else:
#			cro=pearsonr(C1,C2)
#			if str(cro[0]=="nan"):
#				towrite=str(i)+' NA '+str(c)+' NA '+str(b)+'\n'
#			else:
#				towrite=str(i)+' '+str(cro[0])+' '+str(c)+' NA '+str(b)+'\n'
			out.write(towrite)
	out.close()
		
if __name__=='__main__':
	# cwd=os.getcwd()
	# os.chdir(cwd+"/scripts")
	f=sys.argv[1]
	outfile=sys.argv[2]
	sp1=[]
	sp2=[]
	pid=[]
	for line in open(f):
		line=line.rstrip().split('\t')

		if line[0][0]!="#":		
			sp1.append(float(line[1]))
			sp2.append(float(line[2]))
			pid.append(float(line[3]))
               
	#bin_corr(sp1, sp2, pid, outfile)
	#comun_corr(sp1,sp2,pid, outfile)
	both(sp1,sp2,pid, outfile)	

