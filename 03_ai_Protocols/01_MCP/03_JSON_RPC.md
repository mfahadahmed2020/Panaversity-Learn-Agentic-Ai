Introduction to JSON-RPC 2.0

Specification
Learn by Trying JSON-RPC Requests Online

Interactively explore JSON-RPC by sending requests and observing responses in real time.

Explore and experiment with JSON-RPC requests and responses using this online tool:

JSON-RPC Playground
What is JSON-RPC 2.0?

JSON-RPC 2.0 is a lightweight and stateless remote procedure call (RPC) protocol that allows for notifications and remote procedure calls in a simple, standardized way. It uses JSON (JavaScript Object Notation) as its data format, making it easy to use with a wide variety of programming languages and platforms. The protocol is transport-agnostic, meaning it can be used over HTTP, WebSockets, or any other message-passing environment.

At its core, JSON-RPC 2.0 defines a set of data structures and the rules for their processing. It's designed for simplicity and is a popular choice for building APIs and distributed systems.
Key Concepts
1. Request Object

A remote procedure call is initiated by sending a Request object to a server. This object has the following members:

    jsonrpc: A string that specifies the version of the JSON-RPC protocol. For version 2.0, this MUST be exactly "2.0".
    method: A string containing the name of the method to be invoked on the server.
    params: A structured value (either an Array or Object) that holds the parameters for the method. This member can be omitted if the method doesn't require any parameters.
    id: An identifier established by the client. It can be a string, a number, or null. If it's not included, the request is considered a "notification."

2. Notification

A notification is a special type of Request object that does not include the id member. When a client sends a notification, it's signaling that it's not interested in a response from the server. The server MUST NOT reply to a notification.

Notifications are useful for one-way communication, like sending events or logging information. However, because they don't have a corresponding response, the client won't be aware of any errors that might occur.
3. Parameter Structures

When calling a method with parameters, the params member can be structured in two ways:

    By-position: The params member is an Array of values, where each value corresponds to a parameter in the order the server expects.
    By-name: The params member is an Object, where each key-value pair represents a named parameter.

4. Response Object

When a client makes a standard RPC call (not a notification), the server MUST reply with a Response object. This object contains the following members:

    jsonrpc: The JSON-RPC protocol version, which MUST be "2.0".
    result: This member is REQUIRED on success. Its value is determined by the method that was invoked on the server. If there was an error, this member MUST NOT be included.
    error: This member is REQUIRED on error. If there was no error, this member MUST NOT be included. The value of this member is an Error object.
    id: This member is REQUIRED and MUST be the same as the id from the Request object.

A Response object MUST contain either the result or the error member, but not both.
5. Error Object

If an error occurs during an RPC call, the Response object will contain an error member with the following structure:

    code: An integer that indicates the type of error.
    message: A short, single-sentence description of the error.
    data: A primitive or structured value with additional information about the error. This is optional and its format is defined by the server.

Here are some predefined error codes:
Code 	Message 	Meaning
-32700 	Parse error 	Invalid JSON was received by the server.
-32600 	Invalid Request 	The JSON sent is not a valid Request object.
-32601 	Method not found 	The method does not exist or is not available.
-32602 	Invalid params 	Invalid method parameter(s).
-32603 	Internal error 	Internal JSON-RPC error.
-32000 to -32099 	Server error 	Reserved for implementation-defined server errors.
6. Batch Requests

To send multiple Request objects at once, a client can send an Array of Request objects. The server will process all the requests and respond with an Array of the corresponding Response objects. The server can process a batch of requests in any order, and the responses can also be in any order. The client should use the id of each request to match it with its response.
Examples

Here are some examples of JSON-RPC 2.0 in action:

RPC call with positional parameters:

Client sends:

{"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": 1}

Server responds:

{"jsonrpc": "2.0", "result": 19, "id": 1}

RPC call with named parameters:

Client sends:

{"jsonrpc": "2.0", "method": "subtract", "params": {"subtrahend": 23, "minuend": 42}, "id": 3}

Server responds:

{"jsonrpc": "2.0", "result": 19, "id": 3}

A notification:

Client sends:

{"jsonrpc": "2.0", "method": "update", "params": [1, 2, 3, 4, 5]}

(No response from the server)

RPC call to a non-existent method:

Client sends:

{"jsonrpc": "2.0", "method": "foobar", "id": "1"}

Server responds:

{"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": "1"}

Extensions

Method names that start with rpc. are reserved for system extensions and should not be used for anything else.
Why JSON-RPC for Model Context Protocol (MCP), not REST?

Model Context Protocol (MCP) chooses JSON-RPC over REST for several technical and strategic reasons. Understanding this will also give you an edge in designing or integrating agent frameworks!
1. Agent/Model Operations Need More Than REST’s CRUD

REST is built around CRUD (Create, Read, Update, Delete), mapping HTTP verbs (GET, POST, PUT, DELETE) to resources. But LLM/Agent orchestration protocols like MCP need something different:

    Procedural/Command-like Interactions: MCP sessions involve rich operations—start, cancel, resume, stream, call tool, manage prompt state, etc.—that don’t map neatly to CRUD.

JSON-RPC is designed for remote procedure calls (Calling a function on another computer, as if it was a local function in your code.) — “Do this specific thing for me and return the result”—making it a natural fit.
2. Multiplexing & Streaming Support

    Multiple calls on the same connection: JSON-RPC is naturally suited to protocols that need to keep an open channel (e.g., WebSocket, HTTP/2, SSE) and send multiple commands and responses in real-time. REST (over HTTP 1.1) usually opens a new connection/request per action.
    Streaming & Notifications: With agents, you might want progress updates, partial results, or server-initiated messages (notifications). JSON-RPC supports notifications (one-way messages), which is not idiomatic in REST.

3. Explicit Method Names and Structured Requests

    In REST, the endpoint and verb define the operation. In JSON-RPC, you get {"method": "tools/call", ...}—the action is explicit and discoverable, not hidden in URL/HTTP verb combos.
    Easy to extend: Adding new capabilities (new methods) doesn’t require inventing new URLs or overloading HTTP semantics.

4. Stateless vs. Stateful Workflows

    MCP can run stateful workflows (sessions, resumption, tool resources, etc.), which benefit from a protocol that can express both state changes and direct procedure invocations.

    REST is best for stateless, resource-centric operations.
    How can MCP do stateful things if JSON-RPC is stateless?

        The “state” is maintained by the server (or agent), not the protocol.

        MCP uses things like session_id, context_id, or other tokens/IDs to let the server keep track of ongoing workflows or conversations.

        Each JSON-RPC call includes the necessary information (like the session/context) so the server knows which workflow or conversation it’s handling.

5. Strong Error Handling

    JSON-RPC defines a standard, structured error response (error with code, message, data) for every request.
    REST error handling is less standardized and can be messy (status codes + arbitrary payloads).

6. Ecosystem and Alignment with IDE Protocols

    LLM agents and tools are inspired by language servers, debuggers, IDE plugins, etc.—many of which use JSON-RPC.
    Examples: LSP (Language Server Protocol), Debug Adapter Protocol—both JSON-RPC-based!

Summary Table
Feature 	REST 	JSON-RPC (used by MCP)
Paradigm 	Resource/CRUD 	Remote Procedure Call (RPC)
Operations 	Limited to HTTP verbs 	Arbitrary named methods
Streaming 	Tricky, non-standard 	Native via WebSocket/SSE
Multiplexing 	New HTTP req for each op 	Multiple in single connection
Notifications 	Not idiomatic 	Built-in
Error Handling 	Varies, not standardized 	Structured, part of protocol
Statefulness 	Stateless best practice 	Can support sessions/state
Extensibility 	Needs URL/method changes 	Just add new methods
Forward-Looking Take:

Protocols like MCP are designed for the future of AI orchestration, not just simple CRUD APIs. They need:

    Fine-grained control over model context and tools,
    Real-time interactivity and notifications,
    Consistency and extensibility.

JSON-RPC is purpose-built for these requirements, making it a far better fit than REST for advanced agent/model protocols. If you're planning to design LLM-based systems or integrate AI agents at scale, understanding and leveraging these design choices puts you way ahead!

JSON-RPC 2.0 کا تعارف

تفصیلات
آن لائن JSON-RPC درخواستیں آزما کر سیکھیں۔

درخواستیں بھیج کر اور حقیقی وقت میں جوابات کا مشاہدہ کرکے JSON-RPC کو انٹرایکٹو طریقے سے دریافت کریں۔

اس آن لائن ٹول کا استعمال کرتے ہوئے JSON-RPC کی درخواستوں اور جوابات کو دریافت اور تجربہ کریں:

JSON-RPC کھیل کا میدان
JSON-RPC 2.0 کیا ہے؟

JSON-RPC 2.0 ایک ہلکا پھلکا اور سٹیٹ لیس ریموٹ پروسیجر کال (RPC) پروٹوکول ہے جو ایک سادہ، معیاری طریقے سے اطلاعات اور ریموٹ پروسیجر کالز کی اجازت دیتا ہے۔ یہ JSON (JavaScript آبجیکٹ نوٹیشن) کو اپنے ڈیٹا فارمیٹ کے طور پر استعمال کرتا ہے، جس سے پروگرامنگ زبانوں اور پلیٹ فارمز کی وسیع اقسام کے ساتھ استعمال کرنا آسان ہوتا ہے۔ پروٹوکول ٹرانسپورٹ ایگنوسٹک ہے، یعنی اسے HTTP، WebSockets، یا کسی دوسرے پیغام سے گزرنے والے ماحول پر استعمال کیا جا سکتا ہے۔

اس کے بنیادی طور پر، JSON-RPC 2.0 ڈیٹا ڈھانچے کا ایک سیٹ اور ان کی پروسیسنگ کے قواعد کی وضاحت کرتا ہے۔ یہ سادگی کے لیے ڈیزائن کیا گیا ہے اور APIs اور تقسیم شدہ نظاموں کی تعمیر کے لیے ایک مقبول انتخاب ہے۔
کلیدی تصورات
1. اعتراض کی درخواست کریں۔

ایک ریموٹ طریقہ کار کال کا آغاز سرور کو درخواست آبجیکٹ بھیج کر کیا جاتا ہے۔ اس اعتراض کے درج ذیل ارکان ہیں: 

jsonrpc: ایک سٹرنگ جو JSON-RPC پروٹوکول کے ورژن کی وضاحت کرتی ہے۔ ورژن 2.0 کے لیے، یہ بالکل "2.0" ہونا چاہیے۔ 
طریقہ: سرور پر استعمال کیے جانے والے طریقہ کے نام پر مشتمل ایک تار۔ 
params: ایک سٹرکچرڈ ویلیو (یا تو ایک Array یا Object) جس میں طریقہ کار کے پیرامیٹرز ہوتے ہیں۔ اگر طریقہ کار میں کسی پیرامیٹرز کی ضرورت نہیں ہے تو اس رکن کو چھوڑا جا سکتا ہے۔ 
id: ایک شناخت کنندہ جو کلائنٹ کے ذریعہ قائم کیا گیا ہے۔ یہ ایک سٹرنگ، ایک نمبر، یا null ہو سکتا ہے۔ اگر یہ شامل نہیں ہے تو، درخواست کو "اطلاع" سمجھا جاتا ہے۔

2. اطلاع

اطلاع ایک خاص قسم کی درخواست آبجیکٹ ہے جس میں آئی ڈی ممبر شامل نہیں ہوتا ہے۔ جب ایک کلائنٹ ایک اطلاع بھیجتا ہے، تو یہ اشارہ دے رہا ہے کہ اسے سرور کے جواب میں دلچسپی نہیں ہے۔ سرور کو کسی اطلاع کا جواب نہیں دینا چاہیے۔

اطلاعات یک طرفہ مواصلت کے لیے کارآمد ہیں، جیسے واقعات بھیجنا یا معلومات کو لاگ کرنا۔ تاہم، چونکہ ان کے پاس متعلقہ جواب نہیں ہے، اس لیے کلائنٹ کسی بھی غلطی سے آگاہ نہیں ہوگا جو ہو سکتی ہے۔
3. پیرامیٹر سٹرکچرز

پیرامیٹرز کے ساتھ کسی طریقہ کو کال کرتے وقت، پیرامز ممبر کو دو طریقوں سے تشکیل دیا جا سکتا ہے: 

بذریعہ پوزیشن: پیرامز ممبر اقدار کی ایک صف ہے، جہاں ہر قدر ایک پیرامیٹر سے مطابقت رکھتی ہے جس ترتیب سے سرور کی توقع ہے۔ 
بذریعہ نام: پیرامز ممبر ایک آبجیکٹ ہے، جہاں ہر کلیدی قدر کا جوڑا ایک نامزد پیرامیٹر کی نمائندگی کرتا ہے۔

4. جوابی اعتراض

جب کوئی کلائنٹ معیاری RPC کال کرتا ہے (اطلاع نہیں)، تو سرور کو جوابی اعتراض کے ساتھ جواب دینا چاہیے۔ یہ اعتراض درج ذیل ارکان پر مشتمل ہے: 

jsonrpc: JSON-RPC پروٹوکول ورژن، جو "2.0" ہونا چاہیے۔ 
نتیجہ: کامیابی پر اس رکن کی ضرورت ہے۔ اس کی قدر کا تعین اس طریقہ سے ہوتا ہے جسے سرور پر استعمال کیا گیا تھا۔ اگر کوئی غلطی تھی تو اس ممبر کو شامل نہیں کیا جانا چاہیے۔ 
غلطی: غلطی پر اس رکن کی ضرورت ہے۔ اگر کوئی غلطی نہیں تھی تو اس ممبر کو شامل نہیں کیا جانا چاہیے۔ اس ممبر کی قدر ایک ایرر آبجیکٹ ہے۔ 
id: اس رکن کی ضرورت ہے اور اسے درخواست آبجیکٹ کی آئی ڈی جیسا ہی ہونا چاہیے۔

ایک رسپانس آبجیکٹ میں یا تو نتیجہ یا ایرر ممبر ہونا چاہیے، لیکن دونوں نہیں۔
5. ایرر آبجیکٹ

اگر آر پی سی کال کے دوران کوئی ایرر آجاتا ہے تو ریسپانس آبجیکٹ میں درج ذیل ڈھانچے کے ساتھ ایرر ممبر ہوگا: 

کوڈ: ایک عدد جو غلطی کی قسم کی نشاندہی کرتا ہے۔ 
پیغام: غلطی کی ایک مختصر، واحد جملے کی وضاحت۔ 
ڈیٹا: غلطی کے بارے میں اضافی معلومات کے ساتھ ایک قدیم یا ساختی قدر۔ یہ اختیاری ہے اور اس کا فارمیٹ سرور کے ذریعہ بیان کیا گیا ہے۔

یہاں کچھ پہلے سے طے شدہ ایرر کوڈز ہیں:
کوڈ میسج کا مطلب
-32700 تجزیہ کی خرابی غلط JSON سرور کو موصول ہوئی تھی۔
-32600 غلط درخواست JSON بھیجی گئی ایک درست درخواست آبجیکٹ نہیں ہے۔
-32601 طریقہ نہیں ملا طریقہ موجود نہیں ہے یا دستیاب نہیں ہے۔
-32602 غلط پیرامیٹرز غلط طریقہ پیرامیٹر۔
-32603 اندرونی خرابی اندرونی JSON-RPC کی خرابی۔
-32000 سے -32099 سرور کی خرابی نفاذ کی وضاحت کردہ سرور کی خرابیوں کے لیے محفوظ ہے۔
6. بیچ کی درخواستیں

ایک ساتھ متعدد ریکوئسٹ آبجیکٹ بھیجنے کے لیے، ایک کلائنٹ درخواست کی اشیاء کی ایک صف بھیج سکتا ہے۔ سرور تمام درخواستوں پر کارروائی کرے گا اور متعلقہ رسپانس آبجیکٹ کی ایک صف کے ساتھ جواب دے گا۔ سرور کسی بھی ترتیب میں درخواستوں کے بیچ پر کارروائی کر سکتا ہے، اور جوابات بھی کسی بھی ترتیب میں ہو سکتے ہیں۔ کلائنٹ کو ہر درخواست کی آئی ڈی کو اس کے جواب کے ساتھ ملانے کے لیے استعمال کرنا چاہیے۔
مثالیں

عمل میں JSON-RPC 2.0 کی کچھ مثالیں یہ ہیں:

پوزیشنی پیرامیٹرز کے ساتھ RPC کال:

کلائنٹ بھیجتا ہے:

{"jsonrpc": "2.0"، "طریقہ": "منقطع کریں"، "پیرامس": [42، 23]، "id": 1}

سرور جواب دیتا ہے:

{"jsonrpc": "2.0"، "نتائج": 19، "id": 1}

نامزد پیرامیٹرز کے ساتھ RPC کال:

کلائنٹ بھیجتا ہے:

{"jsonrpc": "2.0", "طریقہ": "subtract", "params": {"subtrahend": 23, "minuend": 42}, "id": 3}

سرور جواب دیتا ہے:

{"jsonrpc": "2.0"، "نتائج": 19، "id": 3}

ایک اطلاع:

کلائنٹ بھیجتا ہے:

{"jsonrpc": "2.0"، "طریقہ": "اپ ڈیٹ"، "پیرامز": [1، 2، 3، 4، 5]}

(سرور سے کوئی جواب نہیں)

RPC c

سب ایک غیر موجود طریقہ پر:

کلائنٹ بھیجتا ہے:

{"jsonrpc": "2.0", "طریقہ": "foobar", "id": "1"}

سرور جواب دیتا ہے:

{"jsonrpc": "2.0", "error": {"code": -32601, "message": "طریقہ نہیں ملا"}, "id": "1"}

ایکسٹینشنز

طریقہ کے نام جو rpc سے شروع ہوتے ہیں۔ سسٹم کی توسیع کے لیے مخصوص ہیں اور کسی اور چیز کے لیے استعمال نہیں ہونا چاہیے۔
ماڈل سیاق و سباق پروٹوکول (MCP) کے لیے JSON-RPC، REST کیوں نہیں؟

ماڈل سیاق و سباق پروٹوکول (MCP) کئی تکنیکی اور اسٹریٹجک وجوہات کی بنا پر REST پر JSON-RPC کا انتخاب کرتا ہے۔ اس کو سمجھنا آپ کو ایجنٹ کے فریم ورک کو ڈیزائن کرنے یا انٹیگریٹ کرنے میں بھی برتری دے گا!
1. ایجنٹ/ماڈل آپریشنز کو REST کے CRUD سے زیادہ کی ضرورت ہے۔

REST CRUD کے ارد گرد بنایا گیا ہے (تخلیق کریں، پڑھیں، اپ ڈیٹ کریں، حذف کریں)، HTTP فعل (GET، POST، PUT، DELETE) کو وسائل میں نقشہ بناتا ہے۔ لیکن LLM/Agent آرکیسٹریشن پروٹوکول جیسے MCP کو کچھ مختلف کی ضرورت ہے: 

طریقہ کار/کمانڈ جیسی تعاملات: MCP سیشنز میں بھرپور آپریشنز شامل ہوتے ہیں—شروع، منسوخ، دوبارہ شروع، سلسلہ، کال ٹول، پرامپٹ حالت کا نظم کریں، وغیرہ۔ جو CRUD میں صفائی کے ساتھ نقشہ نہیں بناتے ہیں۔

JSON-RPC کو ریموٹ پروسیجر کالز کے لیے ڈیزائن کیا گیا ہے (کسی دوسرے کمپیوٹر پر کسی فنکشن کو کال کرنا، گویا یہ آپ کے کوڈ میں ایک مقامی فنکشن ہے۔) — "میرے لیے یہ مخصوص کام کریں اور نتیجہ واپس کریں"—اسے قدرتی طور پر موزوں بنانا۔
2. ملٹی پلیکسنگ اور اسٹریمنگ سپورٹ 

ایک ہی کنکشن پر ایک سے زیادہ کالیں: JSON-RPC قدرتی طور پر ان پروٹوکولز کے لیے موزوں ہے جن کو ایک کھلا چینل رکھنے کی ضرورت ہوتی ہے (مثال کے طور پر، WebSocket، HTTP/2، SSE) اور ریئل ٹائم میں متعدد کمانڈز اور جوابات بھیجیں۔ REST (HTTP 1.1 سے زیادہ) عام طور پر فی عمل ایک نیا کنکشن/درخواست کھولتا ہے۔ 
سلسلہ بندی اور اطلاعات: ایجنٹوں کے ساتھ، آپ کو پیش رفت کی تازہ کاری، جزوی نتائج، یا سرور کے ذریعے شروع کردہ پیغامات (اطلاعات) چاہیں گے۔ JSON-RPC اطلاعات (ایک طرفہ پیغامات) کو سپورٹ کرتا ہے، جو کہ REST میں محاورہ نہیں ہے۔

3. واضح طریقہ کے نام اور ساختی درخواستیں۔ 

REST میں، اختتامی نقطہ اور فعل آپریشن کی وضاحت کرتے ہیں۔ JSON-RPC میں، آپ کو ملتا ہے {"method": "tools/call", ...}—عمل واضح اور قابل دریافت ہے، URL/HTTP فعل کے مجموعے میں پوشیدہ نہیں ہے۔ 
توسیع کرنے میں آسان: نئی صلاحیتوں (نئے طریقے) کو شامل کرنے کے لیے نئے یو آر ایل ایجاد کرنے یا HTTP سیمنٹکس کو اوور لوڈ کرنے کی ضرورت نہیں ہے۔

4. اسٹیٹ لیس بمقابلہ اسٹیٹ فل ورک فلوز 

MCP ریاستی کام کے بہاؤ (سیشنز، دوبارہ شروع کرنا، ٹول ریسورسز وغیرہ) چلا سکتا ہے، جو ایک ایسے پروٹوکول سے فائدہ اٹھا سکتا ہے جو ریاستی تبدیلیوں اور براہ راست طریقہ کار کی درخواست دونوں کا اظہار کر سکتا ہے۔ 

REST بے ریاست، وسائل پر مبنی آپریشنز کے لیے بہترین ہے۔ 
اگر JSON-RPC بے وطن ہے تو MCP ریاستی کام کیسے کر سکتا ہے؟ 

"ریاست" کی دیکھ بھال سرور (یا ایجنٹ) کرتی ہے، پروٹوکول نہیں۔ 

MCP سیشن_id، context_id، یا دوسرے ٹوکن/IDs جیسی چیزوں کا استعمال کرتا ہے تاکہ سرور کو جاری ورک فلو یا بات چیت پر نظر رکھے۔ 

ہر JSON-RPC کال میں ضروری معلومات (جیسے سیشن/سیاق و سباق) شامل ہوتی ہے تاکہ سرور کو معلوم ہو کہ وہ کون سا ورک فلو یا گفتگو کر رہا ہے۔

5. مضبوط خرابی ہینڈلنگ 

JSON-RPC ہر درخواست کے لیے ایک معیاری، ساختی غلطی کے جواب (کوڈ، پیغام، ڈیٹا کے ساتھ خرابی) کی وضاحت کرتا ہے۔ 
REST ایرر ہینڈلنگ کم معیاری ہے اور گندا ہو سکتا ہے (اسٹیٹس کوڈز + صوابدیدی پے لوڈز)۔

6. ایکو سسٹم اور IDE پروٹوکول کے ساتھ الائنمنٹ 

LLM ایجنٹس اور ٹولز لینگویج سرورز، ڈیبگرز، IDE پلگ انز وغیرہ سے متاثر ہوتے ہیں۔ جن میں سے اکثر JSON-RPC استعمال کرتے ہیں۔ 
مثالیں: LSP (Language Server Protocol)، Debug Adapter Protocol—دونوں JSON-RPC پر مبنی!

خلاصہ ٹیبل
فیچر REST JSON-RPC (MCP کے ذریعے استعمال کیا جاتا ہے)
پیراڈیم ریسورس/CRUD ریموٹ پروسیجر کال (RPC)
HTTP فعل تک محدود آپریشنز صوابدیدی نام کے طریقے
WebSocket/SSE کے ذریعے مشکل، غیر معیاری مقامی سٹریمنگ
ملٹی پلیکسنگ نئی HTTP درخواست ہر ایک کے لیے ایک سے زیادہ ایک کنکشن میں
اطلاعات محاورہ نہیں بلٹ ان
ایرر ہینڈلنگ مختلف ہوتی ہے، معیاری ساختہ نہیں، پروٹوکول کا حصہ
سٹیٹفلنس سٹیٹ لیس بہترین پریکٹس سیشنز/ریاست کو سپورٹ کر سکتی ہے۔
توسیع پذیری کو URL/طریقہ کار میں تبدیلی کی ضرورت ہے بس نئے طریقے شامل کریں۔
آگے کی طرف دیکھو:

MCP جیسے پروٹوکول کو AI آرکیسٹریشن کے مستقبل کے لیے ڈیزائن کیا گیا ہے، نہ کہ صرف سادہ CRUD APIs۔ انہیں ضرورت ہے: 

ماڈل سیاق و سباق اور ٹولز پر عمدہ کنٹرول، 
ریئل ٹائم انٹرایکٹیویٹی اور اطلاعات، 
مستقل مزاجی اور توسیع پذیری۔

JSON-RPC کو ان تقاضوں کے لیے مقصد سے بنایا گیا ہے، جو اسے جدید ایجنٹ/ماڈل پروٹوکولز کے لیے REST سے کہیں بہتر بناتا ہے۔ اگر آپ LLM پر مبنی سسٹمز ڈیزائن کرنے یا AI ایجنٹوں کو پیمانے پر ضم کرنے کا منصوبہ بنا رہے ہیں، تو ان ڈیزائن کے انتخاب کو سمجھنا اور فائدہ اٹھانا آپ کو آگے بڑھاتا ہے!
