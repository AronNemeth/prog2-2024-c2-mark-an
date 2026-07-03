# 2026-07-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.20154  |       1.03673  |   0.114068 |
| solution-aron-mark |     0.496382 |       0.160063 |   0.250099 |
| solution-pl        |     6.26174  |       0.168295 |   0.251199 |
| solution-1-flask   |     0.457848 |       1.0089   |   0.288397 |
| solution-1         |     7.74148  |       2e-06    |   0.676208 |
| solution-2         |     0.466016 |       0.611989 |   1.00138  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.493205 |       0.166535 |   0.390714 |
| solution-aron-mark |     0.495536 |       0.177013 |   0.392982 |
| solution-flask     |     0.459271 |       1.00905  |   0.419045 |
| solution-1-flask   |     0.471221 |       1.00906  |   0.852289 |
| solution-2         |     0.48725  |       0.59381  |   4.12352  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.454186 |       0.164404 |    1.13839 |
| solution-aron-mark |     0.477862 |       0.166887 |    1.15842 |
| solution-flask     |     0.457346 |       1.00887  |    1.74715 |
| solution-1-flask   |     0.476157 |       1.00922  |    5.9616  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.450586 |       0.191386 |    4.32392 |
| solution-pl        |     0.459194 |       0.190592 |    4.345   |
| solution-flask     |     0.454102 |       1.00925  |    5.74272 |