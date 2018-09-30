import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import matplotlib.pyplot as plt

#import review file and append name of teacher

l=raw_input("Enter name of teacher:")

#load file name to testdata

f=open('testdata1','r')
sentence=f.read()
sid=SIA()
ss=sid.polarity_scores(sentence)


#piechart

if(sid.polarity_scores(sentence)["neg"] <0): #if neg convert to positive
	x=-(sid.polarity_scores(sentence)["neg"])

else:
	x=sid.polarity_scores(sentence)["neg"]

y=sid.polarity_scores(sentence)["pos"]

#z=sid.polarity_scores(sentence)["compound"]

j=sid.polarity_scores(sentence)["neu"]
labels=['NEGATIVE','POSITIVE','NEUTRAL']
sizes=[x,y,j]
explode=[0.1,0.1,0.1]
colors=['#ee1111', '#00a300', '#ffc40d']
fig1, ax1=plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow= True,
startangle=90)
ax1.axis('equal')
plt.tight_layout()
 

#to save as png and plot

plt.savefig(l+'.png', bbox_inches='tight')

# to display plot

plt.show()

#print result
z=str(ss)
print(z)

#write result to txt

g=open("result.txt", "a")
g.write("\m")
g.write(l)
g.write(z)
g.close()
