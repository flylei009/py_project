import requests
from lxml import etree
# data ={
# 'commit': 'Sign in',
# 'authenticity_token':'N24yZ6Hsezh1fSIuUcuku+WEPx8XHd5LbaWrakgc0MjTSbPJW5NOaqzXXJeKwdq3XH4MJAoBNAuomyCKWfNN4w==',
# 'ga_id':'1285086416.1590635051',
# 'login':'flylei009@163.com',
# 'password':'Yanping123',
# 'webauthn-support':'supported',
# 'webauthn-iuvpaa-support':'unsupported',
# # 'return_to':'',
# # 'allow_signup':'',
# # 'client_id':'',
# # 'integration':'',
# # 'required_field_4c32':'',
# # 'timestamp':'1603287239576',
# 'timestamp_secret': '6774e6d764de89eff3cfc326a0619306816de10dfa613b1d6ad7df646885dfd2',
# }


class Login(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath('//div//input[1]/@value')
        return token

    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token()[0],
            'login': email,
            'password': password
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            self.dynamics(response.text)

        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)

    def dynamics(self, html):
        selector = etree.HTML(html)
        dynamics = selector.xpath('//div[contains(@class, "news")]//div[contains(@class, "alert")]')
        for item in dynamics:
            dynamic = ' '.join(item.xpath('.//div[@class="title"]//text()')).strip()
            print(dynamic)

    def profile(self, html):
        selector = etree.HTML(html)
        name = selector.xpath('//input[@id="user_profile_name"]/@value')[0]
        bio = selector.xpath('//textarea[@id="user_profile_bio"]/text()')
        url = selector.xpath('//input[@id="user_profile_blog"]/@value')
        Twitter = selector.xpath('//input[@id="user_profile_twitter_username"]/@value')
        Company = selector.xpath('//input[@id="user_profile_company"]/@value')
        Location = selector.xpath('//input[@id="user_profile_location"]/@value')
        # email = selector.xpath('//select[@id="user_profile_email"]/option[@value!=""]/text()')
        print( name, bio, url,Twitter,Company,Location)


if __name__ == "__main__":
    login = Login()
    login.login(email='flylei009@163.com', password='Yanping123')