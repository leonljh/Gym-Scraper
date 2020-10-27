import config as con
import time
import pandas
from selenium import webdriver
from bs4 import BeautifulSoup

def gymDataColl():
    # selenium gets html code
    elem = driver.find_element_by_xpath("//*")
    source_code = elem.get_attribute('innerHTML')

    # bs4 gets the html data for processing
    soup = BeautifulSoup(source_code, "html.parser")

    # create list for gyms
    onlyDivs = soup.find_all('div','lead mb-3')

    # create list for occupants
    onlyOccupancy = soup.find_all('span', 'occupancy')

    # create list for queue
    onlyQueue = soup.find_all('span', 'queue_length')

    finalList = []
    timeStr = time.ctime()

    df = pandas.DataFrame(data={"Gym": [i.string for i in onlyDivs], "Occupancy": [i.string for i in onlyOccupancy], "Queue Length": [i.string for i in onlyQueue], "Time": [timeStr for _ in range(len(onlyDivs))]})
    # filename = getFileName()
    df.to_csv("./gymdata.csv", mode = 'a', header = False)
    return

url = 'https://smartentry.org/status/gymmboxx'


driver = webdriver.Chrome(con.directory)

driver.get(url)
# delay so dynamic elements can load
time.sleep(5)

# test collection of data
df = pandas.DataFrame(data={"Gym":[], "Occupancy":[], "Queue Length":[], "Time":[]})
df.to_csv("./gymdata.csv", mode = 'w', header = True)

i = 1;
while(i<=20):
    print('script running')
    gymDataColl()
    print( str(i) + "pulling again")
    i += 1
    time.sleep(600)


# with open('gymdata.csv','a') as f:
#     df.to_csv(f, header = False)

