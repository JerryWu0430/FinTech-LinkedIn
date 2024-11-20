"""import requests
import json



headers = {
    "accept": "application/vnd.linkedin.normalized+json+2.1",
    "accept-language": "en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7",
    "csrf-token": "ajax:5870874727930491173",
    "dnt": "1",
    "priority": "u=1, i",
    "referer": "https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords=funeral&origin=FACETED_SEARCH&searchId=0383977d-fd9c-4cf6-a89e-8d176fd18f19&sid=~%2C7",
    "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
    "x-li-lang": "fr_FR",
    "x-li-page-instance": "urn:li:page:d_flagship3_search_srp_people;KQgDM21NRveh465fI58TlA==",
    "x-li-pem-metadata": "Voyager - People SRP=lazy-loaded-advanced-filters",
    "x-li-track": '{"clientVersion":"1.13.15586","mpVersion":"1.13.15586","osName":"web","timezoneOffset":-5,"timezone":"America/Bogota","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1920,"displayHeight":1080}',
    "x-restli-protocol-version": "2.0.0",
}

response = requests.get(
    "https://www.linkedin.com/voyager/api/graphql?variables=(query:(keywords:funeral,flagshipSearchIntent:SEARCH_SRP,queryParameters:List((key:geoUrn,value:List(103644278)),(key:resultType,value:List(PEOPLE)),(key:searchId,value:List(0383977d-fd9c-4cf6-a89e-8d176fd18f19)))))&queryId=voyagerSearchDashFilterClusters.c29056cbb660f3e65a765473ac92fa7c",
    cookies=cookies,
    headers=headers,
)

print(response.status_code)
print(json.dumps(response.json(), indent=4))
with open("searchForPeople.json", "w") as f:
    json.dump(response.json(), f)

"""

import requests
import json
import re
import time
import json

with open("reverseEngineering/LinkdIncookiesMain.json", "r") as file:
    cookies = json.loads(file.read())

headers = {
    "authority": "www.linkedin.com",
    "accept": "application/vnd.linkedin.normalized+json+2.1",
    "accept-language": "en-US,en;q=0.9",
    "csrf-token": "ajax:1514152367892086323",
    "dnt": "1",
    "referer": "https://www.linkedin.com/search/results/all/?keywords=ai&origin=GLOBAL_SEARCH_HEADER&sid=iq)",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "x-li-lang": "fr_FR",
    "x-li-page-instance": "urn:li:page:d_flagship3_search_srp_content;RpMPgDFlTzuSa+62W16AZQ==",
    "x-li-track": '{"clientVersion":"1.13.8499","mpVersion":"1.13.8499","osName":"web","timezoneOffset":1,"timezone":"Europe/Paris","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1920,"displayHeight":1080}',
    "x-restli-protocol-version": "2.0.0",
}


def searchPersons(prompt, count=1):
    print("Sending request : ", end="")
    res = []
    start = 0
    response = requests.get(
        "https://www.linkedin.com/voyager/api/graphql?variables=(start:"
        + str(start)
        + ",origin:FACETED_SEARCH,query:(keywords:"
        + prompt
        + ",flagshipSearchIntent:SEARCH_SRP,queryParameters:List((key:geoUrn,value:List(103644278)),(key:resultType,value:List(PEOPLE)))))&queryId=voyagerSearchDashClusters.0d1dfeebfce461654ef1279a11e52846",
        # queryParameters:List((key:resultType,value:List(CONTENT))))&queryId=voyagerSearchDashFilterClusters.a316af94acc09f9e8762cfb5021dc130
        cookies=cookies,
        headers=headers,
    )
    print(response.status_code)
    # print(response.text)
    # print(response.text)
    with open("reverseEngineering/getPosts/searchPersons.json", "w") as file:
        file.write(response.text)
    data = response.text

    ##print(data)


def extractData(data):

    ##print(data["included"][15])
    ##print(json.dumps(data["included"][15], indent=4))
    for element in data["included"]:
        if "template" in element.keys():
            if (
                element["template"] == "UNIVERSAL"
                and element["title"]["text"] != "Utilisateur LinkedIn"
            ):
                name = element["title"]["text"]
                url = element["navigationContext"]["url"].split("?")[0]
                subtitle = element["primarySubtitle"]["text"]
                summary = element["summary"]["text"]
                image = element["image"]["attributes"][0]["detailData"][
                    "nonEntityProfilePicture"
                ]["vectorImage"]["artifacts"][0]["fileIdentifyingUrlPathSegment"]
                subtitle2 = element["secondarySubtitle"]["text"]
                print(
                    f"Name: {name}\nURL: {url}\nSubtitle: {subtitle}\nSummary: {summary}\nImage: {image}\nSubtitle2: {subtitle2}\n\n"
                )


def getContactInfo(url):
    response = requests.get(url, cookies=cookies, headers=headers)
    print(response.status_code)
    print(response.text)

if __name__ == "__main__":
    """searchPersons("funeral")
    with open("reverseEngineering/getPosts/searchPersons.json", "r") as file:
        data = json.loads(file.read())
    extractData(data=data)"""
    getContactInfo("https://www.linkedin.com/in/c-samuel-mosher-52a2a1a/overlay/contact-info/")
