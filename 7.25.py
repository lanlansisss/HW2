# include <stdio.h>

void
ExactChange(int
userTotal, int
coinVals[]) {
    coinVals[0] = userTotal / 25; // number
of
quarters
userTotal = userTotal % 25;
coinVals[1] = userTotal / 10; // number
of
dimes
userTotal = userTotal % 10;
coinVals[2] = userTotal / 5; // number
of
nickels
userTotal = userTotal % 5;
coinVals[3] = userTotal; // number
of
pennies
}

int
main()
{
    int
numDollars, numQuarters, numDimes, numNickels, numPennies;
int
coinVals[4] = {0};

scanf("%d", & numDollars);

if (numDollars <= 0) {
printf("no change\n");
return 0;
}

ExactChange(numDollars, coinVals);

numQuarters = coinVals[0];
numDimes = coinVals[1];
numNickels = coinVals[2];
numPennies = coinVals[3];

// printing
number
of
pennies
if (numPennies > 0)
{
printf("%d pennies\n", numPennies);
}

// printing
number
of
nickels
if (numNickels > 0)
{
printf("%d nickels\n", numNickels);
}

// printing
number
of
dimes
if (numDimes > 0)
{
printf("%d dimes\n", numDimes);
}

// printing
number
of
quarters
if (numQuarters > 0)
{
printf("%d quarters\n", numQuarters);
}

return 0;
}