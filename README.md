# Flask Chatbot with OpenAI

**Developers:** Deekshita Saikia, Jaya Khan, Satvik Kishore

This project is a Flask application that uses SpeechRecognizer and OpenAI APIs to create a voice chatbot. The chatbot can respond to user input in natural language and is designed to be scalable using AWS EKS and load testing with Locust.

## High level Architecture

![Alt text](images/asset-ce8d8887-7317-4312-bb13-0fe34cd7e1d0.png "Architecture")

## Requirements

* Python 3.6 or higher
* OpenAI API key
* Docker
* Kubernetes command-line tool (kubectl)
* AWS command-line tool (aws)

## Getting Started

To run the chatbot on your local machine, follow these steps:


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

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Set up your OpenAI API credentials as the environment variable:

```
export OPENAI_API_KEY=YOUR_API_KEY
```

Replace YOUR_API_KEY with your OpenAI API key.

5. Run the app locally:

```
export FLASK_APP=app.py
flask run
```

The app will be available at http://localhost:5000/.

## Deployment

To deploy the chatbot to an AWS EKS cluster, follow these steps:


1. Build the Docker image:

```
docker build -t YOUR_IMAGE_NAME .
```

Replace YOUR_IMAGE_NAME with a name for your Docker image.

2. Push the Docker image to a registry:

```
docker tag YOUR_IMAGE_NAME YOUR_REGISTRY_URL/YOUR_IMAGE_NAME
docker push YOUR_REGISTRY_URL/YOUR_IMAGE_NAME
```

Replace YOUR_REGISTRY_URL with the URL of your Docker registry.

3. Create an EKS cluster in your AWS account.
   

4. Deploy the app to EKS:

```
aws eks update-kubeconfig --name YOUR_CLUSTER_NAME --region YOUR_REGION
kubectl apply -f kubernetes/
```

Replace YOUR_CLUSTER_NAME and YOUR_REGION with the name and region of your EKS cluster.

5. Access the app:

```
kubectl get svc chatbot-service
```

This will return the DNS name of the load balancer service. Use this to access the app in your web browser.

## Load Testing

To test the scalability of the chatbot, we use Locust, an open-source load testing tool. Follow these steps to run a load test:


1. Install Locust:

```
pip install locust
```

2. Run Locust:

```
locust --host=http://YOUR_LOAD_BALANCER_DNS_NAME
```

Replace YOUR_LOAD_BALANCER_DNS_NAME with the DNS name of your EKS load balancer service.

3. Access the Locust web interface in your browser:

```
http://localhost:8089/
```

Here, you can start the load test and see the results.

## Contributing

Contributions are welcome. Please open a pull request and we will respond at the earliest.