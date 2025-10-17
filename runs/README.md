# 2025-10-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.89691  |       1.11226  |   0.104134 |
| solution-pl        |     4.52425  |       0.161891 |   0.242847 |
| solution-aron-mark |     0.504616 |       0.157606 |   0.242911 |
| solution-1-flask   |     0.505673 |       1.00807  |   0.264588 |
| solution-1         |     8.2122   |       1e-06    |   1.10056  |
| solution-2         |     0.50135  |       0.876402 |   1.27397  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.508061 |       0.159447 |   0.375689 |
| solution-pl        |     0.538511 |       0.159995 |   0.377767 |
| solution-flask     |     0.50548  |       1.00902  |   0.383421 |
| solution-1-flask   |     0.507986 |       1.00829  |   0.790822 |
| solution-2         |     0.510373 |       0.51998  |   3.01538  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.499257 |       0.171081 |    1.10097 |
| solution-pl        |     0.51266  |       0.165778 |    1.1039  |
| solution-flask     |     0.495174 |       1.00859  |    1.62895 |
| solution-1-flask   |     0.510426 |       1.0086   |    5.59973 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.504028 |       0.19574  |    3.40438 |
| solution-pl        |     0.505529 |       0.199509 |    3.40773 |
| solution-flask     |     0.505683 |       1.0089   |    5.27461 |