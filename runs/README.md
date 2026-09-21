# 2026-09-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.01563  |       1.04598  |   0.110049 |
| solution-pl        |     2.02078  |       0.144464 |   0.213576 |
| solution-aron-mark |     0.388611 |       0.145344 |   0.216741 |
| solution-1-flask   |     0.40161  |       1.00678  |   0.251996 |
| solution-1         |     6.44782  |       1e-06    |   0.613774 |
| solution-2         |     4.56288  |       0.642303 |   1.03567  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.395372 |       0.142284 |   0.330655 |
| solution-aron-mark |     0.392829 |       0.141443 |   0.332585 |
| solution-flask     |     0.389421 |       1.00675  |   0.414201 |
| solution-1-flask   |     0.398479 |       1.00663  |   0.733528 |
| solution-2         |     0.392894 |       0.484426 |   2.10034  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.400998 |       0.149548 |    1.00486 |
| solution-aron-mark |     0.397928 |       0.148616 |    1.02711 |
| solution-flask     |     0.399563 |       1.00673  |    1.74328 |
| solution-1-flask   |     0.391339 |       1.00688  |    5.39992 |
| solution-2         |     0.393837 |       0.532675 |  165.826   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.390452 |       0.175408 |    4.2858  |
| solution-aron-mark |     0.38848  |       0.179098 |    4.33594 |
| solution-flask     |     0.391369 |       1.00701  |    5.75163 |