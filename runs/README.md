# 2025-11-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.4738   |       1.04329  |   0.101717 |
| solution-aron-mark |     0.471968 |       0.164016 |   0.243615 |
| solution-pl        |     0.478234 |       0.159663 |   0.245669 |
| solution-1-flask   |     0.489011 |       1.00825  |   0.266062 |
| solution-1         |     8.74343  |       1e-06    |   0.720573 |
| solution-2         |     4.91269  |       0.685022 |   1.22399  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.474472 |       0.160688 |   0.370141 |
| solution-aron-mark |     0.476112 |       0.16523  |   0.37644  |
| solution-flask     |     0.476459 |       1.00855  |   0.387188 |
| solution-1-flask   |     0.478677 |       1.00841  |   0.817067 |
| solution-2         |     0.4668   |       0.517225 |   3.91992  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.478929 |       0.168506 |    1.08478 |
| solution-aron-mark |     0.475793 |       0.167175 |    1.08807 |
| solution-flask     |     0.480619 |       1.00882  |    1.60218 |
| solution-1-flask   |     0.47971  |       1.00997  |    5.58422 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.482502 |       0.195937 |    3.23492 |
| solution-aron-mark |     0.475704 |       0.192564 |    3.27326 |
| solution-flask     |     0.478256 |       1.00865  |    5.1611  |