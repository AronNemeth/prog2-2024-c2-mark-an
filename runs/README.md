# 2026-11-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.32579  |       1.00925  |   0.07027  |
| solution-1-flask   |     0.833296 |       1.07604  |   0.176034 |
| solution-aron-mark |     0.321642 |       0.127658 |   0.188857 |
| solution-pl        |     5.02002  |       0.131781 |   0.189693 |
| solution-1         |     6.16002  |       0        |   0.425706 |
| solution-2         |     0.324796 |       0.421153 |   0.773949 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.332068 |       1.00922  |   0.16431  |
| solution-aron-mark |     0.333861 |       0.13326  |   0.286497 |
| solution-pl        |     0.328325 |       0.131981 |   0.287961 |
| solution-1-flask   |     0.328721 |       1.00916  |   0.530021 |
| solution-2         |     0.331547 |       0.399584 |   7.43436  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.325561 |       1.00927  |   0.726355 |
| solution-aron-mark |     0.327171 |       0.137451 |   0.819982 |
| solution-pl        |     0.330551 |       0.139614 |   0.84297  |
| solution-1-flask   |     0.330761 |       1.00936  |   3.97531  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.325416 |       0.164737 |    2.67758 |
| solution-pl        |     0.327688 |       0.171228 |    2.68452 |
| solution-flask     |     0.324592 |       1.0093   |    3.2218  |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.330095 |       0.247762 |    14.9221 |
| solution-aron-mark |     0.328169 |       0.238338 |    15.0115 |