What is REST?

    REST is a way to build web applications so that computers can talk to each other over the internet easily and in an organized way.

🔍 Is REST a technology?

No, REST is not a:

    Programming language
    Software
    Tool
    Protocol like HTTP or FTP

✅ REST is a style or design pattern—a set of rules for how web services should work.
📦 Real-Life Analogy

Imagine you're using a food delivery app:

    You search for food
    You add items to cart
    You place an order
    You check order status

All these actions are done by talking to the backend server using RESTful APIs.

Each thing (food, cart, order) is a resource, and you're interacting with representations of them.
🔑 REST Means...
Term 	Simple Meaning
Representational 	You don’t access the real object—you access a copy (e.g., JSON or HTML of it)
State 	The data or condition of something (like your cart contents)
Transfer 	Moving that data between client (you) and server (app backend)
🖼️ How REST Works – Step-by-Step

    Resources (like users, products, orders) are given URLs (like api/products/1)

    The client (browser or app) sends an HTTP request like:
        GET → to read
        POST → to add
        PUT → to update
        DELETE → to delete

    The server sends back a representation (usually in JSON or XML)

🧱 Example: REST in a Shopping App
Action 	HTTP Method 	URL 	What Happens
See products 	GET 	/products 	Get list of all products
See one product 	GET 	/products/5 	Get product with ID 5
Add a product 	POST 	/products 	Add a new product
Update product 	PUT 	/products/5 	Replace product with ID 5
Delete product 	DELETE 	/products/5 	Remove product with ID 5
REST Has 6 Simple Rules (called Constraints)

    Client-Server: Separate frontend (browser/app) from backend (server).
    Stateless: Each request stands alone. Server doesn’t remember past requests.
    Cacheable: Responses can be stored to reduce load and speed things up.
    Uniform Interface: All resources are accessed using the same method (like GET/POST).
    Layered System: You can have layers like proxies or load balancers in between.
    Code on Demand (optional): Server can send code (like JavaScript) to the client to run.

✅ Summary (In Easy Words)
Term 	Meaning
REST 	A design style for creating web services
Not a protocol 	It uses HTTP but it's not HTTP itself
Resource 	Any piece of data (user, product, etc.)
Representation 	A copy of the data (like JSON) sent to the client
Stateless 	Every request is treated like a brand-new one
What Does HATEOAS Mean?

HATEOAS stands for:

    Hypermedia As The Engine Of Application State

🟢 It's a part of REST that says:

    The server should guide the client by sending links in its responses, so the client knows what to do next — just like how you browse a website.

📖 Real-Life Analogy: Browsing a Website

Think about how you use a website:

    You land on the homepage
    You see links like "About", "Products", "Contact"
    You click a link to go to the next page
    You don’t need to memorize URLs — you just follow the links provided

✅ That’s exactly what HATEOAS means for computers talking via REST APIs.
🤖 In REST APIs (Without HATEOAS vs With HATEOAS)
❌ Without HATEOAS:

The client must already know:

    All the URLs (/users, /orders, /cart)
    What it’s allowed to do

It’s like someone saying:

    “Go to store.com/api/products, then store.com/api/cart, and then store.com/api/checkout” Even before you start.

This is fragile. If URLs change, the client breaks.
✅ With HATEOAS:

You only start with one known URL, like:

GET /api

And the server replies with:

{
  "links": {
    "products": "/api/products",
    "cart": "/api/cart",
    "checkout": "/api/checkout"
  }
}

🔗 Now the client follows these links, like a map.

    It’s like the server says: “Here’s what you can do next!”

🔄 Example in REST API (JSON)

Let’s say you get a user profile:

{
  "id": 1,
  "name": "Wania",
  "links": {
    "self": "/api/users/1",
    "update": "/api/users/1",
    "delete": "/api/users/1",
    "orders": "/api/users/1/orders"
  }
}

✅ Now the client knows:

    How to view this user
    How to update/delete the user
    How to get their orders

And it doesn’t need to memorize anything!
🔑 Why is HATEOAS Useful?
Benefit 	Simple Explanation
🔄 Flexible 	Server can change URLs without breaking the client
🧭 Discoverable 	Clients don’t need a full guide or list of all actions
🔐 Secure 	Server controls what links/actions to show
🔧 Evolvable 	New features can be added without updating the client
📝 Summary
Term 	Simple Meaning
HATEOAS 	Server tells the client what it can do next
Hypermedia 	Links (like in websites) in the API response
Client starts with 1 URL 	And discovers others by following links
Less breakable 	Client doesn’t rely on hardcoded URLs
📦 Think of HATEOAS like this:

    The server is a tour guide — it doesn’t give you the whole city map at once, but at every step, it tells you what places you can go next.

Sure! Let’s explain Idempotence in very simple and easy words, so you can understand it without any confusion. We'll also use real-life examples. 😊
What is Idempotence?

    Idempotence means: “Doing the same action many times has the same effect as doing it once.”

🧃 Real-Life Example: Light Switch

Imagine you walk into a room and turn off the light:

    🔁 If you turn it off once, the light goes off ✅
    🔁 If you turn it off 5 times, it's still off ✅

➡️ Same result, no matter how many times you repeat the action ✅ This is idempotent
🍽️ Another Example: Canceling a food order

Let’s say you cancel your food order:

    You cancel once → Order is canceled
    You cancel again → It’s still canceled, nothing changes

✅ Idempotent

But now imagine you place an order:

    You press “Place Order” once → 1 pizza ordered 🍕
    You press it 3 times → 3 pizzas ordered 😱

❌ Not idempotent
🌐 In HTTP (Web Terms)

Here’s how HTTP methods behave regarding idempotence:
✅ Idempotent Methods
Method 	What It Does 	Why It's Idempotent
GET 	Get data (read only) 	Getting the same data many times doesn’t change it
HEAD 	Get only headers 	Like GET, but no body – doesn’t change anything
OPTIONS 	Ask what’s allowed 	Just asks a question, doesn’t modify anything
PUT 	Replace data 	Sending the same data multiple times replaces it again – result stays the same
DELETE 	Delete resource 	Deleting once or 10 times = still deleted

✅ Example:

PUT /users/1
{
  "name": "Wania"
}

Sending this 100 times is the same as sending it once.
❌ Non-idempotent Methods
Method 	What It Does 	Why It’s Not Idempotent
POST 	Create a new item 	Each request usually creates a new item
PATCH 	Modify part of data 	Can be idempotent, but only if handled carefully

🚫 Example:

POST /users
{
  "name": "Wania"
}

Sending this 3 times might create 3 users → Not idempotent
✅ Summary Table
Method 	Idempotent? 	Why?
GET 	✅ Yes 	Reads only
HEAD 	✅ Yes 	Reads headers
OPTIONS 	✅ Yes 	Just asks, doesn’t do
PUT 	✅ Yes 	Replaces existing data
DELETE 	✅ Yes 	Still deleted after many tries
POST 	❌ No 	Adds new items
PATCH 	⚠️ Sometimes 	Depends on how it's used
📦 Final Tip

    If repeating a request doesn’t change the result, it’s idempotent. If it adds more data or creates new things, it’s not idempotent.

REST کیا ہے؟ 

REST ویب ایپلیکیشنز بنانے کا ایک طریقہ ہے تاکہ کمپیوٹر انٹرنیٹ پر آسانی سے اور منظم طریقے سے ایک دوسرے سے بات کر سکیں۔

🔍 کیا REST ایک ٹیکنالوجی ہے؟

نہیں، REST ایک نہیں ہے: 

پروگرامنگ زبان 
سافٹ ویئر 
ٹول 
پروٹوکول جیسے HTTP یا FTP

✅ REST ایک سٹائل یا ڈیزائن پیٹرن ہے — ویب سروسز کو کیسے کام کرنا چاہیے اس کے لیے قواعد کا ایک سیٹ۔
📦 حقیقی زندگی کی تشبیہ

تصور کریں کہ آپ فوڈ ڈیلیوری ایپ استعمال کر رہے ہیں: 

آپ کھانا تلاش کرتے ہیں۔ 
آپ کارٹ میں آئٹمز شامل کرتے ہیں۔ 
آپ آرڈر دیں۔ 
آپ آرڈر کی حیثیت چیک کریں۔

یہ تمام کارروائیاں RESTful APIs کا استعمال کرتے ہوئے بیک اینڈ سرور سے بات کرکے کی جاتی ہیں۔

ہر چیز (کھانا، کارٹ، آرڈر) ایک وسیلہ ہے، اور آپ ان کی نمائندگی کے ساتھ بات چیت کر رہے ہیں۔
🔑 آرام کا مطلب ہے...
اصطلاح کا سادہ مطلب
نمائندگی کے لیے آپ حقیقی آبجیکٹ تک رسائی حاصل نہیں کرتے — آپ ایک کاپی تک رسائی حاصل کرتے ہیں (جیسے، JSON یا اس کا HTML)
کسی چیز کا ڈیٹا یا حالت بیان کریں (جیسے آپ کی ٹوکری کا مواد)
اس ڈیٹا کو کلائنٹ (آپ) اور سرور (ایپ بیک اینڈ) کے درمیان منتقل کرنا
🖼️ آرام کیسے کام کرتا ہے – مرحلہ وار 

وسائل (جیسے صارفین، مصنوعات، آرڈرز) کو یو آر ایل دیا جاتا ہے (جیسے api/products/1) 

کلائنٹ (براؤزر یا ایپ) ایک HTTP درخواست بھیجتا ہے جیسے: 
پڑھنے کے لیے → حاصل کریں۔ 
POST → شامل کرنے کے لیے 
اپ ڈیٹ کرنے کے لیے → ڈالیں۔ 
حذف کرنے کے لیے → حذف کریں۔ 

سرور ایک نمائندگی واپس بھیجتا ہے (عام طور پر JSON یا XML میں)

🧱 مثال: شاپنگ ایپ میں آرام کریں۔
ایکشن HTTP طریقہ URL کیا ہوتا ہے۔
پروڈکٹس GET/مصنوعات دیکھیں تمام پروڈکٹس کی فہرست حاصل کریں۔
ایک پروڈکٹ دیکھیں GET /products/5 ID 5 کے ساتھ پروڈکٹ حاصل کریں۔
ایک پروڈکٹ شامل کریں POST/products ایک نئی پروڈکٹ شامل کریں۔
پروڈکٹ کو اپ ڈیٹ کریں PUT/products/5 پروڈکٹ کو ID 5 سے بدل دیں۔
پروڈکٹ کو حذف کریں DELETE /products/5 ID 5 کے ساتھ پروڈکٹ کو ہٹا دیں۔
REST کے 6 آسان اصول ہیں (جسے رکاوٹیں کہتے ہیں) 

کلائنٹ-سرور: پسدید (سرور) سے فرنٹ اینڈ (براؤزر/ایپ) کو الگ کریں۔ 
بے وطن: ہر درخواست تنہا ہے۔ سرور کو ماضی کی درخواستیں یاد نہیں ہیں۔ 
کیش ایبل: بوجھ کو کم کرنے اور چیزوں کو تیز کرنے کے لیے جوابات کو ذخیرہ کیا جا سکتا ہے۔ 
یکساں انٹرفیس: ایک ہی طریقہ (جیسے GET/POST) کا استعمال کرتے ہوئے تمام وسائل تک رسائی حاصل کی جاتی ہے۔ 
پرتوں والا نظام: آپ کے درمیان پراکسی یا لوڈ بیلنسرز جیسی پرتیں ہوسکتی ہیں۔ 
کوڈ آن ڈیمانڈ (اختیاری): سرور چلانے کے لیے کلائنٹ کو کوڈ (جیسے جاوا اسکرپٹ) بھیج سکتا ہے۔

✅ خلاصہ (آسان الفاظ میں)
اصطلاحی معنی
REST ویب سروسز بنانے کے لیے ایک ڈیزائن اسٹائل
پروٹوکول نہیں یہ HTTP استعمال کرتا ہے لیکن یہ خود HTTP نہیں ہے۔
وسائل کا ڈیٹا کا کوئی حصہ (صارف، پروڈکٹ، وغیرہ)
نمائندگی کلائنٹ کو بھیجے گئے ڈیٹا کی ایک کاپی (جیسے JSON)
بے وطن ہر درخواست کو بالکل نئی کی طرح برتا جاتا ہے۔
HATEOAS کا کیا مطلب ہے؟

HATEOAS کا مطلب ہے: 

ہائپرمیڈیا ایپلیکیشن اسٹیٹ کے انجن کے طور پر

🟢 یہ REST کا ایک حصہ ہے جو کہتا ہے: 

سرور کو اپنے جوابات میں لنکس بھیج کر کلائنٹ کی رہنمائی کرنی چاہیے، تاکہ کلائنٹ کو معلوم ہو کہ آگے کیا کرنا ہے — بالکل اسی طرح جیسے آپ کسی ویب سائٹ کو براؤز کرتے ہیں۔

📖 حقیقی زندگی کی تشبیہ: ویب سائٹ کو براؤز کرنا

اس بارے میں سوچیں کہ آپ ویب سائٹ کیسے استعمال کرتے ہیں: 

آپ ہوم پیج پر اترتے ہیں۔ 
آپ "کے بارے میں"، "مصنوعات"، "رابطہ" جیسے لنکس دیکھتے ہیں 
آپ اگلے صفحے پر جانے کے لیے ایک لنک پر کلک کریں۔ 
آپ کو یو آر ایل کو حفظ کرنے کی ضرورت نہیں ہے - آپ صرف فراہم کردہ لنکس پر عمل کریں۔

✅ REST APIs کے ذریعے بات کرنے والے کمپیوٹرز کے لیے HATEOAS کا بالکل یہی مطلب ہے۔
🤖 REST APIs میں (HATEOAS بمقابلہ HATEOAS کے بغیر)
❌ بغیر HATEOAS:

کلائنٹ کو پہلے سے ہی معلوم ہونا چاہئے: 

تمام یو آر ایل (/صارفین، /آرڈرز، /کارٹ) 
اسے کیا کرنے کی اجازت ہے۔

ایسا ہی ہے جیسے کوئی کہے: 

"store.com/api/products پر جائیں، پھر store.com/api/cart، اور پھر store.com/api/checkout" شروع کرنے سے پہلے ہی۔

یہ نازک ہے۔ اگر یو آر ایل بدل جاتا ہے تو کلائنٹ ٹوٹ جاتا ہے۔
✅ HATEOAS کے ساتھ:

آپ صرف ایک معلوم URL سے شروع کرتے ہیں، جیسے:

حاصل کریں /api

اور سرور اس کے ساتھ جواب دیتا ہے:

{ 
"لنک": { 
"products": "/api/products"، 
"cart": "/api/cart"، 
"چیک آؤٹ": "/api/چیک آؤٹ" 
}
}

🔗 اب کلائنٹ نقشے کی طرح ان لنکس کی پیروی کرتا ہے۔ 

یہ اس طرح ہے جیسے سرور کہتا ہے: "یہ ہے آپ آگے کیا کر سکتے ہیں!"

🔄 REST API (JSON) میں مثال

فرض کریں کہ آپ کو صارف کا پروفائل ملتا ہے:

{ 
"id": 1، 
"نام": "وانیہ"، 
"لنک": { 
"self": "/api/users/1"، 
"update": "/api/users/1", 
"delete": "/api/users/1", 
"orders": "/api/users/1/orders" 
}
}

✅ اب کلائنٹ جانتا ہے: 

اس صارف کو کیسے دیکھیں 
صارف کو اپ ڈیٹ/ڈیلیٹ کرنے کا طریقہ 
ان کے آرڈر کیسے حاصل کیے جائیں۔

اور اسے کچھ بھی یاد کرنے کی ضرورت نہیں ہے!
🔑 HATEOAS کیوں مفید ہے؟
فائدہ سادہ وضاحت
🔄 لچکدار سرور کلائنٹ کو توڑے بغیر URLs کو تبدیل کر سکتا ہے۔
🧭 قابل دریافت کلائنٹس کو مکمل گائیڈ یا تمام اعمال کی فہرست کی ضرورت نہیں ہے۔
🔐 محفوظ سرور کنٹرول کرتا ہے کہ کون سے لنکس/ایکشنز دکھائے جائیں۔
🔧 قابل ارتقائی نئی خصوصیات کلائنٹ کو اپ ڈیٹ کیے بغیر شامل کی جا سکتی ہیں۔
📝 خلاصہ
اصطلاح کا سادہ مطلب
HATEOAS سرور کلائنٹ کو بتاتا ہے کہ وہ آگے کیا کر سکتا ہے۔
API کے جواب میں Hypermedia لنکس (جیسے ویب سائٹس میں)
کلائنٹ 1 یو آر ایل سے شروع ہوتا ہے اور لنکس کی پیروی کرکے دوسروں کو دریافت کرتا ہے۔
کم ٹوٹنے والا کلائنٹ ہارڈ کوڈ شدہ URLs پر انحصار نہیں کرتا ہے۔
📦 HATEOAS کے بارے میں اس طرح سوچیں: 

سرور ایک ٹور گائیڈ ہے — یہ آپ کو ایک ساتھ پورے شہر کا نقشہ نہیں دیتا، لیکن ہر قدم پر، یہ آپ کو بتاتا ہے کہ آپ کن جگہوں پر جا سکتے ہیں

اگلا جانا

ضرور! آئیے Idempotence کو بہت آسان اور آسان الفاظ میں بیان کرتے ہیں، تاکہ آپ اسے بغیر کسی الجھن کے سمجھ سکیں۔ ہم حقیقی زندگی کی مثالیں بھی استعمال کریں گے۔ 😊
Idempotence کیا ہے؟ 

بے حسی کا مطلب ہے: "ایک ہی عمل کو کئی بار کرنے کا وہی اثر ہوتا ہے جتنا ایک بار کرنے کا۔"

🧃 حقیقی زندگی کی مثال: لائٹ سوئچ

تصور کریں کہ آپ ایک کمرے میں جاتے ہیں اور لائٹ بند کرتے ہیں: 

🔁 ایک بار بند کر دیں تو لائٹ چلی جاتی ہے ✅ 
🔁 اگر آپ اسے 5 بار آف کرتے ہیں تو یہ اب بھی بند ہے ✅

➡️ ایک ہی نتیجہ، اس بات سے کوئی فرق نہیں پڑتا ہے کہ آپ کتنی بار عمل کو دہرائیں ✅ یہ بے حسی ہے۔
🍽️ ایک اور مثال: کھانے کا آرڈر منسوخ کرنا

مان لیں کہ آپ اپنے کھانے کا آرڈر منسوخ کر دیتے ہیں: 

آپ ایک بار منسوخ کر دیتے ہیں → آرڈر منسوخ ہو جاتا ہے۔ 
آپ دوبارہ منسوخ کریں → یہ اب بھی منسوخ ہے، کچھ بھی تبدیل نہیں ہوا۔

✅ باہمت

لیکن اب تصور کریں کہ آپ آرڈر دیتے ہیں: 

آپ ایک بار "Place Order" کو دبائیں → 1 پیزا آرڈر کیا گیا 🍕 
آپ اسے 3 بار دبائیں → 3 پیزا آرڈر کیے گئے 😱

❌ کمزور نہیں۔
🌐 HTTP میں (ویب شرائط)

یہاں یہ ہے کہ ایچ ٹی ٹی پی کے طریقے بے ضمیری کے بارے میں کیسے برتاؤ کرتے ہیں:
✅ بے حسی کے طریقے
طریقہ یہ کیا کرتا ہے یہ Idempotent کیوں ہے۔
ڈیٹا حاصل کریں (صرف پڑھنے کے لیے) ایک ہی ڈیٹا کو کئی بار حاصل کرنے سے یہ تبدیل نہیں ہوتا ہے۔
HEAD GET کی طرح صرف ہیڈرز حاصل کریں، لیکن کوئی باڈی نہیں – کچھ بھی نہیں بدلتا
اختیارات پوچھیں کیا اجازت ہے بس ایک سوال پوچھتا ہے، کسی چیز میں ترمیم نہیں کرتا ہے۔
ڈیٹا کو تبدیل کریں ایک ہی ڈیٹا کو متعدد بار بھیجنا اسے دوبارہ بدل دیتا ہے - نتیجہ وہی رہتا ہے۔
حذف کریں وسائل کو حذف کریں ایک بار یا 10 بار حذف کرنا = اب بھی حذف ہے۔

✅ مثال:

ڈالیں /صارفین/1
{ 
"نام": "وانیہ"
}

اسے 100 بار بھیجنا ایک بار بھیجنے کے برابر ہے۔
❌ غیر مقلد طریقے
طریقہ یہ کیا کرتا ہے یہ کیوں بے غیرت نہیں ہے۔
POST ایک نیا آئٹم بنائیں ہر درخواست عام طور پر ایک نئی آئٹم بناتی ہے۔
PATCH اعداد و شمار کے حصے میں ترمیم کریں ناقابل برداشت ہو سکتا ہے، لیکن صرف اس صورت میں جب اسے احتیاط سے سنبھالا جائے۔

🚫 مثال:

پوسٹ/صارفین
{ 
"نام": "وانیہ"
}

اسے 3 بار بھیجنے سے 3 صارفین پیدا ہو سکتے ہیں → بے حس نہیں۔
✅ خلاصہ ٹیبل
طریقہ Idempotent؟ کیوں؟
حاصل کریں ✅ ہاں صرف پڑھتا ہے۔
HEAD ✅ ہاں ہیڈرز پڑھتا ہے۔
اختیارات ✅ ہاں بس پوچھتا ہے، نہیں کرتا
PUT ✅ ہاں موجودہ ڈیٹا کو بدل دیتا ہے۔
DELETE ✅ ہاں بہت کوششوں کے بعد بھی ڈیلیٹ کر دیا گیا۔
پوسٹ ❌ کوئی نئی اشیاء شامل نہیں کرتا ہے۔
PATCH ⚠️ بعض اوقات اس بات پر منحصر ہوتا ہے کہ اسے کیسے استعمال کیا جاتا ہے۔
📦 فائنل ٹپ 

اگر کسی درخواست کو دہرانے سے نتیجہ تبدیل نہیں ہوتا ہے، تو یہ بے ضمیر ہے۔ اگر یہ مزید ڈیٹا شامل کرتا ہے یا نئی چیزیں تخلیق کرتا ہے، تو یہ بے جا نہیں ہے۔
