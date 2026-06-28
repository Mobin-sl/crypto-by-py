from api import get_crypto_prices
from excel_manager import save_excel


def main():
    data = get_crypto_prices()
    for item in data:
        print(item)
    save_excel(data)


if __name__ == "__main__":
    main()