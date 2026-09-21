# Conventional Commits 筆記

## 一句話說明這是什麼
讓使用者進行版本更新的溝通說明,並在說明當中描述功能、修正以及重大變更。

## 為什麼要有這個規範（至少 2 個理由）
- 向其他人表達變化的過程
- 產生修改日誌

## 訊息結構
<類型>[可選填的作用範圍]: <描述>

[可選填的正文]

[可選填的頁腳]

## 類型
|  類型  |   用在什麼時候    | 規範正式定義的？(是/否) |
|-------|-------------------|-----------------------|
| feat  |  新增功能          |  是                   |
| fix   |  修改bug           |  是                  |
| docs  |  改的是文件/README |  否                   |
| style |  程式沒變，只改格式 |  否                   |
| test  |  新增/修改測試     |  否                   |
| chore |  雜項或維護        |  否                   |

## 破壞性變更怎麼標
BREAKING CHANGE:

## 跟版本號的關係
fix對應的是修訂號Patch
feat對應的是次版本Minor
BREAKING CHANGE對應的是主版本Major

## 我自己 repo 裡的例子
feat: show today's date in greeting
docs: resolve title conflict