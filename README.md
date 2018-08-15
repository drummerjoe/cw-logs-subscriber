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
    FILTER_PATTERN: '<cw-logs-filter>'              # Leave empty if n/a

shipper:
  environment:
    ES_CLUSTER_ENDPOINT: '<es_cluster_endpoint>'
    ES_INDEX_PREFIX: '<es_index_prefix>'            # defaults to "cwl"
```

Deploy the stack
```bash
sls deploy --stage prod
```

# Usage
- We can use `LOG_GROUP_FILTER` to select which groups will be subscribed (`if LOG_GROUP_FILTER in log_group_name`). 
- We can use the serverless stage to ship logs to different Elasticsearch clusters. Just make sure to edit `.env.yml` appropriately.
  ```bash
  sls deploy --stage my-prod-es
  sls deploy --stage my-dev-es
  ```

- We've seen issues subscribing more than 50 log groups to the same lambda (probably a number of triggers limit). A work-around would be to create multiple lambdas to handle the workload. If you need to do so, just create another `shipper` and `ShipperLambdaInvokePermission` blocks with different names in the serverless.yml.