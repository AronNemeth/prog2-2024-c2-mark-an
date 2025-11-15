# 2025-11-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.06874  |       1.25802  |   0.104163 |
| solution-aron-mark |     0.524984 |       0.15783  |   0.243405 |
| solution-pl        |     0.473843 |       0.160485 |   0.252266 |
| solution-1-flask   |     0.482728 |       1.00826  |   0.2632   |
| solution-1         |     8.03837  |       1e-06    |   0.727237 |
| solution-2         |     5.05704  |       0.66568  |   1.03485  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.475749 |       0.160756 |   0.371359 |
| solution-pl        |     0.476565 |       0.158128 |   0.371658 |
| solution-flask     |     0.480345 |       1.00861  |   0.383298 |
| solution-1-flask   |     0.486763 |       1.00838  |   0.801441 |
| solution-2         |     0.473717 |       0.514827 |   2.26452  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.475098 |       0.167515 |    1.07529 |
| solution-pl        |     0.48132  |       0.167479 |    1.09854 |
| solution-flask     |     0.482758 |       1.00851  |    1.58299 |
| solution-1-flask   |     0.482633 |       1.00858  |    5.6452  |
| solution-2         |     0.470919 |       0.564595 |   26.055   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.476262 |       0.202866 |    3.33416 |
| solution-pl        |     0.478186 |       0.206208 |    3.34037 |
| solution-flask     |     0.482595 |       1.00847  |    5.2809  |