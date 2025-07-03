# 2025-07-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.86516  |       1.1029   |   0.103166 |
| solution-aron-mark |     7.22223  |       0.244268 |   0.240999 |
| solution-pl        |     0.965493 |       0.165596 |   0.24856  |
| solution-1-flask   |     0.572515 |       1.00827  |   0.278333 |
| solution-1         |     8.4805   |       2e-06    |   0.860485 |
| solution-2         |     0.682893 |       0.713699 |   1.06931  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.528836 |       0.159134 |   0.371431 |
| solution-pl        |     0.524172 |       0.158725 |   0.373425 |
| solution-flask     |     0.517787 |       1.00873  |   0.392393 |
| solution-1-flask   |     0.528566 |       1.00857  |   0.82289  |
| solution-2         |     0.517526 |       0.523843 |   2.11758  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.531191 |       0.169707 |    1.09183 |
| solution-aron-mark |     0.542119 |       0.170707 |    1.10519 |
| solution-flask     |     0.537438 |       1.00894  |    1.6356  |
| solution-1-flask   |     0.537822 |       1.00887  |    5.86255 |
| solution-2         |     0.541288 |       0.611022 |   34.1649  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.537719 |       0.198863 |    3.45262 |
| solution-aron-mark |     0.520164 |       0.203203 |    3.50254 |
| solution-flask     |     0.530819 |       1.00897  |    5.35025 |