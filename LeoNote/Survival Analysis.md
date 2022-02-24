# Survival analysis

## What is survival analysis

Survival analysis: Y = Time & Event occurs

- Y  is outcome
  - outcome has two attributes
    - Time = T
      - Event = 0 is no; 1 is yes

$$
y = Surv(t,e)
$$

## What is censoring

Censoring:

![image](https://www.researchgate.net/publication/273005984/figure/fig1/AS:650508553445384@1532104733179/a-Right-censoring-observations-b-Left-censoring-observations.png)

## Survival function

$$
S(t) = P(T>t)
$$

(2) it means the probability of survival time beyond time T.
$$
Hazard(haz) = P(T<t+\delta | T>t)
$$
(3) means the probability of dying in next δ time given still alive now.
$$
Hazard Ratio(H.R.) = \frac{Haz(x=1)}{Haz(x=0)}
$$
(4) means the hazard to someone exposed to hazard to someone not exposed.



## Three survival models

Kaplan-Meier model (non-parametric); Exponential model (parametric); Cox regression model (semi-parametric)

<div style="text-align:justify;"><img src="https://miro.medium.com/max/1400/1*CtT_2Ohfwi-h9kJAVjOYmQ.png" style="display:inline-block; width:33.33%"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Survival_function_1.svg/400px-Survival_function_1.svg.png" style="display:inline-block; width:33.33%"><img src="https://user-images.githubusercontent.com/37084259/58433194-ec14e280-80ad-11e9-8019-ee5afdd84dc2.png" style="display:inline-block; width:33.33%"></div>



## Comparison between models

|      | Kaplan-Meier model                                           | Exponential Model                                            | Cox regression model                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Pros | - simple to interpret<br />- can estimate S(t)               | - can estimate S(t) and H.R                                  | - allows Haz to fluctuate with time<br />- can estimate H.R. |
| Cons | - no functional form<br />- cannot estimate H.R.<br />- only incorporate few categorial X variable | - not always realistic (it assumes Haz to be constant)<br />- weibull model allows Haz proportionally increase or decrease with time but still not that realistic | - cannot estimate S(t)                                       |



## Kaplan-Meier model (Non-parametric model)

### Data

| Time (Month) | Death |
| ------------ | ----- |
| 2            | 1     |
| 3            | 0     |
| 6            | 1     |
| 6            | 1     |
| 7            | 1     |
| 10           | 0     |
| 15           | 1     |
| 15           | 1     |
| 16           | 1     |
| 27           | 1     |
| 30           | 1     |
| 32           | 1     |

### Lift Table

| Time | Risk | Died |       Haz        |       1-Haz       |                          Surv=S(t)                           |
| :--: | :--: | :--: | :--------------: | :---------------: | :----------------------------------------------------------: |
|  0   |  12  |  0   |        0         |         1         |                              1                               |
|  2   |  12  |  1   | $\frac{1}{12}$ | $\frac{11}{12}$ |                  $\frac{11}{12}$ = 0.917                   |
|  6   |  10  |  2   | $\frac{2}{10}$ | $\frac{8}{10}$  |         $\frac{11}{12}$ * $\frac{8}{10}$ = 0.733         |
|  7   |  8   |  1   | $\frac{1}{8}$  | $\frac{7}{8}$  | $\frac{11}{12}$ * $\frac{8}{10}$ * $\frac{7}{8}$ = 0.642 |
|  15  |  6   |  2   | $\frac{2}{6}$  | $\frac{4}{6}$  | $\frac{11}{12}$ * $\frac{8}{10}$ * $\frac{7}{8}$ * $\frac{4}{6}$ = 0.428 |
|  16  |  4   |  1   | $\frac{1}{4}$  | $\frac{3}{4}$  | $\frac{11}{12}$ * $\frac{8}{10}$ * $\frac{7}{8}$ * $\frac{4}{6}$$ * $\frac{3}{4}$ = 0.321 |
|  27  |  3   |  1   | $\frac{1}{3}$  | $\frac{2}{3}$  | $\frac{11}{12}$ * $\frac{8}{10}$ * $\frac{7}{8}$ * $\frac{4}{6}$$ * $\frac{3}{4}$ * $\frac{2}{3}$ = 0.214 |
|  30  |  2   |  1   | $\frac{1}{2}$  |  $\frac{1}{2}$ | $\frac{11}{12}$ * $\frac{8}{10}$ * $\frac{7}{8}$ * $\frac{4}{6}$ * $\frac{3}{4}$ * $\frac{2}{3}$ * $\frac{1}{2}$ = 0.107 |
|  32  |  1   |  1   | $\frac{1}{1}$  |         0         |                              0                               |



### Kaplan Meier curve

<img src="./Survival Analysis_src/KM_plot.png">

```R
library(ggfortify)
library(survival)
library(ggplot2)

my_data = list(c(2, 3, 6, 6, 7, 10, 15, 15, 16, 27, 30, 32), c(1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1))
names(my_data) <- c("time", "status")

fit<- survfit(Surv(time, status) ~ 1, data=my_data)

p <- autoplot(fit, surv.colour = 'blue', censor.colour = 'red') + theme_classic()
```



## Exponential Model (parametric model)

The exponential survival model assume constant hazard $$\lambda(t) = \lambda$$.

### Survival function

$$
S(t)= e^{-\lambda t}
$$

### Model fitting

<img src="./Survival%20Analysis_src/Exponential_model.png">

<img src="./Survival%20Analysis_src/Exponential_model_details.png">

```R
my_data = list(c(0, 2, 6, 7, 15, 16, 27, 30), c(1, 0.917, 0.733, 0.642, 0.428, 0.321, 0.214, 0.107))
names(my_data) <- c("time", "Surv")

plot(my_data$time, my_data$Surv)

fit <- lm(log(my_data$Surv)~my_data$time)

summary(fit)


##plot
x <- seq(0, 30, by=0.01)
dat <- data.frame(x=x, px=dexp(x, rate=0.068422)/0.068422)
library(ggplot2)
ggplot() + geom_line(aes(x=dat$x, y=dat$px)) + geom_point(aes(my_data$time, my_data$Surv)) + theme_classic()
```



## Cox regression (Proportional hazard model) (semi-parametric model)

### Assumptions

- Censoring is non informative
- Survival time are independent between samples
- Hazard are proportional (H.R. is constant over time)
- $ln(Haz)$ is linear function of parameters
-  Value of parameters don't change over time
- Baseline hazard ($h_0(t)$) is unspecified.

### Hazard unction

$$
h(t)=h_0(t)*e^{b_1x_1+b_2x_2+...+b_n*x_n}
$$

$$
ln(h(t)) = ln(h_0(t)) + b_1x_1+b_2x_2+...+b_n*x_n
$$

