#region debai
"""
--- ma debai / id
get_24hformat_hour(hour_str)

--- nopbai
00 fork github repo tu bainopmau tu nguon duoiday
   https://github.com/namgivu/toyaget24hformathourhourstr

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a mo github web, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubrepourl

02b dán diachi githubrepourl vao mẫu don duoiday
    https://forms.gle/XgvPs4beBaik7UiP7

--- debai / problem
Viết hàm
  get_24hformat_hour(hour_str)
giúp trả về giờ trong ngày theo dạng 24-giờ

Khi chạy với đầuvào / input            | Kếtquả đẩura / output  | Thứtự mẫuthử
-------------------------------------- | ---------------------- | -----------
get_24hformat_hour(hour_str='6am')     | 6                      | 00

# AM / PM format
get_24hformat_hour('6am')              | 6                      | 01
get_24hformat_hour('7 am')             | 7                      | 02
get_24hformat_hour('8AM')              | 8                      | 03
get_24hformat_hour('9 AM')             | 9                      | 04

get_24hformat_hour('6pm')              | 18                     | 05
get_24hformat_hour('7 pm')             | 19                     | 06
get_24hformat_hour('8PM')              | 20                     | 07
get_24hformat_hour('9 PM')             | 21                     | 08

get_24hformat_hour('10 AM')            | 10                     | 09
get_24hformat_hour('11 AM')            | 11                     | 10
get_24hformat_hour('10 PM')            | 22                     | 11
get_24hformat_hour('11 PM')            | 23                     | 12
"""
#endregion debai

#region bailam
def get_24hformat_hour(hour_str):
  if hour_str is None:
    return None

  hour_str = hour_str.strip().lower()

  is_pm = 'pm' in hour_str
  is_am = 'am' in hour_str

  hour_str = hour_str.replace('am', '').replace('pm', '').strip()

  try:
    if len(hour_str) > 2:
      hour_str = hour_str[:2]
    hour = int(hour_str)
  except ValueError:
    return None

  if is_pm and hour < 12:
    hour += 12
  elif is_am and hour == 12:
    hour = 0

  return str(hour)
#endregion bailam
