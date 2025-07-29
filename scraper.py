import requests #webスクレイピングをするためにインポート。メジャーなライブラリ。
from bs4 import BeautifulSoup #HTMLを解析するためにインポート。

def fetch_jr_delay_info():
    # JR九州の遅延情報ページ
    url = "https://www.jrkyushu.co.jp/trains/info/"

    response = requests.get(url)# urlに対し、getリクエストを送ってWebページの内容を取得
    response.encoding = response.apparent_encoding  # 日本語文字化け対策

    # HTMLをパースする。response.textはライブラリで定義されている。HTMLのテキストを取得する。
    # "html.parser"はPython標準のHTML解析ツール
    soup = BeautifulSoup(response.text, "html.parser")

    # 遅延情報の要素を取得（class名に注目）
    info_list = soup.select(".infoText")#infoTextはJR九州のページの遅延情報が書かれている要素のクラス名

    # テキストだけを抽出してリストにする
    messages = [info.get_text(strip=True) for info in info_list]

    return messages

# メイン処理
if __name__ == "__main__":
    delays = fetch_jr_delay_info()

    if delays:
        print("遅延情報が見つかりました：")
        for delay in delays:
            print("-", delay)
    else:
        print("正常運行です")
