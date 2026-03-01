# 2026-03-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.77149  |       1.11628  |   0.112271 |
| solution-aron-mark |     0.496842 |       0.166102 |   0.251347 |
| solution-pl        |     4.56847  |       0.162344 |   0.252779 |
| solution-1-flask   |     0.505942 |       1.00933  |   0.278052 |
| solution-1         |     7.94425  |       1e-06    |   0.693527 |
| solution-2         |     0.510706 |       0.800846 |   0.947373 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.4866   |       0.165743 |   0.390158 |
| solution-pl        |     0.509134 |       0.170001 |   0.396609 |
| solution-flask     |     0.488966 |       1.00991  |   0.401546 |
| solution-1-flask   |     0.542475 |       1.00967  |   0.807537 |
| solution-2         |     0.512539 |       0.587567 |   4.85596  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.465433 |       0.161743 |    1.15924 |
| solution-pl        |     0.510176 |       0.173255 |    1.17412 |
| solution-flask     |     0.502932 |       1.01001  |    1.66315 |
| solution-1-flask   |     0.506757 |       1.00961  |    5.62958 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.475354 |       0.188697 |    4.13613 |
| solution-aron-mark |     0.470447 |       0.186686 |    4.25664 |
| solution-flask     |     0.483278 |       1.00947  |    5.548   |