"""GitHub から あたらしい らぶかし の .exe を ダウンロードするよ"""

# ひつような どうぐ を よぶよ
import os
import requests

# ダウンロード したい アドレス を きめるよ
exe_url = (
    "https://raw.githubusercontent.com/ObsidianMatrix/LoveCard_exe/main/"
    "%E3%83%A9%E3%83%96%E3%82%AB%E3%82%B7%E3%83%9F%E3%83%A5%E3%83%AC%E3%83%BC%E3%82%BF%E3%83%BC.exe"
)

# もとの ファイル の なまえ だよ
exe_name = "ラブカシミュレーター.exe"

# いえ の フォルダ を しらべるよ
home_dir = os.path.expanduser("~")

# デスクトップ が あれば そこ に するよ
# なかったら ダウンロード フォルダ に するよ
desktop_path = os.path.join(home_dir, "Desktop")
downloads_path = os.path.join(home_dir, "Downloads")
if os.path.isdir(desktop_path):
    save_dir = desktop_path
else:
    save_dir = downloads_path

# えらんだ フォルダ が ない とき は つくるよ
os.makedirs(save_dir, exist_ok=True)

# ほぞん する ばしょ を きめるよ
local_exe_path = os.path.join(save_dir, exe_name)

# あたらしい ファイル を もらうよ
response = requests.get(exe_url)
response.raise_for_status()

# おなじ なまえ が あったら けして おきかえるよ
if os.path.exists(local_exe_path):
    os.remove(local_exe_path)

# あたらしい ファイル を おくよ
with open(local_exe_path, "wb") as dst:
    dst.write(response.content)

print(f"{local_exe_path} に あたらしい ファイル を おいたよ！")
