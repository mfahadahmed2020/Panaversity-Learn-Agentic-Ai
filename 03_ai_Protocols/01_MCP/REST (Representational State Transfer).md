REST (Representational State Transfer)

REST, or REpresentational State Transfer, is a software architectural style for designing networked applications, particularly web services.

It was first defined by Roy Fielding in his 2000 doctoral dissertation, drawing upon the principles that guided the architecture of the World Wide Web.

REST is not a protocol or a specific technology but rather a set of constraints that, when applied, lead to scalable, stateless, and reliable systems. The core idea is that clients interact with representations of resources managed by servers.
Core Architectural Constraints of REST

REST is defined by six guiding architectural constraints. Adherence to these constraints aims to produce systems with desirable non-functional properties like performance, scalability, simplicity, modifiability, visibility, portability, and reliability.

    Client-Server Architecture:
        Assumes a separation between the client (which handles user interface concerns) and the server (which handles data storage, business logic, and security).
        This separation allows client and server components to evolve independently, as long as the interface between them remains consistent.

    Statelessness:
        Each request from a client to a server must contain all the information needed for the server to understand and process the request.
        The server does not store any client context (session state) between requests. Any session state is kept on the client side.
        Benefits: Improves scalability (any server can handle any request), reliability (easier to recover from failures), and visibility (monitoring is simpler as each request is self-contained).

    Cacheability:
        Responses from the server must explicitly define themselves as cacheable or non-cacheable.
        If a response is cacheable, a client (or an intermediary cache like a CDN) can reuse that response data for later, equivalent requests.
        Benefits: Reduces latency, improves network efficiency, and decreases server load.

    Layered System:
        REST allows for an architecture composed of hierarchical layers. Components in one layer can only interact with components in adjacent layers.
        A client typically cannot tell whether it is connected directly to the end server or to an intermediary (e.g., load balancer, proxy, API gateway) along the way.
        Benefits: Enhances scalability by enabling load balancing and shared caches. Enforces security policies at different layers.

    Code on Demand (Optional):
        Servers can temporarily extend or customize the functionality of a client by transferring executable code (e.g., JavaScript applets or scripts).
        This is the only optional constraint in REST. While powerful, it can reduce visibility and is less commonly emphasized in modern REST API design compared to data exchange.

    Uniform Interface:
        This is a key principle that distinguishes REST from other architectural styles. It simplifies and decouples the architecture, enabling each part to evolve independently. The uniform interface is defined by four sub-constraints:
            Identification of Resources: Individual resources (e.g., a user profile, a product, a collection of articles) are uniquely identified using Uniform Resource Identifiers (URIs), typically URLs.
            Manipulation of Resources Through Representations: Clients interact with resources by exchanging representations of those resources. A representation is a snapshot of the resource's state at a particular time, commonly in formats like JSON or XML. The representation (along with metadata) should be sufficient for the client to modify or delete the resource on the server.
            Self-Descriptive Messages: Each message (request or response) exchanged between client and server must contain enough information for the recipient to understand how to process it. This includes:
                The resource URI.
                The HTTP method (verb) indicating the desired action.
                Metadata in headers (e.g., Content-Type specifying the media type of the payload, Accept specifying desired response media types).
                The payload itself (for requests like POST/PUT, or for responses).
            Hypermedia as the Engine of Application State (HATEOAS): This is arguably the most mature and often least implemented aspect of REST. Clients should be able to discover possible actions and navigate an application's resources by following hyperlinks provided dynamically in server responses. The client doesn't need prior knowledge of all resource URIs; it starts with an initial URI and discovers others through these server-provided links. This allows the server to evolve its URI space and available actions without breaking clients.

Key Concepts in RESTful APIs

When discussing RESTful APIs (APIs that adhere to REST principles), several concepts are central:

    Resources: The fundamental concept in REST. A resource is any information or entity that can be named and addressed. Examples: a document, an image, a user, a service, a collection of other resources. Resources are identified by URIs.
    Representations: When a client requests a resource, the server sends back a representation of that resource's state. This is commonly in JSON or XML format, but could also be HTML, plain text, images, etc. The same resource can have multiple representations (e.g., a user resource represented as JSON or XML).
    HTTP Methods (Verbs): Standard HTTP methods are used to perform operations (Create, Read, Update, Delete - CRUD) on resources:
        GET: Retrieve a representation of a resource or a collection of resources.
        POST: Create a new resource. Often used for actions that don't fit neatly into CRUD operations on a specific resource.
        PUT: Replace an existing resource entirely with a new representation. If the resource doesn't exist, it may create it.
        DELETE: Remove a resource.
        PATCH: Partially update an existing resource.
        OPTIONS: Get information about the communication options for the target resource (e.g., allowed HTTP methods).
        HEAD: Retrieve only the headers of a resource, not the body (identical to GET but without the response body).
    HTTP Status Codes: Standardized codes used in responses to indicate the outcome of an HTTP request. Examples:
        200 OK: Request succeeded.
        201 Created: Resource successfully created (often in response to POST or PUT).
        204 No Content: Request succeeded, but there is no content to return (e.g., for a successful DELETE).
        400 Bad Request: Server cannot process the request due to a client error (e.g., malformed syntax).
        401 Unauthorized: Authentication is required and has failed or has not yet been provided.
        403 Forbidden: Server understood the request, but refuses to authorize it (client does not have permission).
        404 Not Found: The requested resource could not be found on the server.
        500 Internal ServerError: A generic error message, given when an unexpected condition was encountered on the server.
    Idempotence: An operation is idempotent if making multiple identical requests has the same effect as making a single request. In HTTP:
        GET, HEAD, OPTIONS, PUT, DELETE are typically idempotent.
        POST is generally not idempotent (e.g., multiple POSTs usually create multiple resources).
        PATCH can be idempotent if implemented carefully (e.g., using conditional requests).
    Media Types: Specify the format of the representation (e.g., application/json, application/xml, text/html, image/jpeg). Communicated via Content-Type (for request/response bodies) and Accept (for client-desired response formats) headers.

Designing a RESTful API - Best Practices

While REST is an architectural style, several best practices have emerged for designing practical and user-friendly RESTful HTTP APIs:

    Use Nouns for Resource URIs: URIs should identify resources, not actions. Use plural nouns for collections.
        Good: /users, /users/{userId}, /orders, /products/{productId}/reviews
        Avoid: /getAllUsers, /createNewUser, /products/delete/{productId}
    Use HTTP Methods Correctly: Map CRUD operations to HTTP methods appropriately (GET for read, POST for create, PUT for replace, PATCH for partial update, DELETE for remove).
    Provide Meaningful HTTP Status Codes: Use standard status codes to indicate the outcome of requests accurately.
    Support Common Data Formats: JSON (application/json) is the most common format for modern REST APIs. XML (application/xml) is also used.
    Filtering, Sorting, and Pagination: For collections, provide mechanisms for clients to filter results, sort them, and paginate through large datasets (e.g., using query parameters like /users?status=active&sort=lastName&offset=0&limit=20).
    Versioning: Plan for API evolution. Common strategies include:
        URI Path Versioning: /v1/users, /v2/users (most common and straightforward).
        Query Parameter Versioning: /users?version=1.
        Custom Header Versioning: X-API-Version: 1.
        Media Type Versioning (Content Negotiation): Accept: application/vnd.myapi.v1+json.
    Clear Error Handling: Provide informative error messages in the response body (typically JSON) when an error status code is returned. Include details like an error code, a human-readable message, and potentially links to documentation.

    {
      "error": {
        "code": "INVALID_INPUT",
        "message": "The 'email' field is required and must be a valid email address.",
        "details_url": "https://api.example.com/docs/errors#INVALID_INPUT"
      }
    }

    Security: Implement robust authentication and authorization.
        Authentication (verifying identity): API Keys, OAuth 2.0 (Bearer Tokens), JWTs.
        Authorization (verifying permissions): Role-Based Access Control (RBAC), scopes (with OAuth 2.0).
        Always use HTTPS (TLS encryption) for all API communication.
    Documentation: Provide comprehensive, accurate, and easy-to-understand API documentation. Tools like OpenAPI (formerly Swagger) are widely used to define and document REST APIs.
    HATEOAS (Optional but Recommended for Maturity): Include links in responses to guide clients to related resources and available actions, promoting discoverability.

Practical Example: Raw RESTful API Request and Response Messages

This example illustrates the raw text format of HTTP requests and responses for a RESTful API, showcasing how REST principles—such as resource identification, statelessness, and the use of standard HTTP methods—are applied in practice. The messages demonstrate interactions with a hypothetical RESTful API for managing "users" resources, aligning with the "Core Architectural Constraints of REST" and "Key Concepts in RESTful APIs" sections of the tutorial.
Example Overview

This section includes four raw HTTP messages that adhere to REST principles:

    A GET request to retrieve a representation of a specific user resource (/users/123).
    The server's GET response with a JSON representation of the user.
    A POST request to create a new user resource (/users).
    The server's POST response confirming the creation with a JSON representation of the new user.

These messages simulate interactions with a hypothetical RESTful API at api.example.com using HTTP/1.1. The explanations highlight REST-specific concepts, such as resource URIs, representations, self-descriptive messages, and the optional inclusion of HATEOAS links to demonstrate discoverability.
Raw RESTful API Messages and Their Components

Below are the raw HTTP messages, each followed by an explanation of its components, focusing on how they embody REST principles. The messages are formatted exactly as they would appear in a network transaction, with proper line breaks and spacing.
1. GET Request

GET /users/123 HTTP/1.1
Host: api.example.com
Accept: application/json
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
Accept-Language: en-US,en;q=0.5
Connection: keep-alive
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

Explanation:

    REST Principles Demonstrated:
        Identification of Resources: The URI /users/123 uniquely identifies a specific user resource, following the REST convention of using nouns to represent resources.
        Statelessness: The request contains all necessary information (URI, headers, authentication token) for the server to process it without relying on stored client context.
        Uniform Interface: Uses the GET method to retrieve a representation of the resource, with the Accept header specifying the desired format (application/json).
    Message Components:
        Start-Line: GET /users/123 HTTP/1.1
            Method: GET – Requests a representation of the user resource.
            URI: /users/123 – Identifies the specific user with ID 123.
            HTTP Version: HTTP/1.1.
        Headers:
            Host: api.example.com – Specifies the API domain.
            Accept: application/json – Requests a JSON representation of the resource.
            User-Agent – Identifies the client (e.g., a browser or custom client).
            Accept-Language – Indicates preferred languages for the response.
            Connection: keep-alive – Requests the server to maintain the TCP connection.
            Authorization – Includes a Bearer token for authentication, ensuring secure access to the resource.
        Empty Line: Separates headers from the body (CRLF).
        Body: None – GET requests in REST typically have no body, as they retrieve data.

2. GET Response

HTTP/1.1 200 OK
Date: Thu, 12 Jun 2025 09:19:00 GMT
Server: Nginx/1.18.0
Content-Type: application/json; charset=UTF-8
Content-Length: 165
Cache-Control: max-age=3600
Connection: keep-alive

{
  "id": 123,
  "name": "Alice Smith",
  "email": "alice@example.com",
  "_links": {
    "self": {"href": "/users/123"},
    "update": {"href": "/users/123", "method": "PATCH"},
    "delete": {"href": "/users/123", "method": "DELETE"}
  }
}

Explanation:

    REST Principles Demonstrated:
        Manipulation of Resources Through Representations: The response provides a JSON representation of the user resource's state, including attributes like id, name, and email.
        Self-Descriptive Messages: The Content-Type header specifies the representation format (application/json), and the body includes all necessary data.
        HATEOAS: The _links object provides hyperlinks to related actions (self, update, delete), enabling clients to discover possible next steps dynamically.
        Cacheability: The Cache-Control header (max-age=3600) indicates the response can be cached for one hour, reducing server load for subsequent requests.
    Message Components:
        Start-Line: HTTP/1.1 200 OK
            HTTP Version: HTTP/1.1.
            Status Code: 200 – Indicates the request was successful.
            Reason Phrase: OK.
        Headers:
            Date – Timestamp of the response.
            Server – Identifies the server software (Nginx).
            Content-Type: application/json; charset=UTF-8 – Specifies the JSON format and UTF-8 encoding.
            Content-Length: 165 – Length of the JSON body in bytes.
            Cache-Control – Enables caching for 3600 seconds.
            Connection: keep-alive – Allows connection reuse.
        Empty Line: Separates headers from the body.
        Body: A JSON object representing the user, with HATEOAS links for discoverability.

3. POST Request

POST /users HTTP/1.1
Host: api.example.com
Accept: application/json
Content-Type: application/json
Content-Length: 65
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
Connection: keep-alive
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

{
  "name": "Bob Johnson",
  "email": "bob@example.com"
}

Explanation:

    REST Principles Demonstrated:
        Identification of Resources: The URI /users identifies the collection resource for users, where a new user will be created.
        Statelessness: The request includes all data (JSON payload, authentication token) needed to create the resource, without server-side session state.
        Uniform Interface: Uses the POST method to create a new resource, with Content-Type and Accept headers specifying JSON for the request and response.
        Manipulation of Resources Through Representations: The JSON body provides the representation of the new user to be created.
    Message Components:
        Start-Line: POST /users HTTP/1.1
            Method: POST – Creates a new resource in the users collection.
            URI: /users – Targets the users collection.
            HTTP Version: HTTP/1.1.
        Headers:
            Host, User-Agent, Connection, Authorization – Similar to the GET request.
            Accept: application/json – Requests a JSON response.
            Content-Type: application/json – Indicates the request body is JSON.
            Content-Length: 65 – Length of the JSON body in bytes.
        Empty Line: Separates headers from the body.
        Body: A JSON object with name and email fields for the new user.

4. POST Response

HTTP/1.1 201 Created
Date: Thu, 12 Jun 2025 09:19:05 GMT
Server: Nginx/1.18.0
Content-Type: application/json; charset=UTF-8
Content-Length: 188
Location: /users/124
Connection: keep-alive

{
  "id": 124,
  "name": "Bob Johnson",
  "email": "bob@example.com",
  "_links": {
    "self": {"href": "/users/124"},
    "update": {"href": "/users/124", "method": "PATCH"},
    "delete": {"href": "/users/124", "method": "DELETE"}
  }
}

Explanation:

    REST Principles Demonstrated:
        Manipulation of Resources Through Representations: The response returns a JSON representation of the newly created user, including the server-assigned id.
        Self-Descriptive Messages: The Content-Type and Location headers provide metadata about the response and the new resource's URI.
        HATEOAS: The _links object includes hyperlinks for further actions, supporting dynamic navigation.
        Uniform Interface: The 201 Created status code and Location header indicate successful resource creation and provide the URI of the new resource.
    Message Components:
        Start-Line: HTTP/1.1 201 Created
            HTTP Version: HTTP/1.1.
            Status Code: 201 – Indicates the resource was created successfully.
            Reason Phrase: Created.
        Headers:
            Date, Server, Content-Type, Content-Length, Connection – Similar to the GET response.
            Location: /users/124 – Specifies the URI of the newly created user resource.
        Empty Line: Separates headers from the body.
        Body: A JSON object representing the new user, with HATEOAS links.

Key REST Concepts Demonstrated

This example ties directly to the "Core Architectural Constraints of REST" and "Key Concepts in RESTful APIs" sections by illustrating:

    Client-Server Architecture: The requests and responses separate client concerns (sending requests) from server concerns (processing and storing resources).
    Statelessness: Each request is self-contained, with authentication tokens and data included, requiring no server-side session state.
    Cacheability: The GET response includes a Cache-Control header to enable caching, reducing server load.
    Uniform Interface:
        Identification of Resources: URIs like /users/123 and /users clearly identify resources.
        Manipulation Through Representations: JSON payloads represent resource states for creation and retrieval.
        Self-Descriptive Messages: Headers like Content-Type, Accept, and Authorization make messages interpretable.
        HATEOAS: Response links enable clients to discover related resources and actions dynamically.
    HTTP Methods: GET retrieves a resource representation; POST creates a new resource.
    HTTP Status Codes: 200 OK for successful retrieval, 201 Created for successful creation with a Location header.
    Media Types: application/json is used consistently for representations, as specified in headers.

Working with REST APIs in Python

Python offers excellent libraries for both consuming (client-side) and building (server-side) REST APIs.
Client-Side: requests Library

The requests library is the de facto standard for making HTTP requests in Python.

Installation:

uv init rest_code
cd rest_code
# Install requests
uv add requests

Example: Consuming a Public REST API

import requests
import json

# Using JSONPlaceholder, a free fake online REST API for testing and prototyping.
BASE_URL = "https://jsonplaceholder.typicode.com"

# --- GET request to fetch a single post ---
def get_post(post_id):
    print(f"\\n--- GET Request for post/{post_id} ---")
    try:
        response = requests.get(f"{BASE_URL}/posts/{post_id}")
        response.raise_for_status()  # Raises an HTTPError for bad responses (4XX or 5XX)

        print(f"Status Code: {response.status_code}")
        post_data = response.json()
        print(f"Post Title: {post_data.get('title')}")
        # print(f"Full Response Data: {post_data}")
        return post_data
    except requests.exceptions.HTTPError as errh:
        print(f"  Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"  Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"  Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"  Something Else Went Wrong: {err}")
    return None

# --- POST request to create a new post ---
def create_post(title, body, user_id):
    print("\\n--- POST Request to /posts ---")
    new_post_payload = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    headers = {"Content-Type": "application/json; charset=utf-8"}
    try:
        response = requests.post(f"{BASE_URL}/posts", data=json.dumps(new_post_payload), headers=headers, timeout=5)
        response.raise_for_status()

        print(f"Status Code: {response.status_code}") # Should be 201 Created
        created_post_data = response.json()
        print(f"Created Post ID: {created_post_data.get('id')}")
        print(f"Created Post Title: {created_post_data.get('title')}")
        return created_post_data
    except requests.exceptions.RequestException as e:
        print(f"  POST request failed: {e}")
    return None

if __name__ == "__main__":
    get_post(1)
    get_post(9999) # Example of a resource not found (should trigger 404)

    created_post = create_post("My New Post", "This is the body of my amazing new post.", 101)
    if created_post:
        print(f"Successfully created post with ID: {created_post.get('id')}")

REST vs. Other Architectural Styles/Protocols

    SOAP (Simple Object Access Protocol):
        SOAP is a protocol with a rigid specification, typically using XML for message formats and often relying on WSDL for service description.
        REST is an architectural style with more flexibility, commonly using JSON over HTTP, and can leverage standards like OpenAPI for description.
        SOAP can be more complex and verbose but offers built-in standards for security (WS-Security) and transactions, often favored in enterprise environments.
    GraphQL:
        GraphQL is a query language for APIs and a server-side runtime for executing those queries.
        Clients request exactly the data they need, avoiding over-fetching or under-fetching common with traditional REST APIs that return fixed data structures for resources.
        GraphQL typically uses a single endpoint (e.g., /graphql) and HTTP POST for all operations.
        REST uses multiple endpoints (URIs) and HTTP verbs to define operations on resources.
        They can coexist; some systems use GraphQL for flexible data fetching and REST for simpler resource manipulation or command-like operations.
    gRPC (Google Remote Procedure Call):
        gRPC is a high-performance, open-source RPC framework that can run in any environment. It typically uses Protocol Buffers for defining service contracts and message formats, and HTTP/2 as its transport protocol.
        Focuses on efficiency, low latency, and strong typing. Excellent for microservice communication.
        REST is more focused on resource-oriented architecture and leverages standard HTTP semantics, making it broadly accessible.

Strengths of REST

    Simplicity and Ease of Understanding: Based on familiar HTTP methods and URIs, making it relatively easy to learn and use.
    Scalability: Statelessness and cacheability contribute significantly to the ability to scale horizontally.
    Interoperability and Wide Adoption: Platform and language-agnostic. Supported by virtually all programming languages and web frameworks.
    Flexibility in Data Formats: While JSON is most common, REST can use XML, HTML, plain text, or any other format.
    Leverages Existing Web Infrastructure: Utilizes standard HTTP, URIs, DNS, and caching mechanisms.
    Discoverability (with HATEOAS): Well-implemented HATEOAS allows clients to dynamically navigate APIs.

Weaknesses/Limitations of REST

    Over-fetching and Under-fetching: Fixed resource representations can lead to clients receiving more data than they need (over-fetching) or needing to make multiple requests to get all required data (under-fetching). GraphQL specifically addresses this.
    Multiple Round Trips: Complex data needs might require several client-server round trips to fetch related resources, increasing latency.
    Statelessness Overhead: Since each request must be self-contained, it might carry redundant information (e.g., authentication tokens in every request).
    No Built-in Real-time/Push Capabilities: REST is primarily client-initiated (pull-based). For server-initiated updates or real-time bidirectional communication, technologies like WebSockets or Server-Sent Events (SSE) are generally preferred.
    Standardization can be Loose: Being an architectural style, interpretations of REST can vary, leading to inconsistencies across different APIs if design principles are not strictly followed.
    Managing Many Endpoints: For very complex systems with many resources and operations, the number of distinct endpoints can become large.

Use Cases in Agentic AI Systems (DACA Context)

RESTful APIs are a cornerstone for building modular and interoperable agentic AI systems like those envisioned by the DACA pattern:

    Core Agent Functionality API: Exposing an agent's capabilities, status, and configuration via REST endpoints.
        GET /agents/{agent_id}/status
        POST /agents/{agent_id}/tasks (to assign a new task)
        GET /agents/{agent_id}/tasks/{task_id}
    Tool Integration: Agents can interact with external tools, services, or data sources that expose REST APIs (e.g., weather APIs, knowledge bases, search engines).
    Data Exchange and Persistence: Agents can retrieve data from or store data to databases, vector stores, or other storage services through RESTful interfaces.
    Inter-Agent Communication: For simpler, request-response style communication between agents, REST can be a straightforward choice, especially if agents are developed as independent microservices.
    Management and Orchestration APIs: The DACA infrastructure itself (e.g., for deploying, monitoring, scaling, and configuring agents) can be managed via REST APIs.
    Human-in-the-Loop (HITL) Interfaces: Web-based dashboards or control panels for human oversight and intervention would typically interact with the backend agent systems via REST APIs.
    Model Serving: While specialized model serving solutions exist (like TensorFlow Serving, TorchServe), simpler models or custom inference logic can be exposed as REST endpoints.
        POST /models/{model_id}/predict
    Logging and Monitoring: Agents can send logs or metrics to a central logging/monitoring service via REST.

In DACA, REST APIs provide a standardized, well-understood way to ensure that different components of the agentic system (agents, tools, data stores, UIs) can communicate effectively and be developed/scaled independently.
Further Reading & References

    Foundational:
        Fielding, Roy T. (2000). Chapter 5: Representational State Transfer (REST) in "Architectural Styles and the Design of Network-based Software Architectures".
    Design Principles & Best Practices:
        MDN Web Docs: REST
        Postman Blog: What Is a REST API? Examples, Uses, and Challenges (Your provided link)
        Microsoft API Design Best Practices
        Google Cloud API Design Guide
    Python Libraries:
        requests Documentation
        FastAPI Documentation
    API Description:
        OpenAPI Initiative (Swagger)
    Wikipedia:
        Representational state transfer (REST) (Your provided link)


REST (نمائندہ ریاست کی منتقلی)

REST، یا نمائندہ ریاست کی منتقلی، نیٹ ورک کردہ ایپلی کیشنز، خاص طور پر ویب سروسز کو ڈیزائن کرنے کے لیے ایک سافٹ ویئر آرکیٹیکچرل اسٹائل ہے۔

اس کی تعریف پہلی بار رائے فیلڈنگ نے اپنے 2000 کے ڈاکٹریٹ کے مقالے میں کی تھی، جس میں ان اصولوں پر روشنی ڈالی گئی تھی جو ورلڈ وائڈ ویب کے فن تعمیر کی رہنمائی کرتے تھے۔

REST کوئی پروٹوکول یا مخصوص ٹیکنالوجی نہیں ہے بلکہ رکاوٹوں کا ایک مجموعہ ہے جو لاگو ہونے پر، توسیع پذیر، بے ریاست، اور قابل اعتماد نظام کی طرف لے جاتا ہے۔ بنیادی خیال یہ ہے کہ کلائنٹ سرورز کے زیر انتظام وسائل کی نمائندگی کے ساتھ تعامل کرتے ہیں۔
REST کی بنیادی تعمیراتی رکاوٹیں۔

REST کی تعریف چھ رہنمائی آرکیٹیکچرل رکاوٹوں سے کی گئی ہے۔ ان رکاوٹوں کی پابندی کا مقصد کارکردگی، اسکیل ایبلٹی، سادگی، تبدیلی کی اہلیت، مرئیت، پورٹیبلٹی، اور قابل اعتماد جیسے مطلوبہ غیر فعال خصوصیات کے ساتھ نظام تیار کرنا ہے۔ 

کلائنٹ سرور آرکیٹیکچر: 
کلائنٹ (جو صارف کے انٹرفیس کے خدشات کو ہینڈل کرتا ہے) اور سرور (جو ڈیٹا اسٹوریج، کاروباری منطق، اور سیکورٹی کو سنبھالتا ہے) کے درمیان علیحدگی فرض کرتا ہے۔ 
یہ علیحدگی کلائنٹ اور سرور کے اجزاء کو آزادانہ طور پر تیار ہونے کی اجازت دیتی ہے، جب تک کہ ان کے درمیان انٹرفیس مستقل رہے۔ 

بے وطنی: 
کلائنٹ کی طرف سے سرور سے ہر درخواست میں سرور کے لیے درخواست کو سمجھنے اور اس پر کارروائی کرنے کے لیے درکار تمام معلومات ہونی چاہیے۔ 
سرور درخواستوں کے درمیان کسی بھی کلائنٹ سیاق و سباق (سیشن کی حالت) کو ذخیرہ نہیں کرتا ہے۔ کسی بھی سیشن کی حالت کلائنٹ کی طرف رکھی جاتی ہے۔ 
فوائد: اسکیل ایبلٹی کو بہتر بناتا ہے (کوئی بھی سرور کسی بھی درخواست کو سنبھال سکتا ہے)، وشوسنییتا (ناکامیوں سے بازیافت کرنا آسان) اور مرئیت (مانیٹرنگ آسان ہے کیونکہ ہر درخواست خود پر مشتمل ہے)۔ 

کیش ایبلٹی: 
سرور کے جوابات کو واضح طور پر خود کو کیش ایبل یا غیر کیش ایبل کے طور پر بیان کرنا چاہیے۔ 
اگر جواب قابل کیش ہے تو، ایک کلائنٹ (یا CDN کی طرح ایک درمیانی کیش) اس جوابی ڈیٹا کو بعد میں، مساوی درخواستوں کے لیے دوبارہ استعمال کر سکتا ہے۔ 
فوائد: تاخیر کو کم کرتا ہے، نیٹ ورک کی کارکردگی کو بہتر بناتا ہے، اور سرور کا بوجھ کم کرتا ہے۔ 

پرتوں والا نظام: 
REST درجہ بندی کی تہوں پر مشتمل ایک فن تعمیر کی اجازت دیتا ہے۔ ایک پرت میں اجزاء صرف ملحقہ تہوں کے اجزاء کے ساتھ تعامل کرسکتے ہیں۔ 
ایک کلائنٹ عام طور پر یہ نہیں بتا سکتا کہ یہ راستے میں براہ راست اینڈ سرور سے جڑا ہوا ہے یا کسی بیچوان سے (مثال کے طور پر، لوڈ بیلنسر، پراکسی، API گیٹ وے)۔ 
فوائد: لوڈ بیلنسنگ اور مشترکہ کیشز کو فعال کرکے اسکیل ایبلٹی کو بڑھاتا ہے۔ مختلف سطحوں پر سیکیورٹی پالیسیوں کو نافذ کرتا ہے۔ 

کوڈ آن ڈیمانڈ (اختیاری): 
سرورز عارضی طور پر قابل عمل کوڈ (مثلاً جاوا اسکرپٹ ایپلٹس یا اسکرپٹس) کو منتقل کرکے کلائنٹ کی فعالیت کو بڑھا یا اپنی مرضی کے مطابق کرسکتے ہیں۔ 
یہ REST میں واحد اختیاری رکاوٹ ہے۔ طاقتور ہونے کے باوجود، یہ مرئیت کو کم کر سکتا ہے اور ڈیٹا ایکسچینج کے مقابلے میں جدید REST API ڈیزائن میں اس پر عام طور پر کم زور دیا جاتا ہے۔ 

یکساں انٹرفیس: 
یہ ایک اہم اصول ہے جو REST کو دیگر تعمیراتی طرزوں سے ممتاز کرتا ہے۔ یہ فن تعمیر کو آسان اور ڈیکپل بناتا ہے، ہر حصے کو آزادانہ طور پر تیار کرنے کے قابل بناتا ہے۔ یکساں انٹرفیس کی تعریف چار ذیلی رکاوٹوں سے ہوتی ہے: 
وسائل کی شناخت: انفرادی وسائل (مثال کے طور پر، صارف کا پروفائل، ایک پروڈکٹ، مضامین کا مجموعہ) کی شناخت یکساں وسائل کے شناخت کنندگان (URIs) کے استعمال سے کی جاتی ہے، عام طور پر URLs۔ 
نمائندگی کے ذریعے وسائل کی ہیرا پھیری: کلائنٹ ان وسائل کی نمائندگی کا تبادلہ کرکے وسائل کے ساتھ تعامل کرتے ہیں۔ نمائندگی کسی خاص وقت میں وسائل کی حالت کا ایک سنیپ شاٹ ہے، عام طور پر JSON یا XML جیسے فارمیٹس میں۔ نمائندگی (میٹا ڈیٹا کے ساتھ) کلائنٹ کے لیے سرور پر موجود وسائل میں ترمیم یا حذف کرنے کے لیے کافی ہونا چاہیے۔ 
خود وضاحتی پیغامات: کلائنٹ اور سرور کے درمیان تبادلہ ہونے والے ہر پیغام (درخواست یا جواب) میں وصول کنندہ کے لیے کافی معلومات ہونی چاہیے کہ وہ یہ سمجھ سکے کہ اس پر کیسے عمل کیا جائے۔ اس میں شامل ہیں: 
وسیلہ URI۔ 
HTTP طریقہ (فعل) مطلوبہ کارروائی کی نشاندہی کرتا ہے۔ 
ہیڈر میں میٹا ڈیٹا (مثال کے طور پر، مواد کی قسم پے لوڈ کی میڈیا قسم کی وضاحت کرتا ہے، مطلوبہ ردعمل میڈیا کی قسموں کی وضاحت قبول کرتا ہے)۔ 
پے لوڈ خود (پوسٹ/پوٹ جیسی درخواستوں کے لیے، یا جوابات کے لیے)۔ 
ہائپرمیڈیا بطور ایپلیکیشن اسٹیٹ (HATEOAS): یہ REST کا سب سے زیادہ پختہ اور اکثر کم سے کم لاگو ہونے والا پہلو ہے۔ کلائنٹس کو سرور کے جوابات میں متحرک طور پر فراہم کردہ ہائپر لنکس کی پیروی کرتے ہوئے ممکنہ کارروائیوں کو دریافت کرنے اور ایپلیکیشن کے وسائل کو نیویگیٹ کرنے کے قابل ہونا چاہیے۔ کلائنٹ کو تمام وسائل URIs کی پیشگی معلومات کی ضرورت نہیں ہے۔ یہ ایک ابتدائی URI سے شروع ہوتا ہے اور سرور کے فراہم کردہ ان لنکس کے ذریعے دوسروں کو دریافت کرتا ہے۔ یہ سرور کو کلائنٹس کو توڑے بغیر اپنی URI جگہ اور دستیاب کارروائیوں کو تیار کرنے کی اجازت دیتا ہے۔

RESTful APIs میں کلیدی تصورات

RESTful APIs (APIs جو REST اصولوں پر عمل پیرا ہیں) پر بحث کرتے وقت، کئی تصورات مرکزی ہیں: 

وسائل: بنیادی کمپنی

REST میں ncept. ایک وسیلہ کوئی بھی معلومات یا ادارہ ہے جس کا نام اور پتہ لگایا جاسکتا ہے۔ مثالیں: ایک دستاویز، ایک تصویر، ایک صارف، ایک خدمت، دیگر وسائل کا مجموعہ۔ وسائل کی شناخت URIs سے ہوتی ہے۔ 
نمائندگی: جب کوئی کلائنٹ کسی وسائل کی درخواست کرتا ہے، تو سرور اس وسائل کی حالت کی نمائندگی واپس بھیجتا ہے۔ یہ عام طور پر JSON یا XML فارمیٹ میں ہوتا ہے، لیکن یہ HTML، سادہ متن، تصاویر وغیرہ بھی ہو سکتا ہے۔ ایک ہی وسیلہ میں متعدد نمائندگییں ہو سکتی ہیں (جیسے، صارف کا وسیلہ JSON یا XML کے طور پر پیش کیا جاتا ہے)۔ 
HTTP طریقے (فعل): معیاری HTTP طریقے وسائل پر آپریشنز (تخلیق، پڑھیں، اپ ڈیٹ، ڈیلیٹ - CRUD) انجام دینے کے لیے استعمال کیے جاتے ہیں: 
GET: وسائل کی نمائندگی یا وسائل کے مجموعے کی بازیافت کریں۔ 
پوسٹ: ایک نیا وسیلہ بنائیں۔ اکثر ایسی کارروائیوں کے لیے استعمال کیا جاتا ہے جو کسی مخصوص وسائل پر CRUD آپریشنز میں صاف طور پر فٹ نہیں ہوتے ہیں۔ 
PUT: ایک موجودہ وسائل کو مکمل طور پر ایک نئی نمائندگی سے بدل دیں۔ اگر وسیلہ موجود نہیں ہے تو یہ اسے بنا سکتا ہے۔ 
حذف کریں: وسائل کو ہٹا دیں۔ 
پیچ: موجودہ وسائل کو جزوی طور پر اپ ڈیٹ کریں۔ 
آپشنز: ٹارگٹ ریسورس کے لیے کمیونیکیشن آپشنز کے بارے میں معلومات حاصل کریں (مثال کے طور پر اجازت یافتہ HTTP طریقے)۔ 
HEAD: صرف وسائل کے ہیڈرز کو بازیافت کریں، باڈی نہیں (GET کی طرح لیکن رسپانس باڈی کے بغیر)۔ 
HTTP اسٹیٹس کوڈز: معیاری کوڈز جوابات میں استعمال ہوتے ہیں تاکہ HTTP درخواست کے نتائج کو ظاہر کیا جا سکے۔ مثالیں: 
200 ٹھیک ہے: درخواست کامیاب ہو گئی۔ 
201 تخلیق: وسائل کامیابی کے ساتھ بنائے گئے (اکثر POST یا PUT کے جواب میں)۔ 
204 کوئی مواد نہیں: درخواست کامیاب ہو گئی، لیکن واپس کرنے کے لیے کوئی مواد نہیں ہے (مثال کے طور پر، ایک کامیاب حذف کے لیے)۔ 
400 خراب درخواست: سرور کلائنٹ کی غلطی کی وجہ سے درخواست پر کارروائی نہیں کر سکتا (مثال کے طور پر، خراب نحو)۔ 
401 غیر مجاز: توثیق درکار ہے اور ناکام ہوگئی ہے یا ابھی تک فراہم نہیں کی گئی ہے۔ 
403 ممنوع: سرور نے درخواست کو سمجھا، لیکن اسے اجازت دینے سے انکار کر دیا (کلائنٹ کو اجازت نہیں ہے)۔ 
404 نہیں ملا: درخواست کردہ وسیلہ سرور پر نہیں مل سکا۔ 
500 اندرونی سرور کی خرابی: ایک عام غلطی کا پیغام، جب سرور پر کسی غیر متوقع حالت کا سامنا کرنا پڑا۔ 
Idempotence: اگر ایک سے زیادہ یکساں درخواستیں کرنے کا اثر ایک ہی درخواست کرنے کے برابر ہوتا ہے تو ایک آپریشن ناقابل یقین ہے۔ HTTP میں: 
GET, HEAD, OPTIONS, PUT, DELETE عام طور پر کمزور ہوتے ہیں۔ 
POST عام طور پر کمزور نہیں ہوتا ہے (مثال کے طور پر، ایک سے زیادہ POST عام طور پر متعدد وسائل تخلیق کرتے ہیں)۔ 
اگر احتیاط سے لاگو کیا جائے تو PATCH کمزور ہو سکتا ہے (مثال کے طور پر، مشروط درخواستوں کا استعمال کرتے ہوئے)۔ 
میڈیا کی قسمیں: نمائندگی کی شکل کی وضاحت کریں (مثال کے طور پر، ایپلیکیشن/json، application/xml، text/html، image/jpeg)۔ مواد کی قسم (درخواست/رسپانس باڈیز کے لیے) اور قبول (کلائنٹ کے مطلوبہ جوابی فارمیٹس کے لیے) ہیڈر کے ذریعے بات چیت کی گئی۔

ایک آرام دہ API ڈیزائن کرنا - بہترین طرز عمل

اگرچہ REST ایک آرکیٹیکچرل سٹائل ہے، عملی اور صارف دوست RESTful HTTP APIs کو ڈیزائن کرنے کے لیے کئی بہترین طریقے سامنے آئے ہیں: 

Resource URIs کے لیے Nouns کا استعمال کریں: URIs کو وسائل کی شناخت کرنی چاہیے، اعمال کی نہیں۔ جمع کے لیے جمع اسم استعمال کریں۔ 
اچھا: /users, /users/{userId}, /orders, /products/{productId}/reviews 
اجتناب کریں: /getAllUsers, /createNewUser, /products/delete/{productId} 
HTTP طریقوں کو درست طریقے سے استعمال کریں: CRUD آپریشنز کو HTTP طریقوں سے مناسب طریقے سے نقشہ بنائیں (پڑھنے کے لیے GET، تخلیق کے لیے POST، تبدیل کرنے کے لیے PUT، جزوی اپ ڈیٹ کے لیے PATCH، ہٹانے کے لیے DELETE)۔ 
معنی خیز HTTP اسٹیٹس کوڈز فراہم کریں: درخواستوں کے نتائج کو درست طریقے سے ظاہر کرنے کے لیے معیاری اسٹیٹس کوڈز استعمال کریں۔ 
مشترکہ ڈیٹا فارمیٹس کو سپورٹ کریں: JSON (application/json) جدید REST APIs کے لیے سب سے عام فارمیٹ ہے۔ XML (application/xml) بھی استعمال کیا جاتا ہے۔ 
فلٹرنگ، چھانٹنا، اور صفحہ بندی: مجموعوں کے لیے، کلائنٹس کو نتائج کو فلٹر کرنے، ان کو ترتیب دینے، اور بڑے ڈیٹاسیٹس کے ذریعے صفحہ بندی کرنے کے لیے طریقہ کار فراہم کریں (مثال کے طور پر، استفسار کے پیرامیٹرز کا استعمال کرتے ہوئے جیسے /users?status=active&sort=lastName&offset=0&limit=20)۔ 
ورژننگ: API ارتقاء کا منصوبہ۔ عام حکمت عملیوں میں شامل ہیں: 
URI پاتھ ورژننگ: /v1/users، /v2/users (سب سے عام اور سیدھا)۔ 
سوال پیرامیٹر ورژننگ: /users?version=1. 
حسب ضرورت ہیڈر ورژننگ: X-API-ورژن: 1۔ 
میڈیا ٹائپ ورژننگ (مواد کی گفت و شنید): قبول کریں: application/vnd.myapi.v1+json۔ 
ایرر ہینڈلنگ کو صاف کریں: جب ایرر اسٹیٹس کوڈ واپس آتا ہے تو رسپانس باڈی (عام طور پر JSON) میں معلوماتی ایرر میسیجز فراہم کریں۔ غلطی کا کوڈ، انسانی پڑھنے کے قابل پیغام، اور ممکنہ طور پر دستاویزات کے لنکس جیسی تفصیلات شامل کریں۔ 

{ 
"غلطی": { 
"code": "INVALID_INPUT"، 
"message": "'ای میل' فیلڈ درکار ہے اور ایک درست ای میل پتہ ہونا چاہیے۔", 
"details_url": "https://api.example.com/docs/errors#INVALID_INPUT" 
} 
} 

سیکیورٹی: مضبوط تصدیق اور اجازت کو نافذ کریں۔ 
تصدیق (شناخت کی تصدیق کرنا): API کیز، OAuth 2.0 (Bearer Tokens)، JWTs۔ 
اجازت (اجازت کی تصدیق کرنا): رول پر مبنی رسائی کنٹرول (RB

AC)، اسکوپس (OAuth 2.0 کے ساتھ)۔ 
تمام API مواصلات کے لیے ہمیشہ HTTPS (TLS انکرپشن) کا استعمال کریں۔ 
دستاویزی: جامع، درست، اور سمجھنے میں آسان API دستاویزات فراہم کریں۔ اوپن اے پی آئی (سابقہ ​​سویگر) جیسے ٹولز REST APIs کی وضاحت اور دستاویز کرنے کے لیے بڑے پیمانے پر استعمال ہوتے ہیں۔ 
HATEOAS (اختیاری لیکن پختگی کے لیے تجویز کردہ): متعلقہ وسائل اور دستیاب کارروائیوں کے لیے کلائنٹس کی رہنمائی کے لیے جوابات میں لنکس شامل کریں، دریافت کو فروغ دیں۔

عملی مثال: Raw RESTful API کی درخواست اور جوابی پیغامات

یہ مثال HTTP درخواستوں اور RESTful API کے جوابات کے خام ٹیکسٹ فارمیٹ کی وضاحت کرتی ہے، یہ ظاہر کرتی ہے کہ کس طرح REST اصول — جیسے وسائل کی شناخت، بے وطنی، اور معیاری HTTP طریقوں کا استعمال— عملی طور پر لاگو ہوتے ہیں۔ پیغامات "صارفین" کے وسائل کے انتظام کے لیے ایک فرضی RESTful API کے ساتھ تعامل کا مظاہرہ کرتے ہیں، "REST کی بنیادی تعمیراتی رکاوٹوں" اور "RESTful APIs میں کلیدی تصورات" کے سیکشنز کے ساتھ ہم آہنگ ہوتے ہیں۔
مثال کا جائزہ

اس حصے میں چار خام HTTP پیغامات شامل ہیں جو REST اصولوں پر عمل پیرا ہیں: 

ایک مخصوص صارف کے وسائل (/users/123) کی نمائندگی حاصل کرنے کے لیے ایک GET درخواست۔ 
صارف کی JSON نمائندگی کے ساتھ سرور کا GET جواب۔ 
ایک نیا صارف وسیلہ (/صارف) بنانے کے لیے POST کی درخواست۔ 
سرور کا POST جواب نئے صارف کی JSON نمائندگی کے ساتھ تخلیق کی تصدیق کرتا ہے۔

یہ پیغامات HTTP/1.1 کا استعمال کرتے ہوئے api.example.com پر فرضی RESTful API کے ساتھ تعاملات کی نقل کرتے ہیں۔ وضاحتیں REST سے متعلق مخصوص تصورات کو نمایاں کرتی ہیں، جیسے کہ وسیلہ URIs، نمائندگی، خود وضاحتی پیغامات، اور HATEOAS لنکس کا اختیاری شمولیت دریافت کرنے کے لیے۔
Raw RESTful API پیغامات اور ان کے اجزاء

ذیل میں خام HTTP پیغامات ہیں، جن میں سے ہر ایک کے بعد اس کے اجزاء کی وضاحت ہوتی ہے، اس بات پر توجہ مرکوز کرتے ہوئے کہ وہ کس طرح REST اصولوں کو مجسم کرتے ہیں۔ پیغامات کو بالکل اسی طرح فارمیٹ کیا جاتا ہے جیسا کہ وہ نیٹ ورک کے لین دین میں ظاہر ہوں گے، مناسب لائن بریک اور وقفہ کاری کے ساتھ۔
1. درخواست حاصل کریں۔

GET /users/123 HTTP/1.1
میزبان: api.example.com
قبول کریں: application/json
صارف کا ایجنٹ: Mozilla/5.0 (Windows NT 10.0؛ Win64; x64) AppleWebKit/537.36
قبول زبان: en-US,en;q=0.5
کنکشن: زندہ رکھنا
اجازت: بیئرر eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

وضاحت: 

باقی اصولوں کا مظاہرہ: 
وسائل کی شناخت: URI /users/123 وسائل کی نمائندگی کرنے کے لیے اسم استعمال کرنے کے REST کنونشن کے بعد، مخصوص صارف کے وسائل کی منفرد شناخت کرتا ہے۔ 
بے وطنی: درخواست میں سرور کے لیے تمام ضروری معلومات (URI، ہیڈرز، تصدیقی ٹوکن) موجود ہیں تاکہ ذخیرہ شدہ کلائنٹ کے سیاق و سباق پر انحصار کیے بغیر اس پر کارروائی کی جا سکے۔ 
یکساں انٹرفیس: وسائل کی نمائندگی حاصل کرنے کے لیے GET طریقہ استعمال کرتا ہے، Accept ہیڈر کے ساتھ مطلوبہ فارمیٹ (application/json) کی وضاحت کرتا ہے۔ 
پیغام کے اجزاء: 
اسٹارٹ لائن: GET /users/123 HTTP/1.1 
طریقہ: GET - صارف کے وسائل کی نمائندگی کی درخواست کرتا ہے۔ 
URI: /users/123 - ID 123 کے ساتھ مخصوص صارف کی شناخت کرتا ہے۔ 
HTTP ورژن: HTTP/1.1۔ 
ہیڈرز: 
میزبان: api.example.com - API ڈومین کی وضاحت کرتا ہے۔ 
قبول کریں: درخواست/json - وسائل کی JSON نمائندگی کی درخواست کرتا ہے۔ 
صارف ایجنٹ - کلائنٹ کی شناخت کرتا ہے (مثال کے طور پر، ایک براؤزر یا حسب ضرورت کلائنٹ)۔ 
Accept-Language - جواب کے لیے ترجیحی زبانوں کی نشاندہی کرتا ہے۔ 
کنکشن: زندہ رکھیں - سرور سے TCP کنکشن برقرار رکھنے کی درخواست کرتا ہے۔ 
اجازت - تصدیق کے لیے ایک بیئرر ٹوکن پر مشتمل ہے، وسائل تک محفوظ رسائی کو یقینی بناتا ہے۔ 
خالی لائن: ہیڈر کو باڈی سے الگ کرتا ہے (CRLF)۔ 
باڈی: کوئی نہیں - REST میں GET درخواستوں کا عام طور پر کوئی باڈی نہیں ہوتا ہے، کیونکہ وہ ڈیٹا کو بازیافت کرتی ہیں۔

2. جواب حاصل کریں۔

HTTP/1.1 200 ٹھیک ہے۔
تاریخ: جمعرات، 12 جون 2025 09:19:00 GMT
سرور: Nginx/1.18.0
مواد کی قسم: درخواست/json؛ charset=UTF-8
مواد کی لمبائی: 165
کیش کنٹرول: زیادہ سے زیادہ عمر = 3600
کنکشن: زندہ رکھنا

{ 
"id": 123، 
"نام": "ایلس اسمتھ" 
"ای میل": "alice@example.com"، 
"_links": { 
"self": {"href": "/users/123"}، 
"update": {"href": "/users/123", "method": "PATCH"}، 
"delete": {"href": "/users/123"، "طریقہ": "DELETE"} 
}
}

وضاحت: 

باقی اصولوں کا مظاہرہ: 
نمائندگی کے ذریعے وسائل کی ہیرا پھیری: جواب صارف کے وسائل کی حالت کی JSON نمائندگی فراہم کرتا ہے، بشمول id، نام، اور ای میل جیسی صفات۔ 
خود وضاحتی پیغامات: مواد کی قسم ہیڈر نمائندگی کی شکل (ایپلی کیشن/json) کی وضاحت کرتا ہے، اور باڈی میں تمام ضروری ڈیٹا شامل ہوتا ہے۔ 
HATEOAS: _links آبجیکٹ متعلقہ ایکشنز (خود، اپ ڈیٹ، ڈیلیٹ) کے لیے ہائپر لنکس فراہم کرتا ہے، جو کلائنٹس کو متحرک طور پر اگلے ممکنہ اقدامات کو دریافت کرنے کے قابل بناتا ہے۔ 
Cacheability: Cache-Control ہیڈر (max-age=3600) بتاتا ہے کہ جواب کو ایک گھنٹے کے لیے کیش کیا جا سکتا ہے، جس سے بعد کی درخواستوں کے لیے سرور کا بوجھ کم ہو جاتا ہے۔ 
پیغام کے اجزاء: 
اسٹارٹ لائن: HTTP/1.1 200 ٹھیک ہے۔ 
HTTP ورژن: HTTP/1.1۔

اسٹیٹس کوڈ: 200 - اشارہ کرتا ہے کہ درخواست کامیاب تھی۔ 
وجہ جملہ: ٹھیک ہے۔ 
ہیڈرز: 
تاریخ - جواب کا ٹائم اسٹیمپ۔ 
سرور - سرور سافٹ ویئر (Nginx) کی شناخت کرتا ہے۔ 
مواد کی قسم: درخواست/json؛ charset=UTF-8 - JSON فارمیٹ اور UTF-8 انکوڈنگ کی وضاحت کرتا ہے۔ 
مواد کی لمبائی: 165 - بائٹس میں JSON باڈی کی لمبائی۔ 
کیش کنٹرول - 3600 سیکنڈ کے لیے کیشنگ کو قابل بناتا ہے۔ 
کنکشن: زندہ رکھیں - کنکشن کو دوبارہ استعمال کرنے کی اجازت دیتا ہے۔ 
خالی لائن: ہیڈر کو باڈی سے الگ کرتا ہے۔ 
باڈی: ایک JSON آبجیکٹ جو صارف کی نمائندگی کرتا ہے، جس میں دریافت ہونے کے لیے HATEOAS لنکس ہیں۔

3. درخواست پوسٹ کریں۔

POST/users HTTP/1.1
میزبان: api.example.com
قبول کریں: application/json
مواد کی قسم: درخواست/json
مواد کی لمبائی: 65
صارف کا ایجنٹ: Mozilla/5.0 (Windows NT 10.0؛ Win64; x64) AppleWebKit/537.36
کنکشن: زندہ رکھنا
اجازت: بیئرر eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

{ 
"نام": "باب جانسن"، 
"ای میل": "bob@example.com"
}

وضاحت: 

باقی اصولوں کا مظاہرہ: 
وسائل کی شناخت: URI/users صارفین کے لیے جمع کرنے والے وسائل کی شناخت کرتا ہے، جہاں ایک نیا صارف بنایا جائے گا۔ 
بے وطنی: درخواست میں وہ تمام ڈیٹا (JSON پے لوڈ، تصدیقی ٹوکن) شامل ہے جس کی ضرورت سرور کی طرف سے سیشن کی حالت کے بغیر، وسائل کو بنانے کے لیے درکار ہے۔ 
یکساں انٹرفیس: ایک نیا وسیلہ بنانے کے لیے POST طریقہ استعمال کرتا ہے، جس میں مواد کی قسم اور قبول ہیڈر درخواست اور جواب کے لیے JSON کی وضاحت کرتے ہیں۔ 
نمائندگی کے ذریعے وسائل کی ہیرا پھیری: JSON باڈی تخلیق کیے جانے والے نئے صارف کی نمائندگی فراہم کرتی ہے۔ 
پیغام کے اجزاء: 
اسٹارٹ لائن: POST/users HTTP/1.1 
طریقہ: POST - صارفین کے مجموعہ میں ایک نیا وسیلہ بناتا ہے۔ 
URI: /users - صارفین کے مجموعہ کو نشانہ بناتا ہے۔ 
HTTP ورژن: HTTP/1.1۔ 
ہیڈرز: 
میزبان، صارف-ایجنٹ، کنکشن، اجازت - GET درخواست کی طرح۔ 
قبول کریں: درخواست/json - JSON جواب کی درخواست کرتا ہے۔ 
مواد کی قسم: درخواست/json - اشارہ کرتا ہے کہ درخواست کا باڈی JSON ہے۔ 
مواد کی لمبائی: 65 - بائٹس میں JSON باڈی کی لمبائی۔ 
خالی لائن: ہیڈر کو باڈی سے الگ کرتا ہے۔ 
باڈی: نئے صارف کے لیے نام اور ای میل فیلڈز کے ساتھ ایک JSON آبجیکٹ۔

4. جواب پوسٹ کریں۔

HTTP/1.1 201 بنایا گیا۔
تاریخ: جمعرات، 12 جون 2025 09:19:05 GMT
سرور: Nginx/1.18.0
مواد کی قسم: درخواست/json؛ charset=UTF-8
مواد کی لمبائی: 188
مقام: /users/124
کنکشن: زندہ رکھنا

{ 
"id": 124، 
"نام": "باب جانسن"، 
"email": "bob@example.com"، 
"_links": { 
"self": {"href": "/users/124"}، 
"update": {"href": "/users/124", "method": "PATCH"}، 
"delete": {"href": "/users/124"، "طریقہ": "DELETE"} 
}
}

وضاحت: 

باقی اصولوں کا مظاہرہ: 
نمائندگی کے ذریعے وسائل کی ہیرا پھیری: جواب نئے تخلیق شدہ صارف کی JSON نمائندگی دیتا ہے، بشمول سرور کے ذریعے تفویض کردہ ID۔ 
خود وضاحتی پیغامات: مواد کی قسم اور مقام کے ہیڈر جواب اور نئے وسائل کے URI کے بارے میں میٹا ڈیٹا فراہم کرتے ہیں۔ 
HATEOAS: _links آبجیکٹ میں مزید کارروائیوں کے لیے ہائپر لنکس شامل ہیں، متحرک نیویگیشن کی حمایت کرتے ہیں۔ 
یکساں انٹرفیس: 201 تخلیق شدہ اسٹیٹس کوڈ اور لوکیشن ہیڈر وسائل کی کامیاب تخلیق کی نشاندہی کرتا ہے اور نئے وسائل کا URI فراہم کرتا ہے۔ 
پیغام کے اجزاء: 
اسٹارٹ لائن: HTTP/1.1 201 بنایا گیا۔ 
HTTP ورژن: HTTP/1.1۔ 
اسٹیٹس کوڈ: 201 - اشارہ کرتا ہے کہ وسیلہ کامیابی سے بنایا گیا تھا۔ 
وجہ جملہ: تخلیق کیا گیا۔ 
ہیڈرز: 
تاریخ، سرور، مواد کی قسم، مواد کی لمبائی، کنکشن – GET جواب کی طرح۔ 
مقام: /users/124 - نئے بنائے گئے صارف کے وسائل کے URI کی وضاحت کرتا ہے۔ 
خالی لائن: ہیڈر کو باڈی سے الگ کرتا ہے۔ 
باڈی: ایک JSON آبجیکٹ جو نئے صارف کی نمائندگی کرتا ہے، HATEOAS لنکس کے ساتھ۔

کلیدی REST تصورات کا مظاہرہ کیا گیا۔

یہ مثال براہ راست "REST کی بنیادی تعمیراتی رکاوٹیں" اور "RESTful APIs میں کلیدی تصورات" کے سیکشنز سے اس کی وضاحت کرتی ہے: 

کلائنٹ-سرور آرکیٹیکچر: درخواستیں اور جوابات کلائنٹ کے خدشات (درخواستیں بھیجنے) کو سرور کے خدشات (وسائل پر کارروائی اور ذخیرہ کرنے) سے الگ کرتے ہیں۔ 
بے وطنی: ہر درخواست خود پر مشتمل ہوتی ہے، جس میں تصدیقی ٹوکن اور ڈیٹا شامل ہوتا ہے، جس میں سرور سائیڈ سیشن کی حالت کی ضرورت نہیں ہوتی ہے۔ 
کیچ ایبلٹی: GET جواب میں کیشنگ کو فعال کرنے، سرور کا بوجھ کم کرنے کے لیے کیش کنٹرول ہیڈر شامل ہے۔ 
یکساں انٹرفیس: 
وسائل کی شناخت: URIs جیسے /users/123 اور /users واضح طور پر وسائل کی شناخت کرتے ہیں۔ 
نمائندگی کے ذریعے ہیرا پھیری: JSON پے لوڈز تخلیق اور بازیافت کے لیے وسائل کی ریاستوں کی نمائندگی کرتے ہیں۔ 
خود وضاحتی پیغامات: مواد کی قسم، قبول، اور اجازت جیسے ہیڈر پیغامات کو قابل تشریح بناتے ہیں۔ 
HATEOAS: رسپانس لنکس کلائنٹس کو متعلقہ وسائل اور اعمال کو متحرک طور پر دریافت کرنے کے قابل بناتے ہیں۔ 
HTTP طریقے: GET ایک وسائل کی بازیافت کرتا ہے۔

پیشکش؛ POST ایک نیا وسیلہ بناتا ہے۔ 
HTTP اسٹیٹس کوڈز: کامیاب بازیافت کے لیے 200 OK، 201 مقام ہیڈر کے ساتھ کامیاب تخلیق کے لیے بنایا گیا۔ 
میڈیا کی قسمیں: ایپلیکیشن/json کو مسلسل نمائندگی کے لیے استعمال کیا جاتا ہے، جیسا کہ ہیڈر میں بیان کیا گیا ہے۔

Python میں REST APIs کے ساتھ کام کرنا

Python استعمال کرنے والے (کلائنٹ سائیڈ) اور بلڈنگ (سرور سائیڈ) REST APIs دونوں کے لیے بہترین لائبریریاں پیش کرتا ہے۔
کلائنٹ سائیڈ: لائبریری کی درخواست کرتا ہے۔

درخواستوں کی لائبریری پائتھون میں HTTP درخواستیں کرنے کے لئے ڈی فیکٹو معیار ہے۔

تنصیب:

uv init rest_code
cd rest_code
# درخواستیں انسٹال کریں۔
uv درخواستیں شامل کریں۔

مثال: عوامی REST API کا استعمال

درآمد کی درخواستیں
json درآمد کریں۔

# JSONPlaceholder کا استعمال کرتے ہوئے، جانچ اور پروٹو ٹائپنگ کے لیے ایک مفت جعلی آن لائن REST API۔
BASE_URL = "https://jsonplaceholder.typicode.com"

# --- ایک پوسٹ حاصل کرنے کی درخواست حاصل کریں ---
def get_post(post_id): 
پرنٹ(f"\\n--- پوسٹ کے لیے درخواست حاصل کریں/{post_id}---") 
کوشش کریں: 
response = requests.get(f"{BASE_URL}/posts/{post_id}") 
response.raise_for_status() # خراب جوابات (4XX یا 5XX) کے لیے HTTPError اٹھاتا ہے۔ 

پرنٹ (f"سٹیٹس کوڈ: {response.status_code}") 
post_data = response.json() 
پرنٹ (f"پوسٹ ٹائٹل: {post_data.get('title')}") 
# پرنٹ (f"مکمل جوابی ڈیٹا: {post_data}") 
پوسٹ_ڈیٹا واپس کریں۔ 
سوائے requests.exceptions.HTTPERrror بطور غلطی: 
پرنٹ (f" Http ایرر: {errh}") 
سوائے requests.exceptions.ConnectionError بطور errc: 
پرنٹ (f" جڑنے میں خرابی: {errc}") 
سوائے requests.exceptions.Timeout بطور errt: 
پرنٹ (f" ٹائم آؤٹ کی خرابی: {errt}") 
سوائے requests.exceptions.RequestException بطور غلطی: 
پرنٹ (f" کچھ اور غلط ہوا: {err}") 
کوئی واپس نہیں

# --- ایک نئی پوسٹ بنانے کی درخواست پوسٹ کریں ---
def create_post(عنوان، باڈی، user_id): 
پرنٹ ("\\n--- پوسٹ کرنے کی درخواست /پوسٹ ---") 
new_post_payload = { 
"عنوان": عنوان، 
"جسم": جسم، 
"userId": user_id 
} 
ہیڈر = {"مواد کی قسم": "درخواست/json؛ charset=utf-8"} 
کوشش کریں: 
response = requests.post(f"{BASE_URL}/posts", data=json.dumps(new_post_payload), headers=headers, timeout=5) 
response.raise_for_status() 

پرنٹ(f"سٹیٹس کوڈ: {response.status_code}") # 201 بنایا جانا چاہیے 
create_post_data = response.json() 
پرنٹ(f"تخلیق شدہ پوسٹ ID: {created_post_data.get('id')}") 
پرنٹ(f"تخلیق شدہ پوسٹ کا عنوان: {created_post_data.get('title')}") 
بنایا گیا_پوسٹ_ڈیٹا واپس کریں۔ 
سوائے requests.exceptions.RequestException بطور e: 
پرنٹ (f" پوسٹ کی درخواست ناکام ہوگئی: {e}") 
کوئی واپس نہیں

اگر __name__ == "__main__": 
get_post(1) 
get_post(9999) # وسائل کی مثال نہیں ملی (404 کو ٹرگر کرنا چاہیے) 

create_post = create_post ("میری نئی پوسٹ"، "یہ میری حیرت انگیز نئی پوسٹ کا باڈی ہے۔"، 101) 
اگر بنائی_پوسٹ: 
پرنٹ(f"ID کے ساتھ کامیابی سے پوسٹ بنائی گئی: {created_post.get('id')}")

REST بمقابلہ دیگر تعمیراتی طرزیں/پروٹوکول 

SOAP (سادہ آبجیکٹ ایکسیس پروٹوکول): 
SOAP ایک سخت تصریح کے ساتھ ایک پروٹوکول ہے، عام طور پر پیغام کی شکلوں کے لیے XML استعمال کرتا ہے اور اکثر سروس کی تفصیل کے لیے WSDL پر انحصار کرتا ہے۔ 
REST ایک آرکیٹیکچرل اسٹائل ہے جس میں زیادہ لچک ہے، عام طور پر HTTP پر JSON استعمال کرتا ہے، اور وضاحت کے لیے OpenAPI جیسے معیارات کا فائدہ اٹھا سکتا ہے۔ 
SOAP زیادہ پیچیدہ اور لفظی ہو سکتا ہے لیکن سیکیورٹی (WS-Security) اور لین دین کے لیے پہلے سے موجود معیارات پیش کرتا ہے، جو اکثر انٹرپرائز ماحول میں پسند کیا جاتا ہے۔ 
گراف کیو ایل: 
گراف کیو ایل APIs کے لیے ایک استفسار کی زبان ہے اور ان سوالات کو انجام دینے کے لیے سرور سائیڈ رن ٹائم ہے۔ 
کلائنٹ بالکل وہی ڈیٹا مانگتے ہیں جس کی انہیں ضرورت ہوتی ہے، روایتی REST APIs کے ساتھ عام طور پر اوور فیچنگ یا انڈر فیچنگ سے گریز کرتے ہوئے جو وسائل کے لیے فکسڈ ڈیٹا اسٹرکچر واپس کرتے ہیں۔ 
گراف کیو ایل عام طور پر تمام کارروائیوں کے لیے ایک ہی اختتامی نقطہ (مثال کے طور پر، /graphql) اور HTTP POST استعمال کرتا ہے۔ 
REST وسائل پر کارروائیوں کی وضاحت کرنے کے لیے متعدد اینڈ پوائنٹس (URIs) اور HTTP فعل استعمال کرتا ہے۔ 
وہ ایک ساتھ رہ سکتے ہیں۔ کچھ سسٹمز لچکدار ڈیٹا کی بازیافت کے لیے گراف کیو ایل کا استعمال کرتے ہیں اور آسان وسائل کی ہیرا پھیری یا کمانڈ جیسی کارروائیوں کے لیے REST۔ 
gRPC (گوگل ریموٹ پروسیجر کال): 
gRPC ایک اعلی کارکردگی، اوپن سورس RPC فریم ورک ہے جو کسی بھی ماحول میں چل سکتا ہے۔ یہ عام طور پر سروس کنٹریکٹس اور میسج فارمیٹس کی وضاحت کے لیے پروٹوکول بفرز اور HTTP/2 کو اس کے ٹرانسپورٹ پروٹوکول کے طور پر استعمال کرتا ہے۔ 
کارکردگی، کم تاخیر، اور مضبوط ٹائپنگ پر توجہ مرکوز کرتا ہے۔ مائیکرو سروس مواصلات کے لیے بہترین۔ 
REST وسائل پر مبنی فن تعمیر پر زیادہ توجہ مرکوز کرتا ہے اور معیاری HTTP سیمنٹکس کا فائدہ اٹھاتا ہے، جو اسے وسیع پیمانے پر قابل رسائی بناتا ہے۔

آرام کی طاقتیں۔ 

سادگی اور سمجھنے میں آسانی: مانوس HTTP طریقوں اور URIs پر مبنی، یہ سیکھنے اور استعمال کرنے میں نسبتاً آسان بناتا ہے۔ 
اسکیل ایبلٹی: بے وطنی اور کیچ ایبلٹی افقی طور پر پیمانہ کرنے کی صلاحیت میں اہم کردار ادا کرتی ہے۔ 
انٹرآپریبلٹی اور وسیع اپنانے: پلیٹ فارم اور لینگویج-ایگنوسٹک۔ عملی طور پر تمام پروگرامنگ زبانوں اور ویب فریم ورک کے ذریعہ تعاون یافتہ۔ 
ڈیٹا فارمیٹس میں لچک

: جب کہ JSON سب سے عام ہے، REST XML، HTML، سادہ متن، یا کوئی اور فارمیٹ استعمال کر سکتا ہے۔ 
موجودہ ویب انفراسٹرکچر کا فائدہ اٹھاتا ہے: معیاری HTTP، URIs، DNS، اور کیشنگ میکانزم کا استعمال کرتا ہے۔ 
دریافت (HATEOAS کے ساتھ): اچھی طرح سے لاگو HATEOAS گاہکوں کو متحرک طور پر APIs کو نیویگیٹ کرنے کی اجازت دیتا ہے۔

REST کی کمزوریاں/ حدود 

اوور فیچنگ اور انڈر فیچنگ: فکسڈ ریسورس کی نمائندگی کلائنٹس کو ان کی ضرورت سے زیادہ ڈیٹا حاصل کرنے کا باعث بن سکتی ہے (زیادہ بازیافت) یا تمام مطلوبہ ڈیٹا (انڈر فیچنگ) حاصل کرنے کے لیے متعدد درخواستیں کرنے کی ضرورت ہے۔ گراف کیو ایل خاص طور پر اس سے خطاب کرتا ہے۔ 
متعدد راؤنڈ ٹرپس: پیچیدہ ڈیٹا کی ضروریات کو متعلقہ وسائل کی بازیافت کے لیے کئی کلائنٹ سرور راؤنڈ ٹرپس کی ضرورت پڑ سکتی ہے، تاخیر میں اضافہ۔ 
بے وطنی اوور ہیڈ: چونکہ ہر درخواست کا خود ساختہ ہونا ضروری ہے، اس لیے اس میں بے کار معلومات ہو سکتی ہیں (مثلاً، ہر درخواست میں تصدیقی ٹوکن)۔ 
کوئی بلٹ ان ریئل ٹائم/پش صلاحیتیں نہیں: REST بنیادی طور پر کلائنٹ کے ذریعے شروع کیا جاتا ہے (پل پر مبنی)۔ سرور کی طرف سے شروع کردہ اپ ڈیٹس یا حقیقی وقت میں دو طرفہ مواصلات کے لیے، WebSockets یا Server-Sent Events (SSE) جیسی ٹیکنالوجیز کو عام طور پر ترجیح دی جاتی ہے۔ 
معیاری کاری ڈھیلی ہو سکتی ہے: آرکیٹیکچرل سٹائل ہونے کی وجہ سے، REST کی تشریحات مختلف ہو سکتی ہیں، اگر ڈیزائن کے اصولوں پر سختی سے عمل نہ کیا جائے تو مختلف APIs میں تضادات پیدا ہو سکتے ہیں۔ 
بہت سے اختتامی نقطوں کا انتظام کرنا: بہت سے وسائل اور آپریشنز کے ساتھ بہت پیچیدہ نظاموں کے لیے، الگ الگ اختتامی نقطوں کی تعداد بڑی ہو سکتی ہے۔

Agentic AI سسٹمز میں کیسز کا استعمال کریں (DACA سیاق و سباق)

RESTful APIs ماڈیولر اور انٹرآپریبل ایجنٹ AI سسٹمز کی تعمیر کے لیے ایک سنگ بنیاد ہیں جیسا کہ DACA پیٹرن کے ذریعے تصور کیا گیا ہے: 

کور ایجنٹ فنکشنلٹی API: ایجنٹ کی صلاحیتوں، حیثیت اور ترتیب کو REST اینڈ پوائنٹس کے ذریعے ظاہر کرنا۔ 
/ایجنٹس/{agent_id}/status حاصل کریں۔ 
POST /agents/{agent_id}/tasks (ایک نیا کام تفویض کرنے کے لیے) 
/ایجنٹس/{agent_id}/tasks/{task_id} حاصل کریں 
ٹول انٹیگریشن: ایجنٹ بیرونی ٹولز، سروسز، یا ڈیٹا کے ذرائع کے ساتھ بات چیت کر سکتے ہیں جو REST APIs (مثلاً موسم APIs، نالج بیسز، سرچ انجن) کو ظاہر کرتے ہیں۔ 
ڈیٹا ایکسچینج اور استقامت: ایجنٹ RESTful انٹرفیس کے ذریعے ڈیٹا بیس، ویکٹر اسٹورز، یا دیگر اسٹوریج سروسز سے ڈیٹا بازیافت یا ذخیرہ کرسکتے ہیں۔ 
انٹر-ایجنٹ کمیونیکیشن: ایجنٹوں کے درمیان آسان، درخواست کے جواب کے انداز کے مواصلات کے لیے، REST ایک سیدھا سادھا انتخاب ہو سکتا ہے، خاص طور پر اگر ایجنٹوں کو آزاد مائیکرو سروسز کے طور پر تیار کیا گیا ہو۔ 
مینجمنٹ اور آرکیسٹریشن APIs: خود DACA انفراسٹرکچر (مثال کے طور پر، تعینات کرنے، نگرانی کرنے، اسکیلنگ کرنے، اور کنفیگرنگ ایجنٹوں کے لیے) REST APIs کے ذریعے منظم کیا جا سکتا ہے۔ 
ہیومن ان دی لوپ (HITL) انٹرفیس: انسانی نگرانی اور مداخلت کے لیے ویب پر مبنی ڈیش بورڈز یا کنٹرول پینل عام طور پر REST APIs کے ذریعے بیک اینڈ ایجنٹ سسٹمز کے ساتھ تعامل کریں گے۔ 
ماڈل سرونگ: جب کہ خصوصی ماڈل سرونگ حل موجود ہیں (جیسے TensorFlow Serving، TorchServe)، آسان ماڈلز یا کسٹم انفرنس منطق کو REST اینڈ پوائنٹس کے طور پر سامنے لایا جا سکتا ہے۔ 
پوسٹ کریں /ماڈلز/{model_id}/پیش گوئی 
لاگنگ اور مانیٹرنگ: ایجنٹ REST کے ذریعے مرکزی لاگنگ/مانیٹرنگ سروس کو لاگ یا میٹرکس بھیج سکتے ہیں۔

DACA میں، REST APIs اس بات کو یقینی بنانے کے لیے ایک معیاری، اچھی طرح سے سمجھا جانے والا طریقہ فراہم کرتے ہیں کہ ایجنٹی نظام کے مختلف اجزاء (ایجنٹس، ٹولز، ڈیٹا اسٹورز، UIs) مؤثر طریقے سے بات چیت کر سکتے ہیں اور آزادانہ طور پر تیار/اسکیل کیے جا سکتے ہیں۔
مزید پڑھنا اور حوالہ جات 

بنیادی: 
فیلڈنگ، رائے ٹی (2000)۔ باب 5: "آرکیٹیکچرل اسٹائلز اینڈ دی ڈیزائن آف نیٹ ورک بیسڈ سافٹ ویئر آرکیٹیکچرز" میں نمائندہ ریاست کی منتقلی (REST)۔ 
ڈیزائن کے اصول اور بہترین طرز عمل: 
MDN Web Docs: REST 
پوسٹ مین بلاگ: REST API کیا ہے؟ مثالیں، استعمال، اور چیلنجز (آپ کا فراہم کردہ لنک) 
Microsoft API ڈیزائن کے بہترین طریقے 
گوگل کلاؤڈ API ڈیزائن گائیڈ 
Python لائبریریاں: 
دستاویزات کی درخواست کرتا ہے۔ 
فاسٹ اے پی آئی دستاویزات 
API تفصیل: 
OpenAPI اقدام (Swagger) 
ویکیپیڈیا: 
ریاستی نمائندگی کی منتقلی (REST) ​​(آپ کا فراہم کردہ لنک)
