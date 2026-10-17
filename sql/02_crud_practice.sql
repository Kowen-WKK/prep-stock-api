INSERT

  1. 新增一筆品項
INSERT INTO items(name, quantity) VALUES ('Pork XLB Filling', 5);
 
 2. 一句 INSERT 同時新增 3 筆
INSERT INTO items(name, quantity) VALUES ('Pork XLB Filling', 5), ('Chicken XLB Filling', 10), ('Pork XLB Filling', 15);
 
  3. 新增時不給 id，用 SELECT 看看 id 是多少
--會按最新id+1

  4. 故意不給 name，讀錯誤訊息，說出為什麼被擋
--會顯示column " " does not exist

 5. 新增一筆，並讓它直接回傳新的 id（提示：RETURNING）
INSERT INTO items(name, quantity) VALUES ('Pork XLB Filling', 5) RETURNING id;


SELECT

 1. 查全部
SELECT * FROM items;

 2. 只查名稱和數量兩欄
SELECT name, quantity FROM items;

 3. 查數量小於 5 的品項
SELECT * FROM items WHERE quantity < 5;

 4. 數量最多的前 3 名（提示：ORDER BY、LIMIT）
SELECT * FROM items ORDER BY quantity LIMIT 3;

 5. 名稱裡有某個字的品項（提示：LIKE）
SELECT * FROM items WHERE name LIKE 'Pork XLB Filling';

UPDATE

 1. 用 id 改某一筆的數量
 UPDATE items SET name = 'Mushroom XLB Filling' WHERE id = 3;

 2. 某一筆的數量「加 10」，不是「改成 10」
 UPDATE items SET quantity = quantity + 10 WHERE id = 5;

 3. 一次改同一筆的兩個欄位
UPDATE items SET name = 'Mushroom XLB Filling', quantity = 20 WHERE id = 3;

 4. 符合條件的多筆一起改（例如數量 < 5 的全部補到 5）
 UPDATE items SET quantity = 5 WHERE quantity < 5;

 5. 在 BEGIN 裡故意不寫 WHERE 執行 UPDATE → 看災情 → ROLLBACK → 確認資料回來了


DELETE

 1. 用 id 刪一筆
 DELETE FROM items WHERE id = 5;

 2. 刪除符合條件的多筆
 DELETE FROM items WHERE quantity > 20;

 3. 刪一個不存在的 id，看回傳的 DELETE 0
 DELETE FROM items WHERE id = 5;
→ 對照你的 API：資料庫不會報錯，只說「刪了 0 筆」。所以 404 要誰負責判斷？

 4. 在 BEGIN 裡刪掉全部，再 ROLLBACK


 5. 刪掉最後一筆後再新增一筆，看新 id 有沒有「補位」
→ 想一想：為什麼資料庫不重用刪掉的 id？
--因為計數器只會一直向前取1,它並不會管當前資料庫是否缺失某個id
