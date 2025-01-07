# 2025-01-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.85501  |       1.00889  |   0.104613 |
| solution-aron-mark |     0.552195 |       0.111018 |   0.189943 |
| solution-pl        |     0.548348 |       0.113145 |   0.191392 |
| solution-1-flask   |     5.26408  |       1.03778  |   0.265638 |
| solution-1         |     7.73986  |       1e-06    |   0.607496 |
| solution-2         |     0.545712 |       0.544918 |   1.45631  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.551707 |       0.112641 |   0.318677 |
| solution-pl        |     0.545765 |       0.113947 |   0.321364 |
| solution-flask     |     0.546428 |       1.00892  |   0.475161 |
| solution-1-flask   |     0.575742 |       1.00894  |   0.800517 |
| solution-2         |     0.547846 |       0.502205 |  25.7251   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.54762  |       0.120517 |    1.08096 |
| solution-pl        |     0.543276 |       0.120387 |    1.0822  |
| solution-flask     |     0.537623 |       1.00912  |    2.14478 |
| solution-1-flask   |     0.548743 |       1.00898  |    5.92914 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.548126 |       0.148312 |    4.75626 |
| solution-pl        |     0.543161 |       0.152562 |    4.81951 |
| solution-flask     |     0.545228 |       1.00928  |    8.70112 |