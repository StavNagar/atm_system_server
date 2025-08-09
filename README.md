# ATM System - Server Side

**In-Memory ATM Backend :**
* I implemented a fully functional ATM backend using Flask and JWT-based authentication.
* All data (accounts, balances, logs) are stored in-memory using Python dictionaries and lists.
* Passwords are securely hashed with Werkzeug, ensuring no plain text storage.
* Each API route is protected to ensure users can only access their own account.
* The system supports:
    * User registration and login
    * Getting current account balance
    * Depositing money
    * Withdrawing money (with validation for sufficient funds)

**Data Structure Design :** 
2 main data structures:
* accounts dictionary:
    * Maps account_number → Account info (password hash, balance, timestamps).
* actions dictionary:
    * Maps account_number → list of Action objects representing deposits & withdrawals.
* I chosen to use dictinaries keyed by "account_number" in order to:
    - Enables fast lookups.
    - Organizes data per user cleanly.
    - Allows retrieving transaction history per account easily.

* Account stores user credentials and current balance.
* Action stores immutable logs of money movements.

**Modular code structure :**
- The code is organized into multiple files:
    * auth.py: handles user registration and login
    * services.py: contains business logic for deposit, withdrawal, balance retrieval
    * models.py: defines in-memory data structures and account password hashing
    * app.py: configures Flask app and registers routes

**REST API Design :**
* POST /auth/register: Create new account with unique account_number and password.
* POST /auth/login: Login with credentials to receive JWT.
* GET /accounts/{account_number}/balance: Get current balance.
* POST /accounts/{account_number}/deposit: Deposit money.
* POST /accounts/{account_number}/withdraw: Withdraw money.
* GET /accounts/{account_number}/actions: Get transaction history (optional, added for completeness).

**Logging Design :**
Centralized logger instance configured with timestamps and severity levels.
Logs important events:
  - User registrations
  - Login successes/failures
  - Deposits and withdrawals
  - Authorization failures
Helps trace server activity for debugging and auditing.

**Testing Strategy :**
Used pytest and Flask test client for integration-style tests.
  - Authentication tests (register, login)
  - Account operations (deposit, withdraw, balance)
  - Authorization checks (accessing other accounts)

--------------------------------------------------------------------------------------------------------------------------------------
**Additional Context & Challenges**
I completed this task while using a friend's computer over the weekend, as I am currently on military service and did not have access to my personal development environment. His computer had security restrictions that prevented me from installing external Python packages. This limited my ability to fully run and test the project locally during development, and I was unable to deploy (host) the project myself.

Despite that, I was able to:
- Design and implement the complete backend logic with correct API structure
- Write code that adheres to best practices, modularity, and extensibility
- Prepare automated test cases even though I couldn’t run them immediately

2 additional challenges I faced:
* Designing secure and RESTful endpoints:
   * Choosing the right structure for the endpoints and ensuring proper authentication & authorization per user was essential. Balancing simplicity and security in the /accounts/{account_number} route pattern required careful design thinking.
* Modeling transaction logs cleanly in-memory:
   * Tracking each user’s transaction history per account number — while ensuring the design would remain maintainable and easily extendable to a real database — added complexity to how in-memory data was stored and structured.

