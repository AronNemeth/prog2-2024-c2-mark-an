# 2024-05-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.43199  |       1.06478  |   0.076575 |
| solution-aron-mark |     6.0758   |       0.101512 |   0.157517 |
| solution-pl        |     0.65144  |       0.102669 |   0.157818 |
| solution-1-flask   |     0.677195 |       1.00926  |   0.268321 |
| solution-1         |     8.05563  |       1e-06    |   0.590499 |
| solution-2         |     0.647449 |       0.419844 |   1.07389  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.660657 |       1.00937  |   0.160625 |
| solution-pl        |     0.668016 |       0.102525 |   0.25089  |
| solution-aron-mark |     0.671756 |       0.103238 |   0.251138 |
| solution-1-flask   |     0.678519 |       1.00903  |   0.782247 |
| solution-2         |     0.659081 |       0.433697 |   6.55165  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.665636 |       1.00891  |   0.700517 |
| solution-pl        |     0.663823 |       0.110723 |   0.804429 |
| solution-aron-mark |     0.664508 |       0.111388 |   0.804696 |
| solution-1-flask   |     0.670069 |       1.00886  |   5.53802  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.657043 |       1.00901  |    2.46058 |
| solution-pl        |     0.661865 |       0.148557 |    2.58744 |
| solution-aron-mark |     0.677049 |       0.147383 |    2.63228 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.659024 |       1.00894  |    15.4892 |
| solution-aron-mark |     0.658413 |       0.274104 |    21.8236 |
| solution-pl        |     0.658384 |       0.270506 |    22.1995 |