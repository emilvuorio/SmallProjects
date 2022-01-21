from bs4 import BeautifulSoup
import requests
global duunitoriTyot
global monsteriTyot
global oikotieTyot
duunitoriTyot, monsteriTyot, oikotieTyot = [], [], []


def duuniTori():

    global duunitoriTyot 
    url = "https://duunitori.fi/tyopaikat?alue=Varsinais-suomi&filter_work_relation=summer_job&haku=tieto-%20ja%20tietoliikennetekniikka%20(ala)"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    jobs = doc.find(class_="grid-sandbox grid-sandbox--tight-bottom grid-sandbox--tight-top")


    print("Duunitorin työpaikat \n")
    for link in jobs.find_all('a', class_="job-box__hover gtm-search-result", href=True):
        print("\n")
        print(link.contents)
        print(f"https://duunitori.fi{link['href']}")
        duunitoriTyot.append(f"https://duunitori.fi{link['href']}")
    
    
def monsteri():

    global monsteriTyot
    url = "https://www.monster.fi/tyopaikat/it/varsinais-suomi/kesatyo"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    jobs = doc.find(class_="view-content")
    while True:
        try:

            for link in jobs.find_all('a',  href=True):
                print("\n")
                text = link.text.strip()
                if "Tallenna suosikkeihin" not in text:
                    print(text)
                    print(f"{link['href']}")
                    monsteriTyot.append(f"{link['href']}")
            break
        except AttributeError:
            print("Jokin meni pieleen, tai monsterissa ei ole avoimia työpaik")
            break
def oikotie():

    global oikotieTyot
    url = "https://tyopaikat.oikotie.fi/tyopaikat/varsinais-suomi/it-tech?tyosuhde=kesatyo"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    jobs = doc.find(class_="job-ad-list-with-publication-date-titles")
    while True:
        try:
            for link in jobs.find_all('a', href=True):
                print("\n")
                print(link.text.strip())
                print(f"https://tyopaikat.oikotie.fi{link['href']}")
                oikotieTyot.append(f"{link['href']}")
            break
            
        except AttributeError:
            print("Jokin meni pieleen, tai oikotiellä ei ole avoimia työpaik")
            break

def updateLists():
    print("_________________________\n")
    global duunitoriTyot,  monsteriTyot, oikotieTyot
    fileTori = open("D:\projektit\webscraping_duuni\oldJobsTori.txt", "r")
    jobsTori = fileTori.read()
    fileMonster = open("D:\projektit\webscraping_duuni\oldJobsMonster.txt", "r")
    jobsMonster = fileMonster.read()
    fileOikotie = open("D:\projektit\webscraping_duuni\oldJobsOikotie.txt","r")
    jobsOikotie = fileOikotie.read()

    jobsTori = int(jobsTori)
    jobsMonster = int(jobsMonster)
    jobsOikotie = int(jobsOikotie)

    oldJobs = jobsOikotie + jobsMonster + jobsTori  # counts the sum of previous jobs available
    currentJobs = len(duunitoriTyot) + len(monsteriTyot) + len(oikotieTyot)

    if oldJobs == currentJobs:
        print("Ei uusia työpaikka ilmoituksia")
    
    else:

        print("Uusia työpaikkailmoituksia")


    fileTori = open("D:\projektit\webscraping_duuni\oldJobsTori.txt", "w")
    fileMonster = open("D:\projektit\webscraping_duuni\oldJobsMonster.txt", "w")
    fileOikotie = open("D:\projektit\webscraping_duuni\oldJobsOikotie.txt","w")
    fileTori.write(str(len(duunitoriTyot)))
    fileMonster.write(str(len(monsteriTyot)))
    fileOikotie.write(str(len(oikotieTyot)))

    fileTori.close
    fileMonster.close
    fileOikotie.close

    
def main():
    global duunitoriTyot,  monsteriTyot, oikotieTyot
    duuniTori()
    monsteri()
    oikotie()
    updateLists()

    print("\n")
    print("Duunitorissa avonaisia IT-alan kesätöitä: ", len(duunitoriTyot))
    print("Moinsterissa avonaisia IT-alan kesätöitä: ",len(monsteriTyot))
    print("Oikotiellä avonaisia IT-alan kesätöitä: ",len(oikotieTyot))
    print("\n")



if __name__ == "__main__":
    main()