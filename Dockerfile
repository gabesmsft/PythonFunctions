FROM mcr.microsoft.com/azure-functions/python:2.0-python3.7

ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true \
    AzureWebJobsStorage=DefaultEndpointsProtocol=https;AccountName=storageaccountamanc9278;AccountKey=TTrETaLynmNxWdmgmbdtzx7s0jUMXfAZ85x1sDE8natXEwUEWs0qENjOmD6/g654Z4Bv97jbDeDlITtsKvOm1Q==;EndpointSuffix=core.windows.net

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /home/site/wwwroot