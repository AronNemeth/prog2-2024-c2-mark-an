# 2026-09-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.39012  |       1.0516   |   0.159714 |
| solution-1-flask   |     0.389229 |       1.00753  |   0.180307 |
| solution-aron-mark |     8.48766  |       0.167686 |   0.188975 |
| solution-pl        |     0.36188  |       0.129596 |   0.193207 |
| solution-1         |     8.24009  |       1e-06    |   0.607816 |
| solution-2         |     0.34413  |       0.586985 |   0.754812 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.377584 |       0.130522 |   0.288357 |
| solution-aron-mark |     0.368087 |       0.135042 |   0.295782 |
| solution-flask     |     0.370369 |       1.00765  |   0.318431 |
| solution-1-flask   |     0.360947 |       1.00762  |   0.568039 |
| solution-2         |     0.370521 |       0.479659 |   2.16322  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.358972 |       0.138127 |   0.830077 |
| solution-aron-mark |     0.3753   |       0.133764 |   0.830462 |
| solution-flask     |     0.355203 |       1.0077   |   1.2902   |
| solution-1-flask   |     0.355307 |       1.00765  |   4.51646  |
| solution-2         |     0.354327 |       0.48507  |  23.2832   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.372546 |       0.15526  |    2.8905  |
| solution-pl        |     0.360983 |       0.157004 |    2.95104 |
| solution-flask     |     0.366574 |       1.00788  |    4.4372  |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.371343 |       0.225323 |    17.4588 |
| solution-aron-mark |     0.366513 |       0.220732 |    18.3002 |