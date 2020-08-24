import logging
import os
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    logging.info('Running')
    identity_endpoint = os.environ["IDENTITY_ENDPOINT"] # Env var provided by Azure. Local to service doing the requesting.
    identity_header = os.environ["IDENTITY_HEADER"] # Env var provided by Azure. Local to service doing the requesting.
    api_version = "2019-08-01" # "2018-02-01" #"2019-03-01" #"2019-08-01"
    CLIENT_ID = "wakawaka"
    resource_requested = "https://ossrdbms-aad.database.windows.net"
	# resource_requested = "https://ossrdbms-aad.database.windows.net"

    URL = f"{identity_endpoint}?api-version={api_version}&resource={resource_requested}&client_id={CLIENT_ID}"
    headers = {"X-IDENTITY-HEADER":identity_header}
    logging.info('URL to query:' + str(URL))

    try:
        req = requests.get(URL, headers=headers)
    except Exception as e:
        logging.info(str(e))
        print(str(e))
        return str(e)
    else:
        try:
            password = req.json()["access_token"]
        except:
            password = str(req.text)
    logging.info('Password :' + password)
    return password

    return func.HttpResponse(f"Hello!")