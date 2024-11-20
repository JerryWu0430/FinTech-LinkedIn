import requests



headers = {
    "authority": "www.linkedin.com",
    "accept": "application/vnd.linkedin.normalized+json+2.1",
    "accept-language": "en-US,en;q=0.9",
    # 'cookie': 'bcookie="v=2&530c874f-ee76-458e-8ee0-a9e587e2d5b1"; bscookie="v=1&2024030814185650089f46-79b3-49a5-88bf-ca20c1b5d735AQGS5_qBQ8-w4SywPgJIu6uLhjVgziXH"; li_gc=MTsyMTsxNzA5OTA3NTM4OzI7MDIxNY4x+2km7w0qN1ecGu9Ite9wETiRRBqugH3jHRPp8dY=; li_alerts=e30=; aam_uuid=52241855710450355830888909522564697733; _gcl_au=1.1.1960586322.1709907590; li_rm=AQHgCRy2RsE2CwAAAY4eb0E-YeNIj_NdcRBSTB1-MlFXSduOkNXTmU-TfDDTPMtg0vJNs_F4Cbj-awhh2ajBNrFYJr2RA7e7V5y1oWVlUm2hIYGjf8ToUi3I; fid=AQHPXaGtncws6gAAAY4eb0m4FruXXhON9jUJxoZOGVATJPf2ELkSYdPuqjSTsdqmLMB2UFpmBbBkkQ; li_at=AQEDAUxe6skBYXLUAAABjh5yzwYAAAGOQn9TBk4AiM5zD7oi9r-j7m2XCa44Q4B-h_Nhe0-c3wMaU6Il42ZMdwzX5odQS3f2iVjxwi1hk_5t92LgvNVHIoKpJ20FVzcF4fDQXL_g74vpetOYjjR3yThY; liap=true; timezone=Europe/Paris; li_theme=light; li_theme_set=app; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19791%7CMCMID%7C52104252371688975240907798293388246350%7CMCAAMLH-1710512650%7C6%7CMCAAMB-1710512650%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1709915050s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C-1859114033; dfpfpt=ab78b13e57fe48d4bd0889d2a426566a; JSESSIONID=ajax:3133400725640904784; lang=v=2&lang=fr-fr; li_mc=MTsyMTsxNzEwMDY5MjE4OzI7MDIxfSmhDb7M/1hFtC+VhpPE+QLFYNJ9PNG4umQz7f71w6g=; lidc="b=TB05:s=T:r=T:a=T:p=T:g=7178:u=3:x=1:i=1710069218:t=1710155618:v=2:sig=AQEux4YPVuIgy6zgdz56WTO4o5H5CvAq"; df_ts=1710069221096',
    "csrf-token": "ajax:3133400725640904784",
    "referer": "https://www.linkedin.com/feed/",
    "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "x-li-lang": "fr_FR",
    "x-li-page-instance": "urn:li:page:d_flagship3_feed;t1C0JZAeSQuyl7mr+4tDfw==",
    "x-li-pem-metadata": "Voyager - Feed=recent-feed-updates",
    "x-li-track": '{"clientVersion":"1.13.12043","mpVersion":"1.13.12043","osName":"web","timezoneOffset":1,"timezone":"Europe/Paris","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1920,"displayHeight":1080}',
    "x-restli-protocol-version": "2.0.0",
}

params = {
    "commentsCount": "0",
    "count": "10",
    "likesCount": "0",
    "moduleKey": "home-feed:desktop",
    "q": "feed",
}

response = requests.get(
    "https://www.linkedin.com/voyager/api/feed/updatesV2",
    params=params,
    cookies=cookies,
    headers=headers,
)
print(response.json())
