# Considerations
To my understanding, the key considerations for choosing cloud architecture are:
- **Cost-effectiveness**: To optimise resource usage, we can use containerisation and serverless options. 
- **Scalability**: Handling load balancing.
- **Performance**: Better response times.
- **Availability**: Services will remain to be up and running.
- **Security**: Protection of application from malicious users.

# Decisions
We can make use of AWS S3 to store our raw data of the Excel and JSON files. Amazon RDS will also help to store the structured data that we have. The serverless AWS Lambda could also be considered to handle data processing, for the functions in our `./src` folder.

Alternatively, we could run containerize the application on Docker, for consistency across operating systems, then push the docker image onto AWS EC2, allowing for scalability. We can also use Kubernetes to deploy it to pods with EKS. If the application sees greater growth, maybe something akin to TripAdvisor, we could consider this option as well.

We can make use of AWS IAM for the "principle of least privilege", ensuring users only have access to what they need to. For logs and monitoring, we can use CloudWatch.

We can also make use of AWS SageMaker for the k-means algorithm used, as machine-learning models can be computationally intensive.

A CI/CD pipeline in GitHub Actions might also prove to be helpful.