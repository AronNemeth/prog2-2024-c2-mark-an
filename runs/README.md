# 2026-04-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.8492   |       1.03771  |   0.101771 |
| solution-aron-mark |     5.39961  |       0.150341 |   0.229045 |
| solution-pl        |     0.442958 |       0.149835 |   0.231845 |
| solution-1-flask   |     0.424792 |       1.00832  |   0.264704 |
| solution-1         |     8.51241  |       2e-06    |   0.68904  |
| solution-2         |     0.422775 |       0.712822 |   1.87186  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.442229 |       0.155813 |   0.360418 |
| solution-pl        |     0.437477 |       0.152169 |   0.364848 |
| solution-flask     |     0.420961 |       1.0082   |   0.373857 |
| solution-1-flask   |     0.443386 |       1.00867  |   0.812851 |
| solution-2         |     0.435283 |       0.533331 |   4.946    |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.418637 |        0.15692 |    1.07629 |
| solution-pl        |     0.424375 |        0.15625 |    1.08637 |
| solution-flask     |     0.432163 |        1.00861 |    1.56717 |
| solution-1-flask   |     0.434688 |        1.00852 |    5.66499 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.425428 |       0.180374 |    3.84863 |
| solution-aron-mark |     0.42982  |       0.183487 |    3.98408 |
| solution-flask     |     0.427317 |       1.00866  |    5.15344 |