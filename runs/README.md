# 2026-08-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.48849  |       1.00914  |   0.102336 |
| solution-1-flask   |     1.2615   |       1.06449  |   0.234084 |
| solution-aron-mark |     0.442338 |       0.154148 |   0.234644 |
| solution-pl        |     0.433833 |       0.152911 |   0.234878 |
| solution-1         |     8.5538   |       1e-06    |   0.728324 |
| solution-2         |     4.92354  |       0.679482 |   0.733469 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.445266 |       0.159772 |   0.360282 |
| solution-aron-mark |     0.432142 |       0.15454  |   0.363875 |
| solution-flask     |     0.447114 |       1.00927  |   0.3943   |
| solution-1-flask   |     0.453897 |       1.00911  |   0.734413 |
| solution-2         |     0.432982 |       0.505306 |  11.23     |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.441242 |       0.163383 |    1.05787 |
| solution-aron-mark |     0.443284 |       0.163324 |    1.0668  |
| solution-flask     |     0.449166 |       1.00925  |    1.65997 |
| solution-1-flask   |     0.459253 |       1.00917  |    5.84188 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.447385 |       0.189395 |    3.62229 |
| solution-aron-mark |     0.455786 |       0.190704 |    3.66296 |
| solution-flask     |     0.442971 |       1.00933  |    5.42252 |