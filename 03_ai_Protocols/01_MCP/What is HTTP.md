🌐 What is HTTP?

HTTP stands for HyperText Transfer Protocol.

    It is a way for computers to talk to each other over the internet.
    Specifically, it is how your browser (like Chrome) asks for things like web pages, and how the server responds with what you asked for.

📌 Think of it like this:

    You (the browser) go to a restaurant (the server), look at the menu (webpage), and tell the waiter (HTTP) what you want. The waiter goes to the kitchen (server logic) and brings you the dish (response like HTML, JSON, image, etc.).

Why is HTTP important?

Every time you:

    Open a website
    Submit a form
    Login to a website
    Watch a video

You're using HTTP in the background!
🔄 The HTTP Request-Response Cycle (Very Important!)

This is the heart of HTTP. It’s like a conversation between two people:
👤 1. Client (You / Your Browser)

You are the client. You want something, like a webpage.
🧑‍🍳 2. Server (The Website’s Backend)

The server is like a kitchen. It prepares and gives you what you asked for.
⚙️ Step-by-step: How it works

Let’s say you visit https://example.com.
📨 Step 1: Client Sends Request

Your browser sends a request to the server. The request includes:

    Method (What action you want):
        GET: Get something (like a webpage)
        POST: Send something (like a form)

    URL (What you want to access)

    Headers (Extra info like who you are, your browser type, etc.)

    Body (Only sometimes—used when you're sending data, like login info)

🖥️ Step 2: Server Gets the Request

The server receives the request and decides:

    What is being asked?
    Is it allowed?
    Where is the data?
    Should it return a file? or a web page? or an error?

📬 Step 3: Server Sends Response

The server sends a response back. It contains:

    Status Code: Tells what happened
        200 OK: Everything went well
        404 Not Found: Page not found
        500 Internal Server Error: Something broke

    Headers: Info like file type (HTML, JSON, image), server info

    Body: The actual content (HTML page, JSON data, error message, etc.)

💻 Step 4: Browser Shows Result

Your browser processes the response and shows you the website or data.
🔄 Connection Management (Does it stay open?)

    HTTP/1.1: Usually keeps the connection open (keep-alive) so it doesn’t need to reconnect every time.
    HTTP/2: More efficient, supports multiple requests at once.
    HTTP/3 (QUIC): Even faster and more secure (uses UDP instead of TCP).

Summary Table
Part 	What It Does 	Example
Client 	Sends request 	Your browser
Server 	Sends response 	Google’s server
Request 	Ask for data 	GET /index.html
Response 	Gives back data 	200 OK + HTML
Method 	What you want 	GET, POST
Status Code 	Result 	200, 404
Header 	Extra info 	Content-Type: text/html
Body 	Main content 	Webpage, image, etc.
Common HTTP Status Codes
Code 	Meaning
200 	OK – Success
201 	Created – New resource made
400 	Bad Request – You sent something wrong
401 	Unauthorized – You need to log in
403 	Forbidden – You can’t access this
404 	Not Found – Page doesn’t exist
500 	Server Error – Something broke on the server
Conclusion

HTTP is like a postal system for the web. You send a letter (request), and the post office (server) sends back a reply (response).

Once you understand request → response flow, you're already halfway into understanding how the web works.
✅ 2. Structure of an HTTP Message

Whenever your browser talks to a server (like when loading a website), they exchange HTTP messages.

There are two types of messages:

    📤 Request → Sent by the client (browser)
    📥 Response → Sent by the server

✉️ Structure (Applies to Both Requests and Responses)
Part 	What It Is 	Example
Start Line 	First line (action or status) 	GET /home HTTP/1.1 or HTTP/1.1 200 OK
Headers 	Key-value pairs (extra info) 	Content-Type: text/html
Blank Line 	Separates headers from body 	Just one empty line
Body 	Actual content (optional) 	HTML, JSON, file, etc.
📤 Request Example (from browser to server):

GET /about HTTP/1.1
Host: example.com
User-Agent: Chrome/123.0
Accept: text/html

✅ No body here because we’re just requesting a page.
📥 Response Example (from server to browser):

HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 38

<html><body>Hello, World!</body></html>

✅ This time the body is included — the actual web page.
🧠 Summary of Each Part
Part 	Meaning
Start Line 	Tells what’s happening (GET request or 200 OK response)
Headers 	Extra details like what kind of data is being sent
Empty Line 	A required separator between headers and body
Body 	The actual stuff being sent (page content, data, etc.)
✅ 3. Common HTTP Methods (also called Verbs)

These are actions that a client can request from the server. Think of them like commands.
🔨 List of Common Methods (with Examples)
Method 	What It Does 	Simple Example
GET 	Get data or a page 	GET /home → Fetch home page
POST 	Send data to server (like a form) 	POST /signup → Create new account
PUT 	Update (replace) a resource 	PUT /user/1 → Replace user info
DELETE 	Remove a resource 	DELETE /user/1 → Delete user 1
HEAD 	Just get headers, no body 	Check if a file exists
OPTIONS 	Ask server what methods it allows 	For CORS (cross-origin requests)
PATCH 	Partially update a resource 	PATCH /user/1 → Update user’s email only
🧃 Analogy: Ordering at a Café
Action 	HTTP Method
Looking at the menu 	GET /menu
Placing an order 	POST /order
Changing your whole order 	PUT /order/5
Cancelling your order 	DELETE /order/5
Asking what payment types they accept 	OPTIONS /payment
Asking for receipt only (no food) 	HEAD /receipt
Changing only 1 item in your order 	PATCH /order/5
🎯 Final Recap
Structure of HTTP Message:

    Start line → Command or response
    Headers → Extra info
    Empty line → Divider
    Body → Actual data (optional)

HTTP Methods:

    GET: Read
    POST: Create
    PUT: Replace
    PATCH: Modify
    DELETE: Remove
    HEAD: Only metadata
    OPTIONS: Ask capabilities

🌐 HTTP کیا ہے؟

HTTP کا مطلب ہے ہائپر ٹیکسٹ ٹرانسفر پروٹوکول۔ 

یہ کمپیوٹر کے لیے انٹرنیٹ پر ایک دوسرے سے بات کرنے کا ایک طریقہ ہے۔ 
خاص طور پر، یہ ہے کہ آپ کا براؤزر (جیسے کروم) ویب صفحات جیسی چیزوں کے بارے میں کیسے پوچھتا ہے، اور سرور آپ کے مانگے ہوئے جوابات کا کیسے جواب دیتا ہے۔

📌 اس کے بارے میں اس طرح سوچیں: 

آپ (براؤزر) کسی ریستوراں (سرور) پر جاتے ہیں، مینو (ویب پیج) کو دیکھتے ہیں، اور ویٹر (HTTP) کو بتائیں کہ آپ کیا چاہتے ہیں۔ ویٹر کچن میں جاتا ہے (سرور لاجک) اور آپ کے لیے ڈش لاتا ہے (ایچ ٹی ایم ایل، JSON، امیج وغیرہ جیسے جواب)۔

HTTP کیوں اہم ہے؟

ہر بار جب آپ: 

ایک ویب سائٹ کھولیں۔ 
ایک فارم جمع کروائیں۔ 
کسی ویب سائٹ پر لاگ ان کریں۔ 
ایک ویڈیو دیکھیں

آپ پس منظر میں HTTP استعمال کر رہے ہیں!
🔄 HTTP درخواست جوابی سائیکل (بہت اہم!)

یہ HTTP کا دل ہے۔ یہ دو لوگوں کے درمیان گفتگو کی طرح ہے:
👤 1. کلائنٹ (آپ / آپ کا براؤزر)

آپ کلائنٹ ہیں. آپ کچھ چاہتے ہیں، جیسے ویب صفحہ۔
🧑‍🍳 2. سرور (ویب سائٹ کا بیک اینڈ)

سرور ایک باورچی خانے کی طرح ہے۔ یہ تیار کرتا ہے اور آپ کو دیتا ہے جو آپ نے مانگا ہے۔
⚙️ مرحلہ وار: یہ کیسے کام کرتا ہے۔

مان لیں کہ آپ https://example.com ملاحظہ کرتے ہیں۔
📨 مرحلہ 1: کلائنٹ درخواست بھیجتا ہے۔

آپ کا براؤزر سرور کو ایک درخواست بھیجتا ہے۔ درخواست میں شامل ہیں: 

طریقہ (آپ کون سا عمل چاہتے ہیں): 
GET: کچھ حاصل کریں (جیسے ویب صفحہ) 
پوسٹ: کچھ بھیجیں (جیسے فارم) 

URL (جس تک آپ رسائی حاصل کرنا چاہتے ہیں) 

ہیڈر (اضافی معلومات جیسے کہ آپ کون ہیں، آپ کے براؤزر کی قسم وغیرہ) 

باڈی (صرف کبھی کبھار استعمال کیا جاتا ہے جب آپ ڈیٹا بھیج رہے ہوتے ہیں، جیسے لاگ ان کی معلومات)

🖥️ مرحلہ 2: سرور کو درخواست ملتی ہے۔

سرور درخواست وصول کرتا ہے اور فیصلہ کرتا ہے: 

کیا پوچھا جا رہا ہے؟ 
کیا اس کی اجازت ہے؟ 
ڈیٹا کہاں ہے؟ 
کیا اسے فائل واپس کرنی چاہئے؟ یا ویب صفحہ؟ یا ایک غلطی؟

📬 مرحلہ 3: سرور جواب بھیجتا ہے۔

سرور واپس جواب بھیجتا ہے۔ اس میں شامل ہیں: 

اسٹیٹس کوڈ: بتاتا ہے کہ کیا ہوا ہے۔ 
200 ٹھیک ہے: سب کچھ ٹھیک چلا گیا۔ 
404 نہیں ملا: صفحہ نہیں ملا 
500 اندرونی سرور کی خرابی: کچھ ٹوٹ گیا۔ 

ہیڈر: معلومات جیسے فائل کی قسم (HTML، JSON، تصویر)، سرور کی معلومات 

باڈی: اصل مواد (HTML صفحہ، JSON ڈیٹا، غلطی کا پیغام، وغیرہ)

💻 مرحلہ 4: براؤزر نتیجہ دکھاتا ہے۔

آپ کا براؤزر جواب پر کارروائی کرتا ہے اور آپ کو ویب سائٹ یا ڈیٹا دکھاتا ہے۔
🔄 کنکشن مینجمنٹ (کیا یہ کھلا رہتا ہے؟) 

HTTP/1.1: عام طور پر کنکشن کو کھلا رکھتا ہے (کیپ لائیو) اس لیے اسے ہر بار دوبارہ جوڑنے کی ضرورت نہیں ہے۔ 
HTTP/2: زیادہ موثر، ایک ساتھ متعدد درخواستوں کی حمایت کرتا ہے۔ 
HTTP/3 (QUIC): اس سے بھی تیز اور زیادہ محفوظ (TCP کی بجائے UDP استعمال کرتا ہے)۔

خلاصہ ٹیبل
حصہ یہ کیا کرتا ہے مثال
کلائنٹ آپ کے براؤزر کی درخواست بھیجتا ہے۔
سرور گوگل کا سرور جواب بھیجتا ہے۔
ڈیٹا کے لیے درخواست کریں GET /index.html
جواب ڈیٹا 200 OK + HTML واپس دیتا ہے۔
طریقہ جو آپ چاہتے ہیں حاصل کریں، پوسٹ کریں۔
اسٹیٹس کوڈ کا نتیجہ 200, 404
ہیڈر اضافی معلومات مواد کی قسم: متن/html
باڈی مین مواد ویب صفحہ، تصویر، وغیرہ۔
عام HTTP اسٹیٹس کوڈز
کوڈ کا مطلب
200 ٹھیک ہے - کامیابی
201 تخلیق کیا گیا - نیا وسیلہ بنایا گیا۔
400 غلط درخواست - آپ نے کچھ غلط بھیجا ہے۔
401 غیر مجاز - آپ کو لاگ ان کرنا ہوگا۔
403 حرام - آپ اس تک رسائی حاصل نہیں کر سکتے
404 نہیں ملا - صفحہ موجود نہیں ہے۔
500 سرور کی خرابی - سرور پر کچھ ٹوٹ گیا۔
نتیجہ

HTTP ویب کے لیے ایک پوسٹل سسٹم کی طرح ہے۔ آپ ایک خط (درخواست) بھیجتے ہیں، اور پوسٹ آفس (سرور) جواب (جواب) بھیجتا ہے۔

ایک بار جب آپ درخواست → ردعمل کے بہاؤ کو سمجھ لیتے ہیں، تو آپ یہ سمجھنے میں آدھے راستے پر ہیں کہ ویب کیسے کام کرتا ہے۔
✅ 2. HTTP پیغام کا ڈھانچہ

جب بھی آپ کا براؤزر کسی سرور سے بات کرتا ہے (جیسے ویب سائٹ لوڈ کرتے وقت)، وہ HTTP پیغامات کا تبادلہ کرتے ہیں۔

پیغامات کی دو قسمیں ہیں: 

📤 درخواست → کلائنٹ کی طرف سے بھیجی گئی (براؤزر) 
📥 جواب → سرور کے ذریعے بھیجا گیا۔

✉️ ساخت (درخواستوں اور جوابات دونوں پر لاگو ہوتا ہے)
حصہ یہ کیا ہے مثال
سٹارٹ لائن پہلی لائن (ایکشن یا سٹیٹس) GET /home HTTP/1.1 یا HTTP/1.1 200 ٹھیک ہے
ہیڈر کلیدی قدر کے جوڑے (اضافی معلومات) مواد کی قسم: متن/html
خالی لائن ہیڈر کو باڈی سے الگ کرتی ہے صرف ایک خالی لائن
باڈی ایکچوئل مواد (اختیاری) HTML، JSON، فائل وغیرہ۔
📤 درخواست کی مثال (براؤزر سے سرور تک):

HTTP/1.1 کے بارے میں حاصل کریں۔
میزبان: example.com
صارف کا ایجنٹ: کروم/123.0
قبول کریں: متن/html

✅ یہاں کوئی باڈی نہیں ہے کیونکہ ہم صرف ایک صفحہ کی درخواست کر رہے ہیں۔
📥 جوابی مثال (سرور سے براؤزر تک):

HTTP/1.1 200 ٹھیک ہے۔
مواد کی قسم: متن/html
مواد کی لمبائی: 38

<html><body>ہیلو، ورلڈ!</body></html>

✅ اس بار باڈی شامل ہے — اصل ویب صفحہ۔
🧠 ہر حصے کا خلاصہ
جزوی معنی
اسٹارٹ لائن بتاتی ہے کہ کیا ہو رہا ہے (گیٹ درخواست یا 200 ٹھیک جواب)
ہیڈرز اضافی تفصیلات جیسے کہ کس قسم کا ڈیٹا بھیجا جا رہا ہے۔
خالی لائن ہیڈر اور باڈی کے درمیان ایک مطلوبہ جداکار
باڈی اصل چیز بھیجی جا رہی ہے (صفحہ کا مواد، ڈیٹا، وغیرہ)
✅ 3. عام HTTP طریقے (جسے فعل بھی کہا جاتا ہے)

یہ وہ اعمال ہیں جن کی درخواست کلائنٹ سرور سے کر سکتا ہے۔ ان کے بارے میں احکامات کی طرح سوچیں۔
🔨 عام طریقوں کی فہرست (مثالوں کے ساتھ)
طریقہ یہ کیا کرتا ہے سادہ مثال
ڈیٹا حاصل کریں یا صفحہ حاصل کریں GET /home → ہوم پیج حاصل کریں۔
POST سرور پر ڈیٹا بھیجیں (جیسے فارم) POST/signup → نیا اکاؤنٹ بنائیں
ڈالو

ایک وسیلہ کو اپ ڈیٹ کریں (تبدیل کریں) PUT /user/1 → صارف کی معلومات کو تبدیل کریں۔
DELETE ایک وسیلہ کو ہٹائیں DELETE /user/1 → صارف 1 کو حذف کریں۔
HEAD صرف ہیڈرز حاصل کریں، کوئی باڈی نہیں چیک کریں کہ آیا کوئی فائل موجود ہے۔
آپشنز سرور سے پوچھیں کہ یہ CORS کے لیے کن طریقوں کی اجازت دیتا ہے (کراس اوریجن درخواستیں)
PATCH جزوی طور پر وسائل کو اپ ڈیٹ کریں PATCH /user/1 → صرف صارف کا ای میل اپ ڈیٹ کریں
🧃 تشبیہ: کیفے میں آرڈر کرنا
ایکشن HTTP طریقہ
مینو کو دیکھ کر GET/menu
آرڈر پوسٹ / آرڈر دینا
اپنے پورے آرڈر کو تبدیل کرنا PUT /order/5
آپ کا آرڈر منسوخ کرنا DELETE /order/5
یہ پوچھنا کہ وہ کس قسم کی ادائیگی کو قبول کرتے ہیں آپشنز/ادائیگی
صرف رسید مانگنا (کھانا نہیں) ہیڈ / رسید
آپ کے آرڈر میں صرف 1 آئٹم کو تبدیل کرنا PATCH/order/5
🎯 فائنل ریکیپ
HTTP پیغام کی ساخت: 

شروع لائن → کمانڈ یا جواب 
ہیڈرز → اضافی معلومات 
خالی لائن → ڈیوائیڈر 
باڈی → اصل ڈیٹا (اختیاری)

HTTP طریقے: 

حاصل کریں: پڑھیں 
پوسٹ: تخلیق کریں۔ 
ڈالیں: بدل دیں۔ 
پیچ: ترمیم کریں۔ 
حذف کریں: ہٹا دیں۔ 
ہیڈ: صرف میٹا ڈیٹا 
اختیارات: صلاحیتوں سے پوچھیں۔

