# 2024-12-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |      1.606   |       1.09572  |   0.154925 |
| solution-aron-mark |      1.02918 |       0.111182 |   0.180909 |
| solution-pl        |      6.25707 |       0.110194 |   0.191876 |
| solution-1-flask   |      1.03005 |       1.00903  |   0.26486  |
| solution-2         |      1.02387 |       0.701002 |   0.696011 |
| solution-1         |      8.05564 |       1e-06    |   0.815405 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.5645   |       0.110189 |   0.308766 |
| solution-pl        |     0.76576  |       0.109927 |   0.320095 |
| solution-flask     |     0.575888 |       1.00909  |   0.506042 |
| solution-1-flask   |     0.565911 |       1.00874  |   0.802842 |
| solution-2         |     0.576192 |       0.481091 |   2.96675  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.560387 |       0.116727 |    1.03278 |
| solution-aron-mark |     0.563445 |       0.117435 |    1.03874 |
| solution-flask     |     0.563071 |       1.00924  |    2.24216 |
| solution-1-flask   |     0.573774 |       1.00927  |    5.52195 |
| solution-2         |     0.55943  |       0.534304 |   30.6512  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.565847 |       0.151174 |    4.4205  |
| solution-aron-mark |     0.568957 |       0.149322 |    4.45942 |
| solution-flask     |     0.563901 |       1.00941  |    8.77942 |