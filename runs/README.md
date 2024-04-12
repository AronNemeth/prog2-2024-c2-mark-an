# 2024-04-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.657789 |       1.00882  |   0.06597  |
| solution-aron-mark |     0.658193 |       0.111436 |   0.16756  |
| solution-pl        |     6.43526  |       0.111445 |   0.168267 |
| solution-1-flask   |     1.4389   |       1.04392  |   0.283339 |
| solution-1         |     8.76876  |       1e-06    |   0.673308 |
| solution-2         |     0.705109 |       0.435586 |   1.38296  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.660816 |       1.00911  |   0.179178 |
| solution-pl        |     0.656594 |       0.115066 |   0.255558 |
| solution-aron-mark |     0.655088 |       0.114006 |   0.257725 |
| solution-1-flask   |     0.678361 |       1.00874  |   0.779298 |
| solution-2         |     0.658471 |       0.425386 |   3.14611  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.652226 |       0.121435 |   0.801039 |
| solution-pl        |     0.672187 |       0.121109 |   0.813267 |
| solution-flask     |     0.671925 |       1.00896  |   0.923769 |
| solution-1-flask   |     0.667365 |       1.00875  |   5.61276  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.668146 |       0.155221 |    3.20941 |
| solution-aron-mark |     0.665852 |       0.155009 |    3.26511 |
| solution-flask     |     0.659709 |       1.00921  |    5.01504 |