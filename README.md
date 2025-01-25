# bank-api
<h1>Bank API</h1>
<h3>Overview</h3>
<p>This project implements a simple Bank API using Flask for retrieving data about banks and their branches. The API includes two main endpoints:</p>
<ul>
<li>GET /banks - Retrieves a list of all banks.</li>
<li>GET /banks/{bank_id}/branches - Retrieves all branches of a specific bank by bank_id</li>
</ul>
<h3>Method Used to Solve the Problem</h3>
<ul>
<li>Flask Framework: Used to implement the RESTful API.</li>
<li>Unit Tests: Written using the unittest module to test the functionality of the API, ensuring that the endpoints return the correct status code and response data.</li>
<li>Error Handling: A custom error handler is used to return appropriate error messages in case of invalid requests.</li>
</ul>
<h3>Steps to Implement the Solution</h3>
<ol>
<li>Created the Flask Application:</li>
<ul>
<li>Defined the main app using Flask.</li>
<li>Created two endpoints (/banks and /banks/{bank_id}/branches).</li>
</ul>
<li>Tested the Endpoints:</li>
<li>Written tests using unittest to check for correct response codes and data formatting.</li>
<li>Error Handling:</li>
<li>Added a custom 404 error handler to handle missing URLs.</li>
</ol>
<h3>Core Technologies Used</h3>
<ul>
<li><b>Flask:</b> To create the backend API.</li>
<li>unittest: For writing unit tests to verify the correctness of the API.</li>
<li>Python: The programming language used.</li>
</ul>
<h3>Conclusion</h3>
<p>The API successfully implements the required functionality to fetch bank and branch details and supports error handling for invalid URLs. The solution is complete with unit tests and deployed for public access on Vercel.</p>