# 2024-06-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.502559 |       1.00908  |   0.073356 |
| solution-pl        |     0.513192 |       0.103488 |   0.159437 |
| solution-aron-mark |     5.84617  |       0.10372  |   0.161919 |
| solution-1-flask   |     1.19932  |       1.05728  |   0.255601 |
| solution-1         |     7.90195  |       1e-06    |   0.616016 |
| solution-2         |     0.509216 |       0.523534 |   1.0757   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.499393 |       1.00893  |   0.161746 |
| solution-pl        |     0.50251  |       0.10429  |   0.259729 |
| solution-aron-mark |     0.495294 |       0.109116 |   0.277131 |
| solution-1-flask   |     0.515731 |       1.00919  |   0.78451  |
| solution-2         |     0.499093 |       0.47819  |   2.12427  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.496671 |       1.009    |   0.703683 |
| solution-pl        |     0.514465 |       0.114662 |   0.812154 |
| solution-aron-mark |     0.516058 |       0.114342 |   0.816022 |
| solution-1-flask   |     0.521294 |       1.00917  |   5.63045  |
| solution-2         |     0.508611 |       0.541212 |  32.2667   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.507055 |       1.00934  |    2.50027 |
| solution-aron-mark |     0.512446 |       0.151927 |    2.61245 |
| solution-pl        |     0.493533 |       0.152362 |    2.61804 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.496059 |       1.00894  |    15.6531 |
| solution-aron-mark |     0.494676 |       0.275584 |    20.5154 |
| solution-pl        |     0.497472 |       0.278862 |    22.0081 |