# 2026-10-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.12303  |       1.14243  |   0.091962 |
| solution-1-flask   |     0.43459  |       1.00901  |   0.224476 |
| solution-aron-mark |     6.0607   |       0.190701 |   0.244445 |
| solution-pl        |     0.42708  |       0.164963 |   0.246208 |
| solution-1         |     7.67811  |       1e-06    |   0.657885 |
| solution-2         |     0.422163 |       0.72531  |   1.20846  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.424731 |       1.00897  |   0.218385 |
| solution-aron-mark |     0.426436 |       0.168131 |   0.379697 |
| solution-pl        |     0.425752 |       0.16755  |   0.421481 |
| solution-1-flask   |     0.432854 |       1.00905  |   0.700143 |
| solution-2         |     0.420735 |       0.501521 |   2.22588  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.42763  |       1.00906  |   0.940948 |
| solution-pl        |     0.429111 |       0.180781 |   1.08314  |
| solution-aron-mark |     0.428772 |       0.175447 |   1.10443  |
| solution-1-flask   |     0.428678 |       1.00904  |   5.4139   |
| solution-2         |     0.42788  |       0.564022 |  33.5268   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.438777 |       0.203645 |    3.48576 |
| solution-aron-mark |     0.431154 |       0.203958 |    3.55318 |
| solution-flask     |     0.420351 |       1.00877  |    4.23378 |