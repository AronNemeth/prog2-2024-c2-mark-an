# 2024-03-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.53862  |       1.03729  |   0.065066 |
| solution-pl        |     0.668956 |       0.112235 |   0.16602  |
| solution-aron-mark |     0.695632 |       0.114343 |   0.169465 |
| solution-1-flask   |     0.686862 |       1.0093   |   0.267023 |
| solution-1         |     8.25699  |       1e-06    |   0.793388 |
| solution-2         |     4.67093  |       0.614678 |   0.99861  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.685112 |       1.00884  |   0.176492 |
| solution-aron-mark |     0.672967 |       0.118457 |   0.257051 |
| solution-pl        |     0.675868 |       0.121274 |   0.257925 |
| solution-1-flask   |     0.711221 |       1.00885  |   0.789085 |
| solution-2         |     0.665115 |       0.456624 |   4.18234  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.689928 |       0.120705 |   0.806048 |
| solution-aron-mark |     0.693616 |       0.128068 |   0.823492 |
| solution-flask     |     0.676865 |       1.0091   |   0.957718 |
| solution-1-flask   |     0.685588 |       1.00879  |   5.67673  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.691773 |       0.15502  |    3.31571 |
| solution-aron-mark |     0.696816 |       0.166225 |    3.45792 |
| solution-flask     |     0.668031 |       1.00894  |    6.06634 |