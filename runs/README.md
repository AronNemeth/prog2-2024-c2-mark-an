# 2025-05-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.90171  |       1.00855  |   0.102338 |
| solution-aron-mark |     0.524461 |       0.15174  |   0.236083 |
| solution-pl        |     0.524952 |       0.154343 |   0.237128 |
| solution-1-flask   |     5.62121  |       1.05997  |   0.27291  |
| solution-1         |     8.04668  |       1e-06    |   0.656018 |
| solution-2         |     0.519684 |       0.63534  |   0.802651 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.516818 |       0.153307 |   0.353229 |
| solution-aron-mark |     0.523443 |       0.16081  |   0.358869 |
| solution-flask     |     0.525356 |       1.01005  |   0.366665 |
| solution-1-flask   |     0.540907 |       1.00853  |   0.781462 |
| solution-2         |     0.521016 |       0.536306 |  24.2462   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.502124 |       0.158321 |    1.05031 |
| solution-pl        |     0.513187 |       0.164019 |    1.05433 |
| solution-flask     |     0.507674 |       1.00854  |    1.55103 |
| solution-1-flask   |     0.532225 |       1.00832  |    5.49408 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.502699 |       0.185822 |    3.2381  |
| solution-pl        |     0.501262 |       0.188274 |    3.25954 |
| solution-flask     |     0.50926  |       1.00831  |    5.06234 |