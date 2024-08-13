# 2024-08-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.548761 |       1.00915  |   0.093521 |
| solution-pl        |     0.553524 |       0.102417 |   0.166242 |
| solution-aron-mark |     1.8323   |       0.102241 |   0.171321 |
| solution-1-flask   |     1.06202  |       1.08249  |   0.260663 |
| solution-1         |     7.58413  |       1e-06    |   0.769289 |
| solution-2         |     4.40104  |       0.72366  |   1.23357  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.54811  |       1.00903  |   0.19204  |
| solution-pl        |     0.553433 |       0.102742 |   0.288692 |
| solution-aron-mark |     0.551715 |       0.102883 |   0.300481 |
| solution-1-flask   |     0.558395 |       1.00901  |   0.789221 |
| solution-2         |     0.548758 |       0.470568 |   3.01553  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.548868 |       1.00904  |   0.883344 |
| solution-pl        |     0.56815  |       0.111185 |   0.987381 |
| solution-aron-mark |     0.555365 |       0.110498 |   0.99651  |
| solution-1-flask   |     0.559211 |       1.00902  |   5.50461  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.576087 |       0.141709 |    4.21358 |
| solution-flask     |     0.573851 |       1.00925  |    4.31754 |
| solution-aron-mark |     0.553861 |       0.144721 |    4.41893 |