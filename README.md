# cw-logs-subscriber
Automatically subscribe CloudWatch Log groups to ship to AWS Elasticsearch via AWS Lambda.

# Installation
Install serverless
```bash
npm install -g serverless
```

Install serverless plugins in the app dir
```bash
npm install serverless-pseudo-parameters
```

Create/Update `.env.yml`
```yml
subscriber:
  environment:
    LOG_GROUP_FILTER: '<filter_groups>'
    FILTER_PATTERN: '<cw-logs-filter>'

shipper:
  environment:
    ES_CLUSTER_ENDPOINT: '<es_cluster_endpoint>'
```

Deploy the stack
```bash
sls deploy --stage prod
```