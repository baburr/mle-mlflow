export MLFLOW_S3_ENDPOINT_URL=https://storage.yandexcloud.net
export AWS_ACCESS_KEY_ID=YCAJE3Nlz8iDILW5VTYM1ihQB
export AWS_SECRET_ACCESS_KEY=YCPjvS7uwhvJpUj3bKm8X-IX4QAwBIVsvX61IL44


mlflow server \
  --backend-store-uri postgresql://mle_20250424_b61c63444c:862da5f89661427b873bb1b069c04287@rc1b-uh7kdmcx67eomesf.mdb.yandexcloud.net:6432/playground_mle_20250424_b61c63444c
  --default-artifact-root s3://s3-student-mle-20250424-b61c63444c \
  --no-serve-artifacts
