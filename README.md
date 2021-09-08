# SpamText-ForTatsu
ทำการสแปมข้อความเข้าห้องแชทที่ตั้งไว้ทุกๆ 121 วินาที(ในกรณีที่เป็น Admin ห้อง) เพื่อปั้มเวล
![image](https://user-images.githubusercontent.com/41195318/132435296-09aa28ec-b205-46f1-aeb0-75602e76b9fb.png)

หาไม่ใช่ Admin ห้องจะได้รับ exp ในทุกๆข้อความที่ส่ง ให้ไปปรับเวลาใน sleep() ได้ตามต้องการ
![image](https://user-images.githubusercontent.com/41195318/132435488-383ef84b-160e-4ce3-84c9-2e42cc4fa6aa.png)


## Installation
```
เปิด cmd แล้วติดตั้ง pip install python-decouple
```

```sh
สร้างไฟล์ .env 
```

```sh
ในไฟล์ .env ประกาศตัวแปรชื่อ TOKEN จะมีรูปแบบดังนี้ TOKEN=< your user token > *** เวลาใส่ข้อมูลจริงๆไม่ต้องมี < > ***
```

```sh
ในไฟล์ AutoText.py ให้ใส่ Channel ID แทนลงไปในบริเวณที่เขียนว่า < your channel id > *** เวลาใส่ข้อมูลจริงๆไม่ต้องมี < > ***
```

```sh
เปิด cmd แล้ว cd ไปยังโฟลเดอร์ที่เก็บไฟล์ไว้พิมพ์คำสั่ง py AutoText.py
```
