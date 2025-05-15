# 2025-05-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.06861  |       1.14428  |   0.111592 |
| solution-pl        |     5.60982  |       0.123266 |   0.189777 |
| solution-aron-mark |     0.473685 |       0.119473 |   0.193685 |
| solution-1-flask   |     0.480802 |       1.00823  |   0.262297 |
| solution-1         |     7.40675  |       2e-06    |   0.802172 |
| solution-2         |     0.477573 |       0.769218 |   1.2083   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.469223 |       1.00832  |   0.290408 |
| solution-pl        |     0.47353  |       0.122253 |   0.293607 |
| solution-aron-mark |     0.466127 |       0.123325 |   0.295795 |
| solution-1-flask   |     0.474015 |       1.00844  |   0.787615 |
| solution-2         |     0.467716 |       0.503252 |   4.4322   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.473551 |       0.129811 |   0.876106 |
| solution-pl        |     0.469471 |       0.130235 |   0.910224 |
| solution-flask     |     0.482586 |       1.00838  |   1.22258  |
| solution-1-flask   |     0.479504 |       1.00832  |   5.38179  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.476066 |       0.160195 |    2.82229 |
| solution-pl        |     0.473849 |       0.159589 |    2.84516 |
| solution-flask     |     0.481292 |       1.00828  |    4.27749 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.479019 |       0.270772 |    16.3159 |
| solution-aron-mark |     0.481809 |       0.279245 |    17.0106 |