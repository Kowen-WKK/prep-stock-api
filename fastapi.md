##　瀏覽器開 /healthz
    會顯示{"detail":"Not Found"}, 找不到路由
    而終端機也會顯示"GET /healthz HTTP/1.1" 404 Not Found
    解決方法:輸入正確的路由

##  把 main:app 打成 main:ap 再啟動
    由於在main.py裡面是通過 app = FastAPI() 來建立的, 所以uvicorn 會照著 main:ap 去 main.py 裡找一個叫 ap 的變數，找不到就會報錯
    解決方法:在使用ap時則無法運行FastAPI,改成ap = FastAPI() 和 @ap.get("/health"),這樣的話就沒問題了

##  在 main.py 故意漏一個冒號或括號
    會因SyntaxError而無法執行main.py,
    解決方法:修改main.py的語法錯誤

##  開兩個終端機，兩邊都跑 uvicorn → 第二個報什麼錯？（提示：port 被佔用）
    無法同時使用:8000
    解決方法:只需要關掉一個或是把另外一個改成:8000之外的接口即可


##  把回傳改成 {"status": "ok", "service": "prep-stock-api"}，不重啟，直接刷新瀏覽器 
    驗證成功 --reload 有用, 所以--reload的用處體現在檔案有所變更時,不需要重開伺服器也可以更新到最新的版本

    FastAPI定義路由,將Python字典轉成JSON格式,並同時自動生成/docs說明頁面
    Uvicorn則是伺服器,它等待請求並把請求送到FastAPI,最後傳回回應
    FastAPI defines the routes, converts Python dicts to JSON, and creates the /docs page automatically.
    Uvicorn is the server: it waits for requests, passes them to FastAPI, and sends the response back.

    FastAPI defines what the app does; Uvicorn is the server that runs it and handles the requests.