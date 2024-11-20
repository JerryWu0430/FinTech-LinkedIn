import requests
import json
from PIL import Image
import time
import numpy as np


with open("reverseEngineering/LinkdIncookiesMain.json", "r") as file:
    cookies = json.load(file)


def createImageUrn(imagePath="reverseEngineering/post/black.jpeg", company=None):

    ## get the file size
    with open(imagePath, "rb") as file:
        fileSize = len(file.read())
    print("fileSize : ", fileSize)

    headers = {
        "authority": "www.linkedin.com",
        "accept": "application/vnd.linkedin.normalized+json+2.1",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json; charset=UTF-8",
        "csrf-token": "ajax:1514152367892086323",
        "dnt": "1",
        "origin": "https://www.linkedin.com",
        "referer": "https://www.linkedin.com/feed/",
        "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "x-li-lang": "fr_FR",
        "x-li-page-instance": "urn:li:page:d_flagship3_feed;S5PDtBYHQGOkXC+UaOoXmg==",
        "x-li-track": '{"clientVersion":"1.13.8499","mpVersion":"1.13.8499","osName":"web","timezoneOffset":1,"timezone":"Europe/Paris","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1920,"displayHeight":1080}',
        "x-restli-protocol-version": "2.0.0",
    }

    params = {
        "action": "upload",
    }
    json_data = {
        "mediaUploadType": "IMAGE_SHARING",
        "fileSize": fileSize,
        "filename": imagePath.split("/")[-1],
    }

    if company != None:
        json_data["nonMemberActorUrn"] = "urn:li:fsd_company:" + company

    response = requests.post(
        "https://www.linkedin.com/voyager/api/voyagerVideoDashMediaUploadMetadata",
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    data = response.text
    with open("reverseEngineering/post/uploadRes.json", "w") as file:
        file.write(response.text)
    print(response.text)
    data = json.loads(data)
    url = data["data"]["value"]["singleUploadUrl"]
    print("url : ", url)
    return url


def image_to_raw(image_path):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to a numpy array
    image_array = np.array(image)

    # Flatten the array
    raw_data = image_array.flatten()

    return raw_data


def raw_to_bytes(raw_data):
    # Convert raw data to bytes
    byte_data = bytes(raw_data)
    return byte_data


def intermediaire():

    

    headers = {
        "authority": "www.linkedin.com",
        "accept": "application/vnd.linkedin.normalized+json+2.1",
        "accept-language": "en-US,en;q=0.9,fr;q=0.8",
        # 'cookie': 'li_sugr=3dcab145-e270-42a8-b756-45ed85a6376a; bcookie="v=2&216dd8ed-26e9-4110-86d5-212e1a6d9535"; bscookie="v=1&20240205165805ed0dd9b5-65bd-422f-81ef-1e435879bff4AQE9ItRAMaKlrTwnidZssBCTFCu98c4r"; li_alerts=e30=; li_gc=MTsyMTsxNzA3MTU5NzQ4OzI7MDIxBfMfgW04SiM40QB2RpgoTkmB4cApGGpP/399PGececw=; g_state={"i_l":0}; timezone=Europe/Paris; li_theme=light; li_theme_set=app; _guid=5e77adec-16ac-4ca8-877d-61396f21f920; dfpfpt=e7d9bbf63b924746ba4b34d9ae619916; aam_uuid=87283753636308094992200550697936221048; li_rm=AQHyzzvz-D1dlQAAAY1-tN6atMTY-Mx9GQCnqNGD1So5o-TdeF9d3PlloYDALAXt64jC0QCJn0HKXr15-72TkFuGjhZ7opTTjKdcfSLIuhZZUcPZ0WBkIKlj8_bw3LgOqqZb0ipBWUnqfxGpCAqmK61OjmYcrRovdXwgvAgO0iVEG9lW5t6u8rrT61LDbqDVhCrZtKpjZ0WZF9mbf1yi422tLBJAIzvahlORdQs9RjhLKY-YPm0Ar6tQ2WJ7BFJY0Rt2HssORgUYuFbb_TKwBmRzqhPKAtEO_E8vtHBYSd0l7Wsoqk6p_aMng3uZ8TnhDz2Pi-z0Xj9kjxTA2_w; visit=v=1&M; liap=true; JSESSIONID="ajax:3156239291613562708"; s_ips=855; gpv_pn=www.linkedin.com%2Fcompany%2Fid-redacted%2Fadmin%2Ffeed%2Fposts%2F; s_tslv=1707608114451; s_tp=6448; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19765%7CMCMID%7C87860347984789305122181644442816676019%7CMCAAMLH-1708216086%7C6%7CMCAAMB-1708216086%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1707618486s%7CNONE%7CMCCIDH%7C909951057%7CvVersion%7C5.1.1; fid=AQGrsVmw66YELgAAAY3rFM9j_yt1z3TgeikpsVUtesq8Oh5oH8E4OnUMcokUP3f5rhoIvk90qkZwQQ; li_at=AQEDATnsHuUCYyDNAAABjX606H0AAAGOEHVC6k0ASGLORsnqUOl-v9QkEX4nrA-yOxffika9OoD02Wes6X1enlP_Eu-Pv_f2ZoRH7Px5YReixtUFnuwRYa7T5BUyzKPAkjW7k7Qf8HY47EQ-064tdmPu; AnalyticsSyncHistory=AQI19GhqeJpDAwAAAY4EwHPRvOu56RkRl9QpmAMYfq_swYtYQ6iC7szcRSPuPYXgygnUdHhMKKT00-pkBshQWw; lms_ads=AQGPW4pY69Oa_wAAAY4EwHTJydmWJrk_NYvrJIo4uLvYpoTfyR_jc-d9o5rUIonGGeFFYD63TYbZxixrsYx3IN5RzvhPjl2r; lms_analytics=AQGPW4pY69Oa_wAAAY4EwHTJydmWJrk_NYvrJIo4uLvYpoTfyR_jc-d9o5rUIonGGeFFYD63TYbZxixrsYx3IN5RzvhPjl2r; lang=v=2&lang=fr-fr; lidc="b=TB17:s=T:r=T:a=T:p=T:g=15153:u=215:x=1:i=1709631171:t=1709714793:v=2:sig=AQG4YX1kxYc6QqdSq2nsYC9fXLVsLGth"; UserMatchHistory=AQIS_rFh__O8ywAAAY4N9XljbAkbIDPF7AUqLavqvfzwWvWJXlda0C0MFZ60mzpNGkHitNGOTgFbDXWOEG2Lp6zSc-P7HRwHKKXs287Xl1wcoZ2yVmP2r1vR2CBMZLknR3HzyGjBzudtQYVDjFX7TK-2G8hnciXgpCUS_ZeCfJR4Gl9P2ifRRJu4nI9Aif1L_8YZgji0BqRBamolm8ivwBfFYHlX9K4W-poUt8SZhHDI6FAXNzFhH_zfFN_cYgqDMaQsBdWJMJpi4sYvNxyJQ15km1PRlPLFjvIy5cPlQkaLp_y22-jocyXRUEEATuxjGY-eM0k; fptctx2=taBcrIH61PuCVH7eNCyH0MJojnuUODHcZ6x9WoxhgCm5vNY1%252b4Aow6nJsP1aRpo1ufLTNS7AwR3I60P91lK0xfsHzU6BBytJBGaIQb3ReWYbwTCJiidTnzEHeF%252bhWcs9OdslLHyQXT2EAl0ZXnkjlIcl18OiAd4qyqHaNS9hXPzJ9BVlKr3PS0G9cyYP07oPkA5Ya2Ytqnnccqjg4E1PC%252fupyHAsPLzUUxckt0XuXm%252brxoOaB7MIO5pULzpvDZ5I3824xh8K6g2cRlh9OFw2EVUPvU3us%252b5pTJfGs%252fh7w%252fT9jqb6bjQ11PhOoE5LVlnigxCsMjDw%252bbci6rod7Gz18mbV5kz6KyeHbBCIsoP2Vdk%253d; li_mc=MTsyMTsxNzA5NjMxNzc0OzI7MDIxycLMIPi/51LFwvNLEAHVdD9bkd3k8ZV5QXxKnlR2w0Y=',
        "csrf-token": "ajax:3156239291613562708",
        "dnt": "1",
        "referer": "https://www.linkedin.com/feed/",
        "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "x-li-lang": "fr_FR",
        "x-li-page-instance": "urn:li:page:d_flagship3_feed;c431szc6TUmXmB99xwP+hA==",
        "x-li-track": '{"clientVersion":"1.13.11755","mpVersion":"1.13.11755","osName":"web","timezoneOffset":1,"timezone":"Europe/Paris","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1920,"displayHeight":1080}',
        "x-restli-protocol-version": "2.0.0",
    }

    response = requests.get(
        "https://www.linkedin.com/voyager/api/graphql?variables=(pageKey:feed_share,slotId:be_kind_prompt)&queryId=voyagerLegoDashPageContents.6e5607181411f5835938e105d18564e2",
        cookies=cookies,
        headers=headers,
    )
    print(response.status_code)
    print(response.text)
    with open("reverseEngineering/post/intermediaire.json", "w") as file:
        file.write(response.text)


def uploadImage(mediaAsset, uploadUrl, imagePath):

   
    headers = {
        'authority': 'www.linkedin.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,fr;q=0.8',
        'content-type': 'image/jpeg',
        # 'cookie': 'li_sugr=3dcab145-e270-42a8-b756-45ed85a6376a; bcookie="v=2&216dd8ed-26e9-4110-86d5-212e1a6d9535"; bscookie="v=1&20240205165805ed0dd9b5-65bd-422f-81ef-1e435879bff4AQE9ItRAMaKlrTwnidZssBCTFCu98c4r"; li_alerts=e30=; li_gc=MTsyMTsxNzA3MTU5NzQ4OzI7MDIxBfMfgW04SiM40QB2RpgoTkmB4cApGGpP/399PGececw=; g_state={"i_l":0}; timezone=Europe/Paris; li_theme=light; li_theme_set=app; _guid=5e77adec-16ac-4ca8-877d-61396f21f920; dfpfpt=e7d9bbf63b924746ba4b34d9ae619916; aam_uuid=87283753636308094992200550697936221048; li_rm=AQHyzzvz-D1dlQAAAY1-tN6atMTY-Mx9GQCnqNGD1So5o-TdeF9d3PlloYDALAXt64jC0QCJn0HKXr15-72TkFuGjhZ7opTTjKdcfSLIuhZZUcPZ0WBkIKlj8_bw3LgOqqZb0ipBWUnqfxGpCAqmK61OjmYcrRovdXwgvAgO0iVEG9lW5t6u8rrT61LDbqDVhCrZtKpjZ0WZF9mbf1yi422tLBJAIzvahlORdQs9RjhLKY-YPm0Ar6tQ2WJ7BFJY0Rt2HssORgUYuFbb_TKwBmRzqhPKAtEO_E8vtHBYSd0l7Wsoqk6p_aMng3uZ8TnhDz2Pi-z0Xj9kjxTA2_w; visit=v=1&M; liap=true; JSESSIONID="ajax:3156239291613562708"; s_ips=855; gpv_pn=www.linkedin.com%2Fcompany%2Fid-redacted%2Fadmin%2Ffeed%2Fposts%2F; s_tslv=1707608114451; s_tp=6448; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19765%7CMCMID%7C87860347984789305122181644442816676019%7CMCAAMLH-1708216086%7C6%7CMCAAMB-1708216086%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1707618486s%7CNONE%7CMCCIDH%7C909951057%7CvVersion%7C5.1.1; fid=AQGrsVmw66YELgAAAY3rFM9j_yt1z3TgeikpsVUtesq8Oh5oH8E4OnUMcokUP3f5rhoIvk90qkZwQQ; li_at=AQEDATnsHuUCYyDNAAABjX606H0AAAGOEHVC6k0ASGLORsnqUOl-v9QkEX4nrA-yOxffika9OoD02Wes6X1enlP_Eu-Pv_f2ZoRH7Px5YReixtUFnuwRYa7T5BUyzKPAkjW7k7Qf8HY47EQ-064tdmPu; AnalyticsSyncHistory=AQI19GhqeJpDAwAAAY4EwHPRvOu56RkRl9QpmAMYfq_swYtYQ6iC7szcRSPuPYXgygnUdHhMKKT00-pkBshQWw; lms_ads=AQGPW4pY69Oa_wAAAY4EwHTJydmWJrk_NYvrJIo4uLvYpoTfyR_jc-d9o5rUIonGGeFFYD63TYbZxixrsYx3IN5RzvhPjl2r; lms_analytics=AQGPW4pY69Oa_wAAAY4EwHTJydmWJrk_NYvrJIo4uLvYpoTfyR_jc-d9o5rUIonGGeFFYD63TYbZxixrsYx3IN5RzvhPjl2r; lang=v=2&lang=fr-fr; lidc="b=TB17:s=T:r=T:a=T:p=T:g=15153:u=215:x=1:i=1709631171:t=1709714793:v=2:sig=AQG4YX1kxYc6QqdSq2nsYC9fXLVsLGth"; UserMatchHistory=AQIS_rFh__O8ywAAAY4N9XljbAkbIDPF7AUqLavqvfzwWvWJXlda0C0MFZ60mzpNGkHitNGOTgFbDXWOEG2Lp6zSc-P7HRwHKKXs287Xl1wcoZ2yVmP2r1vR2CBMZLknR3HzyGjBzudtQYVDjFX7TK-2G8hnciXgpCUS_ZeCfJR4Gl9P2ifRRJu4nI9Aif1L_8YZgji0BqRBamolm8ivwBfFYHlX9K4W-poUt8SZhHDI6FAXNzFhH_zfFN_cYgqDMaQsBdWJMJpi4sYvNxyJQ15km1PRlPLFjvIy5cPlQkaLp_y22-jocyXRUEEATuxjGY-eM0k; fptctx2=taBcrIH61PuCVH7eNCyH0MJojnuUODHcZ6x9WoxhgCm5vNY1%252b4Aow6nJsP1aRpo1ufLTNS7AwR3I60P91lK0xfsHzU6BBytJBGaIQb3ReWYbwTCJiidTnzEHeF%252bhWcs9OdslLHyQXT2EAl0ZXnkjlIcl18OiAd4qyqHaNS9hXPzJ9BVlKr3PS0G9cyYP07oPkA5Ya2Ytqnnccqjg4E1PC%252fupyHAsPLzUUxckt0XuXm%252brxoOaB7MIO5pULzpvDZ5I3824xh8K6g2cRlh9OFw2EVUPvU3us%252b5pTJfGs%252fh7w%252fT9jqb6bjQ11PhOoE5LVlnigxCsMjDw%252bbci6rod7Gz18mbV5kz6KyeHbBCIsoP2Vdk%253d; li_mc=MTsyMTsxNzA5NjMzNTkwOzI7MDIxHDgssWu3X3PwW9HFtqiGZ2vJ1egOjJtThzq25MfxZ5g=',
        'csrf-token': 'ajax:3156239291613562708',
        'dnt': '1',
        'media-type-family': 'STILLIMAGE',
        'origin': 'https://www.linkedin.com',
        'referer': 'https://www.linkedin.com/feed/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    params = {
        'ca': 'vector_feedshare',
        'cn': 'uploads',
        'f': 'YmxhY2suanBlZw==',
        'sync': '1',
        'v': 'beta',
        'ut': '2lqAkqshZ9Ob81',
    }

    data = 'ÿØÿà\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00ÿÛ\x00\x84\x00\t\x06\a\b\a\x06\t\b\a\b\n\n\t\v\r\x16\x0f\r\f\f\r\x1b\x14\x15\x10\x16 \x1d"" \x1d\x1f\x1f$(4,$&1\'\x1f\x1f-=-157:::#+?D?8C49:7\x01\n\n\n\r\f\r\x1a\x0f\x0f\x1a7%\x1f%77777777777777777777777777777777777777777777777777ÿÀ\x00\x11\b\x00À\x01\x00\x03\x01"\x00\x02\x11\x01\x03\x11\x01ÿÄ\x00\x16\x00\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\aÿÄ\x00\x17\x10\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x11AÿÄ\x00\x15\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01ÿÄ\x00\x14\x11\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00ÿÚ\x00\f\x03\x01\x00\x02\x11\x03\x11\x00?\x00ÄDP\x10\x00\x00\x00\x00\x00\x02\x8a\b¨"ª(\x02**\n\x80(\bª \n$P\x10\x00\x00@\x05\x10T\x00\x00\x01A\x00\x00\x00\x00A@\x14\x01@\x04\x10T\x11D\x01@\x14\x00\x00\x14\x00D\x00\x8a\x00\x80\x00\n\x98("\x80¨\xa0\bb\xa0(\b\x00\x00"\x80\x00 ¨"\x88EU\x01\x00\x01\x00\x14\x02\x15\x14\x01Q\x05\x10@\x14P\x11QQ@E@\x00\x05\x11@\x00\x05@\x00\x01\x05A\x00\x00\x00\b¨\xa0\x00\x00\x02\x80\x02\n\x8a\x80\x02\x80 \x00\x00¨\x00\x00¢(\x00\x00\x00\b©@\x01C\x82\x88\x80\x00\x8a\n\x01¢(\x00\x00(\x80 *\x00\x00\n\x80\x00\x00\x00 ¨\n\xa0\x00"\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\b¢\x88* \x00\x00\x00\x00\x00\x02\x00\x00¨\n\xa0\x00\x00\b\xa0\x00\x80\xa0\x00\x02\xa0\x02(\x00\x00\x02\n\x02\x00 \x00\xa0\x02\x00\x00\x02\x80\b(\x80ª\x00\x00\x00\x00\x00\x00\x02\x80\x00*A\x00\x05P\x04D\x15\x00\x00@\x00\x00P\x01\x00\x00\x00QD\x8a\x8a\x00\x00\x00\x00\x00*\x82* *\x00µ\x02\x80\x02\x82* \x00¨\x00\x00\b\x00\x00\x00\xa0\x02\n\x84\x15Q@\x00\x00\x00\x00QP\x10\x00\x00\x00\x01\x00\x01P\x00\x00\x00\x00\x00\x10\x00\x14\x15\x14\x00DQ\x14P\x00 ( \n\x00\x00\x00\x00" \n\x00\x00\x00\x00 \x00\xa0\x02\x02¢\x8a\x00\x00\x00\x01\x80\x10 (\x00ÿÙ'.encode()

    response = requests.put(
        uploadUrl,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print(response.status_code)
    print(response.text)


if __name__ == "__main__":
    ## get the upload url
    res = createImageUrn()
    url = res[1]
    print("url: ", url)
 
    uploadImage(None, url, "reverseEngineering/post/black.jpeg")
