import requests
import json
import re


headers = {
    "authority": "www.linkedin.com",
    "accept": "application/vnd.linkedin.normalized+json+2.1",
    "accept-language": "en-US,en;q=0.9,fr;q=0.8",
    # 'cookie': 'li_sugr=3dcab145-e270-42a8-b756-45ed85a6376a; bcookie="v=2&216dd8ed-26e9-4110-86d5-212e1a6d9535"; bscookie="v=1&20240205165805ed0dd9b5-65bd-422f-81ef-1e435879bff4AQE9ItRAMaKlrTwnidZssBCTFCu98c4r"; fid=AQHiRkC3lJOMqQAAAY16pnZefn9nj3mrKbhIUEW6T6ft-WIWr7THknx_ttLPekbGoVrZjyQvRuaVmQ; li_alerts=e30=; li_gc=MTsyMTsxNzA3MTU5NzQ4OzI7MDIxBfMfgW04SiM40QB2RpgoTkmB4cApGGpP/399PGececw=; g_state={"i_l":0}; timezone=Europe/Paris; li_theme=light; li_theme_set=app; _guid=5e77adec-16ac-4ca8-877d-61396f21f920; dfpfpt=e7d9bbf63b924746ba4b34d9ae619916; aam_uuid=87283753636308094992200550697936221048; li_rm=AQHyzzvz-D1dlQAAAY1-tN6atMTY-Mx9GQCnqNGD1So5o-TdeF9d3PlloYDALAXt64jC0QCJn0HKXr15-72TkFuGjhZ7opTTjKdcfSLIuhZZUcPZ0WBkIKlj8_bw3LgOqqZb0ipBWUnqfxGpCAqmK61OjmYcrRovdXwgvAgO0iVEG9lW5t6u8rrT61LDbqDVhCrZtKpjZ0WZF9mbf1yi422tLBJAIzvahlORdQs9RjhLKY-YPm0Ar6tQ2WJ7BFJY0Rt2HssORgUYuFbb_TKwBmRzqhPKAtEO_E8vtHBYSd0l7Wsoqk6p_aMng3uZ8TnhDz2Pi-z0Xj9kjxTA2_w; visit=v=1&M; liap=true; li_at=AQEDATnsHuUCYyDNAAABjX606H0AAAGNosFsfU0AUfzcphO4uIPMMrUKWXTVm6PCFynArp-DnuuVqPGZ0Al4xxPxQfcsJ2talLigZ-8erD0LLaLXSTeVbOtv1VZZ2SzyXVI_hmvPh96Bp_78tQTYO2xl; JSESSIONID="ajax:3156239291613562708"; AnalyticsSyncHistory=AQLl3rfODAxN_QAAAY2Kkxqsc6r5klie_YlF2eCKjCprDxKj3RJbjpLYioNTsGw1zyLmp9PZMiJ-Z1zbpmh0lA; lms_ads=AQFEmT4fulNnbQAAAY2KkxuIS_aKeBU9wFmW4ZC78YgfAvHXEy8inm7Uahvcw8ZFseTyhCisG3qAJsLVr57gC-X-ALxybsqf; lms_analytics=AQFEmT4fulNnbQAAAY2KkxuIS_aKeBU9wFmW4ZC78YgfAvHXEy8inm7Uahvcw8ZFseTyhCisG3qAJsLVr57gC-X-ALxybsqf; s_ips=855; lang=v=2&lang=fr-fr; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19763%7CMCMID%7C87860347984789305122181644442816676019%7CMCAAMLH-1708085972%7C6%7CMCAAMB-1708085972%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1707488372s%7CNONE%7CMCCIDH%7C909951057%7CvVersion%7C5.1.1; fptctx2=taBcrIH61PuCVH7eNCyH0MJojnuUODHcZ6x9WoxhgCm5vNY1%252b4Aow6nJsP1aRpo1ufLTNS7AwR3I60P91lK0xfsHzU6BBytJBGaIQb3ReWYbwTCJiidTnzEHeF%252bhWcs9OdslLHyQXT2EAl0ZXnkjlH4sGObeUO9NwT5eCeFG9X1ghs3C12pWheE2THFBQfwcb8c6LPuWtEnRdy%252bIeD2drTlibPFsbOz9kaJBrcsDHkHkycwwGg5ordzagRBk1rRmOGNtN59Kxh%252b5RYQce7IiUhkoIj7Yye64yxqCfsRdehodEjFGQWEH41rvHWlEG%252f9g4lTMTot1SA6Gd%252fi7XFkkB2VyIDLAofAWqp7lkAOEQ9M%253d; s_cc=true; gpv_pn=www.linkedin.com%2Fcompany%2Fid-redacted%2Fadmin%2Ffeed%2Fposts%2F; s_plt=3.41; s_pltp=www.linkedin.com%2Fcompany%2Fid-redacted%2Fadmin%2Ffeed%2Fposts%2F; s_tp=6600; s_ppv=www.linkedin.com%2Fcompany%2Fid-redacted%2Fadmin%2Ffeed%2Fposts%2F%2C34%2C13%2C2218%2C2%2C7; s_tslv=1707481431260; s_sq=lnkdprod%3D%2526pid%253Dwww.linkedin.com%25252Fcompany%25252Fid-redacted%25252Fadmin%25252Ffeed%25252Fposts%25252F%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.linkedin.com%25252Ffeed%25252F%25253Fnis%25253Dtrue%2526ot%253DA; UserMatchHistory=AQLdJLtjZ-3aEgAAAY2N13zR7fNSDVy0JtPu7gK-hB7zqmZXr0POCyuDkJVzU-RbM5WuITB9JuW7pC2KQJqhzp6h5qgJS4ZhWI5W_QeR_5CABlpgrjbz_iIhapZExNXKJ55ZzCLjzrGTsf_4mUZ8YiIdc14WcUjEzxU761Jw1bz-pZZm65_UJQEjjJ3HdqOn8itmKAUJ5VRRHxkUhlbReNEpGbhEK7lvFkQdRYUBk1AoKfhIPfcSnapX-6-2GiVGippRUGbzP3g8lw0u-i_HAXQ9_o1TibqK-haapfmXPBHWve02bTJQ4pD788GfenJrs_Td-Jw; li_mc=MTsyMTsxNzA3NDgxNzg1OzI7MDIxljLVl0NoaO1EmyOjmAMMlThG3S6kUpbC2p6bySkmYt0=; lidc="b=TB17:s=T:r=T:a=T:p=T:g=13951:u=183:x=1:i=1707481845:t=1707568245:v=2:sig=AQG1wjWkZYRCwax1fmzGVAxJAsASRx04"',
    "csrf-token": "ajax:3156239291613562708",
    "dnt": "1",
    "referer": "https://www.linkedin.com/feed/",
    "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "x-li-lang": "fr_FR",
    "x-li-page-instance": "urn:li:page:d_flagship3_feed;9JF430FvQPGxr6AvYPjPQQ==",
    "x-li-track": '{"clientVersion":"1.13.10539","mpVersion":"1.13.10539","osName":"web","timezoneOffset":1,"timezone":"Europe/Paris","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1920,"displayHeight":1080}',
    "x-restli-protocol-version": "2.0.0",
}


def getPosts(count):
    response = requests.get(
        "https://www.linkedin.com/voyager/api/graphql?variables=(count:"+str(count)+")&queryId=voyagerFeedDashMainFeed.b65bf8aeab9634a31764fb2a947da7e4",
        cookies=cookies,
        headers=headers,
    )
    print("Response status code : ", response.status_code)
    print(response.text)
    data = json.loads(response.text)
    with open("reverseEngineering/getPosts/getFeedPostsRes.json", "w") as file:
        file.write(json.dumps(data, indent=2))
    ugc_post_ids = re.findall(r"ugcPost:(\d+)", str(data))

    posts = list(set(ugc_post_ids))
    print(posts)
    print("Get posts :", posts)
    return posts
    # json_obj = json.dumps(data, indent=2)
    # print(json_obj)


if __name__ == "__main__":
    res = getPosts(count=100)
    print(res)
