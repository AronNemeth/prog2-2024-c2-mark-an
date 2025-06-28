# 2025-06-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.10897  |       1.06498  |   0.103096 |
| solution-pl        |     0.497937 |       0.153751 |   0.237895 |
| solution-aron-mark |     5.81876  |       0.184233 |   0.239996 |
| solution-1-flask   |     0.509374 |       1.0083   |   0.271421 |
| solution-1         |     7.51097  |       1e-06    |   0.879194 |
| solution-2         |     0.515656 |       0.714296 |   1.04119  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.525023 |       0.156049 |   0.365907 |
| solution-pl        |     0.508269 |       0.153666 |   0.370975 |
| solution-flask     |     0.511453 |       1.00839  |   0.380561 |
| solution-1-flask   |     0.507741 |       1.00851  |   0.794874 |
| solution-2         |     0.511763 |       0.543638 |   3.8805   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.50248  |       0.160937 |    1.07355 |
| solution-pl        |     0.526761 |       0.164047 |    1.09399 |
| solution-flask     |     0.512776 |       1.00841  |    1.58268 |
| solution-1-flask   |     0.50637  |       1.00857  |    5.67316 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.501564 |       0.189883 |    3.23225 |
| solution-aron-mark |     0.499872 |       0.190665 |    3.25304 |
| solution-flask     |     0.505853 |       1.0085   |    5.21962 |