# 2026-05-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.20556  |       1.05166  |   0.10519  |
| solution-aron-mark |     4.68801  |       0.156955 |   0.241477 |
| solution-pl        |     0.439609 |       0.163377 |   0.243914 |
| solution-1-flask   |     0.443226 |       1.00848  |   0.262981 |
| solution-1         |     8.19041  |       1e-06    |   0.777769 |
| solution-2         |     0.458693 |       0.760464 |   1.49276  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.469206 |       0.158021 |   0.377966 |
| solution-aron-mark |     0.484643 |       0.165967 |   0.428355 |
| solution-flask     |     0.447235 |       1.00851  |   0.43683  |
| solution-1-flask   |     0.445336 |       1.0085   |   0.817911 |
| solution-2         |     0.439606 |       0.546908 |  12.6468   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.447203 |       0.159786 |    1.12401 |
| solution-pl        |     0.42879  |       0.163596 |    1.14032 |
| solution-flask     |     0.43941  |       1.00879  |    1.72425 |
| solution-1-flask   |     0.442886 |       1.00858  |    5.90755 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.454702 |       0.182978 |    4.02116 |
| solution-pl        |     0.43259  |       0.182519 |    4.09009 |
| solution-flask     |     0.441133 |       1.00858  |    5.56707 |