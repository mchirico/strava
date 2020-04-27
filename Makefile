
build:
	cd angular && ./updateDist.sh
	docker build --no-cache -t gcr.io/septapig/strava -f Dockerfile .
	#gcloud builds submit --tag gcr.io/septapig/strava --project septapig --timeout 35m23s

run:
	docker run -p 8080:8080 --env PORT=8080  --rm -it gcr.io/septapig/strava

push:
	docker push gcr.io/septapig/strava

pull:
	docker pull gcr.io/septapig/strava


deploy:
	cd angular && ./updateDist.sh
	gcloud builds submit --tag gcr.io/septapig/strava --project septapig --timeout 35m23s
	gcloud run deploy strava  --image gcr.io/septapig/strava --platform managed \
              --platform managed --allow-unauthenticated --project septapig \
              --region us-east1 --port 8080 --max-instances 8  --memory 128Mi
