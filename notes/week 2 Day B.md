## 實驗 A：喺其中一個 dict 加多個模型冇寫嘅欄位，例如 "cost": 1.2。回應入面會唔會出現？
    不會,因為有response_model作為條件的限制,而輸出的條件都寫在class item裡面,所以不會出現

## 實驗 B：拎走 response_model，再試一次 A。今次呢？
    當拿走作為條件的response_model後,輸出再沒有任何的限制,此時則會輸出所有的數據

## 實驗 C：把某個數量改成 "abc"。瀏覽器同 terminal 各自顯示咩？
    瀏覽器:
        Internal Server Error, 

    Terminal:
    INFO:     127.0.0.1:50207 - "GET /items HTTP/1.1" 500 Internal Server Error
    ERROR:    Exception in ASGI application

    TypeError: cannot use 'list' as a set element (unhashable type: 'list')

    由於輸出的數據類型跟對應的數據不相同,造成數據無法回傳

## 實驗 D：把數量改成 "12"（有引號嘅數字）。會報錯定會自己變成數字？
    會自己變成數字,證明如果數據類型可以轉換為正確的型別則會正確輸出

## 實驗 E：打開 localhost:8000/docs，搵 /items，睇佢點樣描述你嘅模型
    id* integer
    name* string
    count* integer
    unit* string

## 路由是什麼
    根據不同的網址和請求傳給對應的function去處理

## response model做了什麼
    根據response_model所擁有的條件進行過濾,並輸出所有乎合條件的數據,不需要的就不送出,所需但型別不對的數據就進行報錯但如果能轉換的會自動轉換