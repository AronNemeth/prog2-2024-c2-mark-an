# 2026-06-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.12835  |       1.13985  |   0.107035 |
| solution-pl        |     5.9552   |       0.204145 |   0.235001 |
| solution-aron-mark |     0.433045 |       0.153614 |   0.236782 |
| solution-1-flask   |     0.438905 |       1.00823  |   0.263957 |
| solution-1         |     7.44183  |       3e-06    |   0.763187 |
| solution-2         |     0.419565 |       0.794772 |   1.02899  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.430403 |       0.15006  |   0.368169 |
| solution-aron-mark |     0.433136 |       0.15505  |   0.368604 |
| solution-flask     |     0.435355 |       1.00849  |   0.397096 |
| solution-1-flask   |     0.448763 |       1.00832  |   0.816124 |
| solution-2         |     0.428214 |       0.531495 |   5.51108  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.432412 |       0.159437 |    1.11996 |
| solution-aron-mark |     0.435672 |       0.159405 |    1.13587 |
| solution-flask     |     0.429546 |       1.00853  |    1.66214 |
| solution-1-flask   |     0.441132 |       1.00849  |    5.70203 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.444357 |       0.188549 |    4.01206 |
| solution-aron-mark |     0.437537 |       0.184238 |    4.0928  |
| solution-flask     |     0.442806 |       1.00839  |    5.41363 |