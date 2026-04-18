# 2026-04-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.59118  |       1.07137  |   0.103898 |
| solution-pl        |     0.407637 |       0.145802 |   0.227252 |
| solution-aron-mark |     4.36241  |       0.143513 |   0.231797 |
| solution-1-flask   |     0.417754 |       1.00782  |   0.264688 |
| solution-1         |     7.18141  |       1e-06    |   0.688697 |
| solution-2         |     0.408672 |       0.838797 |   1.21445  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.406079 |       0.144573 |   0.355371 |
| solution-pl        |     0.40444  |       0.150229 |   0.359783 |
| solution-flask     |     0.403052 |       1.00806  |   0.388036 |
| solution-1-flask   |     0.411568 |       1.00818  |   0.79202  |
| solution-2         |     0.404236 |       0.492783 |  14.9803   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.404781 |       0.151171 |    1.09408 |
| solution-aron-mark |     0.40512  |       0.150976 |    1.0947  |
| solution-flask     |     0.403188 |       1.00824  |    1.63705 |
| solution-1-flask   |     0.408836 |       1.00803  |    5.57348 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.401387 |       0.174872 |    3.59276 |
| solution-aron-mark |     0.403146 |       0.175224 |    3.63348 |
| solution-flask     |     0.403136 |       1.00806  |    5.17973 |