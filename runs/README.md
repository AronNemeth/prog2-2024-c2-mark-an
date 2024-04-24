# 2024-04-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.666798 |       1.00901  |   0.07691  |
| solution-pl        |     5.9649   |       0.110349 |   0.168772 |
| solution-aron-mark |     0.663934 |       0.110062 |   0.168893 |
| solution-1-flask   |     1.40538  |       1.04741  |   0.264657 |
| solution-2         |     0.656612 |       0.426754 |   0.772197 |
| solution-1         |     8.06921  |       1e-06    |   0.902959 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.681326 |       1.00888  |   0.16221  |
| solution-aron-mark |     0.653692 |       0.117573 |   0.264724 |
| solution-pl        |     0.655314 |       0.119195 |   0.264801 |
| solution-1-flask   |     0.68309  |       1.00892  |   0.788234 |
| solution-2         |     0.672917 |       0.445294 |   3.57794  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.661859 |       1.00886  |   0.706576 |
| solution-aron-mark |     0.667522 |       0.127355 |   0.81247  |
| solution-pl        |     0.665209 |       0.125638 |   0.819076 |
| solution-1-flask   |     0.671679 |       1.00949  |   5.56344  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.674312 |       1.0091   |    2.46157 |
| solution-aron-mark |     0.674841 |       0.156856 |    2.59699 |
| solution-pl        |     0.664174 |       0.16298  |    2.68032 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.66628  |       1.00924  |    16.4819 |
| solution-aron-mark |     0.66101  |       0.289631 |    16.8312 |
| solution-pl        |     0.663705 |       0.289801 |    16.9872 |