# 2025-07-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.77156  |       1.04457  |   0.099077 |
| solution-aron-mark |     4.74508  |       0.154308 |   0.236535 |
| solution-pl        |     0.506045 |       0.150557 |   0.240819 |
| solution-1-flask   |     0.507766 |       1.00839  |   0.269175 |
| solution-1         |     7.89776  |       1e-06    |   0.626417 |
| solution-2         |     0.494907 |       0.595974 |   1.19642  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.505078 |       0.155242 |   0.358315 |
| solution-aron-mark |     0.505165 |       0.151445 |   0.362181 |
| solution-flask     |     0.499502 |       1.00818  |   0.386529 |
| solution-1-flask   |     0.511809 |       1.00834  |   0.794097 |
| solution-2         |     0.497485 |       0.50637  |   4.14881  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.512447 |       0.158739 |    1.08303 |
| solution-pl        |     0.503385 |       0.159584 |    1.0938  |
| solution-flask     |     0.503871 |       1.00849  |    1.60787 |
| solution-1-flask   |     0.508036 |       1.00849  |    5.65626 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.501484 |       0.187082 |    3.26167 |
| solution-pl        |     0.502175 |       0.189701 |    3.26944 |
| solution-flask     |     0.510197 |       1.00855  |    5.19515 |