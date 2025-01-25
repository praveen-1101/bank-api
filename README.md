# bank-api
<h1>Bank API</h1>
<h3>Overview</h3>
<p>This focusses on implementing an API service to fetch bank and branch details. The API supports REST queries and allows users to retrieve information about different banks and their branches.The API includes two main endpoints:</p>
<ul>
<li>GET /banks - Retrieves a list of all banks.</li>
<li>GET /banks/{bank_id}/branches - Retrieves all branches of a specific bank by bank_id</li>
</ul>
<h2>Method Used</h2>
<h3>Technologies</h3>
<ul>
<li><b>Backend Framework: Flask-</b> Used to implement the RESTful API.</li>
<li><b>Unit Tests:</b> Written using the unittest module to test the functionality of the API, ensuring that the endpoints return the correct status code and response data.</li>
<li><b>Deployment: </b>Vercel (Due to the requirement of adding a payment method in Heroku’s free tier, which I find cautious, I opted to use Vercel for deployment instead).</li>
</ul>
<h3>Implementation</h3>
<ol>
<li>
<b>API Endpoints:</b>
<ul>
<li><u>GET /banks</u>: Returns a list of all banks.<li>
<li><u>GET /banks/{bank_id}/branches</u>: Returns the list of branches for a specified bank.
</li>
</ul>
</li>
<li><b>Error Handling:</b> A custom 404 error handler is used to return appropriate error messages in case of invalid requests or URLs.</li>
<li><b>Unit Tests:</b>
<ul>
<li>The API was tested using Python's unittest framework. The tests include checks for the following:
<ul>
<li>Fetching all banks.</li>
<li>Fetching branches for a specific bank.</li>
<li>Handling requests for non-existing bank IDs.</li>
</ul>
</li>
</ul>
</li>
</ol>
<h3>Deployment</h3>
<p>The API was deployed on Vercel due to issues with Heroku's free-tier requirements, which require a payment method. Since I opted not to add a payment method for cautious reasons, Vercel was used as the deployment platform for easier setup and deployment.</p>
<h3>Vercel Deployment Link: </h3><a href="">
</ul>
<h3>Time Taken</h3>
<p>This project was completed in 2-3 days, focusing on API development, unit testing, and deployment.</p>
<h3>Conclusion</h3>
<p>The API successfully implements the required functionality to fetch bank and branch details and supports error handling for invalid URLs. The solution is complete with unit tests and deployed for public access on Vercel.</p>