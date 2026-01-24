# 2026-01-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.76776  |       1.08695  |   0.104408 |
| solution-pl        |     0.479455 |       0.161963 |   0.249762 |
| solution-aron-mark |     0.860215 |       0.161889 |   0.252177 |
| solution-1-flask   |     0.480652 |       1.00892  |   0.265505 |
| solution-1         |     9.59955  |       1e-06    |   0.712631 |
| solution-2         |     6.08998  |       0.689536 |   0.94845  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.475443 |       0.17228  |   0.373322 |
| solution-pl        |     0.483245 |       0.165237 |   0.376677 |
| solution-flask     |     0.48971  |       1.00863  |   0.382401 |
| solution-1-flask   |     0.488142 |       1.00827  |   0.798939 |
| solution-2         |     0.466949 |       0.512997 |   4.89506  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.47438  |       0.169004 |    1.09204 |
| solution-pl        |     0.478975 |       0.173409 |    1.09353 |
| solution-flask     |     0.475442 |       1.00873  |    1.58543 |
| solution-1-flask   |     0.478202 |       1.00857  |    5.54863 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.488227 |       0.197458 |    3.64081 |
| solution-pl        |     0.47467  |       0.193438 |    3.65574 |
| solution-flask     |     0.475551 |       1.00836  |    5.20931 |