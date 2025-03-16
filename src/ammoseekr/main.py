import ammoseekr


def main():
    s = ammoseekr.Scraper(caliber=ammoseekr.PISTOL_9MM)
    print(s.list_deals())


if __name__ == "__main__":
    main()
