# 2026-02-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.63848  |       1.05421  |   0.107418 |
| solution-pl        |     0.508729 |       0.17608  |   0.26069  |
| solution-aron-mark |     0.505639 |       0.174205 |   0.26205  |
| solution-1-flask   |     0.50508  |       1.0084   |   0.269126 |
| solution-1         |     7.88669  |       2e-06    |   0.811616 |
| solution-2         |     4.70101  |       0.842535 |   0.965326 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.521958 |       0.182818 |   0.3965   |
| solution-aron-mark |     0.513318 |       0.182193 |   0.398561 |
| solution-flask     |     0.503889 |       1.00906  |   0.417833 |
| solution-1-flask   |     0.514337 |       1.0091   |   0.817947 |
| solution-2         |     0.492169 |       0.556304 |   6.00572  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.507501 |       0.182119 |    1.10242 |
| solution-aron-mark |     0.502694 |       0.18236  |    1.12411 |
| solution-flask     |     0.515832 |       1.00882  |    1.64167 |
| solution-1-flask   |     0.504509 |       1.00877  |    5.77458 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.51057  |       0.208113 |    3.89331 |
| solution-pl        |     0.490305 |       0.202211 |    4.06697 |
| solution-flask     |     0.500451 |       1.0087   |    5.66388 |