# Flask Chatbot with OpenAI

This is a Flask application that works like a chatbot and pings OpenAI's API. It is deployed to an AWS EKS cluster and has Elastic Scale-Up Performance via Load Test with Locust.

## Requirements

* Python 3.6 or higher
* OpenAI API key
* Docker
* Kubernetes command-line tool (kubectl)
* AWS command-line tool (aws)

## Setup

1. Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

```

2. Create a virtual environment and activate it:

```
python -m venv venv
source venv/bin/activate
```

3. Install the dependencies:

```
pip install -r requirements.txt
```

4. Set the environment variables:

```
export OPENAI_API_KEY=YOUR_API_KEY
```

Replace YOUR_API_KEY with your OpenAI API key.

55. Run the app locally:

```
export FLASK_APP=app.py
flask run
```

The app will be available at http://localhost:5000/.

6. Build the Docker image:

```
docker build -t YOUR_IMAGE_NAME .
```

Replace YOUR_IMAGE_NAME with a name for your Docker image.

7. Push the Docker image to a registry:

```
docker tag YOUR_IMAGE_NAME YOUR_REGISTRY_URL/YOUR_IMAGE_NAME
docker push YOUR_REGISTRY_URL/YOUR_IMAGE_NAME
```

Replace YOUR_REGISTRY_URL with the URL of your Docker registry.

8. Deploy the app to EKS:

```
aws eks update-kubeconfig --name YOUR_CLUSTER_NAME --region YOUR_REGION
kubectl apply -f kubernetes/
```

Replace YOUR_CLUSTER_NAME and YOUR_REGION with the name and region of your EKS cluster.

9. Access the app:

```
kubectl get svc chatbot-service
```

This will return the DNS name of the load balancer service. Use this to access the app in your web browser.

## Load Testing

To perform a load test on the app, you can use Locust. Follow the steps below:

1. Install Locust:

```
pip install locust
```

2. Run Locust:

```
locust --host=http://YOUR_LOAD_BALANCER_DNS_NAME
```

Replace YOUR_LOAD_BALANCER_DNS_NAME with the DNS name of your EKS load balancer service.

3. Open the web interface:

```
http://localhost:8089/
```

Here, you can start the load test and see the results.

## Contributing

Contributions are welcome. Please open a pull request and we will respond at the earliest.


