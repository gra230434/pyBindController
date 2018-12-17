# 原始資料存放空間
## 檔案格式
CSV 檔案規格，逗號分隔檔案
## 資料型態
1. 一般 A 與 cname 類型

|型別|IP 地址|domain name|cname|
|---|---|---|---|
|A|10.0.0.1|mail|mailserver|
|A|10.0.0.2|www|wwwdev|
|A|10.0.0.3|www1|wwwp|

2. MX 類型，會多增加 MX 的優先度

|型別|IP 地址|priority|domain name|cname|
|---|---|---|---|---|
|MX|10.0.0.30|1|mail|mailserver|
|MX|10.0.0.31|5|mail|maildev|

3. NS 類型

|型別|domain name|
|---|---|
|NS|dns1|
|NS|dns2|

如果管理一個 24 網段的 DNS，建議將所有的 IP 都設定上正解與反解檔案
