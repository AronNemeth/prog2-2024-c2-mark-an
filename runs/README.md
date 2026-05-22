# 2026-05-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.04906  |       1.06487  |   0.118294 |
| solution-aron-mark |     5.96443  |       0.168607 |   0.239899 |
| solution-pl        |     0.432242 |       0.153965 |   0.244336 |
| solution-1-flask   |     0.440778 |       1.00834  |   0.274506 |
| solution-1         |     7.2074   |       1e-06    |   0.656907 |
| solution-2         |     0.427272 |       0.617191 |   1.04359  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.436178 |       0.151961 |   0.387679 |
| solution-pl        |     0.432288 |       0.155421 |   0.39199  |
| solution-flask     |     0.431154 |       1.00843  |   0.423641 |
| solution-1-flask   |     0.451205 |       1.00855  |   0.806584 |
| solution-2         |     0.439261 |       0.523484 |   3.4201   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.434779 |       0.15989  |    1.18644 |
| solution-aron-mark |     0.433429 |       0.164999 |    1.21844 |
| solution-flask     |     0.439433 |       1.00889  |    1.76726 |
| solution-1-flask   |     0.436766 |       1.00854  |    5.68783 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.429222 |       0.18273  |    4.1291  |
| solution-aron-mark |     0.429531 |       0.184472 |    4.15366 |
| solution-flask     |     0.42868  |       1.00846  |    5.56151 |