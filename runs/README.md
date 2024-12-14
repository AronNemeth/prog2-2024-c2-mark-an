# 2024-12-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.96622  |       1.0092   |   0.106853 |
| solution-pl        |     0.559513 |       0.110082 |   0.187459 |
| solution-aron-mark |     0.557385 |       0.112805 |   0.190562 |
| solution-1-flask   |     5.15601  |       1.047    |   0.270596 |
| solution-1         |     7.92408  |       1e-06    |   0.669761 |
| solution-2         |     0.549824 |       0.554539 |   0.871278 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.544161 |       0.112979 |   0.32088  |
| solution-aron-mark |     0.544603 |       0.11153  |   0.343984 |
| solution-flask     |     0.540118 |       1.0095   |   0.509727 |
| solution-1-flask   |     0.553981 |       1.00881  |   0.804686 |
| solution-2         |     0.542863 |       0.491161 |  12.277    |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.541999 |       0.118197 |    1.0747  |
| solution-aron-mark |     0.538706 |       0.117107 |    1.12762 |
| solution-flask     |     0.558885 |       1.00912  |    2.26522 |
| solution-1-flask   |     0.545862 |       1.00956  |    6.18    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.539788 |       0.144753 |    4.32731 |
| solution-aron-mark |     0.532827 |       0.148467 |    4.44939 |
| solution-flask     |     0.537323 |       1.00901  |    9.02319 |