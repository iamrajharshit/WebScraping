from bs4 import BeautifulSoup
import requests
import time
print("Put some skills u r not fimiliar with")
unskill=input('>')
print(f"Flitering out {unskill}")
def find_jobs():
    html_text= requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
    # print(html_text)
    soup = BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li',class_ = "clearfix job-bx wht-shd-bx")
    
    for index,job in enumerate(jobs):
        publish_date = job.find('span', class_="sim-posted").span.text
        if "few" in publish_date:

            company_name = job.find("h3",class_="joblist-comp-name").text.replace(' ','')
            skills = job.find('span',class_="srp-skills").text.replace(" ","")
            more_info= job.header.h2.a['href'] #for only link
            if unskill not in skills:
            #print(company_name)
            #print(skills)
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"Company name: {company_name.strip()}\n")
                    f.write(f"Req Skills:{skills.strip()}\n")
                    f.write(f'More Info:{more_info}\n')
                print(f"file saved:{index}")
if __name__ =='__main__':
    while True:
        find_jobs()
        time_wait=0.1
        print(f"waiting{time_wait} secs...")
        time.sleep(60*time_wait)
