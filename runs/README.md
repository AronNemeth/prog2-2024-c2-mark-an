# 2026-03-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.5195   |       1.07296  |   0.106406 |
| solution-pl        |     4.60069  |       0.148034 |   0.235374 |
| solution-aron-mark |     0.457738 |       0.153336 |   0.239635 |
| solution-1-flask   |     0.454604 |       1.0088   |   0.270523 |
| solution-1         |     7.62212  |       1e-06    |   0.777588 |
| solution-2         |     0.448761 |       0.659758 |   1.02736  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.452541 |       0.147192 |   0.370863 |
| solution-pl        |     0.46938  |       0.153656 |   0.372058 |
| solution-flask     |     0.472093 |       1.00875  |   0.404606 |
| solution-1-flask   |     0.465271 |       1.00896  |   0.794323 |
| solution-2         |     0.448364 |       0.520376 |   2.27034  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.454875 |       0.154405 |    1.12943 |
| solution-aron-mark |     0.451327 |       0.153961 |    1.13085 |
| solution-flask     |     0.446946 |       1.00904  |    1.62927 |
| solution-1-flask   |     0.460198 |       1.00912  |    5.54052 |
| solution-2         |     0.446566 |       0.574482 |   34.9179  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.447025 |       0.18064  |    3.8975  |
| solution-pl        |     0.448156 |       0.179986 |    3.93123 |
| solution-flask     |     0.448084 |       1.009    |    5.22346 |