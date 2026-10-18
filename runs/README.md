# 2026-10-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.14041  |       1.11745  |   0.073214 |
| solution-1-flask   |     0.333091 |       1.00718  |   0.172252 |
| solution-pl        |     0.326749 |       0.13211  |   0.191443 |
| solution-aron-mark |     5.18082  |       0.159592 |   0.191543 |
| solution-1         |     6.35954  |       1e-06    |   0.672179 |
| solution-2         |     0.32662  |       0.57534  |   0.948464 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.342827 |       1.00753  |   0.167832 |
| solution-aron-mark |     0.336839 |       0.131578 |   0.290477 |
| solution-pl        |     0.335198 |       0.132062 |   0.299444 |
| solution-1-flask   |     0.335371 |       1.00744  |   0.538596 |
| solution-2         |     0.33052  |       0.407224 |   2.54988  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.32759  |       1.00732  |   0.73376  |
| solution-pl        |     0.326881 |       0.14014  |   0.836531 |
| solution-aron-mark |     0.331013 |       0.147972 |   0.890103 |
| solution-1-flask   |     0.332891 |       1.00732  |   4.19195  |
| solution-2         |     0.329944 |       0.448268 | 129.327    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.329951 |       0.157591 |    2.69414 |
| solution-pl        |     0.329161 |       0.158146 |    2.69895 |
| solution-flask     |     0.328074 |       1.00754  |    3.224   |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.32893  |       0.225576 |    15.5968 |
| solution-pl        |     0.334905 |       0.223092 |    15.6009 |