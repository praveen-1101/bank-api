<h1>BANK API</h1>
<h3>Overview</h3>
<p>This focusses on implementing an API service to fetch bank and branch details. The API supports REST queries and allows users to retrieve information about different banks and their branches.The API includes two main endpoints:</p>
<ul>
<li>GET /banks - Retrieves a list of all banks.</li>
<li>GET /banks/{bank_id}/branches - Retrieves all branches of a specific bank by bank_id</li>
</ul>
<h2>Method Used</h2>
<h3>Technologies</h3>
<ul>
<li><b>Backend Framework: <u>Flask</u></b> Used to implement the RESTful API.</li>
<li><b>Unit Tests:</b>It ensures that the endpoints return the correct status code and response data.</li>
<li><b>Deployment: </b>Vercel (Due to the requirement of adding a payment method in Heroku’s free tier, which I find cautious, I opted to use Vercel for deployment instead).</li>
</ul>
<h3>Implementation</h3>
<ol>
<li>
<b>API Endpoints:</b>
<ul>
<li><u>GET /banks</u>: Returns a list of all banks.</li>
<li><u>GET /banks/{bank_id}/branches</u>: Returns the list of branches for a specified bank.
</li>
</ul>
</li>
<li><b>Error Handling:</b> A custom 404 error handler is used to return appropriate error messages in case of invalid requests or URLs.</li>
<li><b>Unit Tests:</b>
<ul>
<li>The API is tested using Python's unittest framework. It checks for the following:
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
<p>The API was deployed on Vercel due to issues with Heroku's free-tier requirements, which require a payment method. Since I opted not to add a payment method for cautious reasons, <b><u>Vercel</u></b> was used as the deployment platform for easier setup and deployment.</p>
<b>Vercel Deployment Link: </b> https://bank-api-rust.vercel.app
</ul>
<h3>Time Taken</h3>
<p>I spent 2-3 days working on this project with 8 to 12 hours of focussed work, focusing on building the API , testing, and deploying it.</p>
<h3>Challenges</h3>
<p>I ran into some issues with deployment on Heroku due to the payment method, which led me to use Vercel instead. I learned a lot about deployment and error handling through this process.</p>