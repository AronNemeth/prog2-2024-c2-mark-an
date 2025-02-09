# 2025-02-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.27278  |       1.06623  |   0.082849 |
| solution-aron-mark |     0.530796 |       0.141036 |   0.205677 |
| solution-pl        |     4.64898  |       0.141603 |   0.205823 |
| solution-1-flask   |     0.536899 |       1.00925  |   0.270651 |
| solution-1         |     7.79485  |       1e-06    |   0.595337 |
| solution-2         |     0.535745 |       0.523086 |   0.9631   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.529518 |       1.00889  |   0.29521  |
| solution-pl        |     0.532482 |       0.142703 |   0.31013  |
| solution-aron-mark |     0.535038 |       0.14233  |   0.310162 |
| solution-1-flask   |     0.543513 |       1.00873  |   0.815137 |
| solution-2         |     0.534214 |       0.488782 |   2.15294  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.538643 |       0.148924 |   0.903391 |
| solution-pl        |     0.546554 |       0.149235 |   0.906537 |
| solution-flask     |     0.535925 |       1.00906  |   1.23003  |
| solution-1-flask   |     0.542942 |       1.00907  |   5.67014  |
| solution-2         |     0.527238 |       0.54037  |  25.8103   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.53399  |       0.178023 |    2.81702 |
| solution-aron-mark |     0.539026 |       0.17478  |    2.83128 |
| solution-flask     |     0.533518 |       1.00917  |    4.21317 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.536082 |       0.280641 |    16.3982 |
| solution-aron-mark |     0.532775 |       0.274873 |    16.4061 |