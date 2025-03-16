import requests

from ammoseekr import consts, models


class Scraper:
    BASE_URL = "https://ammoseek.com/"

    def __init__(
        self,
        caliber: consts.Caliber,
        session: requests.Session = None,
    ):
        self.caliber = caliber
        self.casing = consts.Casing.BRASS
        self.condition = consts.Condition.NEW
        self.session = session or requests.Session()

    def list_deals(self) -> list[models.AmmoListing]:
        headers = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": Scraper.BASE_URL,
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": f"https://ammoseek.com/ammo/{self.caliber.readable_name}?sh=low&ca={self.casing}&co={self.condition}",
            "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-requested-with": "XMLHttpRequest",
            # forgive me for lying
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        }

        # if its ugly but it works... its still ugly.
        params = {
            "draw": "1",
            "columns[0][data]": "retailer",
            "columns[0][name]": "",
            "columns[0][searchable]": "true",
            "columns[0][orderable]": "false",
            "columns[0][search][value]": "",
            "columns[0][search][regex]": "false",
            "columns[1][data]": "descr",
            "columns[1][name]": "",
            "columns[1][searchable]": "true",
            "columns[1][orderable]": "false",
            "columns[1][search][value]": "",
            "columns[1][search][regex]": "false",
            "columns[2][data]": "mfg",
            "columns[2][name]": "",
            "columns[2][searchable]": "true",
            "columns[2][orderable]": "false",
            "columns[2][search][value]": "",
            "columns[2][search][regex]": "false",
            "columns[3][data]": "caliber",
            "columns[3][name]": "",
            "columns[3][searchable]": "true",
            "columns[3][orderable]": "false",
            "columns[3][search][value]": "",
            "columns[3][search][regex]": "false",
            "columns[4][data]": "grains",
            "columns[4][name]": "",
            "columns[4][searchable]": "true",
            "columns[4][orderable]": "false",
            "columns[4][search][value]": "",
            "columns[4][search][regex]": "false",
            "columns[5][data]": "when",
            "columns[5][name]": "",
            "columns[5][searchable]": "true",
            "columns[5][orderable]": "false",
            "columns[5][search][value]": "",
            "columns[5][search][regex]": "false",
            "columns[6][data]": "purchaselimit",
            "columns[6][name]": "",
            "columns[6][searchable]": "true",
            "columns[6][orderable]": "false",
            "columns[6][search][value]": "",
            "columns[6][search][regex]": "false",
            "columns[7][data]": "casing",
            "columns[7][name]": "",
            "columns[7][searchable]": "true",
            "columns[7][orderable]": "false",
            "columns[7][search][value]": "",
            "columns[7][search][regex]": "false",
            "columns[8][data]": "condition",
            "columns[8][name]": "",
            "columns[8][searchable]": "true",
            "columns[8][orderable]": "false",
            "columns[8][search][value]": "",
            "columns[8][search][regex]": "false",
            "columns[9][data]": "price",
            "columns[9][name]": "",
            "columns[9][searchable]": "true",
            "columns[9][orderable]": "false",
            "columns[9][search][value]": "",
            "columns[9][search][regex]": "false",
            "columns[10][data]": "count",
            "columns[10][name]": "",
            "columns[10][searchable]": "true",
            "columns[10][orderable]": "false",
            "columns[10][search][value]": "",
            "columns[10][search][regex]": "false",
            "columns[11][data]": "cp",
            "columns[11][name]": "",
            "columns[11][searchable]": "true",
            "columns[11][orderable]": "false",
            "columns[11][search][value]": "",
            "columns[11][search][regex]": "false",
            "columns[12][data]": "shipping_rating",
            "columns[12][name]": "",
            "columns[12][searchable]": "true",
            "columns[12][orderable]": "false",
            "columns[12][search][value]": "",
            "columns[12][search][regex]": "false",
            "columns[13][data]": "share",
            "columns[13][name]": "",
            "columns[13][searchable]": "true",
            "columns[13][orderable]": "false",
            "columns[13][search][value]": "",
            "columns[13][search][regex]": "false",
            "columns[14][data]": "dr",
            "columns[14][name]": "",
            "columns[14][searchable]": "true",
            "columns[14][orderable]": "false",
            "columns[14][search][value]": "",
            "columns[14][search][regex]": "false",
            "start": "0",
            "length": "100",
            "search[value]": "",
            "search[regex]": "false",
            "search_ammo": "1",
            "cal": self.caliber.id,
            "ca": self.casing,
            "ekw": "",
            "co": self.condition,
            "sort": "",
            "ikw": "",
            "seo_name": self.caliber.readable_name,
            "gun": self.caliber.gun_type,
            "sh": "low",
        }
        result = self.session.post(Scraper.BASE_URL, data=params, headers=headers)
        result.raise_for_status()

        data = result.json()["data"]
        return [models.AmmoListing.model_validate(obj) for obj in data]
