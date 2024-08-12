# 2024-08-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.566775 |       1.00938  |   0.095828 |
| solution-pl        |     0.551459 |       0.101586 |   0.168795 |
| solution-aron-mark |     1.89478  |       0.102546 |   0.169348 |
| solution-1-flask   |     1.29443  |       1.11922  |   0.263501 |
| solution-1         |     7.86834  |       1e-06    |   0.594763 |
| solution-2         |     4.55744  |       0.602698 |   1.08618  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.544894 |       1.00961  |   0.222622 |
| solution-pl        |     0.565481 |       0.102667 |   0.285744 |
| solution-aron-mark |     0.563509 |       0.103452 |   0.288875 |
| solution-1-flask   |     0.580944 |       1.00898  |   0.790174 |
| solution-2         |     0.564447 |       0.479585 |  11.9051   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.55413  |       1.00928  |   0.891272 |
| solution-pl        |     0.5625   |       0.112159 |   0.987688 |
| solution-aron-mark |     0.555659 |       0.109922 |   0.990227 |
| solution-1-flask   |     0.559822 |       1.00914  |   5.57287  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.560292 |       0.14229  |    4.22943 |
| solution-flask     |     0.551644 |       1.00907  |    4.25789 |
| solution-aron-mark |     0.564917 |       0.142436 |    4.26203 |