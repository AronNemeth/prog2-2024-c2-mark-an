# 2024-04-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.689229 |       1.0087   |   0.074297 |
| solution-aron-mark |     0.658794 |       0.108949 |   0.171791 |
| solution-pl        |     6.01309  |       0.110814 |   0.172865 |
| solution-1-flask   |     1.59373  |       1.06624  |   0.264256 |
| solution-1         |     8.22059  |       1e-06    |   0.587913 |
| solution-2         |     0.654484 |       0.415425 |   0.823429 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.662446 |       1.00888  |   0.159046 |
| solution-aron-mark |     0.654733 |       0.116932 |   0.261906 |
| solution-pl        |     0.663    |       0.117478 |   0.264131 |
| solution-1-flask   |     0.663872 |       1.00917  |   0.777886 |
| solution-2         |     0.654709 |       0.426862 |  14.7041   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.658623 |       1.00895  |   0.697339 |
| solution-pl        |     0.654505 |       0.124165 |   0.805648 |
| solution-aron-mark |     0.661084 |       0.124623 |   0.814107 |
| solution-1-flask   |     0.678755 |       1.00884  |   5.58142  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.658102 |       1.00889  |    2.47837 |
| solution-pl        |     0.660828 |       0.161749 |    2.58846 |
| solution-aron-mark |     0.663254 |       0.161406 |    2.59332 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.653286 |       1.0087   |    15.5948 |
| solution-pl        |     0.650884 |       0.287333 |    15.7661 |
| solution-aron-mark |     0.653863 |       0.284974 |    15.7675 |