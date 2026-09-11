# 2026-09-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.60646  |       1.05424  |   0.114567 |
| solution-pl        |     2.3214   |       0.1701   |   0.242731 |
| solution-aron-mark |     0.432281 |       0.155331 |   0.246765 |
| solution-1-flask   |     0.434541 |       1.00852  |   0.274867 |
| solution-1         |     8.1083   |       1e-06    |   0.638753 |
| solution-2         |     4.75427  |       0.641933 |   1.02396  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.431784 |       0.155483 |   0.379772 |
| solution-pl        |     0.432685 |       0.158314 |   0.382608 |
| solution-flask     |     0.428967 |       1.00869  |   0.416866 |
| solution-1-flask   |     0.44036  |       1.00843  |   0.819851 |
| solution-2         |     0.432801 |       0.511258 |   5.04486  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.435068 |       0.161495 |    1.15044 |
| solution-pl        |     0.438444 |       0.161371 |    1.16225 |
| solution-flask     |     0.430655 |       1.00969  |    1.73421 |
| solution-1-flask   |     0.442484 |       1.00868  |    5.80592 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.429748 |       0.184426 |    3.58393 |
| solution-pl        |     0.424441 |       0.19501  |    3.61151 |
| solution-flask     |     0.428859 |       1.00877  |    5.45332 |