# 2026-10-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.30652  |       1.04287  |   0.104158 |
| solution-aron-mark |     6.21182  |       0.192564 |   0.271022 |
| solution-pl        |     0.458001 |       0.177082 |   0.271306 |
| solution-1-flask   |     0.450438 |       1.00849  |   0.274121 |
| solution-1         |     8.14609  |       1e-06    |   0.665423 |
| solution-2         |     0.436314 |       0.689822 |   1.23412  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.444956 |       1.00873  |   0.240737 |
| solution-pl        |     0.482787 |       0.192981 |   0.413053 |
| solution-aron-mark |     0.452799 |       0.170601 |   0.41544  |
| solution-1-flask   |     0.452869 |       1.0087   |   0.808805 |
| solution-2         |     0.438592 |       0.534294 |   2.93466  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.43768  |       1.00876  |    1.07655 |
| solution-aron-mark |     0.459433 |       0.180076 |    1.18227 |
| solution-pl        |     0.445405 |       0.178442 |    1.19714 |
| solution-1-flask   |     0.48851  |       1.00895  |    5.50299 |
| solution-2         |     0.440166 |       0.588863 |  158.32    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.439045 |       0.201416 |    3.84258 |
| solution-aron-mark |     0.435593 |       0.207144 |    3.8473  |
| solution-flask     |     0.459751 |       1.01011  |    4.60463 |