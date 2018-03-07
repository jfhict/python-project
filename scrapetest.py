from urllib.request import urlopen
from bs4 import BeautifulSoup

#html=urlopen("http://www.cjstp.cn/cjstp/ch/reader/issue_browser.aspx")
#bsObj=BeautifulSoup(html,"lxml")
issuehtmllist=[]
namefindresult=[]
#for link in bsObj.findAll("a"):
#    if 'href' in link.attrs:
#        print(link.attrs['href'])

#打开期刊浏览中的每一期期刊。
for i in range(1990,1992):    
    for j in range(1,4):        
        issuehtml=urlopen("http://www.cjstp.cn/cjstp/ch/reader/issue_list.aspx?year_id="+str(i)+"&quarter_id="+str(j))
        issuebsObj=BeautifulSoup(issuehtml,"lxml")        
        #for issuelink in issuebsObj.findAll("b"):
            #if 'href' in issuelink.attrs:
                #print(issuelink.attrs['href'])                
        issuehtmllist.append(issuebsObj)
        j+=1
    i+=1

#print(issuehtmllist[0].prettify())
#print(issuehtmllist[0].findAll("table",id="table24"))
#过滤打开的每一期期刊数据，保留文章题目。
namefindresult=issuehtmllist[1].findAll("table",id="table24")
for u1 in namefindresult:
    print(u1.findAll("b"))








