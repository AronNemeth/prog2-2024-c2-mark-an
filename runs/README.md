# 2025-05-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.07615  |       1.07943  |   0.081912 |
| solution-aron-mark |     0.469679 |       0.129704 |   0.18819  |
| solution-pl        |     5.60708  |       0.121213 |   0.191853 |
| solution-1-flask   |     0.47316  |       1.00868  |   0.255097 |
| solution-1         |     7.3614   |       1e-06    |   0.579174 |
| solution-2         |     0.461908 |       0.546218 |   1.71011  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.463473 |       0.121011 |   0.293627 |
| solution-flask     |     0.467654 |       1.00898  |   0.295563 |
| solution-pl        |     0.460631 |       0.122816 |   0.295606 |
| solution-1-flask   |     0.481366 |       1.00903  |   0.775853 |
| solution-2         |     0.457465 |       0.502666 |   2.06067  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.463124 |       0.129681 |   0.889555 |
| solution-aron-mark |     0.466799 |       0.130133 |   0.890336 |
| solution-flask     |     0.459036 |       1.0086   |   1.24016  |
| solution-1-flask   |     0.471702 |       1.00877  |   5.43311  |
| solution-2         |     0.455998 |       0.546676 | 157.284    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.465767 |        0.16059 |    2.78951 |
| solution-aron-mark |     0.46415  |        0.15967 |    2.79773 |
| solution-flask     |     0.45784  |        1.00899 |    4.16637 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.462708 |       0.269341 |    16.1351 |
| solution-aron-mark |     0.487881 |       0.272379 |    16.4883 |