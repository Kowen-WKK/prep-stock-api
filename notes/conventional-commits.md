# Conventional Commits 筆記

## 一句話說明這是什麼
一套 commit 訊息的寫法規則，規範的主要是「Git commit message（提交訊息）的格式與語意」。

## 為什麼要有這個規範（至少 2 個理由）
- 向其他人表達變化的過程
- 自動根據類型的變更而產生日誌及其相應的版本號

## 訊息結構
<類型>[可選填的作用範圍(指主要作用在專案的哪個部分)]: <描述>

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
它要放在頁腳，而且必須全部大寫.
而且還有另外兩種寫法,如下
feat!:
feat(api)!:

## 跟版本號的關係
fix對應的是修訂號Patch
feat對應的是次版本Minor
BREAKING CHANGE對應的是主版本Major

## 我自己 repo 裡的例子
feat: show today's date in greeting 合規範,因為是新增了顯示時間的功能
docs: resolve title conflict 合規範,雖然是解決了衝突,但原則只是修改了文件