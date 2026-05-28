# 2026-05-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.87856  |       1.12922  |   0.098706 |
| solution-pl        |     0.42295  |       0.147952 |   0.225483 |
| solution-aron-mark |     0.421246 |       0.149393 |   0.22867  |
| solution-1-flask   |     0.425538 |       1.00863  |   0.232496 |
| solution-1         |     7.38282  |       1e-06    |   0.642802 |
| solution-2         |     4.33213  |       0.673235 |   1.22205  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.423914 |       0.1532   |   0.351943 |
| solution-aron-mark |     0.423987 |       0.151048 |   0.352667 |
| solution-flask     |     0.443577 |       1.00881  |   0.397258 |
| solution-1-flask   |     0.43062  |       1.00875  |   0.722349 |
| solution-2         |     0.426858 |       0.507729 |   2.06911  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.445293 |       0.157805 |    1.02532 |
| solution-pl        |     0.429818 |       0.157443 |    1.04633 |
| solution-flask     |     0.438194 |       1.00885  |    1.65944 |
| solution-1-flask   |     0.43568  |       1.00883  |    5.5142  |
| solution-2         |     0.441134 |       0.559894 |  176.359   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.422395 |       0.183468 |    3.74124 |
| solution-pl        |     0.425052 |       0.182879 |    3.776   |
| solution-flask     |     0.42318  |       1.00878  |    5.07784 |